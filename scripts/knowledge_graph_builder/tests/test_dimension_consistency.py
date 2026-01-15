"""
Dimension一致性属性测试

Feature: cross-book-knowledge-graph
Requirement Refs: Req 1.6, Req 14.1
Design Refs: Design.md#概念层

Property 18: Dimension Consistency
验证所有ConceptNode的dimension都在其divination_system允许的范围内
"""

from datetime import datetime

import pytest
from hypothesis import given, settings, strategies as st

from scripts.knowledge_graph_builder.models.concept import (
    ConceptNode,
    Dimension,
    DivinationSystem,
    SourceNodeRef,
    SYSTEM_ALLOWED_DIMENSIONS,
)
from scripts.knowledge_graph_builder.models.graph import (
    GraphMetadata,
    KnowledgeGraph,
)
from scripts.knowledge_graph_builder.validation import (
    GraphValidator,
    IssueType,
)


# ============ 基础测试 ============

class TestDimensionConsistency:
    """Dimension一致性基础测试"""
    
    def test_bazi_allowed_dimensions(self):
        """测试八字允许的维度"""
        allowed = SYSTEM_ALLOWED_DIMENSIONS.get(DivinationSystem.BAZI, [])
        
        # 八字应该允许所有核心维度
        assert Dimension.CAREER in allowed
        assert Dimension.WEALTH in allowed
        assert Dimension.MARRIAGE in allowed
        assert Dimension.HEALTH in allowed
    
    def test_cross_system_allows_all(self):
        """测试跨体系允许所有维度"""
        allowed = SYSTEM_ALLOWED_DIMENSIONS.get(DivinationSystem.CROSS_SYSTEM, [])
        
        # 跨体系应该允许所有维度
        for dim in Dimension:
            assert dim in allowed
    
    def test_validator_detects_inconsistency(self):
        """测试验证器检测维度不一致"""
        # 创建一个维度不一致的概念（如果有限制的话）
        # 注意：这取决于SYSTEM_ALLOWED_DIMENSIONS的配置
        metadata = GraphMetadata(version="1.0.0", build_timestamp=datetime.now())
        
        # 查找一个有限制的体系
        restricted_system = None
        disallowed_dim = None
        
        for system, allowed_dims in SYSTEM_ALLOWED_DIMENSIONS.items():
            if len(allowed_dims) < len(Dimension):
                restricted_system = system
                for dim in Dimension:
                    if dim not in allowed_dims:
                        disallowed_dim = dim
                        break
                if disallowed_dim:
                    break
        
        if restricted_system and disallowed_dim:
            concept = ConceptNode(
                concept_id=f"concept_{restricted_system.value}_test_001",
                canonical_label_zh="维度测试",
                divination_system=restricted_system,
                dimension=disallowed_dim,
                source_nodes=[SourceNodeRef(book_id="test", node_id="n_001", snippet_ids=[])],
            )
            
            graph = KnowledgeGraph(
                metadata=metadata,
                concepts=[concept],
                edges=[],
            )
            
            validator = GraphValidator()
            report = validator.validate(graph)
            
            dim_issues = [
                i for i in report.issues
                if i.issue_type == IssueType.DIMENSION_CONSISTENCY
            ]
            assert len(dim_issues) > 0
        else:
            # 如果所有体系都允许所有维度，跳过此测试
            pytest.skip("No restricted dimensions configured")
    
    def test_valid_dimension_passes(self):
        """测试有效维度通过验证"""
        metadata = GraphMetadata(version="1.0.0", build_timestamp=datetime.now())
        
        # 使用跨体系（允许所有维度）
        concept = ConceptNode(
            concept_id="concept_cross_test_001",
            canonical_label_zh="有效维度测试",
            divination_system=DivinationSystem.CROSS_SYSTEM,
            dimension=Dimension.CAREER,
            source_nodes=[SourceNodeRef(book_id="test", node_id="n_001", snippet_ids=[])],
        )
        
        graph = KnowledgeGraph(
            metadata=metadata,
            concepts=[concept],
            edges=[],
        )
        
        validator = GraphValidator()
        report = validator.validate(graph)
        
        dim_issues = [
            i for i in report.issues
            if i.issue_type == IssueType.DIMENSION_CONSISTENCY
        ]
        assert len(dim_issues) == 0


# ============ Property测试 ============

class TestPropertyDimensionConsistency:
    """
    Property 18: Dimension Consistency
    
    验证：对于任意ConceptNode，其dimension必须在其divination_system允许的范围内
    """
    
    @given(
        system=st.sampled_from(list(DivinationSystem)),
        dimension=st.sampled_from(list(Dimension)),
    )
    @settings(max_examples=50)
    def test_property_dimension_in_allowed_set(
        self,
        system: DivinationSystem,
        dimension: Dimension,
    ):
        """Property 18: 验证dimension是否在allowed_dimensions中"""
        allowed = SYSTEM_ALLOWED_DIMENSIONS.get(system, list(Dimension))
        
        metadata = GraphMetadata(version="1.0.0", build_timestamp=datetime.now())
        
        concept = ConceptNode(
            concept_id=f"concept_{system.value}_prop18_001",
            canonical_label_zh="属性测试",
            divination_system=system,
            dimension=dimension,
            source_nodes=[SourceNodeRef(book_id="test", node_id="n_001", snippet_ids=[])],
        )
        
        graph = KnowledgeGraph(
            metadata=metadata,
            concepts=[concept],
            edges=[],
        )
        
        validator = GraphValidator()
        report = validator.validate(graph)
        
        dim_issues = [
            i for i in report.issues
            if i.issue_type == IssueType.DIMENSION_CONSISTENCY
        ]
        
        # 如果dimension在allowed中，不应有问题
        # 如果dimension不在allowed中，应该有警告
        if dimension in allowed:
            assert len(dim_issues) == 0, f"{system.value} should allow {dimension.value}"
        else:
            assert len(dim_issues) > 0, f"{system.value} should not allow {dimension.value}"
    
    @given(system=st.sampled_from(list(DivinationSystem)))
    @settings(max_examples=20)
    def test_property_cross_system_allows_all(self, system: DivinationSystem):
        """Property 18: 验证CROSS_SYSTEM允许所有维度"""
        if system != DivinationSystem.CROSS_SYSTEM:
            return  # 只测试CROSS_SYSTEM
        
        allowed = SYSTEM_ALLOWED_DIMENSIONS.get(system, [])
        
        # CROSS_SYSTEM应该允许所有维度
        for dim in Dimension:
            assert dim in allowed, f"CROSS_SYSTEM should allow {dim.value}"
    
    def test_property_all_systems_have_general(self):
        """Property 18: 验证所有体系都允许GENERAL维度"""
        for system in DivinationSystem:
            allowed = SYSTEM_ALLOWED_DIMENSIONS.get(system, list(Dimension))
            assert Dimension.GENERAL in allowed, f"{system.value} should allow GENERAL dimension"
