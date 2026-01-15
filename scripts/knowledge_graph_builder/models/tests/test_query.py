"""
SemanticQuery和QueryResult模型测试

Feature: cross-book-knowledge-graph, Property 8: Query Pagination Correctness
Requirement Refs: Req 4.1, Req 4.2, Req 4.3, Req 4.4, Req 4.9, Req 4.10
"""

import pytest
from pydantic import ValidationError

from hypothesis import given, settings, strategies as st

from scripts.knowledge_graph_builder.models.concept import (
    ConceptNode,
    Dimension,
    DivinationSystem,
    SourceNodeRef,
)
from scripts.knowledge_graph_builder.models.edge import RelationType
from scripts.knowledge_graph_builder.models.query import (
    BatchQueryRequest,
    BatchQueryResult,
    ConflictSeverity,
    ConflictWarning,
    QueryResult,
    QueryResultItem,
    SemanticQuery,
)


# ============ Fixtures ============

@pytest.fixture
def sample_concept():
    """示例概念"""
    return ConceptNode(
        concept_id="concept_bazi_test",
        canonical_label_zh="测试概念",
        divination_system=DivinationSystem.BAZI,
        source_nodes=[SourceNodeRef(book_id="test", node_id="node_001")],
    )


# ============ ConflictWarning Tests ============

class TestConflictWarning:
    """ConflictWarning模型测试"""
    
    def test_valid_creation(self):
        """有效数据创建成功"""
        warning = ConflictWarning(
            concept_id="concept_a",
            conflicting_concept_id="concept_b",
            conflict_type="direct_contradiction",
        )
        assert warning.severity == ConflictSeverity.MEDIUM
        assert warning.resolution_hint == ""
    
    def test_with_all_fields(self):
        """包含所有字段"""
        warning = ConflictWarning(
            concept_id="concept_a",
            conflicting_concept_id="concept_b",
            conflict_type="direct_contradiction",
            severity=ConflictSeverity.HIGH,
            resolution_hint="以滴天髓为准",
        )
        assert warning.severity == ConflictSeverity.HIGH
        assert warning.resolution_hint == "以滴天髓为准"


# ============ SemanticQuery Tests ============

class TestSemanticQuery:
    """SemanticQuery模型测试"""
    
    def test_default_query(self):
        """默认查询参数"""
        query = SemanticQuery()
        assert query.factor_ids == []
        assert query.dimension is None
        assert query.divination_system is None
        assert query.authority_threshold == 0.0
        assert query.traversal_depth == 1
        assert query.page == 1
        assert query.page_size == 20
    
    def test_with_factor_ids(self):
        """带因子ID的查询"""
        query = SemanticQuery(factor_ids=["factor_1", "factor_2"])
        assert len(query.factor_ids) == 2
    
    def test_with_dimension_filter(self):
        """带维度过滤"""
        query = SemanticQuery(dimension=Dimension.CAREER)
        assert query.dimension == Dimension.CAREER
    
    def test_with_system_filter(self):
        """带体系过滤"""
        query = SemanticQuery(divination_system=DivinationSystem.BAZI)
        assert query.divination_system == DivinationSystem.BAZI
    
    def test_traversal_depth_limits(self):
        """遍历深度限制在[0, 3]"""
        # 正常值
        query = SemanticQuery(traversal_depth=2)
        assert query.traversal_depth == 2
        
        # 超过最大值被截断
        query = SemanticQuery(traversal_depth=5)
        assert query.traversal_depth == 3
        
        # 负值被截断
        query = SemanticQuery(traversal_depth=-1)
        assert query.traversal_depth == 0
    
    def test_page_size_limits(self):
        """页大小限制在[1, 100]"""
        # 正常值
        query = SemanticQuery(page_size=50)
        assert query.page_size == 50
        
        # 超过最大值被截断
        query = SemanticQuery(page_size=200)
        assert query.page_size == 100
        
        # 小于最小值被截断
        query = SemanticQuery(page_size=0)
        assert query.page_size == 1
    
    def test_authority_threshold_limits(self):
        """权威性阈值限制在[0.0, 1.0]"""
        query = SemanticQuery(authority_threshold=0.5)
        assert query.authority_threshold == 0.5
        
        with pytest.raises(ValidationError):
            SemanticQuery(authority_threshold=1.5)
        
        with pytest.raises(ValidationError):
            SemanticQuery(authority_threshold=-0.1)
    
    def test_with_relation_types_filter(self):
        """带关系类型过滤"""
        query = SemanticQuery(
            filter_relation_types=[RelationType.ENTAILS, RelationType.SYNONYM]
        )
        assert len(query.filter_relation_types) == 2


# ============ QueryResultItem Tests ============

class TestQueryResultItem:
    """QueryResultItem模型测试"""
    
    def test_valid_creation(self, sample_concept):
        """有效数据创建成功"""
        item = QueryResultItem(concept=sample_concept)
        assert item.relevance_score == 1.0
        assert item.traversal_depth == 0
        assert item.related_snippet_ids == []
        assert item.conflict_warnings == []
    
    def test_with_all_fields(self, sample_concept):
        """包含所有字段"""
        warning = ConflictWarning(
            concept_id="concept_a",
            conflicting_concept_id="concept_b",
            conflict_type="direct_contradiction",
        )
        item = QueryResultItem(
            concept=sample_concept,
            relevance_score=0.85,
            traversal_depth=2,
            related_snippet_ids=["snippet_001", "snippet_002"],
            conflict_warnings=[warning],
        )
        assert item.relevance_score == 0.85
        assert item.traversal_depth == 2
        assert len(item.related_snippet_ids) == 2
        assert len(item.conflict_warnings) == 1


# ============ QueryResult Tests ============

class TestQueryResult:
    """QueryResult模型测试"""
    
    def test_empty_result(self):
        """空结果"""
        result = QueryResult()
        assert result.items == []
        assert result.total_count == 0
        assert result.has_more is False
    
    def test_has_more_calculation(self, sample_concept):
        """has_more自动计算"""
        items = [QueryResultItem(concept=sample_concept) for _ in range(10)]
        result = QueryResult(
            items=items,
            total_count=25,
            page=1,
            page_size=10,
        )
        assert result.has_more is True
        
        # 最后一页
        result = QueryResult(
            items=items,
            total_count=25,
            page=3,
            page_size=10,
        )
        assert result.has_more is False
    
    def test_pagination_info(self, sample_concept):
        """分页信息"""
        items = [QueryResultItem(concept=sample_concept) for _ in range(5)]
        result = QueryResult(
            items=items,
            total_count=100,
            page=2,
            page_size=5,
        )
        assert result.page == 2
        assert result.page_size == 5
        assert result.total_count == 100
        assert result.has_more is True


# ============ BatchQuery Tests ============

class TestBatchQuery:
    """批量查询测试"""
    
    def test_batch_request(self):
        """批量请求"""
        queries = [SemanticQuery(factor_ids=[f"factor_{i}"]) for i in range(3)]
        request = BatchQueryRequest(queries=queries)
        assert len(request.queries) == 3
    
    def test_batch_request_limit(self):
        """批量请求数量限制"""
        queries = [SemanticQuery() for _ in range(11)]
        with pytest.raises(ValidationError):
            BatchQueryRequest(queries=queries)
    
    def test_batch_result(self):
        """批量结果"""
        results = [QueryResult() for _ in range(3)]
        batch_result = BatchQueryResult(results=results, total_time_ms=50.5)
        assert len(batch_result.results) == 3
        assert batch_result.total_time_ms == 50.5


# ============ Property-Based Testing ============

class TestQueryPropertyBased:
    """
    Property 8: Query Pagination Correctness
    使用hypothesis进行属性测试
    """
    
    @settings(max_examples=100)
    @given(
        page=st.integers(min_value=1, max_value=100),
        page_size=st.integers(min_value=1, max_value=100),
        total_count=st.integers(min_value=0, max_value=10000),
    )
    def test_pagination_correctness(self, page, page_size, total_count):
        """验证分页正确性"""
        # 创建结果
        items_count = min(page_size, max(0, total_count - (page - 1) * page_size))
        
        # 创建示例概念
        sample = ConceptNode(
            concept_id="concept_bazi_test",
            canonical_label_zh="测试",
            divination_system=DivinationSystem.BAZI,
            source_nodes=[SourceNodeRef(book_id="test", node_id="node_001")],
        )
        items = [QueryResultItem(concept=sample) for _ in range(items_count)]
        
        result = QueryResult(
            items=items,
            total_count=total_count,
            page=page,
            page_size=page_size,
        )
        
        # 验证 len(items) <= page_size
        assert len(result.items) <= result.page_size
        
        # 验证 has_more == (page * page_size < total_count)
        expected_has_more = (page * page_size) < total_count
        assert result.has_more == expected_has_more
    
    @settings(max_examples=100)
    @given(
        traversal_depth=st.integers(min_value=-10, max_value=10),
    )
    def test_traversal_depth_clamped(self, traversal_depth):
        """验证遍历深度被正确限制"""
        query = SemanticQuery(traversal_depth=traversal_depth)
        assert 0 <= query.traversal_depth <= 3
    
    @settings(max_examples=100)
    @given(
        page_size=st.integers(min_value=-10, max_value=200),
    )
    def test_page_size_clamped(self, page_size):
        """验证页大小被正确限制"""
        query = SemanticQuery(page_size=page_size)
        assert 1 <= query.page_size <= 100
