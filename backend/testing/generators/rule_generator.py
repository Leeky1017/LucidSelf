"""
Rule Test Case Generator

规则测试用例生成器。

对照 design.md §2.4 测试数据生成
对照 Requirements R-6-2-01, R-6-2-02
"""

from __future__ import annotations

import random
from typing import Any, Dict, List, Optional
from dataclasses import dataclass, field

from backend.core.contracts.test_schema_models import RuleTestCase


@dataclass
class RuleTestCaseGenerator:
    """
    规则测试用例生成器
    
    对照 R-6-2-01: 边界情况自动生成
    对照 R-6-2-02: 因子组合覆盖
    """
    
    # 八字因子值域
    BAZI_FACTORS: Dict[str, List[str]] = field(default_factory=lambda: {
        "day_master": ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"],
        "month_branch": ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"],
        "season": ["spring", "summer", "autumn", "winter"],
        "year_stem": ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"],
        "hour_branch": ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"],
        "day_branch": ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"],
        "month_stem": ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"],
        "hour_stem": ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"],
    })
    
    # 紫微因子值域
    ZIWEI_FACTORS: Dict[str, List[str]] = field(default_factory=lambda: {
        "main_star": ["紫微", "天机", "太阳", "武曲", "天同", "廉贞", "天府", 
                      "太阴", "贪狼", "巨门", "天相", "天梁", "七杀", "破军"],
        "palace": ["命宫", "兄弟", "夫妻", "子女", "财帛", "疾厄",
                   "迁移", "交友", "官禄", "田宅", "福德", "父母"],
        "brightness": ["庙", "旺", "得地", "平", "落陷"],
    })
    
    # 占星因子值域
    ASTRO_FACTORS: Dict[str, List[str]] = field(default_factory=lambda: {
        "sun_sign": ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
                     "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"],
        "moon_sign": ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
                      "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"],
        "rising_sign": ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
                        "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"],
        "aspect": ["conjunction", "opposition", "trine", "square", "sextile"],
    })
    
    def generate_positive_case(
        self,
        rule_id: str,
        engine: str = "bazi",
        expected_dimension: str = "事业",
        expected_level: str = "high",
    ) -> RuleTestCase:
        """
        生成正向测试用例
        
        Args:
            rule_id: 规则ID
            engine: 引擎类型
            expected_dimension: 期望维度
            expected_level: 期望等级
        """
        factors = self._generate_factors(engine)
        
        return RuleTestCase(
            test_id=f"pos_{rule_id}_{random.randint(1000, 9999)}",
            target_rule_id=rule_id,
            test_type="positive",
            mock_factors=factors,
            expect_hit=True,
            expected_dimension=expected_dimension,
            expected_level=expected_level,
            expected_confidence_min=0.6,
            expected_confidence_max=1.0,
            source_book="auto_generated",
            description=f"Auto-generated positive test for {rule_id}",
        )
    
    def generate_negative_case(
        self,
        rule_id: str,
        engine: str = "bazi",
    ) -> RuleTestCase:
        """
        生成负向测试用例
        """
        factors = self._generate_factors(engine)
        
        return RuleTestCase(
            test_id=f"neg_{rule_id}_{random.randint(1000, 9999)}",
            target_rule_id=rule_id,
            test_type="negative",
            mock_factors=factors,
            expect_hit=False,
            source_book="auto_generated",
            description=f"Auto-generated negative test for {rule_id}",
        )
    
    def generate_edge_case(
        self,
        rule_id: str,
        engine: str = "bazi",
        edge_type: str = "boundary",
    ) -> RuleTestCase:
        """
        生成边界测试用例
        
        对照 R-6-2-01
        
        Args:
            edge_type: 边界类型 (boundary, empty, null)
        """
        factors = self._generate_edge_factors(engine, edge_type)
        
        return RuleTestCase(
            test_id=f"edge_{rule_id}_{edge_type}_{random.randint(1000, 9999)}",
            target_rule_id=rule_id,
            test_type="edge",
            mock_factors=factors,
            expect_hit=False,  # 边界通常不触发
            source_book="auto_generated",
            description=f"Auto-generated edge test ({edge_type}) for {rule_id}",
        )
    
    def generate_pairwise_cases(
        self,
        rule_id: str,
        engine: str = "bazi",
        factors_to_test: Optional[List[str]] = None,
        max_cases: int = 20,
    ) -> List[RuleTestCase]:
        """
        生成配对组合测试用例
        
        对照 R-6-2-02: 因子组合覆盖
        
        使用 pairwise 策略减少用例数量同时保证两两覆盖。
        """
        factor_domains = self._get_factor_domains(engine)
        
        if factors_to_test:
            factor_domains = {k: v for k, v in factor_domains.items() if k in factors_to_test}
        
        cases = []
        factor_names = list(factor_domains.keys())
        
        # 简化的 pairwise：随机选取组合
        for i in range(min(max_cases, len(factor_names) * 3)):
            factors = {}
            for name in factor_names:
                factors[name] = random.choice(factor_domains[name])
            
            cases.append(RuleTestCase(
                test_id=f"pair_{rule_id}_{i:03d}",
                target_rule_id=rule_id,
                test_type="positive",
                mock_factors=factors,
                expect_hit=True,
                source_book="auto_generated",
                description=f"Auto-generated pairwise test {i} for {rule_id}",
            ))
        
        return cases
    
    def _generate_factors(self, engine: str) -> Dict[str, Any]:
        """生成随机因子"""
        domains = self._get_factor_domains(engine)
        return {k: random.choice(v) for k, v in domains.items()}
    
    def _generate_edge_factors(self, engine: str, edge_type: str) -> Dict[str, Any]:
        """生成边界因子"""
        domains = self._get_factor_domains(engine)
        factors = {}
        
        for k, v in domains.items():
            if edge_type == "boundary":
                # 使用边界值（首尾）
                factors[k] = v[0] if random.random() < 0.5 else v[-1]
            elif edge_type == "empty":
                # 空值
                factors[k] = ""
            elif edge_type == "null":
                # 不设置该因子
                pass
            else:
                factors[k] = random.choice(v)
        
        return factors
    
    def _get_factor_domains(self, engine: str) -> Dict[str, List[str]]:
        """获取因子值域"""
        if engine == "bazi":
            return self.BAZI_FACTORS
        elif engine == "ziwei":
            return self.ZIWEI_FACTORS
        elif engine == "astro":
            return self.ASTRO_FACTORS
        else:
            return self.BAZI_FACTORS
