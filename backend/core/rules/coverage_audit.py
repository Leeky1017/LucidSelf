"""
规则覆盖度审计

分析因子与规则的匹配情况，找出未覆盖或冗余的规则。

功能:
1. 统计因子被规则引用的情况
2. 识别未被引用的因子
3. 识别无法匹配的规则（条件中的因子不存在）
4. 生成覆盖度报告

对照 roadmap: .kiro/docs/ls_implementation_roadmap.md P2 优化
"""

import logging
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Set

logger = logging.getLogger(__name__)


@dataclass
class FactorCoverage:
    """因子覆盖情况"""
    factor_id: str
    referencing_rules: List[str] = field(default_factory=list)
    is_referenced: bool = False
    reference_count: int = 0


@dataclass
class RuleCoverage:
    """规则覆盖情况"""
    rule_id: str
    required_factors: List[str] = field(default_factory=list)
    missing_factors: List[str] = field(default_factory=list)
    is_matchable: bool = True


@dataclass
class CoverageReport:
    """覆盖度报告"""
    timestamp: datetime = field(default_factory=datetime.utcnow)
    
    # 因子统计
    total_factors: int = 0
    referenced_factors: int = 0
    unreferenced_factors: List[str] = field(default_factory=list)
    
    # 规则统计
    total_rules: int = 0
    matchable_rules: int = 0
    unmatchable_rules: List[str] = field(default_factory=list)
    
    # 详细信息
    factor_details: Dict[str, FactorCoverage] = field(default_factory=dict)
    rule_details: Dict[str, RuleCoverage] = field(default_factory=dict)
    
    # 覆盖率
    factor_coverage_rate: float = 0.0
    rule_matchability_rate: float = 0.0


class RuleCoverageAuditor:
    """
    规则覆盖度审计器
    
    分析因子定义、规则条件之间的关系，识别问题。
    """
    
    def __init__(self):
        """初始化审计器"""
        self._factor_ids: Set[str] = set()
        self._rules: Dict[str, List[str]] = {}  # rule_id -> required_factors
    
    def load_factors(self, factor_ids: List[str]) -> None:
        """
        加载因子 ID 列表
        
        Args:
            factor_ids: 系统支持的因子 ID 列表
        """
        self._factor_ids = set(factor_ids)
        logger.info(f"Loaded {len(self._factor_ids)} factors")
    
    def load_factors_from_registry(self) -> None:
        """从 FactorRegistry 加载因子"""
        try:
            from backend.core.factor_registry import FactorRegistry
            
            registry = FactorRegistry()
            self._factor_ids = set(registry.get_all_factor_ids())
            logger.info(f"Loaded {len(self._factor_ids)} factors from registry")
        except Exception as e:
            logger.warning(f"Failed to load factors from registry: {e}")
    
    def load_rules(self, rules: Dict[str, List[str]]) -> None:
        """
        加载规则
        
        Args:
            rules: {rule_id: [required_factor_ids]}
        """
        self._rules = rules
        logger.info(f"Loaded {len(self._rules)} rules")
    
    def load_rules_from_registry(self) -> None:
        """从 RuleRegistry 加载规则"""
        try:
            from backend.core.rules.registry import RuleRegistry
            
            registry = RuleRegistry()
            all_rules = registry.get_all_rules()
            
            for rule in all_rules:
                # 提取规则的条件中的因子
                required_factors = self._extract_factors_from_rule(rule)
                self._rules[rule.rule_id] = required_factors
            
            logger.info(f"Loaded {len(self._rules)} rules from registry")
        except Exception as e:
            logger.warning(f"Failed to load rules from registry: {e}")
    
    def _extract_factors_from_rule(self, rule: Any) -> List[str]:
        """从规则中提取所需因子"""
        factors = []
        
        # 尝试不同的规则结构
        if hasattr(rule, 'condition'):
            factors.extend(self._extract_factors_from_condition(rule.condition))
        
        if hasattr(rule, 'required_factors'):
            factors.extend(rule.required_factors)
        
        if hasattr(rule, 'triggers'):
            for trigger in rule.triggers:
                if hasattr(trigger, 'factor_id'):
                    factors.append(trigger.factor_id)
        
        return list(set(factors))
    
    def _extract_factors_from_condition(self, condition: Any) -> List[str]:
        """从条件中提取因子"""
        factors = []
        
        if isinstance(condition, dict):
            # 处理字典形式的条件
            if 'factor' in condition:
                factors.append(condition['factor'])
            if 'factors' in condition:
                factors.extend(condition['factors'])
            
            # 递归处理嵌套条件
            for key in ['and', 'or', 'conditions']:
                if key in condition:
                    for sub in condition[key]:
                        factors.extend(self._extract_factors_from_condition(sub))
        
        elif hasattr(condition, 'factor_id'):
            factors.append(condition.factor_id)
        
        elif hasattr(condition, 'conditions'):
            for sub in condition.conditions:
                factors.extend(self._extract_factors_from_condition(sub))
        
        return factors
    
    def audit(self) -> CoverageReport:
        """
        执行覆盖度审计
        
        Returns:
            覆盖度报告
        """
        report = CoverageReport()
        report.total_factors = len(self._factor_ids)
        report.total_rules = len(self._rules)
        
        # 统计因子引用情况
        factor_refs: Dict[str, List[str]] = {fid: [] for fid in self._factor_ids}
        
        for rule_id, required_factors in self._rules.items():
            for factor_id in required_factors:
                if factor_id in factor_refs:
                    factor_refs[factor_id].append(rule_id)
        
        # 生成因子详情
        for factor_id in self._factor_ids:
            refs = factor_refs.get(factor_id, [])
            coverage = FactorCoverage(
                factor_id=factor_id,
                referencing_rules=refs,
                is_referenced=len(refs) > 0,
                reference_count=len(refs),
            )
            report.factor_details[factor_id] = coverage
            
            if coverage.is_referenced:
                report.referenced_factors += 1
            else:
                report.unreferenced_factors.append(factor_id)
        
        # 生成规则详情
        for rule_id, required_factors in self._rules.items():
            missing = [f for f in required_factors if f not in self._factor_ids]
            coverage = RuleCoverage(
                rule_id=rule_id,
                required_factors=required_factors,
                missing_factors=missing,
                is_matchable=len(missing) == 0,
            )
            report.rule_details[rule_id] = coverage
            
            if coverage.is_matchable:
                report.matchable_rules += 1
            else:
                report.unmatchable_rules.append(rule_id)
        
        # 计算覆盖率
        if report.total_factors > 0:
            report.factor_coverage_rate = report.referenced_factors / report.total_factors
        if report.total_rules > 0:
            report.rule_matchability_rate = report.matchable_rules / report.total_rules
        
        logger.info(
            f"Audit complete: "
            f"factor_coverage={report.factor_coverage_rate:.1%}, "
            f"rule_matchability={report.rule_matchability_rate:.1%}"
        )
        
        return report
    
    def generate_summary(self, report: CoverageReport) -> str:
        """
        生成人类可读的摘要
        
        Args:
            report: 覆盖度报告
            
        Returns:
            摘要文本
        """
        lines = [
            "=" * 50,
            "规则覆盖度审计报告",
            f"生成时间: {report.timestamp.isoformat()}",
            "=" * 50,
            "",
            "📊 因子统计",
            f"  总数: {report.total_factors}",
            f"  被引用: {report.referenced_factors} ({report.factor_coverage_rate:.1%})",
            f"  未引用: {len(report.unreferenced_factors)}",
            "",
            "📋 规则统计",
            f"  总数: {report.total_rules}",
            f"  可匹配: {report.matchable_rules} ({report.rule_matchability_rate:.1%})",
            f"  不可匹配: {len(report.unmatchable_rules)}",
            "",
        ]
        
        # 列出问题
        if report.unreferenced_factors:
            lines.append("⚠️ 未被引用的因子 (前10个):")
            for fid in report.unreferenced_factors[:10]:
                lines.append(f"  - {fid}")
            if len(report.unreferenced_factors) > 10:
                lines.append(f"  ... 及另外 {len(report.unreferenced_factors) - 10} 个")
            lines.append("")
        
        if report.unmatchable_rules:
            lines.append("❌ 无法匹配的规则 (前10个):")
            for rid in report.unmatchable_rules[:10]:
                missing = report.rule_details[rid].missing_factors
                lines.append(f"  - {rid}: 缺少 {missing}")
            if len(report.unmatchable_rules) > 10:
                lines.append(f"  ... 及另外 {len(report.unmatchable_rules) - 10} 个")
            lines.append("")
        
        # 建议
        lines.extend([
            "💡 建议",
            f"  1. 检查 {len(report.unreferenced_factors)} 个未引用因子是否需要删除或添加规则",
            f"  2. 修复 {len(report.unmatchable_rules)} 个不可匹配规则的因子依赖",
        ])
        
        return "\n".join(lines)


# =============================================================================
# 便捷函数
# =============================================================================

def run_coverage_audit(verbose: bool = True) -> CoverageReport:
    """
    运行覆盖度审计
    
    Args:
        verbose: 是否打印摘要
        
    Returns:
        覆盖度报告
    """
    auditor = RuleCoverageAuditor()
    auditor.load_factors_from_registry()
    auditor.load_rules_from_registry()
    
    report = auditor.audit()
    
    if verbose:
        summary = auditor.generate_summary(report)
        print(summary)
    
    return report
