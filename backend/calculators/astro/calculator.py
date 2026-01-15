# backend/calculators/astro/calculator.py
"""
AstroCalculator - Western Astrology Calculator.

Implements Layer 1 Calculator standard interface, providing:
- Planetary position calculation (Sun through Pluto)
- House cusp calculation (Placidus default)
- Aspect calculation (major aspects)

Uses Swiss Ephemeris (pyswisseph) for high-precision astronomical data.

Performance target: < 30ms/calculation (P95)
Accuracy target: < 1 arcminute for planetary positions
"""

from __future__ import annotations

import time
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
from zoneinfo import ZoneInfo

import swisseph as swe

from backend.calculators.astro.models import (
    AstroInput,
    AstroFactors,
    PlanetPosition,
    Aspect,
    PLANETS,
    PLANET_SE_IDS,
    SIGNS,
    ASPECT_TYPES,
    ASPECT_ANGLES,
    ASPECT_ORBS,
    HOUSE_SYSTEMS,
)


class AstroCalculator:
    """
    Western Astrology Calculator.
    
    Conforms to Architecture v3 §4.1 Layer 1 Calculator standard.
    
    Example:
        >>> from backend.calculators.astro import AstroCalculator, AstroInput
        >>> 
        >>> calculator = AstroCalculator()
        >>> input_data = AstroInput(
        ...     birth_datetime=datetime(1990, 5, 15, 14, 30),
        ...     birth_location=(116.4, 39.9),
        ...     timezone="Asia/Shanghai"
        ... )
        >>> astro_factors = calculator.calculate(input_data)
        >>> factor_matrix = astro_factors.to_factor_matrix()
    """
    
    # Date range limits
    MIN_YEAR = 1800
    MAX_YEAR = 2400
    
    def __init__(self):
        """Initialize calculator with Swiss Ephemeris."""
        # Set ephemeris path (uses built-in data if not set)
        # swe.set_ephe_path('/path/to/ephe')  # Optional: set custom path
        pass
    
    def calculate(self, input_data: AstroInput) -> AstroFactors:
        """
        Execute complete astrology calculation.
        
        Args:
            input_data: Input parameters
            
        Returns:
            AstroFactors: Astrology factors result
            
        Raises:
            ValueError: If input parameters are invalid
        """
        start_time = time.perf_counter()
        
        # 1. Validate input
        self._validate_input(input_data)
        
        # 2. Convert to UTC and get Julian Day
        utc_datetime = self._convert_to_utc(
            input_data.birth_datetime,
            input_data.timezone
        )
        julian_day = self._datetime_to_julian_day(utc_datetime)
        
        # 3. Get location
        longitude, latitude = input_data.birth_location
        
        # 4. Calculate house cusps and angles
        houses, ascendant, midheaven = self._calculate_houses(
            julian_day,
            latitude,
            longitude,
            input_data.house_system
        )
        
        # 5. Calculate planetary positions
        planets = self._calculate_planets(julian_day, houses)
        
        # 6. Calculate aspects
        aspects = self._calculate_aspects(planets)
        
        # 7. Determine signs for angles
        ascendant_sign = self._longitude_to_sign(ascendant)
        midheaven_sign = self._longitude_to_sign(midheaven)
        
        # 8. Build result
        calculation_time = (time.perf_counter() - start_time) * 1000
        
        return AstroFactors(
            planets=planets,
            houses=houses,
            ascendant=ascendant,
            midheaven=midheaven,
            ascendant_sign=ascendant_sign,
            midheaven_sign=midheaven_sign,
            aspects=aspects,
            julian_day=julian_day,
            house_system=input_data.house_system,
            calculation_time_ms=calculation_time,
        )
    
    def _validate_input(self, input_data: AstroInput) -> None:
        """
        Validate input parameters.
        
        Note: birth_location must be resolved before calling calculate().
        Use LocationResolver to resolve birth_place first.
        
        Raises:
            ValueError: If parameters are invalid
        """
        # Date range validation
        year = input_data.birth_datetime.year
        if year < self.MIN_YEAR or year > self.MAX_YEAR:
            raise ValueError(
                f"Date out of supported range ({self.MIN_YEAR}-{self.MAX_YEAR}): {year}"
            )
        
        # Location validation
        if input_data.birth_location is None:
            raise ValueError(
                "birth_location must be resolved before calculation. "
                "Use LocationResolver to resolve birth_place first."
            )
        
        longitude, latitude = input_data.birth_location
        if longitude < -180 or longitude > 180:
            raise ValueError(f"Longitude out of range (-180 to 180): {longitude}")
        if latitude < -90 or latitude > 90:
            raise ValueError(f"Latitude out of range (-90 to 90): {latitude}")

    
    def _convert_to_utc(
        self,
        dt: datetime,
        timezone: Optional[str] = None
    ) -> datetime:
        """
        Convert datetime to UTC.
        
        Args:
            dt: Local datetime
            timezone: Timezone identifier (e.g., 'Asia/Shanghai')
            
        Returns:
            datetime: UTC datetime
        """
        if timezone:
            local_tz = ZoneInfo(timezone)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=local_tz)
            utc_dt = dt.astimezone(ZoneInfo("UTC"))
            return utc_dt.replace(tzinfo=None)
        
        # If no timezone, assume UTC
        return dt
    
    def _datetime_to_julian_day(self, dt: datetime) -> float:
        """
        Convert datetime to Julian Day number.
        
        Args:
            dt: UTC datetime
            
        Returns:
            float: Julian Day number
        """
        # Swiss Ephemeris uses UT (Universal Time)
        year = dt.year
        month = dt.month
        day = dt.day
        hour = dt.hour + dt.minute / 60.0 + dt.second / 3600.0
        
        # swe.julday returns Julian Day for given date/time
        jd = swe.julday(year, month, day, hour)
        return jd
    
    def _calculate_houses(
        self,
        julian_day: float,
        latitude: float,
        longitude: float,
        house_system: str
    ) -> Tuple[Dict[int, float], float, float]:
        """
        Calculate house cusps and angles.
        
        Args:
            julian_day: Julian Day number
            latitude: Geographic latitude
            longitude: Geographic longitude
            house_system: House system name
            
        Returns:
            Tuple of (house cusps dict, ascendant, midheaven)
        """
        # Get house system code
        hsys = HOUSE_SYSTEMS.get(house_system, b'P')
        
        # swe.houses returns (cusps, ascmc)
        # cusps is a 12-element tuple (indices 0-11 for houses 1-12)
        # ascmc[0] = ASC, ascmc[1] = MC, ascmc[2] = ARMC, ascmc[3] = Vertex
        cusps, ascmc = swe.houses(julian_day, latitude, longitude, hsys)
        
        # Build house dictionary (1-12)
        # cusps[0] = house 1, cusps[1] = house 2, etc.
        houses = {}
        for i in range(12):
            houses[i + 1] = cusps[i]
        
        ascendant = ascmc[0]
        midheaven = ascmc[1]
        
        return houses, ascendant, midheaven
    
    def _calculate_planets(
        self,
        julian_day: float,
        houses: Dict[int, float]
    ) -> Dict[str, PlanetPosition]:
        """
        Calculate positions for all planets.
        
        Args:
            julian_day: Julian Day number
            houses: House cusps dictionary
            
        Returns:
            Dict of planet positions keyed by planet name
        """
        planets = {}
        
        for planet_name in PLANETS:
            planet_id = PLANET_SE_IDS[planet_name]
            
            # swe.calc_ut returns (longitude, latitude, distance, speed_long, speed_lat, speed_dist)
            # Using SEFLG_SPEED to get speed data
            result, ret_flag = swe.calc_ut(julian_day, planet_id, swe.FLG_SPEED)
            
            longitude = result[0]
            latitude = result[1]
            distance = result[2]
            speed = result[3]  # Daily motion in longitude
            
            # Determine sign and degree in sign
            sign = self._longitude_to_sign(longitude)
            degree_in_sign = longitude % 30.0
            
            # Determine house placement
            house = self._longitude_to_house(longitude, houses)
            
            # Retrograde if speed is negative
            retrograde = speed < 0
            
            planets[planet_name] = PlanetPosition(
                planet=planet_name,
                longitude=longitude,
                latitude=latitude,
                distance=distance,
                speed=speed,
                sign=sign,
                degree_in_sign=degree_in_sign,
                house=house,
                retrograde=retrograde,
            )
        
        return planets
    
    def _longitude_to_sign(self, longitude: float) -> str:
        """
        Convert ecliptic longitude to zodiac sign.
        
        Args:
            longitude: Ecliptic longitude (0-360)
            
        Returns:
            str: Sign name
        """
        # Normalize longitude to 0-360
        longitude = longitude % 360.0
        sign_index = int(longitude / 30.0)
        return SIGNS[sign_index]
    
    def _longitude_to_house(
        self,
        longitude: float,
        houses: Dict[int, float]
    ) -> int:
        """
        Determine which house a longitude falls in.
        
        Args:
            longitude: Ecliptic longitude (0-360)
            houses: House cusps dictionary
            
        Returns:
            int: House number (1-12)
        """
        longitude = longitude % 360.0
        
        # Check each house
        for house_num in range(1, 13):
            cusp_start = houses[house_num]
            cusp_end = houses[house_num % 12 + 1]  # Next house cusp
            
            # Handle wrap-around at 0/360 degrees
            if cusp_start <= cusp_end:
                if cusp_start <= longitude < cusp_end:
                    return house_num
            else:
                # Cusp crosses 0 degrees
                if longitude >= cusp_start or longitude < cusp_end:
                    return house_num
        
        # Default to house 1 if not found (shouldn't happen)
        return 1

    
    def _calculate_aspects(
        self,
        planets: Dict[str, PlanetPosition]
    ) -> List[Aspect]:
        """
        Calculate aspects between all planet pairs.
        
        Args:
            planets: Dictionary of planet positions
            
        Returns:
            List of aspects found
        """
        aspects = []
        planet_names = list(planets.keys())
        
        # Check all unique pairs
        for i, planet1 in enumerate(planet_names):
            for planet2 in planet_names[i + 1:]:
                pos1 = planets[planet1]
                pos2 = planets[planet2]
                
                # Calculate angle between planets
                angle = self._calculate_angle(pos1.longitude, pos2.longitude)
                
                # Check each aspect type
                for aspect_type in ASPECT_TYPES:
                    exact_angle = ASPECT_ANGLES[aspect_type]
                    max_orb = ASPECT_ORBS[aspect_type]
                    
                    # Calculate orb (deviation from exact aspect)
                    orb = abs(angle - exact_angle)
                    
                    # Handle opposition (180 degrees)
                    if aspect_type == "opposition":
                        orb = min(orb, abs(360 - angle - exact_angle))
                    
                    if orb <= max_orb:
                        # Determine if applying or separating
                        applying = self._is_applying(pos1, pos2, aspect_type)
                        
                        aspects.append(Aspect(
                            planet1=planet1,
                            planet2=planet2,
                            aspect_type=aspect_type,
                            exact_angle=angle,
                            orb=orb,
                            applying=applying,
                        ))
                        break  # Only one aspect per pair
        
        return aspects
    
    def _calculate_angle(self, long1: float, long2: float) -> float:
        """
        Calculate the angle between two longitudes.
        
        Args:
            long1: First longitude
            long2: Second longitude
            
        Returns:
            float: Angle between 0 and 180 degrees
        """
        diff = abs(long1 - long2)
        if diff > 180:
            diff = 360 - diff
        return diff
    
    def _is_applying(
        self,
        pos1: PlanetPosition,
        pos2: PlanetPosition,
        aspect_type: str
    ) -> bool:
        """
        Determine if an aspect is applying (forming) or separating.
        
        An aspect is applying if the faster planet is moving toward
        the exact aspect angle.
        
        Args:
            pos1: First planet position
            pos2: Second planet position
            aspect_type: Type of aspect
            
        Returns:
            bool: True if applying, False if separating
        """
        # Get the exact angle for this aspect
        exact_angle = ASPECT_ANGLES[aspect_type]
        
        # Current angle
        current_angle = self._calculate_angle(pos1.longitude, pos2.longitude)
        
        # Predict angle in 1 day
        future_long1 = (pos1.longitude + pos1.speed) % 360
        future_long2 = (pos2.longitude + pos2.speed) % 360
        future_angle = self._calculate_angle(future_long1, future_long2)
        
        # Calculate orbs
        current_orb = abs(current_angle - exact_angle)
        future_orb = abs(future_angle - exact_angle)
        
        # Applying if orb is decreasing
        return future_orb < current_orb
