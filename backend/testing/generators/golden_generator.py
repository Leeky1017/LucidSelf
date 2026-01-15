"""
Golden Case Generator

黄金用例生成器。

对照 design.md §2.4 测试数据生成
对照 Requirements R-6-2-03, R-6-2-04
"""

from __future__ import annotations

import hashlib
import json
import random
from datetime import datetime, timedelta
from typing import Any, Dict, List, Optional
from dataclasses import dataclass, field

from backend.core.contracts.test_schema_models import GoldenCase, NarrativeGolden


@dataclass
class GoldenCaseGenerator:
    """
    黄金用例生成器
    
    对照 R-6-2-03: 场景快照生成
    对照 R-6-2-04: 基线版本管理
    """
    
    # 测试场景模板
    SCENARIOS = [
        {"name": "career_analysis", "engines": ["bazi", "ziwei"], "themes": ["事业", "财运"]},
        {"name": "relationship", "engines": ["bazi", "astro"], "themes": ["感情", "人际"]},
        {"name": "health", "engines": ["bazi", "ziwei"], "themes": ["健康", "身心"]},
        {"name": "fortune", "engines": ["bazi", "ziwei", "astro"], "themes": ["运势", "时机"]},
    ]
    
    def generate_golden_case(
        self,
        scenario_name: Optional[str] = None,
        birth_data: Optional[Dict[str, Any]] = None,
    ) -> GoldenCase:
        """
        生成黄金用例
        
        Args:
            scenario_name: 场景名称
            birth_data: 出生数据（不提供则随机生成）
        """
        scenario = self._get_scenario(scenario_name)
        
        if birth_data is None:
            birth_data = self._generate_birth_data()
        
        # 生成期望结果（占位）
        expected_results = self._generate_expected_results(scenario["engines"])
        expected_fusion = self._generate_expected_fusion(scenario["themes"])
        
        # 计算基线哈希
        baseline_hash = self._compute_baseline_hash(expected_results, expected_fusion)
        
        return GoldenCase(
            case_id=f"golden_{scenario['name']}_{random.randint(1000, 9999)}",
            birth_data=birth_data,
            expected_results=expected_results,
            expected_fusion=expected_fusion,
            max_drift=0.1,
            baseline_hash=baseline_hash,
        )
    
    def generate_narrative_golden(
        self,
        scenario_name: Optional[str] = None,
        must_include_themes: Optional[List[str]] = None,
    ) -> NarrativeGolden:
        """
        生成叙事黄金标准
        """
        scenario = self._get_scenario(scenario_name)
        themes = must_include_themes or scenario["themes"]
        
        return NarrativeGolden(
            golden_id=f"narrative_{scenario['name']}_{random.randint(1000, 9999)}",
            scenario={
                "name": scenario["name"],
                "engines": scenario["engines"],
                "query_type": "general_analysis",
            },
            must_include_themes=themes,
            forbidden_expressions=["迷信", "绝对", "一定会", "命中注定"],
            min_quality_score=0.8,
            eval_model="gpt-4o-mini",
        )
    
    def update_baseline(
        self,
        case: GoldenCase,
        new_results: Dict[str, Any],
        new_fusion: Dict[str, Any],
    ) -> GoldenCase:
        """
        更新基线版本
        
        对照 R-6-2-04
        """
        new_hash = self._compute_baseline_hash(new_results, new_fusion)
        
        return GoldenCase(
            case_id=case.case_id,
            birth_data=case.birth_data,
            expected_results=new_results,
            expected_fusion=new_fusion,
            max_drift=case.max_drift,
            baseline_hash=new_hash,
        )
    
    def _get_scenario(self, name: Optional[str]) -> Dict[str, Any]:
        """获取场景配置"""
        if name:
            for s in self.SCENARIOS:
                if s["name"] == name:
                    return s
        return random.choice(self.SCENARIOS)
    
    def _generate_birth_data(self) -> Dict[str, Any]:
        """生成随机出生数据"""
        # 随机生成 1950-2010 年间的日期
        start = datetime(1950, 1, 1)
        end = datetime(2010, 12, 31)
        random_date = start + timedelta(days=random.randint(0, (end - start).days))
        
        return {
            "year": random_date.year,
            "month": random_date.month,
            "day": random_date.day,
            "hour": random.randint(0, 23),
            "minute": random.randint(0, 59),
            "gender": random.choice(["male", "female"]),
            "timezone": "Asia/Shanghai",
            "longitude": 116.4 + random.uniform(-10, 10),
            "latitude": 39.9 + random.uniform(-10, 10),
        }
    
    def _generate_expected_results(self, engines: List[str]) -> Dict[str, Any]:
        """生成期望结果模板"""
        results = {}
        for engine in engines:
            results[engine] = {
                "status": "success",
                "rules_hit": random.randint(3, 10),
                "dimensions": ["事业", "财运", "健康"],
            }
        return results
    
    def _generate_expected_fusion(self, themes: List[str]) -> Dict[str, Any]:
        """生成融合结果模板"""
        return {
            "themes": themes,
            "cross_validation_score": 0.75 + random.uniform(0, 0.2),
            "confidence": 0.8 + random.uniform(0, 0.15),
        }
    
    def _compute_baseline_hash(
        self,
        results: Dict[str, Any],
        fusion: Dict[str, Any],
    ) -> str:
        """计算基线哈希"""
        content = json.dumps({"results": results, "fusion": fusion}, sort_keys=True)
        return hashlib.sha256(content.encode()).hexdigest()[:16]


@dataclass
class ScenarioLibrary:
    """
    场景库
    
    预定义的测试场景集合。
    """
    
    CAREER_SCENARIOS = [
        {"query": "分析我的事业运势", "themes": ["事业", "职场"]},
        {"query": "我适合创业吗", "themes": ["事业", "财运"]},
        {"query": "今年工作会顺利吗", "themes": ["事业", "运势"]},
    ]
    
    RELATIONSHIP_SCENARIOS = [
        {"query": "分析我的感情运势", "themes": ["感情", "婚姻"]},
        {"query": "我什么时候能遇到真爱", "themes": ["感情", "时机"]},
    ]
    
    HEALTH_SCENARIOS = [
        {"query": "我的健康状况如何", "themes": ["健康", "身心"]},
        {"query": "需要注意哪些健康问题", "themes": ["健康", "预防"]},
    ]
    
    @classmethod
    def get_all_scenarios(cls) -> List[Dict[str, Any]]:
        """获取所有场景"""
        return (
            cls.CAREER_SCENARIOS +
            cls.RELATIONSHIP_SCENARIOS +
            cls.HEALTH_SCENARIOS
        )
    
    @classmethod
    def get_scenario_by_category(cls, category: str) -> List[Dict[str, Any]]:
        """按类别获取场景"""
        if category == "career":
            return cls.CAREER_SCENARIOS
        elif category == "relationship":
            return cls.RELATIONSHIP_SCENARIOS
        elif category == "health":
            return cls.HEALTH_SCENARIOS
        return []
