"""
人生版本生成器

从融合结果生成多个可选的人生版本。

对照文档: docs/ls_roadmap_executable.md §四、Phase 3: Life Versions 核心
"""

import logging
import uuid
from collections import defaultdict
from typing import Any, Dict, List, Optional

from backend.core.contracts.life_version_models import (
    LifeVersion,
    LifeVersionSet,
    VERSION_TEMPLATES,
)
from backend.core.contracts.unified_dimensions import (
    DOMAIN_TO_DECISION_AXES,
    LifeDomain,
)

logger = logging.getLogger(__name__)


class LifeVersionGenerator:
    """
    人生版本生成器
    
    职责:
    - 从融合结果生成 2-3 个可选版本
    - 确保版本间有足够差异化
    - 为每个版本计算预期收益
    """
    
    # 最小差异化阈值
    MIN_DIFFERENTIATION = 0.2
    
    def __init__(self):
        """初始化生成器"""
        pass
    
    def generate(
        self,
        rule_results: List[Any],
        domain: LifeDomain,
        scenario_id: str = "",
        user_id: str = "",
        version_count: int = 3,
    ) -> LifeVersionSet:
        """
        从规则结果生成多个人生版本
        
        核心逻辑:
        1. 获取场景的决策维度
        2. 聚类规则结果，识别不同"倾向"
        3. 为每个倾向生成版本
        4. 验证版本差异化
        
        Args:
            rule_results: RuntimeRuleResult 列表
            domain: 目标生活领域
            scenario_id: 场景 ID
            user_id: 用户 ID
            version_count: 生成版本数量
            
        Returns:
            LifeVersionSet 包含 2-4 个版本
        """
        # 获取该领域的决策维度
        decision_axes = DOMAIN_TO_DECISION_AXES.get(domain, [])
        axis_ids = [a.axis_id for a in decision_axes]
        
        # 聚类规则为不同策略倾向
        clusters = self._cluster_strategies(rule_results)
        
        # 生成版本
        versions = []
        for i, (cluster_name, cluster_rules) in enumerate(clusters[:version_count]):
            template = VERSION_TEMPLATES[i] if i < len(VERSION_TEMPLATES) else VERSION_TEMPLATES[1]
            
            version = self._build_version(
                cluster_name=cluster_name,
                cluster_rules=cluster_rules,
                template=template,
                axis_ids=axis_ids,
                domain=domain,
            )
            versions.append(version)
        
        # 验证差异化
        if len(versions) >= 2:
            self._ensure_differentiation(versions, axis_ids)
        
        set_id = f"vset_{uuid.uuid4().hex[:12]}"
        
        return LifeVersionSet(
            set_id=set_id,
            user_id=user_id,
            scenario_id=scenario_id,
            domain=domain,
            versions=versions,
            comparison_axes=axis_ids,
            recommended_version_id=self._recommend_version(versions),
        )
    
    def _cluster_strategies(
        self, 
        rules: List[Any],
    ) -> List[tuple]:
        """
        将规则聚类为不同策略倾向
        
        MVP: 基于 level (吉/凶) 和 tags 简单分组
        后续: 使用 embedding 聚类
        """
        conservative = []
        balanced = []
        aggressive = []
        
        for rule in rules:
            if not hasattr(rule, "matched") or not rule.matched:
                continue
            
            # 提取规则属性
            tags = str(getattr(rule, "tags", ""))
            description = str(getattr(rule, "description", ""))
            level = getattr(rule, "level", "中等")
            
            # 分类
            if any(k in tags or k in description for k in ["稳", "守", "安全", "保守", "谨慎"]):
                conservative.append(rule)
            elif any(k in tags or k in description for k in ["变", "突破", "进取", "拓展", "激进"]):
                aggressive.append(rule)
            else:
                balanced.append(rule)
        
        return [
            ("conservative", conservative),
            ("balanced", balanced),
            ("aggressive", aggressive),
        ]
    
    def _build_version(
        self,
        cluster_name: str,
        cluster_rules: List[Any],
        template: Dict,
        axis_ids: List[str],
        domain: LifeDomain,
    ) -> LifeVersion:
        """构建单个版本"""
        version_id = f"ver_{uuid.uuid4().hex[:12]}"
        
        # 计算预期收益
        expected_outcomes = self._calculate_outcomes(
            cluster_rules, 
            axis_ids, 
            template.get("bias_toward", []),
            template.get("bias_away", []),
        )
        
        # 提取策略描述
        strategies = self._extract_strategies(cluster_rules, template)
        key_actions = self._extract_key_actions(cluster_rules)
        
        # 提取风险和代价
        risks = self._extract_risks(cluster_rules, template)
        costs = self._extract_costs(template)
        
        # 适合人群
        suitable_for = self._get_suitable_for(template)
        not_suitable_for = self._get_not_suitable_for(template)
        
        # 计算置信度
        confidence = min(1.0, len(cluster_rules) / 10.0) if cluster_rules else 0.3
        
        return LifeVersion(
            version_id=version_id,
            title=template.get("title_zh", "默认版"),
            subtitle=self._generate_subtitle(template, domain),
            strategy=strategies,
            key_actions=key_actions,
            expected_outcomes=expected_outcomes,
            risks=risks,
            costs=costs,
            suitable_for=suitable_for,
            not_suitable_for=not_suitable_for,
            confidence=confidence,
            source_factors=[],  # TODO: 从规则提取关联因子
            source_rules=[getattr(r, "rule_id", "") for r in cluster_rules[:5]],
        )
    
    def _calculate_outcomes(
        self,
        rules: List[Any],
        axis_ids: List[str],
        bias_toward: List[str],
        bias_away: List[str],
    ) -> Dict[str, float]:
        """
        计算各维度的预期得分
        
        TODO: 更精确的计算逻辑
        """
        outcomes = {}
        
        # 基础分数
        base_score = 0.5
        if rules:
            # 从规则提取平均得分
            scores = [getattr(r, "score", 0.5) for r in rules if hasattr(r, "score")]
            base_score = sum(scores) / len(scores) if scores else 0.5
        
        for axis_id in axis_ids:
            score = base_score
            
            # 偏向加成
            if axis_id in bias_toward:
                score = min(1.0, score + 0.15)
            elif axis_id in bias_away:
                score = max(0.0, score - 0.15)
            
            outcomes[axis_id] = round(score, 2)
        
        return outcomes
    
    def _extract_strategies(self, rules: List[Any], template: Dict) -> List[str]:
        """提取策略描述"""
        # MVP: 基于模板生成
        strategy_templates = {
            "conservative": ["保持现有优势", "稳扎稳打", "规避风险"],
            "balanced": ["兼顾发展与稳定", "适度拓展", "平衡各方"],
            "aggressive": ["积极寻求突破", "把握机遇", "大胆尝试"],
        }
        
        name = template.get("name", "balanced")
        return strategy_templates.get(name, strategy_templates["balanced"])[:3]
    
    def _extract_key_actions(self, rules: List[Any]) -> List[str]:
        """提取关键行动"""
        actions = []
        for rule in rules[:3]:
            if hasattr(rule, "advice") and rule.advice:
                actions.append(str(rule.advice)[:50])
        return actions if actions else ["制定详细计划", "持续执行"]
    
    def _extract_risks(self, rules: List[Any], template: Dict) -> List[str]:
        """提取风险因素"""
        risk_templates = {
            "conservative": ["可能错过机遇", "增长空间有限"],
            "balanced": ["需要持续投入精力", "结果中庸"],
            "aggressive": ["失败风险较高", "需要更多资源投入", "可能影响稳定性"],
        }
        name = template.get("name", "balanced")
        return risk_templates.get(name, risk_templates["balanced"])
    
    def _extract_costs(self, template: Dict) -> List[str]:
        """提取代价"""
        cost_templates = {
            "conservative": ["成长机会成本"],
            "balanced": ["时间精力成本"],
            "aggressive": ["稳定性代价", "资源投入"],
        }
        name = template.get("name", "balanced")
        return cost_templates.get(name, cost_templates["balanced"])
    
    def _get_suitable_for(self, template: Dict) -> List[str]:
        """获取适合人群"""
        suitable_templates = {
            "conservative": ["风险厌恶型", "重视稳定"],
            "balanced": ["追求平衡", "稳中求进"],
            "aggressive": ["风险承受力强", "追求突破"],
        }
        name = template.get("name", "balanced")
        return suitable_templates.get(name, suitable_templates["balanced"])
    
    def _get_not_suitable_for(self, template: Dict) -> List[str]:
        """获取不适合人群"""
        not_suitable_templates = {
            "conservative": ["急于求成"],
            "balanced": [],
            "aggressive": ["风险厌恶", "需要稳定"],
        }
        name = template.get("name", "balanced")
        return not_suitable_templates.get(name, [])
    
    def _generate_subtitle(self, template: Dict, domain: LifeDomain) -> str:
        """生成一句话描述"""
        domain_labels = {
            LifeDomain.CAREER: "事业",
            LifeDomain.WEALTH: "财务",
            LifeDomain.RELATIONSHIP: "感情",
            LifeDomain.HEALTH: "健康",
        }
        domain_label = domain_labels.get(domain, domain.value)
        
        subtitle_templates = {
            "conservative": f"以稳定为核心的{domain_label}策略",
            "balanced": f"兼顾发展与稳定的{domain_label}规划",
            "aggressive": f"积极进取的{domain_label}发展路径",
        }
        name = template.get("name", "balanced")
        return subtitle_templates.get(name, f"{domain_label}发展方案")
    
    def _ensure_differentiation(
        self, 
        versions: List[LifeVersion], 
        axis_ids: List[str],
    ) -> None:
        """确保版本间有足够差异化"""
        if len(versions) < 2:
            return
        
        # 计算版本间距离
        for i, v1 in enumerate(versions):
            for j, v2 in enumerate(versions[i+1:], i+1):
                diff = self._calculate_differentiation(v1, v2, axis_ids)
                
                if diff < self.MIN_DIFFERENTIATION:
                    # 强制增加差异
                    self._increase_differentiation(v1, v2, axis_ids)
    
    def _calculate_differentiation(
        self,
        v1: LifeVersion,
        v2: LifeVersion,
        axis_ids: List[str],
    ) -> float:
        """计算两个版本间的差异度"""
        total_diff = 0.0
        count = 0
        
        for axis_id in axis_ids:
            s1 = v1.expected_outcomes.get(axis_id, 0.5)
            s2 = v2.expected_outcomes.get(axis_id, 0.5)
            total_diff += abs(s1 - s2)
            count += 1
        
        return total_diff / count if count > 0 else 0.0
    
    def _increase_differentiation(
        self,
        v1: LifeVersion,
        v2: LifeVersion,
        axis_ids: List[str],
    ) -> None:
        """增加两个版本间的差异"""
        # 对差异最小的维度进行调整
        for axis_id in axis_ids:
            s1 = v1.expected_outcomes.get(axis_id, 0.5)
            s2 = v2.expected_outcomes.get(axis_id, 0.5)
            
            if abs(s1 - s2) < 0.1:
                # 将 v1 调高，v2 调低
                v1.expected_outcomes[axis_id] = min(1.0, s1 + 0.1)
                v2.expected_outcomes[axis_id] = max(0.0, s2 - 0.1)
    
    def _recommend_version(self, versions: List[LifeVersion]) -> Optional[str]:
        """推荐一个版本"""
        # MVP: 推荐平衡版
        for v in versions:
            if "平衡" in v.title or "balanced" in v.title.lower():
                return v.version_id
        
        # 默认推荐第一个
        return versions[0].version_id if versions else None
