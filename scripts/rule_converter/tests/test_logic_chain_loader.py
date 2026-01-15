"""
Tests for LogicChainLoader

Requirement Refs: Req 1.1-1.8
"""

import tempfile
from pathlib import Path

import pytest
import yaml

from scripts.rule_converter.loaders.logic_chain_loader import (
    LoaderError,
    LogicChainData,
    LogicChainEdge,
    LogicChainLoader,
    LogicChainNode,
)


class TestLogicChainNode:
    """测试 LogicChainNode 数据类"""
    
    def test_is_convertible_with_factor_refs(self):
        """有 factor_refs 的节点应该是可转换的"""
        node = LogicChainNode(
            node_id="test_node",
            factor_refs=["factor1", "factor2"],
        )
        assert node.is_convertible is True
    
    def test_is_convertible_with_condition(self):
        """有显式 condition 的节点应该是可转换的"""
        node = LogicChainNode(
            node_id="test_node",
            condition="some condition",
        )
        assert node.is_convertible is True
    
    def test_not_convertible_without_refs_or_condition(self):
        """没有 factor_refs 也没有 condition 的节点不可转换"""
        node = LogicChainNode(node_id="test_node")
        assert node.is_convertible is False
    
    def test_source_ref_from_metadata(self):
        """source_ref 应该从 metadata 中获取"""
        node = LogicChainNode(
            node_id="test_node",
            metadata={"source_ref": "《滴天髓》#第1条"},
        )
        assert node.source_ref == "《滴天髓》#第1条"
    
    def test_snippet_count_from_metadata(self):
        """snippet_count 应该从 metadata 中获取"""
        node = LogicChainNode(
            node_id="test_node",
            metadata={"snippet_count": 5},
        )
        assert node.snippet_count == 5
    
    def test_snippet_count_fallback_to_list_length(self):
        """如果 metadata 没有 snippet_count，使用 snippet_ids 长度"""
        node = LogicChainNode(
            node_id="test_node",
            snippet_ids=["s1", "s2", "s3"],
        )
        assert node.snippet_count == 3


class TestLogicChainData:
    """测试 LogicChainData 数据类"""
    
    def test_convertible_nodes(self):
        """convertible_nodes 应该只返回可转换的节点"""
        data = LogicChainData(
            chain_id="test_chain",
            book_id="test_book",
            nodes=[
                LogicChainNode(node_id="n1", factor_refs=["f1"]),
                LogicChainNode(node_id="n2"),  # 不可转换
                LogicChainNode(node_id="n3", condition="cond"),
            ],
        )
        convertible = data.convertible_nodes
        assert len(convertible) == 2
        assert convertible[0].node_id == "n1"
        assert convertible[1].node_id == "n3"
    
    def test_counts(self):
        """测试各种计数属性"""
        data = LogicChainData(
            chain_id="test_chain",
            book_id="test_book",
            nodes=[
                LogicChainNode(node_id="n1", factor_refs=["f1"]),
                LogicChainNode(node_id="n2"),
            ],
            edges=[
                LogicChainEdge(from_node="n1", to_node="n2", relation="leads_to"),
            ],
        )
        assert data.node_count == 2
        assert data.convertible_count == 1
        assert data.edge_count == 1


class TestLogicChainLoader:
    """测试 LogicChainLoader"""
    
    @pytest.fixture
    def sample_yaml_content(self):
        """示例 YAML 内容"""
        return {
            "chain_id": "chain_test",
            "book_id": "test_book",
            "nodes": [
                {
                    "node_id": "n_test_1",
                    "snippet_ids": ["ns_001", "ns_002"],
                    "role": "主干",
                    "condition": None,
                    "summary": "测试节点1",
                    "metadata": {
                        "source_ref": "《测试书》#第1章",
                        "snippet_count": 2,
                    },
                    "factor_refs": ["factor_a", "factor_b"],
                },
                {
                    "node_id": "n_test_2",
                    "snippet_ids": ["ns_003"],
                    "role": "条件分支",
                    "summary": "测试节点2",
                    "metadata": {
                        "source_ref": "《测试书》#第2章",
                    },
                },
            ],
            "edges": [
                {
                    "from_node": "n_test_1",
                    "to_node": "n_test_2",
                    "relation": "leads_to",
                    "condition": "条件成立时",
                },
            ],
        }
    
    @pytest.fixture
    def temp_dir(self):
        """创建临时目录"""
        with tempfile.TemporaryDirectory() as tmpdir:
            yield Path(tmpdir)
    
    def test_load_file_success(self, temp_dir, sample_yaml_content):
        """测试成功加载单个文件"""
        yaml_path = temp_dir / "test_book.yaml"
        with open(yaml_path, "w", encoding="utf-8") as f:
            yaml.dump(sample_yaml_content, f, allow_unicode=True)
        
        loader = LogicChainLoader(temp_dir)
        data = loader.load_file(yaml_path)
        
        assert data.chain_id == "chain_test"
        assert data.book_id == "test_book"
        assert len(data.nodes) == 2
        assert len(data.edges) == 1
        
        # 验证节点解析
        node1 = data.nodes[0]
        assert node1.node_id == "n_test_1"
        assert node1.snippet_ids == ["ns_001", "ns_002"]
        assert node1.role == "主干"
        assert node1.factor_refs == ["factor_a", "factor_b"]
        assert node1.is_convertible is True
        
        node2 = data.nodes[1]
        assert node2.node_id == "n_test_2"
        assert node2.is_convertible is False  # 没有 factor_refs
        
        # 验证边解析
        edge = data.edges[0]
        assert edge.from_node == "n_test_1"
        assert edge.to_node == "n_test_2"
        assert edge.relation == "leads_to"
        assert edge.condition == "条件成立时"
    
    def test_load_file_malformed_yaml(self, temp_dir):
        """测试加载格式错误的 YAML"""
        yaml_path = temp_dir / "bad.yaml"
        with open(yaml_path, "w", encoding="utf-8") as f:
            f.write("chain_id: test\nnodes:\n  - invalid: [unclosed")
        
        loader = LogicChainLoader(temp_dir)
        with pytest.raises(LoaderError) as exc_info:
            loader.load_file(yaml_path)
        
        assert "YAML parse error" in str(exc_info.value)
        assert exc_info.value.file_path == yaml_path
    
    def test_load_file_empty(self, temp_dir):
        """测试加载空文件"""
        yaml_path = temp_dir / "empty.yaml"
        yaml_path.touch()
        
        loader = LogicChainLoader(temp_dir)
        with pytest.raises(LoaderError) as exc_info:
            loader.load_file(yaml_path)
        
        assert "Empty YAML file" in str(exc_info.value)
    
    def test_load_all_success(self, temp_dir, sample_yaml_content):
        """测试批量加载"""
        # 创建多个文件
        for i in range(3):
            content = sample_yaml_content.copy()
            content["book_id"] = f"book_{i}"
            content["chain_id"] = f"chain_{i}"
            
            yaml_path = temp_dir / f"book_{i}.yaml"
            with open(yaml_path, "w", encoding="utf-8") as f:
                yaml.dump(content, f, allow_unicode=True)
        
        loader = LogicChainLoader(temp_dir)
        chains = loader.load_all()
        
        assert len(chains) == 3
        assert "book_0" in chains
        assert "book_1" in chains
        assert "book_2" in chains
        
        # 验证统计信息
        stats = loader.stats
        assert stats["total_files"] == 3
        assert stats["loaded_files"] == 3
        assert stats["total_nodes"] == 6  # 每个文件2个节点
        assert stats["nodes_with_factor_refs"] == 3  # 每个文件1个有refs的节点
    
    def test_skip_backup_files(self, temp_dir, sample_yaml_content):
        """测试跳过备份文件"""
        # 创建正常文件
        yaml_path = temp_dir / "test.yaml"
        with open(yaml_path, "w", encoding="utf-8") as f:
            yaml.dump(sample_yaml_content, f, allow_unicode=True)
        
        # 创建失败文件 (*.failed.yaml 会被 glob 匹配到然后跳过)
        failed_path = temp_dir / "test.failed.yaml"
        with open(failed_path, "w", encoding="utf-8") as f:
            yaml.dump(sample_yaml_content, f, allow_unicode=True)
        
        # 注意: *.yaml.bak 不会被 glob("*.yaml") 匹配到，所以不需要跳过
        # 实际的备份文件是 xxx.20251204_152807.bak 格式，也不会被匹配
        
        loader = LogicChainLoader(temp_dir)
        chains = loader.load_all()
        
        assert len(chains) == 1
        stats = loader.stats
        assert stats["skipped_files"] == 1  # 只有 test.failed.yaml 被匹配并跳过
    
    def test_get_all_convertible_nodes(self, temp_dir, sample_yaml_content):
        """测试获取所有可转换节点"""
        yaml_path = temp_dir / "test.yaml"
        with open(yaml_path, "w", encoding="utf-8") as f:
            yaml.dump(sample_yaml_content, f, allow_unicode=True)
        
        loader = LogicChainLoader(temp_dir)
        loader.load_all()
        
        convertible = loader.get_all_convertible_nodes()
        assert len(convertible) == 1
        
        book_id, node = convertible[0]
        assert book_id == "test_book"
        assert node.node_id == "n_test_1"
    
    def test_get_chain(self, temp_dir, sample_yaml_content):
        """测试获取指定书籍的 LogicChain"""
        yaml_path = temp_dir / "test.yaml"
        with open(yaml_path, "w", encoding="utf-8") as f:
            yaml.dump(sample_yaml_content, f, allow_unicode=True)
        
        loader = LogicChainLoader(temp_dir)
        loader.load_all()
        
        chain = loader.get_chain("test_book")
        assert chain is not None
        assert chain.book_id == "test_book"
        
        # 不存在的书籍
        assert loader.get_chain("nonexistent") is None
    
    def test_load_nonexistent_directory(self, temp_dir):
        """测试加载不存在的目录"""
        loader = LogicChainLoader(temp_dir / "nonexistent")
        chains = loader.load_all()
        assert len(chains) == 0


class TestLogicChainLoaderIntegration:
    """集成测试：使用实际的 LogicChain 文件"""
    
    @pytest.mark.skipif(
        not Path("data/logic_chains").exists(),
        reason="需要实际的 LogicChain 数据"
    )
    def test_load_real_data(self):
        """测试加载实际数据"""
        loader = LogicChainLoader()
        chains = loader.load_all()
        
        # 验证加载成功
        assert len(chains) > 0
        
        stats = loader.stats
        print(f"\n=== LogicChain 加载统计 ===")
        print(f"总文件数: {stats['total_files']}")
        print(f"加载成功: {stats['loaded_files']}")
        print(f"跳过文件: {stats['skipped_files']}")
        print(f"加载失败: {stats['failed_files']}")
        print(f"总节点数: {stats['total_nodes']}")
        print(f"有factor_refs的节点: {stats['nodes_with_factor_refs']}")
        print(f"可转换节点: {stats['convertible_nodes']}")
        print(f"总边数: {stats['total_edges']}")
        
        # 验证统计合理
        assert stats["total_nodes"] > 0
        assert stats["nodes_with_factor_refs"] > 0
