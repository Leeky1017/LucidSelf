"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.101598
Version: 1.0.0

对照 Requirements 6.4 - 带 @SemanticRegistry.register 装饰器的 Python 模块
"""

from backend.semantics.core.base import SemanticEntry, SemanticRegistry, NarrativeSnippetExtended
from backend.core.contracts import (
    SnippetRole,
    SourceMetadata,
    ConfigRelation,
    EvidenceChainEntry,
    RelationType,
    EffectDirection,
    ConfidenceLevel,
)


@SemanticRegistry.register(
    semantic_id="smth_v1.0.0_论浮沉与破煞_001",
    book_id="sanming",
    engine_id="bazi"
)
class 论浮沉与破煞(SemanticEntry):
    """
    - **原文（source_text）**：
  浮沉煞。从戌上起，子逆行至本生年位，却从年宫数，看在何宫。只在财帛宫，名串钱，主富蓄。余皆凶。甲乙己庚壬人犯之，稍轻；丙丁戊辛癸人犯之，重。在寅午申未...
    """
    
    original_text: str = """- **原文（source_text）**：
  浮沉煞。从戌上起，子逆行至本生年位，却从年宫数，看在何宫。只在财帛宫，名串钱，主富蓄。余皆凶。甲乙己庚壬人犯之，稍轻；丙丁戊辛癸人犯之，重。在寅午申未年中，此煞多主水厄。仍各随宫分论灾，如在田宅，则主破祖。余宫类推。
  破煞。此煞，卯与午，丑与辰，子与酉，未与戌，皆相破。惟寅申巳亥原破，却三合，故不取，犯者主少年灾滞，财产耗散，兼有折伤之灾。

- **分字分词释义**：
  - **浮沉煞**：从戌逆推至年宫，仅在财帛宫主富，余宫主灾，特定年份主水厄。
  - **破煞**：六破组合（卯午、丑辰、子酉、未戌），主少年灾滞与财产耗散。

- **规范化释义（primary_lang_explained）**：
  浮沉煞从戌位起子逆推至生年，再从年宫推算落何宫位。唯独落财帛宫称"串钱"主富，其余宫位皆凶。特定日干（丙丁戊辛癸）犯之更重，在寅午申未年中尤主水厄。破煞指六组"相破"组合（卯午、丑辰、子酉、未戌），寅申巳亥虽破但成三合故不取。犯者主少年波折、财产损耗与肢体折伤。

- **次语种完整诠释（secondary_lang_full）**：
  Floating-Sinking Sha (Fu Chen) calculates backward from Xu to Birth Year, then forward to see which palace it lands. Only in Wealth Palace ("String Money") it indicates prosperity; elsewhere it's malefic. Certain Day Stems (Bing/Ding/Wu/Xin/Gui) suffer more. In Yin/Wu/Shen/Wei years, it especially indicates drowning. Breaking Sha (Po) involves six "breaking" pairs (Mao-Wu, Chou-Chen, Zi-You, Wei-Xu); Yin-Shen-Si-Hai pairs are excluded as they form Triads. Those afflicted face youthful setbacks, wealth dissipation, and physical injury.

- **核心要点**：
  - 浮沉：宫位吉凶差异（唯财帛宫吉）
  - 破煞：六破组合主耗散折伤

- **详细解说**：
  浮沉煞是罕见的"单宫吉、余宫凶"型神煞，体现了古人对"财富稳定性"的关注——唯有财帛宫能"串钱"成链，其他宫位则如浮萍无根。破煞则是地支六破理论的应用，代表"结构性损耗"，类似于现代的"资源破碎化"风险。"""
    normalized_text_zh: str = """"""
    subject: str = "论浮沉与破煞"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate']
    
    # 叙事素材（包含 trigger_human）
    narrative_snippets: list = [

    ]
    
    # L2.5 因子关系
    related_semantics: list = [

    ]
    
    # L2.5 证据链
    evidence_refs: list = [

    ]
    
    metadata: SourceMetadata = SourceMetadata(
        book_id="sanming",
        chapter="",
        l1_anchor="smth_v1.0.0_论浮沉与破煞_001_L1",
    )
    version: str = "1.0.0"
