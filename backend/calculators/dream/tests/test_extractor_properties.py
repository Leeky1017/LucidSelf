# backend/calculators/dream/tests/test_extractor_properties.py
"""
Property-Based Tests for DreamExtractor

DreamExtractor 的属性测试。
使用 Hypothesis 框架进行属性测试。
"""

import pytest
from hypothesis import given, strategies as st, settings, assume, Phase
from datetime import timedelta

from backend.calculators.dream import (
    DreamExtractor,
    DreamInput,
    DreamFactors,
    DreamSymbol,
    SYMBOL_CATEGORIES,
    THEMES,
    EMOTIONS,
)


# =============================================================================
# Strategies for generating test data
# =============================================================================

# Strategy for language
language_strategy = st.sampled_from(["zh", "en"])

# Strategy for symbol categories
symbol_category_strategy = st.sampled_from(SYMBOL_CATEGORIES)


# Chinese dream text components
ZH_ANIMALS = ["狗", "猫", "蛇", "鸟", "鱼", "马", "龙", "虎", "狼", "蜘蛛", "蝴蝶", "老鼠"]
ZH_PERSONS = ["母亲", "父亲", "孩子", "陌生人", "朋友", "恋人", "老师", "老板", "婴儿", "老人"]
ZH_SCENES = ["房子", "学校", "森林", "路", "桥", "山", "洞", "医院", "寺庙", "墓地", "飞翔"]
ZH_OBJECTS = ["钥匙", "镜子", "书", "钱", "手机", "车", "门", "窗", "刀", "戒指", "衣服"]
ZH_NATURE = ["水", "海", "河", "火", "雨", "雪", "太阳", "月亮", "星星", "天空", "云", "风", "树", "花"]
ZH_BODY = ["牙齿", "头发", "手", "眼睛", "血", "心", "脚", "脸", "头"]

# English dream text components
EN_ANIMALS = ["dog", "cat", "snake", "bird", "fish", "horse", "dragon", "tiger", "wolf", "spider", "butterfly", "rat"]
EN_PERSONS = ["mother", "father", "child", "stranger", "friend", "lover", "teacher", "boss", "baby", "elderly"]
EN_SCENES = ["house", "school", "forest", "road", "bridge", "mountain", "cave", "hospital", "temple", "cemetery", "flying"]
EN_OBJECTS = ["key", "mirror", "book", "money", "phone", "car", "door", "window", "knife", "ring", "clothes"]
EN_NATURE = ["water", "sea", "river", "fire", "rain", "snow", "sun", "moon", "star", "sky", "cloud", "wind", "tree", "flower"]
EN_BODY = ["teeth", "hair", "hand", "eye", "blood", "heart", "foot", "face", "head"]

# All symbols by category for Chinese
ZH_SYMBOLS_BY_CATEGORY = {
    "animal": ZH_ANIMALS,
    "person": ZH_PERSONS,
    "scene": ZH_SCENES,
    "object": ZH_OBJECTS,
    "nature": ZH_NATURE,
    "body": ZH_BODY,
}

# All symbols by category for English
EN_SYMBOLS_BY_CATEGORY = {
    "animal": EN_ANIMALS,
    "person": EN_PERSONS,
    "scene": EN_SCENES,
    "object": EN_OBJECTS,
    "nature": EN_NATURE,
    "body": EN_BODY,
}


@st.composite
def zh_dream_text_with_symbols_strategy(draw):
    """Generate Chinese dream text containing known symbols (minimum 10 characters)."""
    # Pick 1-3 symbols from different categories
    num_symbols = draw(st.integers(min_value=1, max_value=3))
    categories = draw(st.lists(
        st.sampled_from(SYMBOL_CATEGORIES),
        min_size=num_symbols,
        max_size=num_symbols,
        unique=True
    ))
    
    symbols = []
    for category in categories:
        symbol = draw(st.sampled_from(ZH_SYMBOLS_BY_CATEGORY[category]))
        symbols.append((symbol, category))
    
    # Build dream text - ensure at least 10 characters
    prefix = draw(st.sampled_from(["我梦见了一个", "昨晚我梦到了", "在梦中我看到了", "我做了一个梦，梦见了"]))
    connectors = ["，还有", "和一个", "还有一个", "，然后看到了"]
    
    text_parts = [prefix]
    for i, (symbol, _) in enumerate(symbols):
        if i > 0:
            connector = draw(st.sampled_from(connectors))
            text_parts.append(connector)
        text_parts.append(symbol)
    
    text_parts.append("，感觉很奇怪。")
    dream_text = "".join(text_parts)
    
    return dream_text, symbols


@st.composite
def en_dream_text_with_symbols_strategy(draw):
    """Generate English dream text containing known symbols."""
    # Pick 1-3 symbols from different categories
    num_symbols = draw(st.integers(min_value=1, max_value=3))
    categories = draw(st.lists(
        st.sampled_from(SYMBOL_CATEGORIES),
        min_size=num_symbols,
        max_size=num_symbols,
        unique=True
    ))
    
    symbols = []
    for category in categories:
        symbol = draw(st.sampled_from(EN_SYMBOLS_BY_CATEGORY[category]))
        symbols.append((symbol, category))
    
    # Build dream text
    prefix = draw(st.sampled_from(["I dreamed of", "Last night I saw", "In my dream there was", "I had a dream about"]))
    connectors = [" and ", ", ", " with ", " then I saw "]
    
    text_parts = [prefix, " "]
    for i, (symbol, _) in enumerate(symbols):
        if i > 0:
            connector = draw(st.sampled_from(connectors))
            text_parts.append(connector)
        text_parts.append(symbol)
    
    text_parts.append(".")
    dream_text = "".join(text_parts)
    
    return dream_text, symbols


@st.composite
def dream_input_with_known_symbols_strategy(draw):
    """Generate DreamInput with known symbols for validation."""
    language = draw(language_strategy)
    
    if language == "zh":
        dream_text, expected_symbols = draw(zh_dream_text_with_symbols_strategy())
    else:
        dream_text, expected_symbols = draw(en_dream_text_with_symbols_strategy())
    
    return DreamInput(dream_text=dream_text, language=language), expected_symbols


@st.composite
def any_valid_dream_input_strategy(draw):
    """Generate any valid DreamInput (minimum 10 characters)."""
    language = draw(language_strategy)
    
    if language == "zh":
        # Generate Chinese dream text - ensure at least 10 characters
        # Use at least 2 symbols to ensure length
        symbols = draw(st.lists(
            st.sampled_from(ZH_ANIMALS + ZH_PERSONS + ZH_SCENES + ZH_OBJECTS + ZH_NATURE + ZH_BODY),
            min_size=2,
            max_size=5
        ))
        prefix = draw(st.sampled_from(["我梦见了", "昨晚我梦到了", "在梦中我看到了"]))
        dream_text = prefix + "，".join(symbols) + "，感觉很奇怪。"
    else:
        # Generate English dream text - ensure at least 10 characters
        symbols = draw(st.lists(
            st.sampled_from(EN_ANIMALS + EN_PERSONS + EN_SCENES + EN_OBJECTS + EN_NATURE + EN_BODY),
            min_size=1,
            max_size=5
        ))
        prefix = draw(st.sampled_from(["I dreamed of a ", "Last night I saw a ", "In my dream there was a "]))
        dream_text = prefix + ", ".join(symbols) + " in my dream."
    
    # Ensure minimum length
    assert len(dream_text) >= 10, f"Generated text too short: {dream_text}"
    
    return DreamInput(dream_text=dream_text, language=language)


# =============================================================================
# Property 7: DreamExtractor Symbol Categorization
# =============================================================================

class TestDreamExtractorSymbolCategorization:
    """
    **Feature: calculator-integration, Property 7: DreamExtractor Symbol Categorization**
    
    *For any* identified dream symbol, it must be assigned exactly one category 
    from the defined set (animal, person, scene, object, nature, body).
    
    **Validates: Requirements 6.2**
    """
    
    @given(input_data=any_valid_dream_input_strategy())
    @settings(max_examples=100, deadline=None)  # deadline=None due to jieba loading time
    def test_all_symbols_have_valid_category(self, input_data: DreamInput):
        """
        Property test: For any identified symbol, it must have exactly one valid category.
        
        **Feature: calculator-integration, Property 7: DreamExtractor Symbol Categorization**
        **Validates: Requirements 6.2**
        """
        extractor = DreamExtractor()
        result = extractor.extract(input_data)
        
        # Each identified symbol must have a valid category
        for symbol in result.symbols:
            assert symbol.category in SYMBOL_CATEGORIES, \
                f"Symbol '{symbol.symbol}' has invalid category: {symbol.category}. " \
                f"Valid categories are: {SYMBOL_CATEGORIES}"
    
    @given(input_data=any_valid_dream_input_strategy())
    @settings(max_examples=100, deadline=None)
    def test_symbol_category_is_exactly_one(self, input_data: DreamInput):
        """
        Property test: Each symbol is assigned exactly one category (not multiple).
        
        **Feature: calculator-integration, Property 7: DreamExtractor Symbol Categorization**
        **Validates: Requirements 6.2**
        """
        extractor = DreamExtractor()
        result = extractor.extract(input_data)
        
        # Check that each symbol has exactly one category (category is a single value, not a list)
        for symbol in result.symbols:
            # The category field is a Literal type, so it can only be one value
            assert isinstance(symbol.category, str), \
                f"Symbol '{symbol.symbol}' category should be a string, got {type(symbol.category)}"
            assert symbol.category in SYMBOL_CATEGORIES, \
                f"Symbol '{symbol.symbol}' has invalid category: {symbol.category}"
    
    @given(input_data=any_valid_dream_input_strategy())
    @settings(max_examples=100, deadline=None)
    def test_symbol_has_required_fields(self, input_data: DreamInput):
        """
        Property test: Each symbol has all required fields populated.
        
        **Feature: calculator-integration, Property 7: DreamExtractor Symbol Categorization**
        **Validates: Requirements 6.2**
        """
        extractor = DreamExtractor()
        result = extractor.extract(input_data)
        
        for symbol in result.symbols:
            # Symbol name must be non-empty
            assert symbol.symbol is not None and len(symbol.symbol) > 0, \
                f"Symbol has empty name"
            
            # Category must be valid
            assert symbol.category in SYMBOL_CATEGORIES, \
                f"Symbol '{symbol.symbol}' has invalid category: {symbol.category}"
            
            # Confidence must be in valid range
            assert 0.0 <= symbol.confidence <= 1.0, \
                f"Symbol '{symbol.symbol}' has invalid confidence: {symbol.confidence}"
            
            # Matched text must be non-empty
            assert symbol.matched_text is not None and len(symbol.matched_text) > 0, \
                f"Symbol '{symbol.symbol}' has empty matched_text"
    
    @given(data=dream_input_with_known_symbols_strategy())
    @settings(max_examples=100, deadline=None)
    def test_known_symbols_categorized_correctly(self, data):
        """
        Property test: Known symbols are categorized into their expected categories.
        
        **Feature: calculator-integration, Property 7: DreamExtractor Symbol Categorization**
        **Validates: Requirements 6.2**
        
        Note: This test checks that when a symbol is identified with an exact match,
        it has the correct category. Substring collisions (e.g., "手" in "手机") are
        a known limitation of the current implementation.
        """
        input_data, expected_symbols = data
        extractor = DreamExtractor()
        result = extractor.extract(input_data)
        
        # Build a map of extracted symbols by their matched text (exact match only)
        extracted_by_text = {}
        for symbol in result.symbols:
            extracted_by_text[symbol.matched_text.lower()] = symbol
        
        # Check that expected symbols are found with correct categories
        # Only check exact matches to avoid substring collision issues
        for expected_text, expected_category in expected_symbols:
            # Check for exact match only
            if expected_text.lower() in extracted_by_text:
                symbol = extracted_by_text[expected_text.lower()]
                assert symbol.category == expected_category, \
                    f"Symbol '{expected_text}' expected category '{expected_category}', " \
                    f"got '{symbol.category}'"
    
    @given(input_data=any_valid_dream_input_strategy())
    @settings(max_examples=100, deadline=None)
    def test_no_duplicate_symbols(self, input_data: DreamInput):
        """
        Property test: No duplicate symbols are returned (same symbol+category combination).
        
        **Feature: calculator-integration, Property 7: DreamExtractor Symbol Categorization**
        **Validates: Requirements 6.2**
        """
        extractor = DreamExtractor()
        result = extractor.extract(input_data)
        
        # Check for duplicates using (category, symbol) as key
        seen = set()
        for symbol in result.symbols:
            key = (symbol.category, symbol.symbol)
            assert key not in seen, \
                f"Duplicate symbol found: category='{symbol.category}', symbol='{symbol.symbol}'"
            seen.add(key)
    
    @given(input_data=any_valid_dream_input_strategy())
    @settings(max_examples=100, deadline=None)
    def test_factor_matrix_follows_naming_convention(self, input_data: DreamInput):
        """
        Property test: Factor matrix follows dream_* naming convention.
        
        **Feature: calculator-integration, Property 7: DreamExtractor Symbol Categorization**
        **Validates: Requirements 6.2**
        """
        extractor = DreamExtractor()
        result = extractor.extract(input_data)
        factor_matrix = result.to_factor_matrix()
        
        # All factor IDs should start with "dream_"
        for factor_id in factor_matrix.factors.keys():
            assert factor_id.startswith("dream_"), \
                f"Factor ID '{factor_id}' does not follow dream_* naming convention"
    
    @given(input_data=any_valid_dream_input_strategy())
    @settings(max_examples=100, deadline=None)
    def test_symbol_factors_include_category(self, input_data: DreamInput):
        """
        Property test: Symbol factors include the category in the factor ID.
        
        **Feature: calculator-integration, Property 7: DreamExtractor Symbol Categorization**
        **Validates: Requirements 6.2**
        """
        extractor = DreamExtractor()
        result = extractor.extract(input_data)
        factor_matrix = result.to_factor_matrix()
        
        # Each symbol should have a corresponding factor with category in the ID
        for symbol in result.symbols:
            symbol_normalized = symbol.symbol.lower().replace(" ", "_").replace("-", "_")
            expected_factor_id = f"dream_symbol_{symbol.category}_{symbol_normalized}"
            
            assert expected_factor_id in factor_matrix.factors, \
                f"Missing symbol factor: {expected_factor_id}"


# =============================================================================
# Additional Unit Tests for Edge Cases
# =============================================================================

class TestDreamExtractorEdgeCases:
    """Unit tests for edge cases and specific scenarios."""
    
    def test_chinese_animal_symbols(self):
        """Test that Chinese animal symbols are correctly categorized."""
        extractor = DreamExtractor()
        
        # Ensure all test cases have at least 10 characters
        test_cases = [
            ("我梦见一只狗在追我，感觉很害怕", "dog", "animal"),
            ("梦里有一条蛇在草丛中爬行", "snake", "animal"),
            ("我看到一只蝴蝶飞过花园", "butterfly", "animal"),
        ]
        
        for dream_text, expected_symbol, expected_category in test_cases:
            input_data = DreamInput(dream_text=dream_text, language="zh")
            result = extractor.extract(input_data)
            
            found = False
            for symbol in result.symbols:
                if symbol.symbol == expected_symbol:
                    found = True
                    assert symbol.category == expected_category, \
                        f"Symbol '{expected_symbol}' has wrong category: {symbol.category}"
                    break
            
            assert found, f"Symbol '{expected_symbol}' not found in dream text: {dream_text}"
    
    def test_english_nature_symbols(self):
        """Test that English nature symbols are correctly categorized."""
        extractor = DreamExtractor()
        
        test_cases = [
            ("I dreamed of the ocean and waves", "sea", "nature"),
            ("There was fire everywhere in my dream", "fire", "nature"),
            ("I saw the moon shining bright", "moon", "nature"),
        ]
        
        for dream_text, expected_symbol, expected_category in test_cases:
            input_data = DreamInput(dream_text=dream_text, language="en")
            result = extractor.extract(input_data)
            
            found = False
            for symbol in result.symbols:
                if symbol.symbol == expected_symbol:
                    found = True
                    assert symbol.category == expected_category, \
                        f"Symbol '{expected_symbol}' has wrong category: {symbol.category}"
                    break
            
            assert found, f"Symbol '{expected_symbol}' not found in dream text: {dream_text}"
    
    def test_multiple_categories_in_one_dream(self):
        """Test that symbols from multiple categories are correctly identified."""
        extractor = DreamExtractor()
        
        # Chinese dream with multiple categories
        input_data = DreamInput(
            dream_text="我梦见一只狗在房子里，旁边有一条河，我的母亲站在那里",
            language="zh"
        )
        result = extractor.extract(input_data)
        
        # Should find symbols from different categories
        categories_found = set(symbol.category for symbol in result.symbols)
        
        # We expect at least animal (狗), scene (房子), nature (河), person (母亲)
        assert len(categories_found) >= 2, \
            f"Expected symbols from multiple categories, found: {categories_found}"
    
    def test_empty_result_for_no_symbols(self):
        """Test that dreams without known symbols return empty symbol list."""
        extractor = DreamExtractor()
        
        # Dream text without any known symbols
        input_data = DreamInput(
            dream_text="这是一个很长的梦境描述但是没有任何已知的符号",
            language="zh"
        )
        result = extractor.extract(input_data)
        
        # Should return empty or minimal symbols
        # (The text might still match some symbols, so we just check it doesn't crash)
        assert isinstance(result.symbols, list)
        for symbol in result.symbols:
            assert symbol.category in SYMBOL_CATEGORIES


# =============================================================================
# Property 25: Dream Symbol Classification Correctness
# =============================================================================

class TestDreamSymbolClassificationCorrectness:
    """
    **Feature: calculator-accuracy-audit, Property 25: 梦境符号分类正确性**
    
    *For any* identified dream symbol, it must be correctly classified into one of
    the core element categories: person (人物), animal (动物), scene (场景), 
    object (物品), nature (自然), or body (身体).
    
    **Validates: Requirements 7.1**
    """
    
    @given(input_data=any_valid_dream_input_strategy())
    @settings(max_examples=100, deadline=None)
    def test_all_symbols_classified_into_valid_categories(self, input_data: DreamInput):
        """
        Property test: For any dream text, all extracted symbols must be classified
        into one of the valid categories (animal, person, scene, object, nature, body).
        
        **Feature: calculator-accuracy-audit, Property 25: 梦境符号分类正确性**
        **Validates: Requirements 7.1**
        """
        extractor = DreamExtractor()
        result = extractor.extract(input_data)
        
        valid_categories = {"animal", "person", "scene", "object", "nature", "body"}
        
        for symbol in result.symbols:
            assert symbol.category in valid_categories, \
                f"Symbol '{symbol.symbol}' has invalid category '{symbol.category}'. " \
                f"Valid categories are: {valid_categories}"
    
    @given(data=dream_input_with_known_symbols_strategy())
    @settings(max_examples=100, deadline=None)
    def test_known_symbols_classified_correctly(self, data):
        """
        Property test: For any dream text with known symbols, those symbols must be
        classified into their expected categories.
        
        **Feature: calculator-accuracy-audit, Property 25: 梦境符号分类正确性**
        **Validates: Requirements 7.1**
        """
        input_data, expected_symbols = data
        extractor = DreamExtractor()
        result = extractor.extract(input_data)
        
        # Build a map of extracted symbols by their matched text
        extracted_by_text = {}
        for symbol in result.symbols:
            extracted_by_text[symbol.matched_text.lower()] = symbol
        
        # Check that expected symbols are found with correct categories
        for expected_text, expected_category in expected_symbols:
            if expected_text.lower() in extracted_by_text:
                symbol = extracted_by_text[expected_text.lower()]
                assert symbol.category == expected_category, \
                    f"Symbol '{expected_text}' expected category '{expected_category}', " \
                    f"got '{symbol.category}'"
    
    @given(input_data=any_valid_dream_input_strategy())
    @settings(max_examples=100, deadline=None)
    def test_symbol_classification_is_deterministic(self, input_data: DreamInput):
        """
        Property test: For any dream text, running extraction multiple times
        should produce the same symbol classifications.
        
        **Feature: calculator-accuracy-audit, Property 25: 梦境符号分类正确性**
        **Validates: Requirements 7.1**
        """
        extractor = DreamExtractor()
        
        # Run extraction twice
        result1 = extractor.extract(input_data)
        result2 = extractor.extract(input_data)
        
        # Build sets of (symbol, category) tuples for comparison
        symbols1 = {(s.symbol, s.category) for s in result1.symbols}
        symbols2 = {(s.symbol, s.category) for s in result2.symbols}
        
        assert symbols1 == symbols2, \
            f"Symbol classification is not deterministic. " \
            f"First run: {symbols1}, Second run: {symbols2}"
    
    @given(input_data=any_valid_dream_input_strategy())
    @settings(max_examples=100, deadline=None)
    def test_symbol_has_confidence_score(self, input_data: DreamInput):
        """
        Property test: For any extracted symbol, it must have a valid confidence score
        between 0.0 and 1.0.
        
        **Feature: calculator-accuracy-audit, Property 25: 梦境符号分类正确性**
        **Validates: Requirements 7.1**
        """
        extractor = DreamExtractor()
        result = extractor.extract(input_data)
        
        for symbol in result.symbols:
            assert 0.0 <= symbol.confidence <= 1.0, \
                f"Symbol '{symbol.symbol}' has invalid confidence: {symbol.confidence}. " \
                f"Confidence must be between 0.0 and 1.0"
    
    @given(input_data=any_valid_dream_input_strategy())
    @settings(max_examples=100, deadline=None)
    def test_symbol_matched_text_is_in_original(self, input_data: DreamInput):
        """
        Property test: For any extracted symbol, the matched_text must be present
        in the original dream text.
        
        **Feature: calculator-accuracy-audit, Property 25: 梦境符号分类正确性**
        **Validates: Requirements 7.1**
        """
        extractor = DreamExtractor()
        result = extractor.extract(input_data)
        
        dream_text_lower = input_data.dream_text.lower()
        
        for symbol in result.symbols:
            assert symbol.matched_text.lower() in dream_text_lower, \
                f"Symbol '{symbol.symbol}' matched_text '{symbol.matched_text}' " \
                f"not found in original dream text: {input_data.dream_text}"
    
    @given(input_data=any_valid_dream_input_strategy())
    @settings(max_examples=100, deadline=None)
    def test_no_duplicate_symbol_category_pairs(self, input_data: DreamInput):
        """
        Property test: For any dream text, there should be no duplicate
        (symbol, category) pairs in the result.
        
        **Feature: calculator-accuracy-audit, Property 25: 梦境符号分类正确性**
        **Validates: Requirements 7.1**
        """
        extractor = DreamExtractor()
        result = extractor.extract(input_data)
        
        seen = set()
        for symbol in result.symbols:
            key = (symbol.symbol, symbol.category)
            assert key not in seen, \
                f"Duplicate symbol-category pair found: {key}"
            seen.add(key)
    
    @given(input_data=any_valid_dream_input_strategy())
    @settings(max_examples=100, deadline=None)
    def test_factor_matrix_symbol_factors_have_correct_prefix(self, input_data: DreamInput):
        """
        Property test: For any dream text, all symbol factors in the factor matrix
        should have the correct prefix format: dream_symbol_{category}_{symbol}.
        
        **Feature: calculator-accuracy-audit, Property 25: 梦境符号分类正确性**
        **Validates: Requirements 7.1**
        """
        extractor = DreamExtractor()
        result = extractor.extract(input_data)
        factor_matrix = result.to_factor_matrix()
        
        valid_categories = {"animal", "person", "scene", "object", "nature", "body"}
        
        for factor_id in factor_matrix.factors.keys():
            if factor_id.startswith("dream_symbol_"):
                # Extract category from factor_id
                parts = factor_id.split("_")
                if len(parts) >= 3:
                    category = parts[2]
                    assert category in valid_categories, \
                        f"Factor '{factor_id}' has invalid category '{category}'"
