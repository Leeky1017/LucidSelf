"""
Unit Tests for AmapProvider

高德地图地理编码提供商的单元测试。

Requirements: 6.1, 6.2, 6.3, 6.4
"""

import asyncio
import os
import pytest
from unittest.mock import AsyncMock, MagicMock, patch
import httpx

from backend.core.geocoding.providers.amap import (
    AmapProvider,
    RateLimiter,
    ENV_AMAP_API_KEY,
    ENV_GEOCODING_ENABLE_AMAP,
)
from backend.core.geocoding.models import Place
from backend.core.geocoding.exceptions import ProviderError


# =============================================================================
# Test Fixtures
# =============================================================================

@pytest.fixture
def mock_amap_response_success():
    """Mock successful Amap API response."""
    return {
        "status": "1",
        "info": "OK",
        "infocode": "10000",
        "count": "1",
        "geocodes": [
            {
                "formatted_address": "内蒙古自治区包头市",
                "country": "中国",
                "province": "内蒙古自治区",
                "city": "包头市",
                "district": [],
                "township": [],
                "neighborhood": {"name": [], "type": []},
                "building": {"name": [], "type": []},
                "adcode": "150200",
                "street": [],
                "number": [],
                "location": "109.840405,40.658168",
                "level": "市"
            }
        ]
    }


@pytest.fixture
def mock_amap_response_municipality():
    """Mock Amap response for municipality (city is empty list)."""
    return {
        "status": "1",
        "info": "OK",
        "infocode": "10000",
        "count": "1",
        "geocodes": [
            {
                "formatted_address": "北京市",
                "country": "中国",
                "province": "北京市",
                "city": [],  # Municipalities have empty city
                "district": [],
                "adcode": "110000",
                "location": "116.407526,39.904030",
                "level": "省"
            }
        ]
    }


@pytest.fixture
def mock_amap_response_not_found():
    """Mock Amap API response with no results."""
    return {
        "status": "1",
        "info": "OK",
        "infocode": "10000",
        "count": "0",
        "geocodes": []
    }


@pytest.fixture
def mock_amap_response_error():
    """Mock Amap API error response."""
    return {
        "status": "0",
        "info": "INVALID_USER_KEY",
        "infocode": "10001"
    }


# =============================================================================
# Test AmapProvider.is_enabled()
# =============================================================================

class TestAmapProviderIsEnabled:
    """Tests for AmapProvider.is_enabled() method."""
    
    def test_enabled_with_api_key(self):
        """
        Test: Provider is enabled when API key is provided.
        
        Requirements: 6.4, 11.1
        """
        provider = AmapProvider(api_key="test_key", enabled=True)
        assert provider.is_enabled() is True
    
    def test_disabled_without_api_key(self):
        """
        Test: Provider is disabled when API key is missing.
        
        Requirements: 6.4
        """
        provider = AmapProvider(api_key=None, enabled=True)
        assert provider.is_enabled() is False
    
    def test_disabled_with_empty_api_key(self):
        """
        Test: Provider is disabled when API key is empty string.
        
        Requirements: 6.4
        """
        provider = AmapProvider(api_key="", enabled=True)
        assert provider.is_enabled() is False
    
    def test_disabled_when_feature_flag_off(self):
        """
        Test: Provider is disabled when feature flag is off.
        
        Requirements: 11.2
        """
        provider = AmapProvider(api_key="test_key", enabled=False)
        assert provider.is_enabled() is False
    
    def test_disabled_when_both_missing(self):
        """
        Test: Provider is disabled when both API key and flag are missing.
        
        Requirements: 6.4, 11.2
        """
        provider = AmapProvider(api_key=None, enabled=False)
        assert provider.is_enabled() is False
    
    def test_reads_api_key_from_env(self):
        """
        Test: Provider reads API key from environment variable.
        
        Requirements: 11.1
        """
        with patch.dict(os.environ, {ENV_AMAP_API_KEY: "env_test_key"}):
            provider = AmapProvider(enabled=True)
            assert provider.is_enabled() is True
    
    def test_reads_enabled_from_env_true(self):
        """
        Test: Provider reads enabled flag from environment variable (true).
        
        Requirements: 11.2
        """
        with patch.dict(os.environ, {
            ENV_AMAP_API_KEY: "test_key",
            ENV_GEOCODING_ENABLE_AMAP: "true"
        }):
            provider = AmapProvider()
            assert provider.is_enabled() is True
    
    def test_reads_enabled_from_env_false(self):
        """
        Test: Provider reads enabled flag from environment variable (false).
        
        Requirements: 11.2
        """
        with patch.dict(os.environ, {
            ENV_AMAP_API_KEY: "test_key",
            ENV_GEOCODING_ENABLE_AMAP: "false"
        }, clear=True):
            provider = AmapProvider()
            assert provider.is_enabled() is False


# =============================================================================
# Test AmapProvider.geocode() - API Response Parsing
# =============================================================================

class TestAmapProviderGeocode:
    """Tests for AmapProvider.geocode() method."""
    
    @pytest.mark.asyncio
    async def test_geocode_success(self, mock_amap_response_success):
        """
        Test: Successful geocoding returns Place with correct fields.
        
        Requirements: 6.1, 6.2
        """
        # Create mock HTTP client
        mock_response = MagicMock()
        mock_response.json.return_value = mock_amap_response_success
        mock_response.raise_for_status = MagicMock()
        
        mock_client = AsyncMock()
        mock_client.get = AsyncMock(return_value=mock_response)
        
        provider = AmapProvider(api_key="test_key", enabled=True, http_client=mock_client)
        
        result = await provider.geocode("包头")
        
        assert result is not None
        assert result.source == "amap"
        assert result.country_code == "CN"
        assert result.city_name == "包头市"
        assert result.timezone == "Asia/Shanghai"
        assert result.accuracy == "city"
        assert abs(result.lat - 40.658168) < 0.0001
        assert abs(result.lng - 109.840405) < 0.0001
        assert result.place_id.startswith("amap-")
    
    @pytest.mark.asyncio
    async def test_geocode_municipality(self, mock_amap_response_municipality):
        """
        Test: Geocoding municipality (city is empty list) uses province name.
        
        Requirements: 6.2
        """
        mock_response = MagicMock()
        mock_response.json.return_value = mock_amap_response_municipality
        mock_response.raise_for_status = MagicMock()
        
        mock_client = AsyncMock()
        mock_client.get = AsyncMock(return_value=mock_response)
        
        provider = AmapProvider(api_key="test_key", enabled=True, http_client=mock_client)
        
        result = await provider.geocode("北京")
        
        assert result is not None
        assert result.source == "amap"
        assert result.city_name == "北京市"  # Falls back to province
        assert result.country_code == "CN"
    
    @pytest.mark.asyncio
    async def test_geocode_not_found(self, mock_amap_response_not_found):
        """
        Test: Geocoding returns None when no results found.
        
        Requirements: 6.1
        """
        mock_response = MagicMock()
        mock_response.json.return_value = mock_amap_response_not_found
        mock_response.raise_for_status = MagicMock()
        
        mock_client = AsyncMock()
        mock_client.get = AsyncMock(return_value=mock_response)
        
        provider = AmapProvider(api_key="test_key", enabled=True, http_client=mock_client)
        
        result = await provider.geocode("不存在的城市xyz")
        
        assert result is None
    
    @pytest.mark.asyncio
    async def test_geocode_api_error(self, mock_amap_response_error):
        """
        Test: Geocoding returns None when API returns error status.
        
        Requirements: 6.1
        """
        mock_response = MagicMock()
        mock_response.json.return_value = mock_amap_response_error
        mock_response.raise_for_status = MagicMock()
        
        mock_client = AsyncMock()
        mock_client.get = AsyncMock(return_value=mock_response)
        
        provider = AmapProvider(api_key="test_key", enabled=True, http_client=mock_client)
        
        result = await provider.geocode("包头")
        
        assert result is None
    
    @pytest.mark.asyncio
    async def test_geocode_http_error_raises_provider_error(self):
        """
        Test: HTTP errors raise ProviderError.
        
        Requirements: 6.1
        """
        mock_client = AsyncMock()
        mock_client.get = AsyncMock(side_effect=httpx.HTTPError("Connection failed"))
        
        provider = AmapProvider(api_key="test_key", enabled=True, http_client=mock_client)
        
        with pytest.raises(ProviderError) as exc_info:
            await provider.geocode("包头")
        
        assert exc_info.value.provider == "amap"
    
    @pytest.mark.asyncio
    async def test_geocode_returns_none_when_disabled(self):
        """
        Test: Geocoding returns None when provider is disabled.
        
        Requirements: 6.4, 11.2
        """
        provider = AmapProvider(api_key="test_key", enabled=False)
        
        result = await provider.geocode("包头")
        
        assert result is None
    
    @pytest.mark.asyncio
    async def test_geocode_returns_none_when_no_api_key(self):
        """
        Test: Geocoding returns None when API key is missing.
        
        Requirements: 6.4
        """
        provider = AmapProvider(api_key=None, enabled=True)
        
        result = await provider.geocode("包头")
        
        assert result is None


# =============================================================================
# Test RateLimiter
# =============================================================================

class TestRateLimiter:
    """Tests for RateLimiter class."""
    
    @pytest.mark.asyncio
    async def test_rate_limiter_allows_first_call_immediately(self):
        """
        Test: First call is allowed immediately.
        
        Requirements: 6.3
        """
        limiter = RateLimiter(max_qps=5.0)
        
        import time
        start = time.monotonic()
        await limiter.acquire()
        elapsed = time.monotonic() - start
        
        # First call should be nearly instant
        assert elapsed < 0.1
    
    @pytest.mark.asyncio
    async def test_rate_limiter_enforces_interval(self):
        """
        Test: Rate limiter enforces minimum interval between calls.
        
        Requirements: 6.3
        """
        # Use 10 QPS for faster test (0.1s interval)
        limiter = RateLimiter(max_qps=10.0)
        
        import time
        
        # First call
        await limiter.acquire()
        start = time.monotonic()
        
        # Second call should wait
        await limiter.acquire()
        elapsed = time.monotonic() - start
        
        # Should have waited at least 0.1s (1/10 QPS)
        assert elapsed >= 0.09  # Allow small tolerance
    
    @pytest.mark.asyncio
    async def test_rate_limiter_5_qps(self):
        """
        Test: Rate limiter enforces 5 QPS (0.2s interval).
        
        Requirements: 6.3
        """
        limiter = RateLimiter(max_qps=5.0)
        
        import time
        
        # First call
        await limiter.acquire()
        start = time.monotonic()
        
        # Second call should wait ~0.2s
        await limiter.acquire()
        elapsed = time.monotonic() - start
        
        # Should have waited at least 0.2s (1/5 QPS)
        assert elapsed >= 0.19  # Allow small tolerance


# =============================================================================
# Test AmapProvider Properties
# =============================================================================

class TestAmapProviderProperties:
    """Tests for AmapProvider properties."""
    
    def test_name_property(self):
        """Test: Provider name is 'amap'."""
        provider = AmapProvider(api_key="test", enabled=True)
        assert provider.name == "amap"
    
    def test_source_tag_property(self):
        """Test: Source tag is 'amap'."""
        provider = AmapProvider(api_key="test", enabled=True)
        assert provider.source_tag == "amap"
