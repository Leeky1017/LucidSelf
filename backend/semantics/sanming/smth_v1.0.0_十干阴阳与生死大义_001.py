"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.042247
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
    semantic_id="smth_v1.0.0_十干阴阳与生死大义_001",
    book_id="sanming",
    engine_id="bazi"
)
class 十干阴阳与生死大义(SemanticEntry):
    """
    - **原文（source_text）**：
  或问：十干有阴阳、刚柔、生死之分，其说然否？答曰：十干五阳五阴，阳者为刚，阴者为柔，其生死之分，如母生子，子成而母老死，理之自然。赋曰：阳生阴死，阳死...
    """
    
    original_text: str = """- **原文（source_text）**：
  或问：十干有阴阳、刚柔、生死之分，其说然否？答曰：十干五阳五阴，阳者为刚，阴者为柔，其生死之分，如母生子，子成而母老死，理之自然。赋曰：阳生阴死，阳死阴生，循环逆顺，变化见矣。

- **分字分词释义**：
  - **五阳五阴**：十天干中，甲丙戊庚壬属阳，乙丁己辛癸属阴，对应刚柔之性。
  - **生死之分**：以「母子」比喻同类气机的递嬗：新气生则旧气衰亡。
  - **阳生阴死 / 阳死阴生**：阳气发动，则阴气为其所生、所用；阳衰而死，则阴气承续其用事，反成主宰。

- **规范化释义（primary_lang_explained）**：
  本段先总提纲：十干各有阴阳属性，阳为刚，阴为柔，而所谓「生死」，不是生物学的生死，而是气机交替——就像母生子，子长成之后，母必衰老，这是气势更迭的自然规律。赋文以「阳生阴死、阳死阴生」概括这一循环：一轮阳气兴起，必有一轮阴气退藏；阳气退而阴气又承接其用，如此往复，构成十干轮值的背景逻辑。

- **完整对等诠释（secondary_lang_full）**：
  This passage introduces the fundamental principle: the Ten Heavenly Stems each possess yin-yang attributes—yang represents firmness while yin represents flexibility. The concept of "life-death" here does not mean biological termination but rather the succession of qi phases, analogous to mother giving birth to child: when the child matures, the mother naturally ages and recedes. The classic formula "yang arises then yin recedes, yang recedes then yin arises" summarizes this cyclical pattern—one round of yang qi rising necessitates one round of yin qi withdrawing; when yang qi retreats, yin qi takes over its function, continuing this eternal rotation. This forms the background logic for the Ten Stems' rotation in duty, representing any structural pattern of "new-old succession" and "peak-decline rhythm" in destiny analysis."""
    normalized_text_zh: str = """"""
    subject: str = "十干阴阳与生死大义"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'wuxing_sheng_chain', 'bazi_calculator', 'wuxing_ke_chain', 'bazi_calculator', 'wuxing_parent_child_link', 'bazi_semantic', 'yinyang_balance_score', 'bazi_calculator', 'season_alignment_score', 'bazi_calculator', 'element_dominance_score', 'bazi_calculator', 'seasonal_phase', 'bazi_calculator', 'missing_pillar_info_flag', 'bazi_calculator', 'congge_purity_level', 'bazi_rule_engine', 'evi_smth_02_009', 'yinyang_balance_score', 'rule_yinyang_cycle', 'evi_smth_02_010', 'wuxing_parent_child_link', 'rule_parent_child_succession', 'map_smth_02_009', 'map_smth_02_010']
    
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
        l1_anchor="smth_v1.0.0_十干阴阳与生死大义_001_L1",
    )
    version: str = "1.0.0"
