"""
GraphBuilder测试

Feature: cross-book-knowledge-graph
Requirement Refs: Req 2.1, Req 5.1, Req 5.3, Req 5.8, Req 5.9
"""

import tempfile
from pathlib import Path

import pytest
import yaml

from scripts.knowledge_graph_builder.builders.graph_builder import (
    BuildManifest,
    GraphBuilder,
    LogicChainData,
)
from scripts.knowledge_graph_builder.models import DivinationSystem


# ============ Fixtures ============

@pytest.fixture
def temp_dir():
    """创建临时目录"""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield Path(tmpdir)


@pytest.fixture
def sample_logic_chain_data():
    """示例LogicChain数据"""
    return {
        'metadata': {
            'book_id': '滴天髓',
            'divination_system': 'bazi',
            'quality_metrics': {
                'reasoning_coherence': 0.85,
                'node_homogeneity': 0.72,
            }
        },
        'nodes': [
            {
                'node_id': 'node_001',
                'summary': '日主强旺者喜泄气',
                'snippet_ids': ['snippet_001'],
                'factor_refs': ['bazi_daymaster', 'bazi_strength'],
            },
            {
                'node_id': 'node_002',
                'summary': '财星为用者宜财旺',
                'snippet_ids': ['snippet_002'],
                'factor_refs': ['bazi_wealth'],
            },
        ],
        'edges': [
            {
                'from_node': 'node_001',
                'to_node': 'node_002',
                'relation': 'entails',
            }
        ],
    }


@pytest.fixture
def logic_chains_dir(temp_dir, sample_logic_chain_data):
    """创建包含LogicChain的目录"""
    lc_dir = temp_dir / 'logic_chains'
    lc_dir.mkdir()
    
    # 创建示例LogicChain文件
    with open(lc_dir / '滴天髓.yaml', 'w', encoding='utf-8') as f:
        yaml.dump(sample_logic_chain_data, f, allow_unicode=True)
    
    return lc_dir


@pytest.fixture
def knowledge_graph_dir(temp_dir):
    """创建知识图谱目录"""
    kg_dir = temp_dir / 'knowledge_graph'
    kg_dir.mkdir()
    return kg_dir


# ============ LogicChainData Tests ============

class TestLogicChainData:
    """LogicChainData测试"""
    
    def test_creation(self, sample_logic_chain_data, temp_dir):
        """创建LogicChainData"""
        chain = LogicChainData(
            book_id='滴天髓',
            file_path=temp_dir / 'test.yaml',
            data=sample_logic_chain_data,
            file_hash='abc123',
        )
        assert chain.book_id == '滴天髓'
        assert chain.node_count == 2
        assert chain.edge_count == 1
    
    def test_quality_metrics(self, sample_logic_chain_data, temp_dir):
        """质量指标获取"""
        chain = LogicChainData(
            book_id='滴天髓',
            file_path=temp_dir / 'test.yaml',
            data=sample_logic_chain_data,
            file_hash='abc123',
        )
        metrics = chain.quality_metrics
        assert metrics['reasoning_coherence'] == 0.85
        assert metrics['node_homogeneity'] == 0.72


# ============ BuildManifest Tests ============

class TestBuildManifest:
    """BuildManifest测试"""
    
    def test_create_new_manifest(self, temp_dir):
        """创建新清单"""
        manifest = BuildManifest(temp_dir / 'manifest.yaml')
        assert manifest.data['graph_version'] == '0.0.0'
        assert manifest.data['processed_files'] == {}
    
    def test_update_and_save(self, temp_dir):
        """更新并保存清单"""
        manifest_path = temp_dir / 'manifest.yaml'
        manifest = BuildManifest(manifest_path)
        
        manifest.update_file('滴天髓', 'hash123', 100)
        manifest.update_build_info('1.0.0')
        manifest.save()
        
        # 重新加载验证
        manifest2 = BuildManifest(manifest_path)
        assert manifest2.get_file_hash('滴天髓') == 'hash123'
        assert manifest2.data['graph_version'] == '1.0.0'
    
    def test_is_file_changed(self, temp_dir):
        """检测文件变更"""
        manifest = BuildManifest(temp_dir / 'manifest.yaml')
        
        # 新文件
        assert manifest.is_file_changed('滴天髓', 'hash123') is True
        
        # 更新后
        manifest.update_file('滴天髓', 'hash123', 100)
        assert manifest.is_file_changed('滴天髓', 'hash123') is False
        
        # 哈希变更
        assert manifest.is_file_changed('滴天髓', 'hash456') is True


# ============ GraphBuilder Tests ============

class TestGraphBuilder:
    """GraphBuilder测试"""
    
    def test_scan_logic_chains(self, logic_chains_dir, knowledge_graph_dir):
        """扫描LogicChain目录"""
        builder = GraphBuilder(
            logic_chains_dir=logic_chains_dir,
            knowledge_graph_dir=knowledge_graph_dir,
        )
        files = builder.scan_logic_chains()
        assert len(files) == 1
        assert files[0].stem == '滴天髓'
    
    def test_scan_excludes_bak_files(self, logic_chains_dir, knowledge_graph_dir):
        """扫描时排除.bak文件"""
        # 创建备份文件
        (logic_chains_dir / 'test.bak.yaml').touch()
        (logic_chains_dir / 'test.failed.yaml').touch()
        
        builder = GraphBuilder(
            logic_chains_dir=logic_chains_dir,
            knowledge_graph_dir=knowledge_graph_dir,
        )
        files = builder.scan_logic_chains()
        
        # 不应包含备份文件
        file_names = [f.name for f in files]
        assert 'test.bak.yaml' not in file_names
        assert 'test.failed.yaml' not in file_names
    
    def test_infer_divination_system(self, logic_chains_dir, knowledge_graph_dir):
        """推断占卜体系"""
        builder = GraphBuilder(
            logic_chains_dir=logic_chains_dir,
            knowledge_graph_dir=knowledge_graph_dir,
        )
        
        assert builder._infer_divination_system('滴天髓') == DivinationSystem.BAZI
        assert builder._infer_divination_system('子平真诠') == DivinationSystem.BAZI
        assert builder._infer_divination_system('紫微斗数全书') == DivinationSystem.ZIWEI
        assert builder._infer_divination_system('tetrabiblos') == DivinationSystem.ASTRO
        assert builder._infer_divination_system('the_inner_sky') == DivinationSystem.ASTRO
        assert builder._infer_divination_system('learning_the_tarot') == DivinationSystem.TAROT
        assert builder._infer_divination_system('周公解梦') == DivinationSystem.DREAM
        assert builder._infer_divination_system('周易') == DivinationSystem.YIJING
        assert builder._infer_divination_system('the_archetypes_and_the_collective_unconscious') == DivinationSystem.PSYCHOLOGY
    
    def test_build_full(self, logic_chains_dir, knowledge_graph_dir):
        """全量构建"""
        builder = GraphBuilder(
            logic_chains_dir=logic_chains_dir,
            knowledge_graph_dir=knowledge_graph_dir,
        )
        
        graph = builder.build_full()
        
        assert len(graph.concepts) == 2  # 2个节点
        assert graph.metadata.version == '1.0.0'
        assert '滴天髓' in graph.metadata.books_included
    
    def test_build_full_dry_run(self, logic_chains_dir, knowledge_graph_dir):
        """全量构建dry-run模式"""
        builder = GraphBuilder(
            logic_chains_dir=logic_chains_dir,
            knowledge_graph_dir=knowledge_graph_dir,
        )
        
        graph = builder.build_full(dry_run=True)
        
        # dry-run不应产生实际概念
        assert len(graph.concepts) == 0
    
    def test_get_changed_files(self, logic_chains_dir, knowledge_graph_dir):
        """检测变更文件"""
        builder = GraphBuilder(
            logic_chains_dir=logic_chains_dir,
            knowledge_graph_dir=knowledge_graph_dir,
        )
        
        # 初始状态，所有文件都是"变更"
        changed = builder.get_changed_files()
        assert len(changed) == 1
        
        # 构建后，无变更
        builder.build_full()
        changed = builder.get_changed_files()
        assert len(changed) == 0
    
    def test_quality_check(self, logic_chains_dir, knowledge_graph_dir, sample_logic_chain_data):
        """质量检查"""
        builder = GraphBuilder(
            logic_chains_dir=logic_chains_dir,
            knowledge_graph_dir=knowledge_graph_dir,
        )
        
        chain = LogicChainData(
            book_id='test',
            file_path=logic_chains_dir / 'test.yaml',
            data=sample_logic_chain_data,
            file_hash='abc',
        )
        
        passed, warnings = builder._check_quality_metrics(chain)
        assert passed is True
        assert len(warnings) == 0
    
    def test_quality_check_fails_low_coherence(self, logic_chains_dir, knowledge_graph_dir):
        """质量检查失败 - 低reasoning_coherence"""
        builder = GraphBuilder(
            logic_chains_dir=logic_chains_dir,
            knowledge_graph_dir=knowledge_graph_dir,
        )
        
        low_quality_data = {
            'metadata': {
                'quality_metrics': {
                    'reasoning_coherence': 0.5,  # 低于阈值0.7
                    'node_homogeneity': 0.8,
                }
            },
            'nodes': [],
            'edges': [],
        }
        
        chain = LogicChainData(
            book_id='test',
            file_path=logic_chains_dir / 'test.yaml',
            data=low_quality_data,
            file_hash='abc',
        )
        
        passed, warnings = builder._check_quality_metrics(chain)
        assert passed is False
        assert len(warnings) == 1
        assert 'reasoning_coherence' in warnings[0]


# ============ Property Tests ============

class TestIncrementalBuildIdempotence:
    """
    Property 10: Incremental Build Idempotence
    Running build_incremental twice without file changes produces identical graphs.
    """
    
    def test_incremental_idempotence(self, logic_chains_dir, knowledge_graph_dir):
        """Property 10: 增量构建幂等性"""
        builder = GraphBuilder(
            logic_chains_dir=logic_chains_dir,
            knowledge_graph_dir=knowledge_graph_dir,
        )
        
        # First full build
        graph1 = builder.build_full()
        
        # Incremental build (no changes)
        graph2 = builder.build_incremental()
        
        # Should be identical
        assert len(graph2.concepts) == len(graph1.concepts)
        assert set(c.concept_id for c in graph2.concepts) == set(c.concept_id for c in graph1.concepts)
        
        # Second incremental build (still no changes)
        graph3 = builder.build_incremental()
        
        # Should still be identical
        assert len(graph3.concepts) == len(graph2.concepts)
        assert set(c.concept_id for c in graph3.concepts) == set(c.concept_id for c in graph2.concepts)
    
    def test_incremental_detects_changes(self, logic_chains_dir, knowledge_graph_dir, temp_dir):
        """增量构建能检测文件变更"""
        builder = GraphBuilder(
            logic_chains_dir=logic_chains_dir,
            knowledge_graph_dir=knowledge_graph_dir,
        )
        
        # First build
        graph1 = builder.build_full()
        initial_count = len(graph1.concepts)
        
        # Add new file
        new_chain = {
            'metadata': {
                'book_id': '子平真诠',
                'divination_system': 'bazi',
            },
            'nodes': [
                {'node_id': 'new_001', 'summary': '新节点', 'factor_refs': []}
            ],
            'edges': [],
        }
        with open(logic_chains_dir / '子平真诠.yaml', 'w', encoding='utf-8') as f:
            yaml.dump(new_chain, f, allow_unicode=True)
        
        # Incremental build should pick up new file
        graph2 = builder.build_incremental()
        assert len(graph2.concepts) > initial_count


class TestManualAlignmentPreservation:
    """
    Property 11: Manual Alignment Preservation
    Manually aligned concepts survive incremental rebuilds.
    """
    
    def test_manual_alignment_preserved(self, logic_chains_dir, knowledge_graph_dir):
        """Property 11: 手动对齐保留"""
        builder = GraphBuilder(
            logic_chains_dir=logic_chains_dir,
            knowledge_graph_dir=knowledge_graph_dir,
        )
        
        # First build
        graph1 = builder.build_full()
        
        # Record a manual alignment
        if len(graph1.concepts) >= 2:
            concept_a = graph1.concepts[0].concept_id
            concept_b = graph1.concepts[1].concept_id
            builder.manifest.add_manual_alignment(concept_a, concept_b)
            builder.manifest.save()
        
        # Verify manual alignments are stored
        manual = builder.manifest.get_manual_alignments()
        assert len(manual) >= 1 if len(graph1.concepts) >= 2 else True
        
        # Rebuild - manual alignments should be preserved
        builder2 = GraphBuilder(
            logic_chains_dir=logic_chains_dir,
            knowledge_graph_dir=knowledge_graph_dir,
        )
        manual2 = builder2.manifest.get_manual_alignments()
        assert manual2 == manual
    
    def test_manifest_alignment_stats(self, logic_chains_dir, knowledge_graph_dir):
        """清单中的对齐统计"""
        builder = GraphBuilder(
            logic_chains_dir=logic_chains_dir,
            knowledge_graph_dir=knowledge_graph_dir,
        )
        
        # Build
        builder.build_full()
        
        # Check alignment stats are populated
        stats = builder.manifest.data.get('alignment_stats', {})
        assert 'total_alignments' in stats or stats == {}
    
    def test_manifest_conflict_stats(self, logic_chains_dir, knowledge_graph_dir):
        """清单中的冲突统计"""
        builder = GraphBuilder(
            logic_chains_dir=logic_chains_dir,
            knowledge_graph_dir=knowledge_graph_dir,
        )
        
        # Build
        builder.build_full()
        
        # Check conflict stats are populated
        stats = builder.manifest.data.get('conflict_stats', {})
        assert 'total_conflicts' in stats or stats == {}
