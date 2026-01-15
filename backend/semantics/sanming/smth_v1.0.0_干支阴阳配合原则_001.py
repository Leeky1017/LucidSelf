"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228022
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
    semantic_id="smth_v1.0.0_干支阴阳配合原则_001",
    book_id="sanming",
    engine_id="bazi"
)
class 干支阴阳配合原则(SemanticEntry):
    """
    - **原文（source_text）**：
  夫甲、丙、戊、庚壬，阳干也；子寅辰、午申戌，阳枝也；乙、丁、己辛癸，阴干也，丑卯巳、未酉亥，阴枝也。法以阳干配阳枝，阴干配阴枝，犹木之有干而有枝。

...
    """
    
    original_text: str = """- **原文（source_text）**：
  夫甲、丙、戊、庚壬，阳干也；子寅辰、午申戌，阳枝也；乙、丁、己辛癸，阴干也，丑卯巳、未酉亥，阴枝也。法以阳干配阳枝，阴干配阴枝，犹木之有干而有枝。

- **分字分词释义**：
  - **阳干**：五个阳天干。
  - **阳枝**：六个阳地支。
  - **阴干**：五个阴天干。
  - **阴枝**：六个阴地支。
  - **法以**：规则是。
  - **犹木之有干而有枝**：如同树木有干有枝。

- **规范化释义（primary_lang_explained）**：
  甲丙戊庚壬是阳干，子寅辰午申戌是阳支；乙丁己辛癸是阴干，丑卯巳未酉亥是阴支。规则是阳干配阳支，阴干配阴支，就像树木有干有枝一样。

- **完整对等诠释（secondary_lang_full）**：
  Jia-Bing-Wu-Geng-Ren are yang Stems; Zi-Yin-Chen-Wu-Shen-Xu are yang Branches; Yi-Ding-Ji-Xin-Gui are yin Stems; Chou-Mao-Si-Wei-You-Hai are yin Branches. The rule is yang Stems pair with yang Branches, yin Stems pair with yin Branches, like a tree having both trunk and branches.

- **核心要点**：
  - 五阳干：甲丙戊庚壬
  - 六阳支：子寅辰午申戌
  - 五阴干：乙丁己辛癸
  - 六阴支：丑卯巳未酉亥
  - 配合原则：阳干配阳支，阴干配阴支
  - 比喻：犹如树木干枝

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_162]` `[trigger: 干支阴阳配合原则]` `[factor_trigger: yang_stems AND yin_stems AND yang_branches AND yin_branches]` `[role: 主干]` 甲丙戊庚壬，阳干也；子寅辰午申戌，阳枝也。法以阳干配阳枝，阴干配阴枝，犹木之有干而有枝。 → 《三命通会》卷一#干支阴阳配合原则

- **详细解说**：
  此条明确干支配合的基本原则。天干五阳五阴，地支六阳六阴，配合时遵循"同性相配"原则：阳干只配阳支，阴干只配阴支。这样五阳干与六阳支配合形成30个组合（甲子、甲寅、甲辰、甲午、甲申、甲戌，丙子...），五阴干与六阴支配合形成30个组合（乙丑、乙卯、乙巳、乙未、乙酉、乙亥，丁丑...），共60个甲子组合。"犹木之有干而有枝"是形象比喻，天干如树干，地支如树枝，干枝配合形成完整的树木，体现天地阴阳的和谐统一。

- **校勘与字词辨析（双语）**：
  - **中文**："犹"指如同、好像。干支配合遵循阴阳同类相配原则，不会出现阳干配阴支的情况。
  - **English**: "犹" means "like" or "as if"; Stem-Branch pairing follows the principle of matching same-type yin-yang, never yang Stem with yin Branch."""
    normalized_text_zh: str = """"""
    subject: str = "干支阴阳配合原则"
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
        l1_anchor="smth_v1.0.0_干支阴阳配合原则_001_L1",
    )
    version: str = "1.0.0"
