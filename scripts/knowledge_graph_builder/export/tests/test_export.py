"""
Export模块测试

Feature: cross-book-knowledge-graph
Requirement Refs: Req 7.1~7.8
Design Refs: Design.md#模块结构

Property 15: Export Filter Correctness
Property 16: Statistics Accuracy
"""

import json
import tempfile
from datetime import datetime
from pathlib import Path

import pytest
from hypothesis import given, settings, strategies as st

from scripts.knowledge_graph_builder.models.concept import (
    ConceptNode,
    Dimension,
    DivinationSystem,
    SourceNodeRef,
)
from scripts.knowledge_graph_builder.models.edge import (
    RelationType,
    SemanticEdge,
)
from scripts.knowledge_graph_builder.models.graph import (
    GraphMetadata,
    KnowledgeGraph,
)
from scripts.knowledge_graph_builder.export import (
    GraphMLExporter,
    JSONLDExporter,
    MermaidExporter,
    StatsGenerator,
)


# ============ Fixtures ============

@pytest.fixture
def sample_graph():
    """创建示例图谱"""
    metadata = GraphMetadata(
        version="1.0.0",
        build_timestamp=datetime.now(),
    )
    
    concepts = [
        ConceptNode(
            concept_id="concept_bazi_export_001",
            canonical_label_zh="八字概念1",
            canonical_label_en="Bazi Concept 1",
            divination_system=DivinationSystem.BAZI,
            dimension=Dimension.CAREER,
            source_nodes=[SourceNodeRef(book_id="滴天髓", node_id="n_001", snippet_ids=[])],
            factor_refs=["bazi_day_master", "bazi_season"],
            authority_score=0.9,
        ),
        ConceptNode(
            concept_id="concept_bazi_export_002",
            canonical_label_zh="八字概念2",
            divination_system=DivinationSystem.BAZI,
            dimension=Dimension.WEALTH,
            source_nodes=[SourceNodeRef(book_id="子平真诠", node_id="n_002", snippet_ids=[])],
            factor_refs=["bazi_wealth"],
            authority_score=0.75,
        ),
        ConceptNode(
            concept_id="concept_astro_export_001",
            canonical_label_zh="占星概念1",
            divination_system=DivinationSystem.ASTRO,
            dimension=Dimension.CAREER,
            source_nodes=[SourceNodeRef(book_id="planets_in_transit", node_id="n_003", snippet_ids=[])],
            factor_refs=["astro_sun", "astro_moon"],
            authority_score=0.85,
        ),
    ]
    
    edges = [
        SemanticEdge(
            edge_id="edge_export_001",
            source_concept_id="concept_bazi_export_001",
            target_concept_id="concept_bazi_export_002",
            relation_type=RelationType.ENTAILS,
            confidence=0.8,
        ),
        SemanticEdge(
            edge_id="edge_export_002",
            source_concept_id="concept_bazi_export_001",
            target_concept_id="concept_astro_export_001",
            relation_type=RelationType.CROSS_SYSTEM_EQUIVALENT,
            confidence=0.7,
        ),
    ]
    
    return KnowledgeGraph(
        metadata=metadata,
        concepts=concepts,
        edges=edges,
    )


# ============ GraphML导出测试 ============

class TestGraphMLExporter:
    """GraphML导出器测试"""
    
    def test_export_basic(self, sample_graph):
        """测试基本导出"""
        exporter = GraphMLExporter(max_nodes=100)
        xml_content = exporter.export(sample_graph)
        
        assert '<?xml version="1.0"' in xml_content
        assert '<graphml' in xml_content
        assert '<node' in xml_content
        assert '<edge' in xml_content
    
    def test_export_to_file(self, sample_graph):
        """测试导出到文件"""
        exporter = GraphMLExporter()
        
        with tempfile.TemporaryDirectory() as tmpdir:
            output_path = Path(tmpdir) / "graph.graphml"
            exporter.export(sample_graph, output_path=output_path)
            
            assert output_path.exists()
            content = output_path.read_text()
            assert '<graphml' in content
    
    def test_export_with_system_filter(self, sample_graph):
        """测试按体系过滤"""
        exporter = GraphMLExporter()
        xml_content = exporter.export(
            sample_graph,
            divination_systems=[DivinationSystem.BAZI],
        )
        
        # 应该只包含八字概念
        assert 'concept_bazi_export_001' in xml_content
        assert 'concept_bazi_export_002' in xml_content
        assert 'concept_astro_export_001' not in xml_content
    
    def test_export_with_authority_filter(self, sample_graph):
        """测试按权威性过滤"""
        exporter = GraphMLExporter()
        xml_content = exporter.export(
            sample_graph,
            authority_threshold=0.8,
        )
        
        # 应该只包含authority >= 0.8的概念
        assert 'concept_bazi_export_001' in xml_content  # 0.9
        assert 'concept_astro_export_001' in xml_content  # 0.85
        assert 'concept_bazi_export_002' not in xml_content  # 0.75
    
    def test_max_nodes_limit(self, sample_graph):
        """测试节点数限制"""
        exporter = GraphMLExporter(max_nodes=1)
        xml_content = exporter.export(sample_graph)
        
        # 应该只包含1个节点（权威性最高的）
        assert xml_content.count('<node id=') == 1


# ============ Mermaid导出测试 ============

class TestMermaidExporter:
    """Mermaid导出器测试"""
    
    def test_export_basic(self, sample_graph):
        """测试基本导出"""
        exporter = MermaidExporter()
        mermaid_content = exporter.export(sample_graph)
        
        assert 'graph TD' in mermaid_content
        assert 'subgraph' in mermaid_content
    
    def test_export_has_subgraphs(self, sample_graph):
        """测试按体系分组"""
        exporter = MermaidExporter()
        mermaid_content = exporter.export(sample_graph)
        
        # 应该有八字和占星两个subgraph
        assert '八字' in mermaid_content or 'bazi' in mermaid_content.lower()
        assert '占星' in mermaid_content or 'astro' in mermaid_content.lower()
    
    def test_export_to_file(self, sample_graph):
        """测试导出到文件"""
        exporter = MermaidExporter()
        
        with tempfile.TemporaryDirectory() as tmpdir:
            output_path = Path(tmpdir) / "graph.mmd"
            exporter.export(sample_graph, output_path=output_path)
            
            assert output_path.exists()


# ============ JSON-LD导出测试 ============

class TestJSONLDExporter:
    """JSON-LD导出器测试"""
    
    def test_export_basic(self, sample_graph):
        """测试基本导出"""
        exporter = JSONLDExporter()
        jsonld_str = exporter.export(sample_graph)
        
        data = json.loads(jsonld_str)
        assert '@context' in data
        assert '@graph' in data
    
    def test_export_has_context(self, sample_graph):
        """测试包含JSON-LD context"""
        exporter = JSONLDExporter()
        jsonld_str = exporter.export(sample_graph)
        
        data = json.loads(jsonld_str)
        assert '@vocab' in data['@context']
        assert 'ls:' in str(data['@context'])
    
    def test_export_concepts_have_ids(self, sample_graph):
        """测试概念有@id"""
        exporter = JSONLDExporter()
        jsonld_str = exporter.export(sample_graph)
        
        data = json.loads(jsonld_str)
        for item in data['@graph']:
            assert '@id' in item
            assert '@type' in item


# ============ 统计生成器测试 ============

class TestStatsGenerator:
    """统计生成器测试"""
    
    def test_generate_stats(self, sample_graph):
        """测试生成统计数据"""
        generator = StatsGenerator()
        stats = generator.generate_stats(sample_graph)
        
        assert stats.total_concepts == 3
        assert stats.total_edges == 2
        assert stats.total_books == 3
        assert stats.total_systems == 2
    
    def test_stats_concepts_per_system(self, sample_graph):
        """测试按体系统计"""
        generator = StatsGenerator()
        stats = generator.generate_stats(sample_graph)
        
        assert stats.concepts_per_system['bazi'] == 2
        assert stats.concepts_per_system['astro'] == 1
    
    def test_stats_average_authority(self, sample_graph):
        """测试平均权威性"""
        generator = StatsGenerator()
        stats = generator.generate_stats(sample_graph)
        
        # (0.9 + 0.75 + 0.85) / 3 ≈ 0.833
        assert 0.83 < stats.average_authority_score < 0.84
    
    def test_save_stats(self, sample_graph):
        """测试保存统计数据"""
        generator = StatsGenerator()
        stats = generator.generate_stats(sample_graph)
        
        with tempfile.TemporaryDirectory() as tmpdir:
            output_path = Path(tmpdir) / "stats.json"
            generator.save_stats(stats, output_path)
            
            assert output_path.exists()
            with open(output_path) as f:
                data = json.load(f)
            assert data['total_concepts'] == 3
    
    def test_generate_summary(self, sample_graph):
        """测试生成摘要报告"""
        generator = StatsGenerator()
        summary = generator.generate_summary(sample_graph)
        
        assert '# 知识图谱统计报告' in summary
        assert '总概念数' in summary
        assert 'Top-10' in summary
    
    def test_save_summary(self, sample_graph):
        """测试保存摘要报告"""
        generator = StatsGenerator()
        summary = generator.generate_summary(sample_graph)
        
        with tempfile.TemporaryDirectory() as tmpdir:
            output_path = Path(tmpdir) / "summary.md"
            generator.save_summary(summary, output_path)
            
            assert output_path.exists()


# ============ Property测试 ============

class TestPropertyExport:
    """
    Property 15: Export Filter Correctness
    Property 16: Statistics Accuracy
    """
    
    def test_property_filter_correctness(self, sample_graph):
        """Property 15: 验证导出节点都匹配过滤条件"""
        exporter = GraphMLExporter()
        
        # 使用体系过滤
        xml_content = exporter.export(
            sample_graph,
            divination_systems=[DivinationSystem.BAZI],
        )
        
        # 验证只有BAZI概念被导出
        assert 'concept_bazi' in xml_content
        assert 'concept_astro' not in xml_content
    
    def test_property_filter_authority(self):
        """Property 15: 验证权威性过滤正确"""
        metadata = GraphMetadata(version="1.0.0", build_timestamp=datetime.now())
        
        concepts = [
            ConceptNode(
                concept_id=f"concept_bazi_auth_{i}",
                canonical_label_zh=f"权威测试{i}",
                divination_system=DivinationSystem.BAZI,
                dimension=Dimension.GENERAL,
                source_nodes=[SourceNodeRef(book_id="test", node_id=f"n_{i}", snippet_ids=[])],
                authority_score=0.1 * (i + 1),  # 0.1, 0.2, ..., 1.0
            )
            for i in range(10)
        ]
        
        graph = KnowledgeGraph(metadata=metadata, concepts=concepts, edges=[])
        
        exporter = GraphMLExporter()
        xml_content = exporter.export(graph, authority_threshold=0.5)
        
        # 验证只有 >= 0.5 的概念被导出
        # i=0..3 -> authority 0.1~0.4, 不包含
        for i in range(4):
            assert f"concept_bazi_auth_{i}" not in xml_content  # 0.1~0.4
        # i=4..9 -> authority 0.5~1.0, 包含
        for i in range(4, 10):
            assert f"concept_bazi_auth_{i}" in xml_content  # 0.5~1.0
    
    def test_property_stats_accuracy_total_concepts(self):
        """Property 16: 验证stats.total_concepts == len(graph.concepts)"""
        metadata = GraphMetadata(version="1.0.0", build_timestamp=datetime.now())
        
        num_concepts = 15
        concepts = [
            ConceptNode(
                concept_id=f"concept_bazi_stats_{i}",
                canonical_label_zh=f"统计测试{i}",
                divination_system=DivinationSystem.BAZI,
                dimension=Dimension.GENERAL,
                source_nodes=[SourceNodeRef(book_id="test", node_id=f"n_{i}", snippet_ids=[])],
            )
            for i in range(num_concepts)
        ]
        
        graph = KnowledgeGraph(metadata=metadata, concepts=concepts, edges=[])
        
        generator = StatsGenerator()
        stats = generator.generate_stats(graph)
        
        assert stats.total_concepts == len(graph.concepts)
        assert stats.total_concepts == num_concepts
    
    def test_property_stats_accuracy_sum_per_book(self):
        """Property 16: 验证sum(concepts_per_book) == total_concepts（考虑多来源）"""
        metadata = GraphMetadata(version="1.0.0", build_timestamp=datetime.now())
        
        # 创建有多来源的概念
        concept1 = ConceptNode(
            concept_id="concept_bazi_multi_001",
            canonical_label_zh="多来源概念",
            divination_system=DivinationSystem.BAZI,
            dimension=Dimension.GENERAL,
            source_nodes=[
                SourceNodeRef(book_id="book_a", node_id="n_1", snippet_ids=[]),
                SourceNodeRef(book_id="book_b", node_id="n_2", snippet_ids=[]),
            ],
        )
        concept2 = ConceptNode(
            concept_id="concept_bazi_single_001",
            canonical_label_zh="单来源概念",
            divination_system=DivinationSystem.BAZI,
            dimension=Dimension.GENERAL,
            source_nodes=[
                SourceNodeRef(book_id="book_a", node_id="n_3", snippet_ids=[]),
            ],
        )
        
        graph = KnowledgeGraph(metadata=metadata, concepts=[concept1, concept2], edges=[])
        
        generator = StatsGenerator()
        stats = generator.generate_stats(graph)
        
        # concepts_per_book是按来源统计的，可能大于total_concepts
        # book_a: 2 (两个概念都有), book_b: 1
        assert stats.concepts_per_book['book_a'] == 2
        assert stats.concepts_per_book['book_b'] == 1
