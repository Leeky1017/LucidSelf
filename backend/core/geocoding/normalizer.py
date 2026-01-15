"""
Input Normalizer

输入文本规范化处理，包括全角转半角、去除地理后缀等。
"""

import re
import unicodedata
from typing import Optional


# Geographic suffixes to remove during normalization
# Chinese suffixes
CHINESE_SUFFIXES = ['市', '省', '州', '区', '郡', '县', '镇', '乡', '村']
# English suffixes (case-insensitive matching)
ENGLISH_SUFFIXES = ['city', 'state', 'province', 'county', 'town', 'village', 'district']


class Normalizer:
    """
    Input text normalization.
    
    输入文本规范化处理类。
    """
    
    def __init__(self):
        # Pre-compile regex patterns for efficiency
        # Pattern for English suffixes (word boundary, case-insensitive)
        suffix_pattern = r'\b(' + '|'.join(ENGLISH_SUFFIXES) + r')$'
        self._english_suffix_re = re.compile(suffix_pattern, re.IGNORECASE)
        
        # Pattern for Chinese suffixes at end of string
        chinese_suffix_pattern = '[' + ''.join(CHINESE_SUFFIXES) + ']$'
        self._chinese_suffix_re = re.compile(chinese_suffix_pattern)
    
    def _fullwidth_to_halfwidth(self, text: str) -> str:
        """
        Convert full-width characters to half-width.
        
        全角字符转半角。
        """
        result = []
        for char in text:
            code = ord(char)
            # Full-width ASCII variants (！to ～) -> half-width (! to ~)
            if 0xFF01 <= code <= 0xFF5E:
                result.append(chr(code - 0xFEE0))
            # Full-width space -> half-width space
            elif code == 0x3000:
                result.append(' ')
            else:
                result.append(char)
        return ''.join(result)
    
    def _remove_suffixes(self, text: str) -> str:
        """
        Remove geographic suffixes from text.
        
        移除地理后缀。
        """
        # Remove Chinese suffixes
        text = self._chinese_suffix_re.sub('', text)
        
        # Remove English suffixes (with optional preceding space)
        text = self._english_suffix_re.sub('', text)
        
        # Clean up any trailing whitespace from suffix removal
        return text.strip()
    
    def normalize(self, text: str) -> str:
        """
        Normalize input text (trim, half-width, case).
        
        规范化输入文本：去除首尾空白、全角转半角、统一大小写、移除地理后缀。
        
        The normalization process:
        1. Trim leading/trailing whitespace
        2. Convert full-width characters to half-width
        3. Normalize Unicode (NFC form)
        4. Standardize case (lowercase for ASCII)
        5. Remove geographic suffixes
        6. Collapse multiple spaces to single space
        
        Args:
            text: Input text to normalize
            
        Returns:
            Normalized text string
        """
        if not text:
            return ''
        
        # Step 1: Trim whitespace
        result = text.strip()
        
        if not result:
            return ''
        
        # Step 2: Convert full-width to half-width
        result = self._fullwidth_to_halfwidth(result)
        
        # Step 3: Unicode normalization (NFC)
        result = unicodedata.normalize('NFC', result)
        
        # Step 4: Standardize case (lowercase)
        result = result.lower()
        
        # Step 5: Remove geographic suffixes
        result = self._remove_suffixes(result)
        
        # Step 6: Collapse multiple spaces to single space
        result = ' '.join(result.split())
        
        return result

    def parse_city_country(self, text: str) -> tuple[str, Optional[str]]:
        """
        Parse city and country from input.
        
        从输入中解析城市名和国家提示。
        
        Supports formats:
        - "city, country" (e.g., "Beijing, China" or "北京, 中国")
        - "city" (no country hint)
        
        Args:
            text: Input text, possibly containing comma-separated city and country
            
        Returns:
            Tuple of (city_name, country_hint) where country_hint may be None
        """
        if not text:
            return ('', None)
        
        # Normalize the text first
        normalized = self.normalize(text)
        
        if not normalized:
            return ('', None)
        
        # Split on comma (supports both , and ，)
        # Replace Chinese comma with standard comma first
        normalized = normalized.replace('，', ',')
        
        parts = [p.strip() for p in normalized.split(',')]
        
        if len(parts) >= 2:
            # Has city and country
            city = parts[0].strip()
            country = parts[1].strip()
            
            # Return country as None if empty after stripping
            if not country:
                return (city, None)
            
            return (city, country)
        else:
            # Just city, no country
            return (normalized, None)
    
    def build_cache_key(self, normalized_query: str, hint_country: Optional[str] = None) -> str:
        """
        Generate stable cache key.
        
        生成稳定的缓存键。
        
        Format: normalized_query + '|' + (hint_country or '')
        
        Args:
            normalized_query: Already normalized query string
            hint_country: Optional country hint (ISO 3166-1 alpha-2 code)
            
        Returns:
            Stable cache key string
        """
        # Ensure normalized_query is actually normalized
        # (caller should have already normalized, but we ensure consistency)
        query = normalized_query.strip().lower() if normalized_query else ''
        
        # Country hint should be uppercase if provided
        country = hint_country.strip().upper() if hint_country else ''
        
        return f"{query}|{country}"
