"""
统一维度体系

解决 GAP-01: 三套维度定义不统一问题

设计原则：
1. 三层维度各有职责，不混用
2. 提供完整的映射关系
3. 所有现有代码通过此模块访问维度

对照文档: docs/ls_roadmap_executable.md §二、统一维度体系
"""

from enum import Enum
from typing import Dict, List, Optional, Tuple

from pydantic import BaseModel, Field


# =============================================================================
# Layer 1: 生活领域 (产品层面向用户)
# =============================================================================

class LifeDomain(str, Enum):
    """
    生活领域 - 用户可感知的人生维度
    
    用于：场景选择、版本分类、用户交互
    """
    CAREER = "career"           # 职业/事业
    WEALTH = "wealth"           # 财富/收入
    RELATIONSHIP = "relationship"  # 感情/人际
    HEALTH = "health"           # 健康/身体
    FAMILY = "family"           # 家庭/亲属
    CREATIVITY = "creativity"   # 创造力/学习
    SPIRITUAL = "spiritual"     # 精神/内心


LIFE_DOMAIN_LABELS: Dict[LifeDomain, Dict[str, str]] = {
    LifeDomain.CAREER: {"zh": "事业", "en": "Career"},
    LifeDomain.WEALTH: {"zh": "财富", "en": "Wealth"},
    LifeDomain.RELATIONSHIP: {"zh": "感情", "en": "Relationship"},
    LifeDomain.HEALTH: {"zh": "健康", "en": "Health"},
    LifeDomain.FAMILY: {"zh": "家庭", "en": "Family"},
    LifeDomain.CREATIVITY: {"zh": "创造力", "en": "Creativity"},
    LifeDomain.SPIRITUAL: {"zh": "精神", "en": "Spiritual"},
}


# =============================================================================
# Layer 2: 分析维度 (规则引擎层面)
# =============================================================================

class AnalysisDimension(str, Enum):
    """
    分析维度 - 规则执行结果的分类
    
    用于：RuntimeRuleResult.dimension、主题映射
    
    与 dimension.py 中的 STANDARD_DIMENSIONS 保持一致
    """
    CAREER = "career"           # 事业
    HEALTH = "health"           # 健康
    MARRIAGE = "marriage"       # 婚姻（比 relationship 更具体）
    WEALTH = "wealth"           # 财富
    PERSONALITY = "personality" # 性格
    FORTUNE = "fortune"         # 运势
    OMEN = "omen"               # 预兆
    GUIDANCE = "guidance"       # 指引
    UNCONSCIOUS = "unconscious" # 潜意识
    GENERAL = "general"         # 通用


ANALYSIS_DIMENSION_LABELS: Dict[AnalysisDimension, Dict[str, str]] = {
    AnalysisDimension.CAREER: {"zh": "事业", "en": "Career"},
    AnalysisDimension.HEALTH: {"zh": "健康", "en": "Health"},
    AnalysisDimension.MARRIAGE: {"zh": "婚姻", "en": "Marriage"},
    AnalysisDimension.WEALTH: {"zh": "财富", "en": "Wealth"},
    AnalysisDimension.PERSONALITY: {"zh": "性格", "en": "Personality"},
    AnalysisDimension.FORTUNE: {"zh": "运势", "en": "Fortune"},
    AnalysisDimension.OMEN: {"zh": "预兆", "en": "Omen"},
    AnalysisDimension.GUIDANCE: {"zh": "指引", "en": "Guidance"},
    AnalysisDimension.UNCONSCIOUS: {"zh": "潜意识", "en": "Unconscious"},
    AnalysisDimension.GENERAL: {"zh": "通用", "en": "General"},
}


# =============================================================================
# 维度映射关系
# =============================================================================

# LifeDomain → 对应的 AnalysisDimensions
DOMAIN_TO_DIMENSIONS: Dict[LifeDomain, List[AnalysisDimension]] = {
    LifeDomain.CAREER: [
        AnalysisDimension.CAREER,
        AnalysisDimension.FORTUNE,
        AnalysisDimension.GUIDANCE,
    ],
    LifeDomain.WEALTH: [
        AnalysisDimension.WEALTH,
        AnalysisDimension.FORTUNE,
    ],
    LifeDomain.RELATIONSHIP: [
        AnalysisDimension.MARRIAGE,
        AnalysisDimension.PERSONALITY,
    ],
    LifeDomain.HEALTH: [
        AnalysisDimension.HEALTH,
    ],
    LifeDomain.FAMILY: [
        AnalysisDimension.MARRIAGE,
        AnalysisDimension.PERSONALITY,
    ],
    LifeDomain.CREATIVITY: [
        AnalysisDimension.PERSONALITY,
        AnalysisDimension.GUIDANCE,
        AnalysisDimension.UNCONSCIOUS,
    ],
    LifeDomain.SPIRITUAL: [
        AnalysisDimension.UNCONSCIOUS,
        AnalysisDimension.OMEN,
        AnalysisDimension.GUIDANCE,
    ],
}

# AnalysisDimension → 可能归属的 LifeDomains (自动生成反向映射)
DIMENSION_TO_DOMAINS: Dict[AnalysisDimension, List[LifeDomain]] = {}
for _dim in AnalysisDimension:
    DIMENSION_TO_DOMAINS[_dim] = [
        d for d, dims in DOMAIN_TO_DIMENSIONS.items() if _dim in dims
    ]


# =============================================================================
# Layer 3: 决策维度 (版本比较层面)
# =============================================================================

class DecisionAxis(BaseModel):
    """
    决策维度 - 用于 Life Versions 比较
    
    每个场景(LifeDomain)有自己的决策维度集合
    """
    axis_id: str = Field(..., pattern=r"^[a-z][a-z0-9_]*$")
    label_zh: str
    label_en: str
    description: str = ""
    value_type: str = Field(default="float", pattern=r"^(float|enum|boolean)$")
    value_range: Tuple[float, float] = Field(default=(0.0, 1.0))
    default_weight: float = Field(default=1.0, ge=0.0, le=2.0)


# 各场景的决策维度定义
CAREER_DECISION_AXES: List[DecisionAxis] = [
    DecisionAxis(
        axis_id="income_ceiling",
        label_zh="收入上限",
        label_en="Income Ceiling",
        description="该路径的预期最高收入水平",
    ),
    DecisionAxis(
        axis_id="stability",
        label_zh="稳定性",
        label_en="Stability",
        description="工作/收入的稳定程度",
    ),
    DecisionAxis(
        axis_id="autonomy",
        label_zh="自主性",
        label_en="Autonomy",
        description="工作的自由度和决策权",
    ),
    DecisionAxis(
        axis_id="growth_potential",
        label_zh="成长性",
        label_en="Growth Potential",
        description="技能和职级的上升空间",
    ),
    DecisionAxis(
        axis_id="social_exposure",
        label_zh="社交曝光",
        label_en="Social Exposure",
        description="社交和人脉拓展机会",
    ),
    DecisionAxis(
        axis_id="work_life_balance",
        label_zh="工作生活平衡",
        label_en="Work-Life Balance",
        description="工作与生活的平衡程度",
    ),
]

RELATIONSHIP_DECISION_AXES: List[DecisionAxis] = [
    DecisionAxis(
        axis_id="emotional_depth",
        label_zh="情感深度",
        label_en="Emotional Depth",
        description="关系的情感连接程度",
    ),
    DecisionAxis(
        axis_id="compatibility",
        label_zh="匹配度",
        label_en="Compatibility",
        description="价值观和生活方式的匹配",
    ),
    DecisionAxis(
        axis_id="independence",
        label_zh="独立性",
        label_en="Independence",
        description="保持个人空间的程度",
    ),
    DecisionAxis(
        axis_id="social_harmony",
        label_zh="社交和谐",
        label_en="Social Harmony",
        description="与双方社交圈的融洽程度",
    ),
    DecisionAxis(
        axis_id="future_planning",
        label_zh="未来规划",
        label_en="Future Planning",
        description="对未来的共同规划清晰度",
    ),
]

WEALTH_DECISION_AXES: List[DecisionAxis] = [
    DecisionAxis(
        axis_id="income_growth",
        label_zh="收入增长",
        label_en="Income Growth",
        description="收入的增长潜力",
    ),
    DecisionAxis(
        axis_id="asset_security",
        label_zh="资产安全",
        label_en="Asset Security",
        description="资产的保值和安全性",
    ),
    DecisionAxis(
        axis_id="liquidity",
        label_zh="流动性",
        label_en="Liquidity",
        description="资金的灵活使用程度",
    ),
    DecisionAxis(
        axis_id="risk_tolerance",
        label_zh="风险承受",
        label_en="Risk Tolerance",
        description="投资风险的承受能力匹配",
    ),
]

HEALTH_DECISION_AXES: List[DecisionAxis] = [
    DecisionAxis(
        axis_id="physical_vitality",
        label_zh="身体活力",
        label_en="Physical Vitality",
        description="身体机能和精力水平",
    ),
    DecisionAxis(
        axis_id="mental_wellness",
        label_zh="心理健康",
        label_en="Mental Wellness",
        description="心理状态和情绪稳定性",
    ),
    DecisionAxis(
        axis_id="lifestyle_sustainability",
        label_zh="生活方式可持续性",
        label_en="Lifestyle Sustainability",
        description="健康生活方式的可持续程度",
    ),
]

# 场景到决策维度的映射
DOMAIN_TO_DECISION_AXES: Dict[LifeDomain, List[DecisionAxis]] = {
    LifeDomain.CAREER: CAREER_DECISION_AXES,
    LifeDomain.WEALTH: WEALTH_DECISION_AXES,
    LifeDomain.RELATIONSHIP: RELATIONSHIP_DECISION_AXES,
    LifeDomain.HEALTH: HEALTH_DECISION_AXES,
    LifeDomain.FAMILY: RELATIONSHIP_DECISION_AXES,  # 复用感情维度
    LifeDomain.CREATIVITY: CAREER_DECISION_AXES[:4],  # 复用部分事业维度
    LifeDomain.SPIRITUAL: [],  # 精神领域暂无标准决策维度
}


# =============================================================================
# 统一访问接口
# =============================================================================

class DimensionRegistry:
    """
    维度注册表 - 所有维度访问的统一入口
    
    废弃直接使用 dimension.py 的旧接口
    """
    
    @staticmethod
    def get_life_domain_label(domain: LifeDomain, lang: str = "zh") -> str:
        """获取生活领域标签"""
        return LIFE_DOMAIN_LABELS[domain][lang]
    
    @staticmethod
    def get_analysis_dimension_label(dim: AnalysisDimension, lang: str = "zh") -> str:
        """获取分析维度标签"""
        return ANALYSIS_DIMENSION_LABELS[dim][lang]
    
    @staticmethod
    def get_dimensions_for_domain(domain: LifeDomain) -> List[AnalysisDimension]:
        """获取生活领域对应的分析维度列表"""
        return DOMAIN_TO_DIMENSIONS.get(domain, [])
    
    @staticmethod
    def get_domains_for_dimension(dim: AnalysisDimension) -> List[LifeDomain]:
        """获取分析维度可能归属的生活领域列表"""
        return DIMENSION_TO_DOMAINS.get(dim, [])
    
    @staticmethod
    def get_decision_axes_for_domain(domain: LifeDomain) -> List[DecisionAxis]:
        """获取生活领域对应的决策维度列表"""
        return DOMAIN_TO_DECISION_AXES.get(domain, [])
    
    @staticmethod
    def normalize_dimension(raw: str) -> AnalysisDimension:
        """
        标准化维度名称（兼容旧数据）
        
        支持：
        - 英文小写: "career" -> CAREER
        - 中文: "事业" -> CAREER
        - 未知 -> GENERAL
        """
        # 英文小写匹配
        lower = raw.lower().strip()
        for dim in AnalysisDimension:
            if dim.value == lower:
                return dim
        
        # 中文映射
        for dim, labels in ANALYSIS_DIMENSION_LABELS.items():
            if raw.strip() == labels["zh"]:
                return dim
        
        return AnalysisDimension.GENERAL
    
    @staticmethod
    def normalize_life_domain(raw: str) -> Optional[LifeDomain]:
        """
        标准化生活领域名称
        
        支持：
        - 英文小写: "career" -> CAREER
        - 中文: "事业" -> CAREER
        - 未知 -> None
        """
        lower = raw.lower().strip()
        for domain in LifeDomain:
            if domain.value == lower:
                return domain
        
        for domain, labels in LIFE_DOMAIN_LABELS.items():
            if raw.strip() == labels["zh"]:
                return domain
        
        return None
    
    @staticmethod
    def get_all_life_domains() -> List[LifeDomain]:
        """获取所有生活领域"""
        return list(LifeDomain)
    
    @staticmethod
    def get_all_analysis_dimensions() -> List[AnalysisDimension]:
        """获取所有分析维度"""
        return list(AnalysisDimension)
    
    @staticmethod
    def get_playbook_dimensions(lang: str = "zh") -> List[str]:
        """
        获取 Playbook 使用的维度列表
        
        返回用户面向的生活领域标签（如 ["事业", "财富", "感情", "健康"]）
        """
        # 核心四个领域用于 Playbook
        core_domains = [
            LifeDomain.CAREER,
            LifeDomain.WEALTH,
            LifeDomain.RELATIONSHIP,
            LifeDomain.HEALTH,
        ]
        return [LIFE_DOMAIN_LABELS[d][lang] for d in core_domains]
