"""
Tests for FactorOntology

Requirement Refs: Req 3.1-3.12
"""

import tempfile
from pathlib import Path

import pytest
import yaml

from scripts.rule_converter.loaders.factor_ontology import FactorDef, FactorOntology


class TestFactorDef:
    """测试 FactorDef 数据类"""
    
    def test_is_boolean(self):
        """测试 boolean 类型"""
        factor = FactorDef(id="test", value_type="boolean")
        assert factor.is_boolean is True
        assert factor.is_numeric is False
        assert factor.is_enum is False
    
    def test_is_numeric(self):
        """测试 numeric 类型"""
        factor = FactorDef(id="test", value_type="numeric", value_range=[0, 1])
        assert factor.is_boolean is False
        assert factor.is_numeric is True
        assert factor.is_enum is False
        
        range_tuple = factor.get_numeric_range()
        assert range_tuple == (0, 1)
    
    def test_is_enum(self):
        """测试 enum 类型"""
        factor = FactorDef(id="test", value_type="enum", value_range=["a", "b", "c"])
        assert factor.is_boolean is False
        assert factor.is_numeric is False
        assert factor.is_enum is True
        
        enum_values = factor.get_enum_values()
        assert enum_values == ["a", "b", "c"]
    
    def test_enum_string_format(self):
        """测试枚举的字符串格式（如 "辰戌/丑未"）"""
        factor = FactorDef(id="test", value_type="enum", value_range="辰戌/丑未")
        
        enum_values = factor.get_enum_values()
        assert enum_values == ["辰戌", "丑未"]


class TestFactorOntology:
    """测试 FactorOntology"""
    
    @pytest.fixture
    def sample_certified_content(self):
        """示例认证因子内容"""
        return {
            "system": "bazi",
            "certified_time": "2025-12-05T00:07:50",
            "total_certified": 3,
            "by_category": {
                "relation": [
                    {
                        "id": "chong_movement",
                        "status": "existing",
                        "display_zh": "冲动关系",
                        "display_en": "ChongMovement",
                        "description_zh": "土气互激",
                        "category": "relation",
                        "value_type": "enum",
                        "applicable_systems": ["bazi"],
                        "value_range": "辰戌/丑未",
                    },
                ],
                "state": [
                    {
                        "id": "day_master_strength",
                        "status": "existing",
                        "display_zh": "日主强度",
                        "value_type": "numeric",
                        "applicable_systems": ["bazi"],
                        "value_range": [0, 1],
                    },
                    {
                        "id": "bazi_deling",
                        "status": "existing",
                        "display_zh": "得令",
                        "value_type": "boolean",
                        "applicable_systems": ["bazi"],
                    },
                ],
            },
        }
    
    @pytest.fixture
    def sample_base_content(self):
        """示例基础因子内容"""
        return {
            "factors": [
                {
                    "id": "base_factor_1",
                    "status": "existing",
                    "display_zh": "基础因子1",
                    "category": "structure",
                    "value_type": "boolean",
                    "applicable_systems": ["bazi"],
                },
                {
                    "id": "base_factor_2",
                    "status": "existing",
                    "display_zh": "基础因子2",
                    "category": "structure",
                    "value_type": "enum",
                    "value_range": ["甲", "乙", "丙"],
                    "applicable_systems": ["bazi"],
                },
            ],
        }
    
    @pytest.fixture
    def temp_dirs(self, sample_certified_content, sample_base_content):
        """创建临时目录"""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmpdir = Path(tmpdir)
            
            # 创建 certified 目录
            certified_dir = tmpdir / "certified"
            certified_dir.mkdir()
            
            certified_file = certified_dir / "bazi_certified.yaml"
            with open(certified_file, "w", encoding="utf-8") as f:
                yaml.dump(sample_certified_content, f, allow_unicode=True)
            
            # 创建 base 目录
            base_dir = tmpdir / "base" / "bazi"
            base_dir.mkdir(parents=True)
            
            base_file = base_dir / "structure.yaml"
            with open(base_file, "w", encoding="utf-8") as f:
                yaml.dump(sample_base_content, f, allow_unicode=True)
            
            yield certified_dir, tmpdir / "base"
    
    def test_load_certified_factors(self, temp_dirs):
        """测试加载认证因子"""
        certified_dir, base_dir = temp_dirs
        
        ontology = FactorOntology(certified_dir=certified_dir, base_dir=base_dir)
        ontology.load()
        
        # 验证加载数量
        assert len(ontology) == 5  # 3 certified + 2 base
        
        stats = ontology.stats
        assert stats["certified_factors"] == 3
        assert stats["base_factors"] == 2
    
    def test_get_factor(self, temp_dirs):
        """测试获取单个因子"""
        certified_dir, base_dir = temp_dirs
        
        ontology = FactorOntology(certified_dir=certified_dir, base_dir=base_dir)
        ontology.load()
        
        # 获取认证因子
        factor = ontology.get("day_master_strength")
        assert factor is not None
        assert factor.display_zh == "日主强度"
        assert factor.value_type == "numeric"
        assert factor.is_numeric is True
        
        # 获取基础因子
        factor2 = ontology.get("base_factor_1")
        assert factor2 is not None
        assert factor2.display_zh == "基础因子1"
        
        # 获取不存在的
        assert ontology.get("nonexistent") is None
    
    def test_is_valid(self, temp_dirs):
        """测试验证因子ID"""
        certified_dir, base_dir = temp_dirs
        
        ontology = FactorOntology(certified_dir=certified_dir, base_dir=base_dir)
        ontology.load()
        
        assert ontology.is_valid("day_master_strength") is True
        assert ontology.is_valid("base_factor_1") is True
        assert ontology.is_valid("nonexistent") is False
        
        # 使用 in 操作符
        assert "day_master_strength" in ontology
        assert "nonexistent" not in ontology
    
    def test_get_system(self, temp_dirs):
        """测试获取体系"""
        certified_dir, base_dir = temp_dirs
        
        ontology = FactorOntology(certified_dir=certified_dir, base_dir=base_dir)
        ontology.load()
        
        assert ontology.get_system("day_master_strength") == "bazi"
        assert ontology.get_system("nonexistent") is None
    
    def test_get_by_system(self, temp_dirs):
        """测试按体系获取因子"""
        certified_dir, base_dir = temp_dirs
        
        ontology = FactorOntology(certified_dir=certified_dir, base_dir=base_dir)
        ontology.load()
        
        bazi_factors = ontology.get_by_system("bazi")
        assert len(bazi_factors) == 5
    
    def test_get_by_category(self, temp_dirs):
        """测试按分类获取因子"""
        certified_dir, base_dir = temp_dirs
        
        ontology = FactorOntology(certified_dir=certified_dir, base_dir=base_dir)
        ontology.load()
        
        state_factors = ontology.get_by_category("state")
        assert len(state_factors) == 2
        
        structure_factors = ontology.get_by_category("structure")
        assert len(structure_factors) == 2
    
    def test_validate_all(self, temp_dirs):
        """测试批量验证"""
        certified_dir, base_dir = temp_dirs
        
        ontology = FactorOntology(certified_dir=certified_dir, base_dir=base_dir)
        ontology.load()
        
        valid, invalid = ontology.validate_all([
            "day_master_strength",
            "bazi_deling",
            "nonexistent1",
            "base_factor_1",
            "nonexistent2",
        ])
        
        assert len(valid) == 3
        assert len(invalid) == 2
        assert "nonexistent1" in invalid
        assert "nonexistent2" in invalid
    
    def test_systems_and_categories(self, temp_dirs):
        """测试获取体系和分类列表"""
        certified_dir, base_dir = temp_dirs
        
        ontology = FactorOntology(certified_dir=certified_dir, base_dir=base_dir)
        ontology.load()
        
        assert "bazi" in ontology.systems
        assert "state" in ontology.categories
        assert "relation" in ontology.categories
        assert "structure" in ontology.categories
    
    def test_certified_priority(self, temp_dirs, sample_base_content):
        """测试认证因子优先于基础因子"""
        certified_dir, base_dir = temp_dirs
        
        # 在基础目录中创建一个与认证因子同ID的因子
        conflict_content = {
            "factors": [
                {
                    "id": "day_master_strength",  # 与认证因子冲突
                    "display_zh": "基础版日主强度",  # 不同的显示名
                    "value_type": "boolean",  # 不同的类型
                },
            ],
        }
        
        conflict_file = base_dir / "bazi" / "conflict.yaml"
        with open(conflict_file, "w", encoding="utf-8") as f:
            yaml.dump(conflict_content, f, allow_unicode=True)
        
        ontology = FactorOntology(certified_dir=certified_dir, base_dir=base_dir)
        ontology.load()
        
        # 应该使用认证因子的定义
        factor = ontology.get("day_master_strength")
        assert factor.display_zh == "日主强度"  # 认证版
        assert factor.value_type == "numeric"  # 认证版


class TestFactorOntologyIntegration:
    """集成测试：使用实际的因子本体数据"""
    
    @pytest.mark.skipif(
        not Path("data/factor_ontology/certified").exists(),
        reason="需要实际的因子本体数据"
    )
    def test_load_real_data(self):
        """测试加载实际数据"""
        ontology = FactorOntology()
        ontology.load()
        
        stats = ontology.stats
        print(f"\n=== FactorOntology 加载统计 ===")
        print(f"总因子数: {stats['total_factors']}")
        print(f"认证因子: {stats['certified_factors']}")
        print(f"基础因子: {stats['base_factors']}")
        
        print(f"\n按体系统计:")
        for system, count in sorted(stats['factors_by_system'].items()):
            print(f"  {system}: {count}")
        
        print(f"\n按分类统计:")
        for cat, count in sorted(stats['factors_by_category'].items()):
            print(f"  {cat}: {count}")
        
        # 验证加载成功
        assert stats["total_factors"] > 0
        assert stats["certified_factors"] > 0
    
    @pytest.mark.skipif(
        not Path("data/factor_ontology/certified").exists(),
        reason="需要实际的因子本体数据"
    )
    def test_value_type_distribution(self):
        """测试 value_type 分布"""
        ontology = FactorOntology()
        ontology.load()
        
        type_counts = {"boolean": 0, "numeric": 0, "enum": 0, "other": 0}
        
        for fid in ontology._factors:
            factor = ontology.get(fid)
            vtype = factor.value_type
            if vtype in type_counts:
                type_counts[vtype] += 1
            else:
                type_counts["other"] += 1
        
        print(f"\n=== value_type 分布 ===")
        for vtype, count in type_counts.items():
            print(f"  {vtype}: {count}")
        
        # 验证主要类型存在
        assert type_counts["boolean"] > 0 or type_counts["enum"] > 0
