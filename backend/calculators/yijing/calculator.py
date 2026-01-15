# backend/calculators/yijing/calculator.py
"""
YijingCalculator - I Ching (六爻/易经) Divination Calculator.

Implements hexagram generation and calculation:
- Multiple divination methods (coin, yarrow, time, manual)
- Trigram identification
- Mutual hexagram calculation
- Changed hexagram calculation
- Moving line detection

Follows Architecture v3 Layer 1 Calculator standard.
"""

from __future__ import annotations

import random
import time
from datetime import datetime
from typing import Dict, List, Optional, Tuple

from backend.calculators.yijing.models import (
    Hexagram,
    Trigram,
    YijingFactors,
    YijingInput,
    TRIGRAM_DATA,
    LINES_TO_TRIGRAM,
    MOVING_LINE_VALUES,
)


class YijingCalculator:
    """
    六爻/易经计算器.
    
    Provides hexagram generation and calculation using various methods.
    All calculations are synchronous and deterministic (except random methods).
    
    Usage:
        calculator = YijingCalculator()
        result = calculator.calculate(YijingInput(
            divination_method="coin"
        ))
    """
    
    def __init__(self, hexagram_data: Optional[Dict] = None):
        """
        Initialize the calculator.
        
        Args:
            hexagram_data: Optional custom hexagram data. If None, loads from
                          data/yijing/hexagrams.yaml
        """
        self._hexagram_data = hexagram_data or self._load_hexagram_data()
        self._trigram_data = TRIGRAM_DATA
    
    def _load_hexagram_data(self) -> Dict:
        """Load hexagram data from YAML file."""
        import yaml
        from pathlib import Path
        
        data_path = Path(__file__).parent.parent.parent.parent / "data" / "yijing" / "hexagrams.yaml"
        if data_path.exists():
            with open(data_path, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f)
        
        # Return empty dict if file doesn't exist yet
        return {}
    
    def calculate(self, input_data: YijingInput) -> YijingFactors:
        """
        Calculate hexagram based on input.
        
        Args:
            input_data: YijingInput with divination method and parameters
            
        Returns:
            YijingFactors with complete hexagram information
        """
        start_time = time.perf_counter()
        
        # Generate raw lines based on method
        raw_lines = self._generate_lines(input_data)
        
        # Convert raw lines to binary (0/1)
        binary_lines = self._raw_to_binary(raw_lines)
        
        # Identify main hexagram
        main_hexagram = self._identify_hexagram(binary_lines, raw_lines)
        
        # Calculate mutual hexagram (互卦)
        mutual_hexagram = self._calculate_mutual_hexagram(binary_lines)
        
        # Identify moving lines and calculate changed hexagram
        moving_lines = self._identify_moving_lines(raw_lines)
        changed_hexagram = None
        if moving_lines:
            changed_lines = self._apply_changes(raw_lines)
            changed_hexagram = self._identify_hexagram(changed_lines, None)
        
        calculation_time = (time.perf_counter() - start_time) * 1000
        
        return YijingFactors(
            main_hexagram=main_hexagram,
            mutual_hexagram=mutual_hexagram,
            changed_hexagram=changed_hexagram,
            moving_lines=moving_lines,
            divination_method=input_data.divination_method,
            query_time=input_data.query_time or datetime.now(),
            question=input_data.question,
            calculation_time_ms=calculation_time
        )
    
    def _generate_lines(self, input_data: YijingInput) -> List[int]:
        """
        Generate 6 raw line values based on divination method.
        
        Returns:
            List of 6 integers (6, 7, 8, or 9)
        """
        method = input_data.divination_method
        
        if method == "manual":
            return input_data.manual_lines
        elif method == "coin":
            return self._coin_method()
        elif method == "yarrow":
            return self._yarrow_method()
        elif method == "time":
            return self._time_method(input_data.query_time)
        else:
            raise ValueError(f"Unknown divination method: {method}")
    
    def _coin_method(self) -> List[int]:
        """
        Three-coin toss method (铜钱法).
        
        Each coin: heads=3, tails=2
        Sum of 3 coins: 6, 7, 8, or 9
        - 6 (2+2+2): 老阴 (Old Yin, moving)
        - 7 (2+2+3): 少阳 (Young Yang, static)
        - 8 (2+3+3): 少阴 (Young Yin, static)
        - 9 (3+3+3): 老阳 (Old Yang, moving)
        """
        lines = []
        for _ in range(6):
            # Simulate 3 coin tosses
            coins = [random.choice([2, 3]) for _ in range(3)]
            lines.append(sum(coins))
        return lines
    
    def _yarrow_method(self) -> List[int]:
        """
        Traditional yarrow stalk method (蓍草法).
        
        More complex probability distribution than coin method:
        - 6 (老阴): 1/16 probability
        - 7 (少阳): 5/16 probability
        - 8 (少阴): 7/16 probability
        - 9 (老阳): 3/16 probability
        """
        lines = []
        for _ in range(6):
            # Simulate yarrow stalk probabilities
            r = random.random()
            if r < 1/16:
                lines.append(6)  # 老阴
            elif r < 6/16:
                lines.append(7)  # 少阳
            elif r < 13/16:
                lines.append(8)  # 少阴
            else:
                lines.append(9)  # 老阳
        return lines
    
    def _time_method(self, query_time: Optional[datetime] = None) -> List[int]:
        """
        Time-based hexagram generation (时间起卦).
        
        Uses datetime components to generate hexagram:
        - Upper trigram: (year + month + day) % 8
        - Lower trigram: (year + month + day + hour) % 8
        - Moving line: (year + month + day + hour) % 6 + 1
        
        Args:
            query_time: Time to use, defaults to current time
        """
        dt = query_time or datetime.now()
        
        # Use Chinese calendar year calculation (simplified)
        year = dt.year
        month = dt.month
        day = dt.day
        hour = dt.hour
        
        # Calculate upper trigram index (1-8, then map to trigram)
        upper_num = (year + month + day) % 8
        if upper_num == 0:
            upper_num = 8
        
        # Calculate lower trigram index
        lower_num = (year + month + day + hour) % 8
        if lower_num == 0:
            lower_num = 8
        
        # Map numbers to trigrams (先天八卦序)
        trigram_order = ["乾", "兑", "离", "震", "巽", "坎", "艮", "坤"]
        upper_trigram = trigram_order[upper_num - 1]
        lower_trigram = trigram_order[lower_num - 1]
        
        # Get trigram lines
        upper_lines = list(TRIGRAM_DATA[upper_trigram]["lines"])
        lower_lines = list(TRIGRAM_DATA[lower_trigram]["lines"])
        
        # Combine: lower trigram first (lines 1-3), then upper (lines 4-6)
        binary_lines = lower_lines + upper_lines
        
        # Calculate moving line position (1-6)
        moving_pos = (year + month + day + hour) % 6
        if moving_pos == 0:
            moving_pos = 6
        
        # Convert to raw lines (7 for yang, 8 for yin, with moving line)
        raw_lines = []
        for i, line in enumerate(binary_lines, 1):
            if i == moving_pos:
                # Moving line: 9 for yang->yin, 6 for yin->yang
                raw_lines.append(9 if line == 1 else 6)
            else:
                # Static line: 7 for yang, 8 for yin
                raw_lines.append(7 if line == 1 else 8)
        
        return raw_lines
    
    def _raw_to_binary(self, raw_lines: List[int]) -> List[int]:
        """
        Convert raw line values (6/7/8/9) to binary (0/1).
        
        - 6 (老阴) -> 0 (yin)
        - 7 (少阳) -> 1 (yang)
        - 8 (少阴) -> 0 (yin)
        - 9 (老阳) -> 1 (yang)
        """
        return [1 if line in (7, 9) else 0 for line in raw_lines]
    
    def _identify_moving_lines(self, raw_lines: List[int]) -> List[int]:
        """
        Identify positions of moving lines (动爻).
        
        Moving lines are 6 (老阴) or 9 (老阳).
        
        Returns:
            List of positions (1-6) where moving lines occur
        """
        return [i + 1 for i, line in enumerate(raw_lines) if line in MOVING_LINE_VALUES]
    
    def _apply_changes(self, raw_lines: List[int]) -> List[int]:
        """
        Apply changes to moving lines to get changed hexagram.
        
        - 6 (老阴) -> 1 (yang)
        - 9 (老阳) -> 0 (yin)
        - 7 (少阳) -> 1 (yang, unchanged)
        - 8 (少阴) -> 0 (yin, unchanged)
        """
        changed = []
        for line in raw_lines:
            if line == 6:
                changed.append(1)  # 老阴变阳
            elif line == 9:
                changed.append(0)  # 老阳变阴
            elif line == 7:
                changed.append(1)  # 少阳不变
            else:  # line == 8
                changed.append(0)  # 少阴不变
        return changed
    
    def _identify_hexagram(
        self, 
        binary_lines: List[int], 
        raw_lines: Optional[List[int]] = None
    ) -> Hexagram:
        """
        Identify hexagram from binary lines.
        
        Args:
            binary_lines: 6 binary values (0/1)
            raw_lines: Optional original raw values for reference
            
        Returns:
            Hexagram object with full information
        """
        # Split into lower (1-3) and upper (4-6) trigrams
        lower_lines = tuple(binary_lines[0:3])
        upper_lines = tuple(binary_lines[3:6])
        
        # Identify trigrams
        lower_trigram = LINES_TO_TRIGRAM.get(lower_lines)
        upper_trigram = LINES_TO_TRIGRAM.get(upper_lines)
        
        if not lower_trigram or not upper_trigram:
            raise ValueError(f"Invalid trigram lines: lower={lower_lines}, upper={upper_lines}")
        
        # Look up hexagram in data
        hexagram_info = self._find_hexagram(upper_trigram, lower_trigram)
        
        return Hexagram(
            number=hexagram_info["number"],
            name_zh=hexagram_info["name_zh"],
            name_pinyin=hexagram_info["name_pinyin"],
            upper_trigram=upper_trigram,
            lower_trigram=lower_trigram,
            lines=binary_lines,
            raw_lines=raw_lines
        )
    
    def _find_hexagram(self, upper: str, lower: str) -> Dict:
        """
        Find hexagram by upper and lower trigrams.
        
        Args:
            upper: Upper trigram name (Chinese)
            lower: Lower trigram name (Chinese)
            
        Returns:
            Dict with hexagram info (number, name_zh, name_pinyin)
        """
        # Search in loaded hexagram data
        for num, data in self._hexagram_data.items():
            if data.get("upper") == upper and data.get("lower") == lower:
                return {
                    "number": int(num),
                    "name_zh": data["name_zh"],
                    "name_pinyin": data["name_pinyin"]
                }
        
        # Fallback: generate from trigram combination
        return self._generate_hexagram_info(upper, lower)
    
    def _generate_hexagram_info(self, upper: str, lower: str) -> Dict:
        """
        Generate hexagram info when not found in data file.
        
        Uses the 64 hexagram sequence based on trigram combinations.
        """
        # Standard 64 hexagram sequence (King Wen sequence)
        # This is a simplified mapping - full data should come from YAML
        trigram_order = ["乾", "坤", "震", "巽", "坎", "离", "艮", "兑"]
        
        # Calculate hexagram number based on trigram indices
        upper_idx = trigram_order.index(upper) if upper in trigram_order else 0
        lower_idx = trigram_order.index(lower) if lower in trigram_order else 0
        
        # Simple formula for hexagram number (not King Wen sequence)
        number = upper_idx * 8 + lower_idx + 1
        
        # Generate pinyin from trigram pinyins
        upper_pinyin = TRIGRAM_DATA[upper]["pinyin"]
        lower_pinyin = TRIGRAM_DATA[lower]["pinyin"]
        
        # For same trigrams, use single name
        if upper == lower:
            name_zh = upper
            name_pinyin = upper_pinyin
        else:
            name_zh = f"{upper}{lower}"
            name_pinyin = f"{upper_pinyin}_{lower_pinyin}"
        
        return {
            "number": number,
            "name_zh": name_zh,
            "name_pinyin": name_pinyin
        }
    
    def _calculate_mutual_hexagram(self, binary_lines: List[int]) -> Hexagram:
        """
        Calculate mutual hexagram (互卦).
        
        Mutual hexagram is formed by:
        - Lower trigram: lines 2, 3, 4
        - Upper trigram: lines 3, 4, 5
        
        Args:
            binary_lines: 6 binary values (0/1)
            
        Returns:
            Hexagram object for mutual hexagram
        """
        # Extract mutual hexagram lines (0-indexed: 1,2,3 and 2,3,4)
        mutual_lower = binary_lines[1:4]  # lines 2, 3, 4
        mutual_upper = binary_lines[2:5]  # lines 3, 4, 5
        
        mutual_lines = mutual_lower + mutual_upper
        
        return self._identify_hexagram(mutual_lines, None)
    
    def get_trigram(self, name: str) -> Optional[Trigram]:
        """
        Get trigram information by name.
        
        Args:
            name: Trigram name in Chinese (e.g., "乾")
            
        Returns:
            Trigram object or None if not found
        """
        data = self._trigram_data.get(name)
        if not data:
            return None
        
        return Trigram(
            name_zh=name,
            name_pinyin=data["pinyin"],
            lines=data["lines"],
            element=data["element"],
            nature=data["nature"]
        )
