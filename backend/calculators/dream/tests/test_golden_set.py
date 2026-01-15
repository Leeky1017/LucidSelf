# backend/calculators/dream/tests/test_golden_set.py
"""
Golden Set Tests for DreamExtractor

Tests the DreamExtractor against the Golden Set of verified test cases.
Requirements: 10.6 - 创建梦境 Golden Set，覆盖高频梦象符号，达到至少 100 个测试用例
"""

import json
import pytest
from pathlib import Path
from typing import Dict, List, Any

from backend.calculators.dream import DreamExtractor, DreamInput


# Path to Golden Set file
GOLDEN_SET_PATH = Path(__file__).parent / "golden_cases" / "dream_golden_set.jsonl"


def load_golden_set() -> List[Dict[str, Any]]:
    """Load Golden Set test cases from JSONL file."""
    cases = []
    if GOLDEN_SET_PATH.exists():
        with open(GOLDEN_SET_PATH, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line:
                    cases.append(json.loads(line))
    return cases


def get_case_ids() -> List[str]:
    """Get list of case IDs for parametrization."""
    cases = load_golden_set()
    return [case['case_id'] for case in cases]


def get_case_by_id(case_id: str) -> Dict[str, Any]:
    """Get a specific case by ID."""
    cases = load_golden_set()
    for case in cases:
        if case['case_id'] == case_id:
            return case
    raise ValueError(f"Case {case_id} not found")


class TestDreamGoldenSet:
    """Golden Set tests for DreamExtractor."""
    
    @pytest.fixture
    def extractor(self):
        return DreamExtractor()
    
    def test_golden_set_exists(self):
        """Verify Golden Set file exists."""
        assert GOLDEN_SET_PATH.exists(), f"Golden Set file not found: {GOLDEN_SET_PATH}"
    
    def test_golden_set_has_minimum_cases(self):
        """Verify Golden Set has at least 100 test cases."""
        cases = load_golden_set()
        assert len(cases) >= 100, f"Golden Set should have at least 100 cases, got {len(cases)}"
    
    def test_golden_set_case_format(self):
        """Verify all Golden Set cases have required fields."""
        cases = load_golden_set()
        required_fields = ['case_id', 'calculator_type', 'input_data', 'expected_output', 'coverage_tags']
        
        for case in cases:
            for field in required_fields:
                assert field in case, f"Case {case.get('case_id', 'unknown')} missing field: {field}"
            
            # Verify input_data has required fields
            assert 'dream_text' in case['input_data'], f"Case {case['case_id']} missing dream_text"
            assert 'language' in case['input_data'], f"Case {case['case_id']} missing language"
    
    def test_golden_set_coverage_tags(self):
        """Verify Golden Set covers all major categories."""
        cases = load_golden_set()
        all_tags = set()
        
        for case in cases:
            all_tags.update(case.get('coverage_tags', []))
        
        # Check for coverage of major categories
        expected_prefixes = ['animal_', 'person_', 'scene_', 'object_', 'nature_', 'body_', 'theme_', 'emotion_']
        
        for prefix in expected_prefixes:
            matching_tags = [t for t in all_tags if t.startswith(prefix)]
            assert len(matching_tags) > 0, f"No coverage tags found for prefix: {prefix}"
    
    def test_golden_set_language_coverage(self):
        """Verify Golden Set covers both Chinese and English."""
        cases = load_golden_set()
        languages = set()
        
        for case in cases:
            languages.add(case['input_data'].get('language'))
        
        assert 'zh' in languages, "Golden Set should include Chinese cases"
        assert 'en' in languages, "Golden Set should include English cases"
    
    @pytest.mark.parametrize("case_id", get_case_ids())
    def test_golden_case_symbols(self, extractor, case_id: str):
        """Test symbol extraction against Golden Set expected output."""
        case = get_case_by_id(case_id)
        
        input_data = DreamInput(
            dream_text=case['input_data']['dream_text'],
            language=case['input_data']['language']
        )
        result = extractor.extract(input_data)
        
        expected_symbols = case['expected_output'].get('symbols', [])
        
        # Build set of extracted (symbol, category) pairs
        extracted_pairs = {(s.symbol, s.category) for s in result.symbols}
        
        # Check that all expected symbols are found
        for expected in expected_symbols:
            expected_pair = (expected['symbol'], expected['category'])
            assert expected_pair in extracted_pairs, \
                f"Case {case_id}: Expected symbol {expected_pair} not found. " \
                f"Extracted: {extracted_pairs}"
    
    @pytest.mark.parametrize("case_id", get_case_ids())
    def test_golden_case_themes(self, extractor, case_id: str):
        """Test theme detection against Golden Set expected output."""
        case = get_case_by_id(case_id)
        
        input_data = DreamInput(
            dream_text=case['input_data']['dream_text'],
            language=case['input_data']['language']
        )
        result = extractor.extract(input_data)
        
        expected_themes = case['expected_output'].get('themes', [])
        
        # Check that all expected themes are found
        for expected in expected_themes:
            assert expected in result.themes, \
                f"Case {case_id}: Expected theme '{expected}' not found. " \
                f"Extracted: {result.themes}"
    
    @pytest.mark.parametrize("case_id", get_case_ids())
    def test_golden_case_emotions(self, extractor, case_id: str):
        """Test emotion detection against Golden Set expected output."""
        case = get_case_by_id(case_id)
        
        input_data = DreamInput(
            dream_text=case['input_data']['dream_text'],
            language=case['input_data']['language']
        )
        result = extractor.extract(input_data)
        
        expected_emotions = case['expected_output'].get('emotions', [])
        
        # Check that all expected emotions are found
        for expected in expected_emotions:
            assert expected in result.emotions, \
                f"Case {case_id}: Expected emotion '{expected}' not found. " \
                f"Extracted: {result.emotions}"


class TestGoldenSetCoverageMatrix:
    """Tests for Golden Set coverage matrix."""
    
    def test_coverage_matrix_by_category(self):
        """Generate and verify coverage matrix by symbol category."""
        cases = load_golden_set()
        
        category_counts = {
            'animal': 0,
            'person': 0,
            'scene': 0,
            'object': 0,
            'nature': 0,
            'body': 0,
        }
        
        for case in cases:
            tags = case.get('coverage_tags', [])
            for tag in tags:
                for category in category_counts:
                    if tag.startswith(f"{category}_"):
                        category_counts[category] += 1
                        break
        
        # Each category should have at least 5 test cases
        for category, count in category_counts.items():
            assert count >= 5, f"Category '{category}' has only {count} cases, expected at least 5"
    
    def test_coverage_matrix_by_theme(self):
        """Generate and verify coverage matrix by theme."""
        cases = load_golden_set()
        
        theme_counts = {}
        
        for case in cases:
            tags = case.get('coverage_tags', [])
            for tag in tags:
                if tag.startswith('theme_'):
                    theme = tag[6:]  # Remove 'theme_' prefix
                    theme_counts[theme] = theme_counts.get(theme, 0) + 1
        
        # Should have at least 5 different themes covered
        assert len(theme_counts) >= 5, f"Only {len(theme_counts)} themes covered, expected at least 5"
    
    def test_coverage_matrix_by_emotion(self):
        """Generate and verify coverage matrix by emotion."""
        cases = load_golden_set()
        
        emotion_counts = {}
        
        for case in cases:
            tags = case.get('coverage_tags', [])
            for tag in tags:
                if tag.startswith('emotion_'):
                    emotion = tag[8:]  # Remove 'emotion_' prefix
                    emotion_counts[emotion] = emotion_counts.get(emotion, 0) + 1
        
        # Should have at least 5 different emotions covered
        assert len(emotion_counts) >= 5, f"Only {len(emotion_counts)} emotions covered, expected at least 5"
    
    def test_print_coverage_summary(self):
        """Print coverage summary for documentation."""
        cases = load_golden_set()
        
        # Count by language
        zh_count = sum(1 for c in cases if c['input_data'].get('language') == 'zh')
        en_count = sum(1 for c in cases if c['input_data'].get('language') == 'en')
        
        # Count by category
        category_counts = {}
        theme_counts = {}
        emotion_counts = {}
        
        for case in cases:
            tags = case.get('coverage_tags', [])
            for tag in tags:
                if tag.startswith('theme_'):
                    theme = tag[6:]
                    theme_counts[theme] = theme_counts.get(theme, 0) + 1
                elif tag.startswith('emotion_'):
                    emotion = tag[8:]
                    emotion_counts[emotion] = emotion_counts.get(emotion, 0) + 1
                elif '_' in tag and not tag.startswith('multi'):
                    category = tag.split('_')[0]
                    if category in ['animal', 'person', 'scene', 'object', 'nature', 'body']:
                        category_counts[category] = category_counts.get(category, 0) + 1
        
        print(f"\n=== Dream Golden Set Coverage Summary ===")
        print(f"Total cases: {len(cases)}")
        print(f"Chinese cases: {zh_count}")
        print(f"English cases: {en_count}")
        print(f"\nCategory coverage:")
        for cat, count in sorted(category_counts.items()):
            print(f"  {cat}: {count}")
        print(f"\nTheme coverage:")
        for theme, count in sorted(theme_counts.items()):
            print(f"  {theme}: {count}")
        print(f"\nEmotion coverage:")
        for emotion, count in sorted(emotion_counts.items()):
            print(f"  {emotion}: {count}")
        
        # This test always passes - it's for documentation
        assert True
