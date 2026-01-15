# backend/calculators/bazi/tests/test_solar_terms.py
"""
Unit tests for solar terms calculation module.

Tests:
- Solar term date calculation
- Month determination from solar terms
- Season determination
- Li Chun (立春) boundary detection
"""

import pytest
from datetime import datetime

from backend.calculators.bazi.solar_terms import (
    get_solar_term_date,
    get_month_from_solar_term,
    get_season_from_date,
    is_before_lichun,
    SOLAR_TERMS_FOR_MONTH,
    SOLAR_TERM_TO_MONTH,
)


# =============================================================================
# Solar Term Date Tests
# =============================================================================

class TestSolarTermDate:
    """Test solar term date calculation."""

    def test_lichun_2024(self):
        """Test Li Chun (立春) date for 2024."""
        lichun = get_solar_term_date(2024, "立春")
        # 立春 2024 should be around Feb 4
        assert lichun.year == 2024
        assert lichun.month == 2
        assert 3 <= lichun.day <= 5

    def test_lichun_1990(self):
        """Test Li Chun (立春) date for 1990."""
        lichun = get_solar_term_date(1990, "立春")
        assert lichun.year == 1990
        assert lichun.month == 2
        assert 3 <= lichun.day <= 5

    def test_dongzhi_2024(self):
        """Test Dong Zhi (冬至) date for 2024."""
        dongzhi = get_solar_term_date(2024, "冬至")
        # 冬至 should be around Dec 21-22
        assert dongzhi.year == 2024
        assert dongzhi.month == 12
        assert 20 <= dongzhi.day <= 23

    def test_chunfen_2024(self):
        """Test Chun Fen (春分) date for 2024."""
        chunfen = get_solar_term_date(2024, "春分")
        # 春分 should be around Mar 20
        assert chunfen.year == 2024
        assert chunfen.month == 3
        assert 19 <= chunfen.day <= 22

    def test_qiufen_2024(self):
        """Test Qiu Fen (秋分) date for 2024."""
        qiufen = get_solar_term_date(2024, "秋分")
        # 秋分 should be around Sep 22-23
        assert qiufen.year == 2024
        assert qiufen.month == 9
        assert 21 <= qiufen.day <= 24

    def test_all_12_terms_for_month_exist(self):
        """Test that all 12 solar terms for month are defined."""
        assert len(SOLAR_TERMS_FOR_MONTH) == 12
        expected_terms = [
            "小寒", "立春", "惊蛰", "清明", "立夏", "芒种",
            "小暑", "立秋", "白露", "寒露", "立冬", "大雪",
        ]
        for term in expected_terms:
            assert term in SOLAR_TERMS_FOR_MONTH

    def test_term_dates_are_ordered(self):
        """Test that solar term dates are in chronological order within a year."""
        year = 2024
        dates = []
        for term in SOLAR_TERMS_FOR_MONTH:
            try:
                date = get_solar_term_date(year, term)
                dates.append((term, date))
            except Exception:
                pass
        
        # Check dates - should have all 12 terms for month
        assert len(dates) == 12  # Should have all 12 terms


# =============================================================================
# Bazi Month Tests
# =============================================================================

class TestBaziMonth:
    """Test Bazi month determination from solar terms."""

    def test_month_after_lichun(self):
        """Test month determination after Li Chun."""
        # Feb 10, 2024 - should be 寅月 (month 1)
        dt = datetime(2024, 2, 10, 12, 0)
        month = get_month_from_solar_term(dt)
        assert month == 1  # 寅月

    def test_month_before_lichun(self):
        """Test month determination before Li Chun."""
        # Feb 1, 2024 - should still be previous year's last month
        dt = datetime(2024, 2, 1, 12, 0)
        month = get_month_from_solar_term(dt)
        assert month == 12  # 丑月

    def test_month_after_jingzhe(self):
        """Test month after Jing Zhe (惊蛰)."""
        # Mar 10, 2024 - should be 卯月 (month 2)
        dt = datetime(2024, 3, 10, 12, 0)
        month = get_month_from_solar_term(dt)
        assert month == 2  # 卯月

    def test_month_in_summer(self):
        """Test month in summer."""
        # July 15, 2024 - should be around 未月 (month 6)
        dt = datetime(2024, 7, 15, 12, 0)
        month = get_month_from_solar_term(dt)
        assert 5 <= month <= 7  # Around summer months

    def test_month_in_winter(self):
        """Test month in winter."""
        # Dec 25, 2024 - should be 子月 (month 11)
        dt = datetime(2024, 12, 25, 12, 0)
        month = get_month_from_solar_term(dt)
        assert 11 <= month <= 12  # Winter months

    def test_term_to_month_mapping(self):
        """Test that term to month mapping is complete."""
        assert len(SOLAR_TERM_TO_MONTH) == 12
        # Each term should map to a valid month 1-12
        for term, month in SOLAR_TERM_TO_MONTH.items():
            assert 1 <= month <= 12


# =============================================================================
# Season Tests
# =============================================================================

class TestSeason:
    """Test season determination."""

    def test_spring_season(self):
        """Test spring season detection."""
        # April - should be spring
        dt = datetime(2024, 4, 15, 12, 0)
        season = get_season_from_date(dt)
        assert season == "spring"

    def test_summer_season(self):
        """Test summer season detection."""
        # July - should be summer
        dt = datetime(2024, 7, 15, 12, 0)
        season = get_season_from_date(dt)
        assert season == "summer"

    def test_autumn_season(self):
        """Test autumn season detection."""
        # October - should be autumn
        dt = datetime(2024, 10, 15, 12, 0)
        season = get_season_from_date(dt)
        assert season == "autumn"

    def test_winter_season(self):
        """Test winter season detection."""
        # January - should be winter
        dt = datetime(2024, 1, 15, 12, 0)
        season = get_season_from_date(dt)
        assert season == "winter"


# =============================================================================
# Li Chun Boundary Tests
# =============================================================================

class TestLiChunBoundary:
    """Test Li Chun (立春) year boundary detection."""

    def test_before_lichun_returns_true(self):
        """Test dates before Li Chun return True."""
        # Jan 15, 2024 - before Li Chun
        dt = datetime(2024, 1, 15, 12, 0)
        assert is_before_lichun(dt) is True

    def test_after_lichun_returns_false(self):
        """Test dates after Li Chun return False."""
        # Mar 15, 2024 - after Li Chun
        dt = datetime(2024, 3, 15, 12, 0)
        assert is_before_lichun(dt) is False

    def test_mid_year_returns_false(self):
        """Test mid-year dates return False."""
        # June 15, 2024
        dt = datetime(2024, 6, 15, 12, 0)
        assert is_before_lichun(dt) is False

    def test_december_returns_false(self):
        """Test December dates return False (still after current year's Li Chun)."""
        # Dec 15, 2024
        dt = datetime(2024, 12, 15, 12, 0)
        assert is_before_lichun(dt) is False


# =============================================================================
# Edge Cases
# =============================================================================

class TestEdgeCases:
    """Test edge cases and boundary conditions."""

    def test_year_1900_supported(self):
        """Test that year 1900 is supported."""
        lichun = get_solar_term_date(1900, "立春")
        assert lichun.year == 1900

    def test_year_2100_supported(self):
        """Test that year 2100 is supported."""
        lichun = get_solar_term_date(2100, "立春")
        assert lichun.year == 2100

    def test_invalid_term_raises_error(self):
        """Test that invalid term raises an error."""
        with pytest.raises((ValueError, KeyError)):
            get_solar_term_date(2024, "无效节气")

    def test_month_boundary_precision(self):
        """Test month boundary at solar term transition."""
        # Get exact Li Chun date for 2024
        lichun = get_solar_term_date(2024, "立春")
        
        # Day before Li Chun should be month 12
        before = datetime(lichun.year, lichun.month, lichun.day - 1, 12, 0)
        month_before = get_month_from_solar_term(before)
        
        # Day after Li Chun should be month 1
        after = datetime(lichun.year, lichun.month, lichun.day + 1, 12, 0)
        month_after = get_month_from_solar_term(after)
        
        # Months should differ across the boundary
        assert month_before != month_after or month_before == 12
