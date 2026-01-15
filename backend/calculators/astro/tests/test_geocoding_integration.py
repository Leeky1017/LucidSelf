# backend/calculators/astro/tests/test_geocoding_integration.py
"""
Integration tests for AstroCalculator Geocoding integration.

Tests:
- birth_place 解析流程
- birth_location 优先级
- 错误处理

Requirements: 4.1, 4.2, 4.3, 4.4, 4.5
"""

import pytest
from datetime import datetime
from unittest.mock import AsyncMock, MagicMock

from backend.calculators.astro import (
    AstroInput,
    AstroFactors,
    calculate_with_geocoding,
    calculate_with_geocoding_sync,
)
from backend.core.geocoding.service import GeocodingService
from backend.core.geocoding.models import Place
from backend.core.geocoding.exceptions import InvalidInputError, NotFoundError


# =============================================================================
# Fixtures
# =============================================================================

@pytest.fixture
def mock_place_beijing() -> Place:
    """Create a mock Place for Beijing."""
    return Place(
        place_id="gn-beijing-1",
        country_code="CN",
        city_name="Beijing",
        lat=39.9042,
        lng=116.4074,
        timezone="Asia/Shanghai",
        source="local_db",
        accuracy="city",
    )


@pytest.fixture
def mock_place_newyork() -> Place:
    """Create a mock Place for New York."""
    return Place(
        place_id="gn-newyork-1",
        country_code="US",
        city_name="New York",
        lat=40.7128,
        lng=-74.0060,
        timezone="America/New_York",
        source="local_db",
        accuracy="city",
    )


@pytest.fixture
def mock_geocoding_service(mock_place_beijing: Place) -> MagicMock:
    """Create a mock GeocodingService."""
    service = MagicMock(spec=GeocodingService)
    service.resolve_place = AsyncMock(return_value=mock_place_beijing)
    return service


# =============================================================================
# Test: birth_place 解析流程 (Requirement 4.1)
# =============================================================================

class TestBirthPlaceResolution:
    """Test birth_place resolution flow."""

    @pytest.mark.asyncio
    async def test_birth_place_resolves_to_coordinates(
        self, mock_geocoding_service: MagicMock, mock_place_beijing: Place
    ):
        """
        Test that birth_place is resolved to coordinates via GeocodingService.
        
        Requirements: 4.1
        """
        input_data = AstroInput(
            birth_datetime=datetime(1990, 5, 15, 14, 30),
            birth_place="北京",
        )
        
        result = await calculate_with_geocoding(
            input_data, 
            geocoding_service=mock_geocoding_service
        )
        
        # Verify GeocodingService was called
        mock_geocoding_service.resolve_place.assert_called_once()
        
        # Verify result is valid AstroFactors
        assert isinstance(result, AstroFactors)
        assert result.ascendant_sign is not None
        assert result.planets is not None
        assert len(result.planets) == 10  # 10 major celestial bodies

    @pytest.mark.asyncio
    async def test_birth_place_uses_resolved_timezone(
        self, mock_place_newyork: Place
    ):
        """
        Test that resolved Place.timezone is used when no explicit timezone.
        
        Requirements: 4.3
        """
        mock_service = MagicMock(spec=GeocodingService)
        mock_service.resolve_place = AsyncMock(return_value=mock_place_newyork)
        
        input_data = AstroInput(
            birth_datetime=datetime(1990, 5, 15, 14, 30),
            birth_place="New York",
        )
        
        result = await calculate_with_geocoding(
            input_data,
            geocoding_service=mock_service
        )
        
        # Result should be valid (timezone was used for calculation)
        assert isinstance(result, AstroFactors)
        assert result.ascendant_sign is not None
        # Verify all 12 houses are calculated
        assert len(result.houses) == 12


# =============================================================================
# Test: birth_location 优先级 (Requirement 4.2)
# =============================================================================

class TestBirthLocationPriority:
    """Test birth_location priority over birth_place."""

    @pytest.mark.asyncio
    async def test_birth_location_takes_priority(
        self, mock_geocoding_service: MagicMock
    ):
        """
        Test that birth_location is used when both are provided.
        
        Requirements: 4.2
        """
        # Provide both birth_place and birth_location
        input_data = AstroInput(
            birth_datetime=datetime(1990, 5, 15, 14, 30),
            birth_place="北京",
            birth_location=(121.5, 31.2),  # Shanghai coordinates
        )
        
        result = await calculate_with_geocoding(
            input_data,
            geocoding_service=mock_geocoding_service
        )
        
        # GeocodingService should NOT be called
        mock_geocoding_service.resolve_place.assert_not_called()
        
        # Result should be valid
        assert isinstance(result, AstroFactors)

    def test_birth_location_priority_sync(self, mock_geocoding_service: MagicMock):
        """
        Test sync version also prioritizes birth_location.
        
        Requirements: 4.2
        """
        input_data = AstroInput(
            birth_datetime=datetime(1990, 5, 15, 14, 30),
            birth_place="北京",
            birth_location=(116.4, 39.9),
        )
        
        result = calculate_with_geocoding_sync(
            input_data,
            geocoding_service=mock_geocoding_service
        )
        
        # Result should be valid
        assert isinstance(result, AstroFactors)
        assert result.ascendant_sign is not None

    @pytest.mark.asyncio
    async def test_explicit_timezone_overrides_resolved(
        self, mock_place_newyork: Place
    ):
        """
        Test that explicit timezone overrides Place.timezone.
        
        Requirements: 4.3
        """
        mock_service = MagicMock(spec=GeocodingService)
        mock_service.resolve_place = AsyncMock(return_value=mock_place_newyork)
        
        input_data = AstroInput(
            birth_datetime=datetime(1990, 5, 15, 14, 30),
            birth_place="New York",
            timezone="Asia/Shanghai",  # Override with different timezone
        )
        
        result = await calculate_with_geocoding(
            input_data,
            geocoding_service=mock_service
        )
        
        # Result should be valid
        assert isinstance(result, AstroFactors)


# =============================================================================
# Test: 错误处理 (Requirement 4.4, 4.5)
# =============================================================================

class TestErrorHandling:
    """Test error handling for geocoding integration."""

    @pytest.mark.asyncio
    async def test_geocoding_failure_raises_error(self):
        """
        Test that GeocodingService failure raises clear error.
        
        Requirements: 4.4
        """
        mock_service = MagicMock(spec=GeocodingService)
        mock_service.resolve_place = AsyncMock(
            side_effect=NotFoundError("Unknown City")
        )
        
        input_data = AstroInput(
            birth_datetime=datetime(1990, 5, 15, 14, 30),
            birth_place="Unknown City",
        )
        
        with pytest.raises(NotFoundError):
            await calculate_with_geocoding(
                input_data,
                geocoding_service=mock_service
            )

    def test_neither_location_raises_validation_error(self):
        """
        Test that neither birth_place nor birth_location raises error.
        
        Requirements: 4.5
        """
        with pytest.raises(ValueError) as exc_info:
            AstroInput(
                birth_datetime=datetime(1990, 5, 15, 14, 30),
                # Neither birth_place nor birth_location
            )
        
        assert "birth_place" in str(exc_info.value) or "birth_location" in str(exc_info.value)

    def test_empty_birth_place_with_no_location_raises_error(self):
        """
        Test that empty birth_place with no birth_location raises error.
        
        Requirements: 4.5
        """
        with pytest.raises(ValueError):
            AstroInput(
                birth_datetime=datetime(1990, 5, 15, 14, 30),
                birth_place="",  # Empty string
            )


# =============================================================================
# Test: 向后兼容性
# =============================================================================

class TestBackwardCompatibility:
    """Test backward compatibility with existing code."""

    def test_existing_birth_location_code_works(self):
        """
        Test that existing code using birth_location still works.
        """
        # This is how existing code creates AstroInput
        input_data = AstroInput(
            birth_datetime=datetime(1990, 5, 15, 14, 30),
            birth_location=(116.4, 39.9),
        )
        
        result = calculate_with_geocoding_sync(input_data)
        
        assert isinstance(result, AstroFactors)
        assert result.ascendant_sign is not None
        assert len(result.planets) == 10

    def test_birth_location_with_timezone_works(self):
        """
        Test that birth_location with explicit timezone works.
        """
        input_data = AstroInput(
            birth_datetime=datetime(1990, 5, 15, 14, 30),
            birth_location=(116.4, 39.9),
            timezone="Asia/Shanghai",
        )
        
        result = calculate_with_geocoding_sync(input_data)
        
        assert isinstance(result, AstroFactors)

    def test_different_house_systems_work(self):
        """
        Test that different house systems work with geocoding.
        """
        for house_system in ["placidus", "koch", "equal", "whole_sign"]:
            input_data = AstroInput(
                birth_datetime=datetime(1990, 5, 15, 14, 30),
                birth_location=(116.4, 39.9),
                house_system=house_system,
            )
            
            result = calculate_with_geocoding_sync(input_data)
            
            assert isinstance(result, AstroFactors)
            assert result.house_system == house_system
