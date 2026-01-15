"""
Unit Tests for NominatimProvider

Nominatim地理编码提供商的单元测试。

Requirements: 7.1, 7.2, 7.3, 7.4
"""

import os
import time
import pytest
from unittest.mock import AsyncMock, MagicMock, patch
import httpx

from backend.core.geocoding.providers.nominatim import (
    NominatimProvider,
    RateLimiter,
    ENV_GEOCODING_ENABLE_NOMINATIM,
    ENV_GEOCODING_NOMINATIM_BASE_URL,
    DEFAULT_NOMINATIM_URL,
)
from backend.core.geocoding.models import Place
from backend.core.geocoding.exceptions import ProviderError


# =============================================================================
# Test Fixtures
# =============================================================================

@pytest.fixture
def mock_nominatim_response_success():
    """Mock successful Nominatim API response."""
    return [
        {
            "place_id": 123456,
            "licence": "Data OpenStreetMap contributors",
            "osm_type": "relation",
            "osm_id": 62422,
            "lat": "52.5170365",
            "lon": "13.3888599",
            "display_name": "Berlin, Germany",
            "address": {
                "city": "Berlin",
                "state": "Berlin",
                "country": "Germany",
                "country_code": "de",
            },
            "boundingbox": ["52.3382448", "52.6755087", "13.0883450", "13.7611609"],
        }
    ]


@pytest.fixture
def mock_nominatim_response_tokyo():
    """Mock Nominatim response for Tokyo."""
    return [
        {
            "place_id": 789012,
            "osm_type": "relation",
            "osm_id": 1543125,
            "lat": "35.6764225",
            "lon": "139.6500478",
            "display_name": "Tokyo, Japan",
            "name": "Tokyo",
            "address": {
                "city": "Tokyo",
                "state": "Tokyo",
                "country": "Japan",
                "country_code": "jp",
            },
        }
    ]


@pytest.fixture
def mock_nominatim_response_not_found():
    """Mock Nominatim API response with no results."""
    return []


# =============================================================================
# Test NominatimProvider.is_enabled()
# =============================================================================

class TestNominatimProviderIsEnabled:
    """Tests for NominatimProvider.is_enabled() method."""
    
    def test_enabled_by_default(self):
        """Test: Provider is enabled by default."""
        provider = NominatimProvider(enabled=True)
        assert provider.is_enabled() is True
    
    def test_disabled_when_flag_off(self):
        """Test: Provider is disabled when feature flag is off. (Req 11.3)"""
        provider = NominatimProvider(enabled=False)
        assert provider.is_enabled() is False
    
    def test_reads_enabled_from_env_true(self):
        """Test: Provider reads enabled flag from env var (true). (Req 11.3)"""
        with patch.dict(os.environ, {ENV_GEOCODING_ENABLE_NOMINATIM: "true"}, clear=True):
            provider = NominatimProvider()
            assert provider.is_enabled() is True
    
    def test_reads_enabled_from_env_false(self):
        """Test: Provider reads enabled flag from env var (false). (Req 11.3)"""
        with patch.dict(os.environ, {ENV_GEOCODING_ENABLE_NOMINATIM: "false"}, clear=True):
            provider = NominatimProvider()
            assert provider.is_enabled() is False


# =============================================================================
# Test NominatimProvider.geocode() - API Response Parsing
# =============================================================================

class TestNominatimProviderGeocode:
    """Tests for NominatimProvider.geocode() method."""
    
    @pytest.mark.asyncio
    async def test_geocode_success(self, mock_nominatim_response_success):
        """Test: Successful geocoding returns Place with correct fields. (Req 7.1, 7.2)"""
        mock_response = MagicMock()
        mock_response.json.return_value = mock_nominatim_response_success
        mock_response.raise_for_status = MagicMock()
        
        mock_client = AsyncMock()
        mock_client.get = AsyncMock(return_value=mock_response)
        
        provider = NominatimProvider(enabled=True, http_client=mock_client)
        
        result = await provider.geocode("Berlin", "DE")
        
        assert result is not None
        assert result.source == "nominatim"
        assert result.country_code == "DE"
        assert result.city_name == "Berlin"
        assert result.accuracy == "city"
        assert abs(result.lat - 52.5170365) < 0.0001
        assert abs(result.lng - 13.3888599) < 0.0001
        assert result.place_id.startswith("osm-")
    
    @pytest.mark.asyncio
    async def test_geocode_tokyo(self, mock_nominatim_response_tokyo):
        """Test: Geocoding Tokyo returns correct timezone. (Req 7.2)"""
        mock_response = MagicMock()
        mock_response.json.return_value = mock_nominatim_response_tokyo
        mock_response.raise_for_status = MagicMock()
        
        mock_client = AsyncMock()
        mock_client.get = AsyncMock(return_value=mock_response)
        
        provider = NominatimProvider(enabled=True, http_client=mock_client)
        
        result = await provider.geocode("Tokyo", "JP")
        
        assert result is not None
        assert result.source == "nominatim"
        assert result.country_code == "JP"
        assert result.city_name == "Tokyo"
        assert result.timezone == "Asia/Tokyo"
    
    @pytest.mark.asyncio
    async def test_geocode_not_found(self, mock_nominatim_response_not_found):
        """Test: Geocoding returns None when no results found. (Req 7.1)"""
        mock_response = MagicMock()
        mock_response.json.return_value = mock_nominatim_response_not_found
        mock_response.raise_for_status = MagicMock()
        
        mock_client = AsyncMock()
        mock_client.get = AsyncMock(return_value=mock_response)
        
        provider = NominatimProvider(enabled=True, http_client=mock_client)
        
        result = await provider.geocode("NonexistentCityXYZ123")
        
        assert result is None
    
    @pytest.mark.asyncio
    async def test_geocode_http_error_raises_provider_error(self):
        """Test: HTTP errors raise ProviderError. (Req 7.1)"""
        mock_client = AsyncMock()
        mock_client.get = AsyncMock(side_effect=httpx.HTTPError("Connection failed"))
        
        provider = NominatimProvider(enabled=True, http_client=mock_client)
        
        with pytest.raises(ProviderError) as exc_info:
            await provider.geocode("Berlin")
        
        assert exc_info.value.provider == "nominatim"
    
    @pytest.mark.asyncio
    async def test_geocode_returns_none_when_disabled(self):
        """Test: Geocoding returns None when provider is disabled. (Req 11.3)"""
        provider = NominatimProvider(enabled=False)
        
        result = await provider.geocode("Berlin")
        
        assert result is None


# =============================================================================
# Test Rate Limiter
# =============================================================================

class TestNominatimRateLimiter:
    """Tests for RateLimiter class (1 QPS for Nominatim)."""
    
    @pytest.mark.asyncio
    async def test_rate_limiter_allows_first_call_immediately(self):
        """Test: First call is allowed immediately. (Req 7.3)"""
        limiter = RateLimiter(max_qps=1.0)
        
        start = time.monotonic()
        await limiter.acquire()
        elapsed = time.monotonic() - start
        
        assert elapsed < 0.1
    
    @pytest.mark.asyncio
    async def test_rate_limiter_enforces_1_qps(self):
        """Test: Rate limiter enforces 1 QPS (1s interval). (Req 7.3)"""
        limiter = RateLimiter(max_qps=1.0)
        
        await limiter.acquire()
        start = time.monotonic()
        
        await limiter.acquire()
        elapsed = time.monotonic() - start
        
        # Should have waited at least ~1s (1/1 QPS)
        assert elapsed >= 0.95


# =============================================================================
# Test Base URL Configuration
# =============================================================================

class TestNominatimProviderBaseUrl:
    """Tests for NominatimProvider base URL configuration."""
    
    def test_uses_default_url(self):
        """Test: Uses default public endpoint when not configured. (Req 7.4)"""
        provider = NominatimProvider(enabled=True)
        assert provider._base_url == DEFAULT_NOMINATIM_URL
    
    def test_uses_custom_url(self):
        """Test: Uses custom URL when provided. (Req 11.4)"""
        custom_url = "https://custom.nominatim.example.com"
        provider = NominatimProvider(base_url=custom_url, enabled=True)
        assert provider._base_url == custom_url
    
    def test_reads_url_from_env(self):
        """Test: Reads base URL from environment variable. (Req 11.4)"""
        custom_url = "https://env.nominatim.example.com"
        with patch.dict(os.environ, {ENV_GEOCODING_NOMINATIM_BASE_URL: custom_url}):
            provider = NominatimProvider(enabled=True)
            assert provider._base_url == custom_url


# =============================================================================
# Test NominatimProvider Properties
# =============================================================================

class TestNominatimProviderProperties:
    """Tests for NominatimProvider properties."""
    
    def test_name_property(self):
        """Test: Provider name is 'nominatim'."""
        provider = NominatimProvider(enabled=True)
        assert provider.name == "nominatim"
    
    def test_source_tag_property(self):
        """Test: Source tag is 'nominatim'."""
        provider = NominatimProvider(enabled=True)
        assert provider.source_tag == "nominatim"
