# backend/calculators/dream/extractor.py
"""
DreamExtractor - Dream Symbol Extractor.

Implements Layer 1 Calculator standard interface, providing:
- Symbol identification from dream text
- Theme detection
- Emotion recognition

Does NOT require location information.

Performance target: < 20ms/extraction (P95)
Accuracy target: Symbol matching recall > 90%
"""

from __future__ import annotations

import time
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

import yaml

from backend.calculators.dream.models import (
    DreamInput,
    DreamFactors,
    DreamSymbol,
    SymbolCategory,
    SYMBOL_CATEGORIES,
    THEMES,
    EMOTIONS,
)


# Data directory path
DATA_DIR = Path(__file__).parent.parent.parent.parent / "data" / "dream"


class DreamExtractor:
    """
    Dream Symbol Extractor.
    
    Conforms to Architecture v3 §4.1 Layer 1 Calculator standard.
    
    Implementation strategy:
    1. Use jieba (Chinese) or simple tokenization (English) for word segmentation
    2. Match tokens against predefined symbol dictionaries
    3. Detect themes using keyword lists
    4. Identify emotions using emotion lexicon
    
    Example:
        >>> from backend.calculators.dream import DreamExtractor, DreamInput
        >>> 
        >>> extractor = DreamExtractor()
        >>> input_data = DreamInput(
        ...     dream_text="我梦见自己在飞翔，下面是一片大海",
        ...     language="zh"
        ... )
        >>> dream_factors = extractor.extract(input_data)
        >>> factor_matrix = dream_factors.to_factor_matrix()
    """
    
    def __init__(self, data_dir: Optional[Path] = None):
        """
        Initialize extractor with symbol dictionaries.
        
        Args:
            data_dir: Optional custom data directory path
        """
        self._data_dir = data_dir or DATA_DIR
        
        # Load dictionaries
        self._symbols_zh: Dict[str, Tuple[str, SymbolCategory]] = {}
        self._symbols_en: Dict[str, Tuple[str, SymbolCategory]] = {}
        self._theme_keywords_zh: Dict[str, List[str]] = {}
        self._theme_keywords_en: Dict[str, List[str]] = {}
        self._emotion_keywords_zh: Dict[str, List[str]] = {}
        self._emotion_keywords_en: Dict[str, List[str]] = {}
        
        self._load_dictionaries()
        
        # Lazy load jieba
        self._jieba = None
    
    def _load_dictionaries(self) -> None:
        """Load symbol, theme, and emotion dictionaries from YAML files."""
        # Load Chinese symbols
        zh_symbols_path = self._data_dir / "symbols_zh.yaml"
        if zh_symbols_path.exists():
            with open(zh_symbols_path, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f) or {}
                self._symbols_zh = self._parse_symbols(data)
        
        # Load English symbols
        en_symbols_path = self._data_dir / "symbols_en.yaml"
        if en_symbols_path.exists():
            with open(en_symbols_path, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f) or {}
                self._symbols_en = self._parse_symbols(data)
        
        # Load themes
        themes_path = self._data_dir / "themes.yaml"
        if themes_path.exists():
            with open(themes_path, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f) or {}
                self._theme_keywords_zh = data.get('zh', {})
                self._theme_keywords_en = data.get('en', {})
        
        # Load emotions
        emotions_path = self._data_dir / "emotions.yaml"
        if emotions_path.exists():
            with open(emotions_path, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f) or {}
                self._emotion_keywords_zh = data.get('zh', {})
                self._emotion_keywords_en = data.get('en', {})
    
    def _parse_symbols(self, data: Dict) -> Dict[str, Tuple[str, SymbolCategory]]:
        """
        Parse symbol dictionary from YAML data.
        
        Expected format:
        {
            "animal": {
                "dog": ["狗", "犬", "小狗"],
                "cat": ["猫", "小猫"]
            },
            ...
        }
        
        Returns:
            Dict mapping keyword to (symbol_name, category)
        """
        result: Dict[str, Tuple[str, SymbolCategory]] = {}
        
        for category, symbols in data.items():
            if category not in SYMBOL_CATEGORIES:
                continue
            
            for symbol_name, keywords in symbols.items():
                if isinstance(keywords, list):
                    for keyword in keywords:
                        result[keyword.lower()] = (symbol_name, category)
                else:
                    # Single keyword
                    result[keywords.lower()] = (symbol_name, category)
        
        return result
    
    def _get_jieba(self):
        """Lazy load jieba for Chinese tokenization."""
        if self._jieba is None:
            import jieba
            self._jieba = jieba
        return self._jieba
    
    def extract(self, input_data: DreamInput) -> DreamFactors:
        """
        Extract symbols, themes, and emotions from dream text.
        
        Args:
            input_data: Input parameters
            
        Returns:
            DreamFactors: Extraction result
        """
        start_time = time.perf_counter()
        
        # Tokenize text
        tokens = self._tokenize(input_data.dream_text, input_data.language)
        
        # Match symbols
        symbols = self._match_symbols(
            input_data.dream_text, 
            tokens, 
            input_data.language
        )
        
        # Detect themes
        themes = self._detect_themes(
            input_data.dream_text, 
            tokens, 
            input_data.language
        )
        
        # Detect emotions
        emotions = self._detect_emotions(
            input_data.dream_text, 
            tokens, 
            input_data.language
        )
        
        calculation_time = (time.perf_counter() - start_time) * 1000
        
        return DreamFactors(
            symbols=symbols,
            themes=themes,
            emotions=emotions,
            raw_tokens=tokens,
            language=input_data.language,
            calculation_time_ms=calculation_time,
        )
    
    def _tokenize(self, text: str, language: str) -> List[str]:
        """
        Tokenize text based on language.
        
        Args:
            text: Input text
            language: Language code ('zh' or 'en')
            
        Returns:
            List of tokens
        """
        if language == "zh":
            # Use jieba for Chinese
            jieba = self._get_jieba()
            return list(jieba.cut(text))
        else:
            # Simple whitespace tokenization for English
            # Also handle punctuation
            import re
            tokens = re.findall(r'\b\w+\b', text.lower())
            return tokens
    
    def _match_symbols(
        self, 
        text: str, 
        tokens: List[str], 
        language: str
    ) -> List[DreamSymbol]:
        """
        Match symbols from text and tokens.
        
        Args:
            text: Original text
            tokens: Tokenized text
            language: Language code
            
        Returns:
            List of matched symbols
        """
        symbols: List[DreamSymbol] = []
        seen_symbols: Set[str] = set()
        
        # Select appropriate dictionary
        symbol_dict = self._symbols_zh if language == "zh" else self._symbols_en
        
        # Match against tokens
        for token in tokens:
            token_lower = token.lower()
            if token_lower in symbol_dict:
                symbol_name, category = symbol_dict[token_lower]
                
                # Avoid duplicates
                symbol_key = f"{category}_{symbol_name}"
                if symbol_key not in seen_symbols:
                    seen_symbols.add(symbol_key)
                    symbols.append(DreamSymbol(
                        symbol=symbol_name,
                        category=category,
                        confidence=0.95,  # High confidence for exact match
                        matched_text=token
                    ))
        
        # Also do substring matching for Chinese (compound words)
        if language == "zh":
            text_lower = text.lower()
            for keyword, (symbol_name, category) in symbol_dict.items():
                if keyword in text_lower:
                    symbol_key = f"{category}_{symbol_name}"
                    if symbol_key not in seen_symbols:
                        seen_symbols.add(symbol_key)
                        symbols.append(DreamSymbol(
                            symbol=symbol_name,
                            category=category,
                            confidence=0.85,  # Slightly lower for substring match
                            matched_text=keyword
                        ))
        
        return symbols
    
    def _detect_themes(
        self, 
        text: str, 
        tokens: List[str], 
        language: str
    ) -> List[str]:
        """
        Detect dream themes from text.
        
        Args:
            text: Original text
            tokens: Tokenized text
            language: Language code
            
        Returns:
            List of detected themes
        """
        themes: List[str] = []
        
        # Select appropriate keywords
        theme_keywords = self._theme_keywords_zh if language == "zh" else self._theme_keywords_en
        
        text_lower = text.lower()
        tokens_set = set(t.lower() for t in tokens)
        
        for theme, keywords in theme_keywords.items():
            if theme not in THEMES:
                continue
                
            for keyword in keywords:
                keyword_lower = keyword.lower()
                # Check both token match and substring match
                if keyword_lower in tokens_set or keyword_lower in text_lower:
                    if theme not in themes:
                        themes.append(theme)
                    break
        
        return themes
    
    def _detect_emotions(
        self, 
        text: str, 
        tokens: List[str], 
        language: str
    ) -> List[str]:
        """
        Detect emotional tones from text.
        
        Args:
            text: Original text
            tokens: Tokenized text
            language: Language code
            
        Returns:
            List of detected emotions
        """
        emotions: List[str] = []
        
        # Select appropriate keywords
        emotion_keywords = self._emotion_keywords_zh if language == "zh" else self._emotion_keywords_en
        
        text_lower = text.lower()
        tokens_set = set(t.lower() for t in tokens)
        
        for emotion, keywords in emotion_keywords.items():
            if emotion not in EMOTIONS:
                continue
                
            for keyword in keywords:
                keyword_lower = keyword.lower()
                # Check both token match and substring match
                if keyword_lower in tokens_set or keyword_lower in text_lower:
                    if emotion not in emotions:
                        emotions.append(emotion)
                    break
        
        return emotions
    
    def get_supported_categories(self) -> List[str]:
        """Get list of supported symbol categories."""
        return list(SYMBOL_CATEGORIES)
    
    def get_supported_themes(self) -> List[str]:
        """Get list of supported themes."""
        return list(THEMES)
    
    def get_supported_emotions(self) -> List[str]:
        """Get list of supported emotions."""
        return list(EMOTIONS)
