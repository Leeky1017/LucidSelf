"""
Auto-generated semantic module for zhouyi
Generated at: 2025-12-05T13:30:19.899924
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
    semantic_id="zy_v1.0.0_无妄卦_001",
    book_id="zhouyi",
    engine_id="yijing"
)
class 无妄卦(SemanticEntry):
    """
    - **原文（source_text）**：

  【卦辞】
  无妄：元亨，利贞。其匪正，有眚。不利有攸往。

  【彖传】
  《彖》曰：“无妄，刚自外来而为主于内，动而健，刚中而应；大亨以正，天...
    """
    
    original_text: str = """- **原文（source_text）**：

  【卦辞】
  无妄：元亨，利贞。其匪正，有眚。不利有攸往。

  【彖传】
  《彖》曰：“无妄，刚自外来而为主于内，动而健，刚中而应；大亨以正，天之命也。其匪正，有眚，不利有攸往；无妄之往，何之矣？天命不祐，行矣哉！”

  【象传】
  《象》曰：天下雷行，无妄；先王以茂对，时育万物。

  【爻辞】
  初九，无妄，往，吉。
  六二，不耕获，不菑畬，则利有攸往。
  六三，无妄之灾；或系之牛，行人之得，邑人之灾。
  九四，可贞，无咎。
  九五，无妄之疾，勿药，有喜。
  上九，无妄，行，有眚，无攸利。

- 分字分词释义：

  - **无妄**：无虚妄、无妄为之意；既指不凭空妄作，也指不执著于不合天道之念。
  - **元亨，利贞**：大通大顺而利于守正，前提是“不妄”；一旦偏离正道，则转为“有眚”。
  - **其匪正，有眚**：若所行之事不合正道，就会有灾祸（眚，多指过失所招之祸）。
  - **天之命也 / 天命不祐**：无妄之亨通源自天命；若执意妄行，则失去天命的庇护。
  - **天下雷行，无妄**：雷在天下震行，万物各安其位而不敢妄为，比喻秩序井然。
  - **不耕获，不菑畬**：不求即刻收获，不急于扩张开垦，强调不以急功近利之心行事。
  - **无妄之灾**：自身并无妄行，却遭遇外来的灾祸，提示“系统之错”与“牵连之祸”。
  - **或系之牛，行人之得，邑人之灾**：牛系在此处，被路人牵走，村人蒙受灾祸；象征责任落在无妄之人身上。
  - **无妄之疾，勿药有喜**：本无妄为而得病，不必乱用药，顺势调养自可得喜。
  - **无妄之行，有眚，无攸利**：在已非其位之时仍自信为“无妄之行”，终致灾祸且无所利。

- **规范化释义（primary_lang_explained）**：

  无妄卦讨论的是“顺天命而行”与“戒妄动”的结构。卦辞言：“无妄：元亨，利贞。其匪正，有眚。不利有攸往。”——只要行事合乎正道，不凭空妄作，则可以大亨而利于守正；一旦所行不正，即便自以为无妄，也必有过失与灾祸，不宜再贸然前往。

  彖传以卦象说明：初九阳刚自外而来为主于内，下卦震动，上承干之健，刚中而应，构成“动而健、刚中而应”的格局；在此条件下，以正道行事便是“天之命”，自然大亨。若偏离此一结构，以“自我之欲”替代“天命之正”，则虽号称无妄，其实“匪正”，于是“有眚，不利有攸往”。末句“天命不祐，行矣哉！”指出：当不再受天命庇护时，还要勉强前行，是对“妄动”的警告。

  象传“天下雷行，无妄；先王以茂对，时育万物”进一步把无妄放在“时育万物”的大结构中：雷行天下而各得其所，正是自然界“各随其分而不妄为”的状态；先王体此之道，以丰盛的德行回应天时，按时养育万物，而非出于私欲的妄行。

- **完整对等诠释（secondary_lang_full）**：

  The Hexagram Wu Wang, "Innocence" or "The Unexpected", describes a state of natural sincerity and spontaneity, free from artifice or ulterior motives. The Judgment, "Wu Wang: great success through correctness; if one is not correct, there will be error; it is not favorable to have anywhere to go", emphasizes that true innocence brings fortune, but any deviation from authenticity invites disaster.

- 核心要点：

  - 无妄卦强调：**不是“什么都不做”，而是在天命与正道之内做事**，避免出于私欲和执念的妄动。
  - “其匪正，有眚”提醒：只要不合正道，即便当事人主观觉得“无妄”，客观上仍会招致过失与灾祸。
  - 六三“无妄之灾”与九五“无妄之疾，勿药有喜”展示：无妄者也可能受灾，但若不以妄动应对，仍有转机。

- 详细解说：

  无妄卦核心在于"顺天命而不妄为"。卦象天下雷行，雷动于天下而万物各安其位，象征动而不妄。刚自外来而为主于内，动而健，刚中而应，构成以正道行事的理想格局。"""
    normalized_text_zh: str = """"""
    subject: str = "无妄卦（䷘）"
    factor_refs: list = ['zhouyi_gua_wuwang']
    
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
        book_id="zhouyi",
        chapter="",
        l1_anchor="zy_v1.0.0_无妄卦_001_L1",
    )
    version: str = "1.0.0"
