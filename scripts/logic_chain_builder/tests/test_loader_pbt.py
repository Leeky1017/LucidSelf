# scripts/logic_chain_builder/tests/test_loader_pbt.py
"""
Property-Based Tests for SchemaLoader

**Feature: logic-chain-builder, Property 9: Output Schema Conformance** (partial - input validation)
**Validates: Requirements 1.4**

Tests that SchemaLoader correctly validates and loads YAML data:
- Loaded snippets conform to NarrativeSnippet schema
- Loaded relations conform to ConfigRelation schema
- Invalid data is handled gracefully
"""

import pytest
import tempfile
import os
from pathlib import Path
from typing import List, Optional

import yaml
from hypothesis import given, settings, assume
from hypothesis import strategies as st

from scripts.logic_chain_builder.loader import (
    SchemaLoader,
    SchemaValidationError,
)
from scripts.schema_extractor.models import NarrativeSnippet, ConfigRelation, SnippetRole


# =============================================================================
# Hypothesis Strategies
# =============================================================================

# Strategy for valid snippet roles
snippet_role_strategy = st.sampled_from([role.value for role in SnippetRole])

# Strategy for snippet IDs
snippet_id_strategy = st.from_regex(r"ns_[a-z]{2,5}_\d{3}", fullmatch=True)

# Strategy for relation IDs
relation_id_strategy = st.from_regex(r"rel_[a-z]{2,5}_\d{3}", fullmatch=True)

# Strategy for trigger text
trigger_strategy = st.text(min_size=1, max_size=50, alphabet=st.characters(
    whitelist_categories=('L', 'N', 'P'),
    whitelist_characters=' '
)).filter(lambda x: x.strip())

# Strategy for snippet text
snippet_text_strategy = st.text(min_size=5, max_size=200, alphabet=st.characters(
    whitelist_categories=('L', 'N', 'P'),
    whitelist_characters=' '
)).filter(lambda x: x.strip())

# Strategy for source reference
source_ref_strategy = st.from_regex(r"《[^》]+》#[^#]+", fullmatch=True)

# Strategy for relation types
relation_type_strategy = st.sampled_from([
    "hierarchy", "dependency", "cooperation", "supports",
    "conditional", "gateway", "conflict", "triad", "behavior", "dynamic"
])

# Strategy for effect directions
effect_direction_strategy = st.sampled_from([
    "增益", "损害", "限制", "中性", "混合", "主从", "包含",
    "强制", "条件依赖", "通则吉滞则凶", "主导", "关键", "动态", "正向增强"
])


@st.composite
def valid_snippet_dict_strategy(draw):
    """Generate a valid snippet dictionary."""
    return {
        "snippet_id": draw(snippet_id_strategy),
        "trigger": draw(trigger_strategy),
        "factor_trigger": draw(st.one_of(st.none(), trigger_strategy)),
        "role": draw(snippet_role_strategy),
        "snippet_text": draw(snippet_text_strategy),
        "source_ref": draw(source_ref_strategy),
        "source_book": draw(st.one_of(st.none(), st.text(min_size=1, max_size=20))),
        "source_chapter": draw(st.one_of(st.none(), st.text(min_size=1, max_size=50))),
    }


@st.composite
def valid_relation_dict_strategy(draw):
    """Generate a valid relation dictionary."""
    return {
        "relation_id": draw(relation_id_strategy),
        "relation_type": draw(relation_type_strategy),
        "factor_a": draw(st.from_regex(r"[a-z][a-z0-9_]*", fullmatch=True)),
        "factor_b": draw(st.from_regex(r"[a-z][a-z0-9_]*", fullmatch=True)),
        "relation_nature": draw(st.text(min_size=1, max_size=50)),
        "condition_constraint": draw(st.text(min_size=1, max_size=100)),
        "effect_direction": draw(effect_direction_strategy),
        "source_ref": draw(source_ref_strategy),
        "source_book": draw(st.one_of(st.none(), st.text(min_size=1, max_size=20))),
        "source_chapter": draw(st.one_of(st.none(), st.text(min_size=1, max_size=50))),
    }


# =============================================================================
# Property-Based Tests
# =============================================================================


class TestSnippetLoadingSchemaConformance:
    """
    **Feature: logic-chain-builder, Property 9: Output Schema Conformance** (partial - input validation)
    **Validates: Requirements 1.4**
    
    *For any* valid snippet YAML file, loading it should produce valid NarrativeSnippet objects
    that pass Pydantic validation.
    """

    @settings(max_examples=100)
    @given(snippets=st.lists(valid_snippet_dict_strategy(), min_size=1, max_size=10))
    def test_valid_snippets_load_successfully(self, snippets: List[dict]):
        """
        **Feature: logic-chain-builder, Property 9: Output Schema Conformance**
        **Validates: Requirements 1.4**
        
        Property: Any YAML file with valid snippet structure should load successfully
        and produce NarrativeSnippet objects.
        """
        with tempfile.TemporaryDirectory() as tmpdir:
            snippets_dir = Path(tmpdir) / "snippets"
            relations_dir = Path(tmpdir) / "relations"
            snippets_dir.mkdir()
            relations_dir.mkdir()
            
            # Write snippets file
            book_id = "test_book"
            snippets_file = snippets_dir / f"{book_id}_snippets.yaml"
            data = {
                "book_id": book_id,
                "snippets": snippets
            }
            with open(snippets_file, 'w', encoding='utf-8') as f:
                yaml.dump(data, f, allow_unicode=True)
            
            # Write empty relations file (required for list_available_books)
            relations_file = relations_dir / f"{book_id}_relations.yaml"
            with open(relations_file, 'w', encoding='utf-8') as f:
                yaml.dump({"book_id": book_id, "relations": []}, f)
            
            # Load and verify
            loader = SchemaLoader(
                snippets_dir=str(snippets_dir),
                relations_dir=str(relations_dir)
            )
            loaded_snippets = loader.load_snippets(book_id)
            
            # All loaded snippets should be valid NarrativeSnippet instances
            assert len(loaded_snippets) == len(snippets)
            for snippet in loaded_snippets:
                assert isinstance(snippet, NarrativeSnippet)
                assert snippet.snippet_id is not None
                assert snippet.trigger is not None
                assert snippet.role is not None
                assert snippet.snippet_text is not None
                assert snippet.source_ref is not None

    @settings(max_examples=100)
    @given(relations=st.lists(valid_relation_dict_strategy(), min_size=1, max_size=10))
    def test_valid_relations_load_successfully(self, relations: List[dict]):
        """
        **Feature: logic-chain-builder, Property 9: Output Schema Conformance**
        **Validates: Requirements 1.4**
        
        Property: Any YAML file with valid relation structure should load successfully
        and produce ConfigRelation objects.
        """
        with tempfile.TemporaryDirectory() as tmpdir:
            snippets_dir = Path(tmpdir) / "snippets"
            relations_dir = Path(tmpdir) / "relations"
            snippets_dir.mkdir()
            relations_dir.mkdir()
            
            # Write relations file
            book_id = "test_book"
            relations_file = relations_dir / f"{book_id}_relations.yaml"
            data = {
                "book_id": book_id,
                "relations": relations
            }
            with open(relations_file, 'w', encoding='utf-8') as f:
                yaml.dump(data, f, allow_unicode=True)
            
            # Write empty snippets file
            snippets_file = snippets_dir / f"{book_id}_snippets.yaml"
            with open(snippets_file, 'w', encoding='utf-8') as f:
                yaml.dump({"book_id": book_id, "snippets": []}, f)
            
            # Load and verify
            loader = SchemaLoader(
                snippets_dir=str(snippets_dir),
                relations_dir=str(relations_dir)
            )
            loaded_relations = loader.load_relations(book_id)
            
            # All loaded relations should be valid ConfigRelation instances
            assert len(loaded_relations) == len(relations)
            for relation in loaded_relations:
                assert isinstance(relation, ConfigRelation)
                assert relation.relation_id is not None
                assert relation.relation_type is not None
                assert relation.factor_a is not None
                assert relation.factor_b is not None


class TestSchemaLoaderErrorHandling:
    """
    Tests for SchemaLoader error handling.
    
    **Validates: Requirements 1.3, 1.4**
    """

    def test_missing_snippets_file_raises_error(self):
        """Property: Missing snippets file should raise FileNotFoundError."""
        with tempfile.TemporaryDirectory() as tmpdir:
            loader = SchemaLoader(
                snippets_dir=tmpdir,
                relations_dir=tmpdir
            )
            with pytest.raises(FileNotFoundError):
                loader.load_snippets("nonexistent_book")

    def test_missing_relations_file_raises_error(self):
        """Property: Missing relations file should raise FileNotFoundError."""
        with tempfile.TemporaryDirectory() as tmpdir:
            loader = SchemaLoader(
                snippets_dir=tmpdir,
                relations_dir=tmpdir
            )
            with pytest.raises(FileNotFoundError):
                loader.load_relations("nonexistent_book")

    def test_invalid_yaml_raises_validation_error(self):
        """Property: Invalid YAML syntax should raise SchemaValidationError."""
        with tempfile.TemporaryDirectory() as tmpdir:
            snippets_dir = Path(tmpdir) / "snippets"
            snippets_dir.mkdir()
            
            # Write invalid YAML
            book_id = "test_book"
            snippets_file = snippets_dir / f"{book_id}_snippets.yaml"
            with open(snippets_file, 'w', encoding='utf-8') as f:
                f.write("invalid: yaml: content: [")
            
            loader = SchemaLoader(
                snippets_dir=str(snippets_dir),
                relations_dir=tmpdir
            )
            with pytest.raises(SchemaValidationError):
                loader.load_snippets(book_id)

    def test_missing_snippets_key_raises_validation_error(self):
        """Property: YAML without 'snippets' key should raise SchemaValidationError."""
        with tempfile.TemporaryDirectory() as tmpdir:
            snippets_dir = Path(tmpdir) / "snippets"
            snippets_dir.mkdir()
            
            # Write YAML without snippets key
            book_id = "test_book"
            snippets_file = snippets_dir / f"{book_id}_snippets.yaml"
            with open(snippets_file, 'w', encoding='utf-8') as f:
                yaml.dump({"book_id": book_id, "data": []}, f)
            
            loader = SchemaLoader(
                snippets_dir=str(snippets_dir),
                relations_dir=tmpdir
            )
            with pytest.raises(SchemaValidationError):
                loader.load_snippets(book_id)

    def test_missing_relations_key_raises_validation_error(self):
        """Property: YAML without 'relations' key should raise SchemaValidationError."""
        with tempfile.TemporaryDirectory() as tmpdir:
            relations_dir = Path(tmpdir) / "relations"
            relations_dir.mkdir()
            
            # Write YAML without relations key
            book_id = "test_book"
            relations_file = relations_dir / f"{book_id}_relations.yaml"
            with open(relations_file, 'w', encoding='utf-8') as f:
                yaml.dump({"book_id": book_id, "data": []}, f)
            
            loader = SchemaLoader(
                snippets_dir=tmpdir,
                relations_dir=str(relations_dir)
            )
            with pytest.raises(SchemaValidationError):
                loader.load_relations(book_id)


class TestListAvailableBooks:
    """
    Tests for list_available_books functionality.
    
    **Validates: Requirements 1.1, 1.2**
    """

    @settings(max_examples=50)
    @given(book_ids=st.lists(
        st.from_regex(r"[a-z][a-z0-9_]*", fullmatch=True),
        min_size=1,
        max_size=10,
        unique=True
    ))
    def test_list_returns_books_with_both_files(self, book_ids: List[str]):
        """
        **Feature: logic-chain-builder, Property 9: Output Schema Conformance**
        **Validates: Requirements 1.1, 1.2**
        
        Property: list_available_books should return only book_ids that have
        both snippets and relations files.
        """
        with tempfile.TemporaryDirectory() as tmpdir:
            snippets_dir = Path(tmpdir) / "snippets"
            relations_dir = Path(tmpdir) / "relations"
            snippets_dir.mkdir()
            relations_dir.mkdir()
            
            # Create files for all book_ids
            for book_id in book_ids:
                snippets_file = snippets_dir / f"{book_id}_snippets.yaml"
                relations_file = relations_dir / f"{book_id}_relations.yaml"
                
                with open(snippets_file, 'w', encoding='utf-8') as f:
                    yaml.dump({"book_id": book_id, "snippets": []}, f)
                with open(relations_file, 'w', encoding='utf-8') as f:
                    yaml.dump({"book_id": book_id, "relations": []}, f)
            
            loader = SchemaLoader(
                snippets_dir=str(snippets_dir),
                relations_dir=str(relations_dir)
            )
            available = loader.list_available_books()
            
            # All created book_ids should be available
            assert set(available) == set(book_ids)

    def test_list_excludes_books_with_only_snippets(self):
        """Property: Books with only snippets file should not be listed."""
        with tempfile.TemporaryDirectory() as tmpdir:
            snippets_dir = Path(tmpdir) / "snippets"
            relations_dir = Path(tmpdir) / "relations"
            snippets_dir.mkdir()
            relations_dir.mkdir()
            
            # Create only snippets file
            book_id = "snippets_only"
            snippets_file = snippets_dir / f"{book_id}_snippets.yaml"
            with open(snippets_file, 'w', encoding='utf-8') as f:
                yaml.dump({"book_id": book_id, "snippets": []}, f)
            
            loader = SchemaLoader(
                snippets_dir=str(snippets_dir),
                relations_dir=str(relations_dir)
            )
            available = loader.list_available_books()
            
            assert book_id not in available

    def test_list_excludes_books_with_only_relations(self):
        """Property: Books with only relations file should not be listed."""
        with tempfile.TemporaryDirectory() as tmpdir:
            snippets_dir = Path(tmpdir) / "snippets"
            relations_dir = Path(tmpdir) / "relations"
            snippets_dir.mkdir()
            relations_dir.mkdir()
            
            # Create only relations file
            book_id = "relations_only"
            relations_file = relations_dir / f"{book_id}_relations.yaml"
            with open(relations_file, 'w', encoding='utf-8') as f:
                yaml.dump({"book_id": book_id, "relations": []}, f)
            
            loader = SchemaLoader(
                snippets_dir=str(snippets_dir),
                relations_dir=str(relations_dir)
            )
            available = loader.list_available_books()
            
            assert book_id not in available


class TestRealDataLoading:
    """
    Integration tests with real data files.
    
    **Validates: Requirements 1.1, 1.2, 1.3, 1.4**
    """

    def test_load_real_snippets_file(self):
        """Property: Real snippets files should load successfully."""
        loader = SchemaLoader()
        available_books = loader.list_available_books()
        
        # Should have 21 books
        assert len(available_books) == 21
        
        # Load snippets from first available book
        if available_books:
            snippets = loader.load_snippets(available_books[0])
            assert len(snippets) > 0
            for snippet in snippets:
                assert isinstance(snippet, NarrativeSnippet)

    def test_load_real_relations_file(self):
        """Property: Real relations files should load successfully."""
        loader = SchemaLoader()
        available_books = loader.list_available_books()
        
        # Load relations from first available book
        if available_books:
            relations = loader.load_relations(available_books[0])
            assert len(relations) > 0
            for relation in relations:
                assert isinstance(relation, ConfigRelation)

    def test_all_21_books_available(self):
        """Property: All 21 target books should be available."""
        loader = SchemaLoader()
        available_books = loader.list_available_books()
        
        assert len(available_books) == 21, (
            f"Expected 21 books, found {len(available_books)}: {available_books}"
        )
