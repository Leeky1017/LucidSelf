"""
Auto-generated semantic module for yuanhaiziping
Generated at: 2025-12-05T13:30:19.559300
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
    semantic_id="yhzp_v1.0.0_喜忌篇_001",
    book_id="yuanhaiziping",
    engine_id="bazi"
)
class 喜忌篇(SemanticEntry):
    """
    - **原文（source_text）**：四柱排定，三才次分，专以日上天元，配合八字支干；有见不见之形，无时不有；神煞相绊，轻重较量。若乃，时逢七杀，见之未必为凶；月制干强，其杀反为权印。财官印绶全...
    """
    
    original_text: str = """- **原文（source_text）**：四柱排定，三才次分，专以日上天元，配合八字支干；有见不见之形，无时不有；神煞相绊，轻重较量。若乃，时逢七杀，见之未必为凶；月制干强，其杀反为权印。财官印绶全备，藏蓄于月季之中。

- **分字分词释义**：
  - **四柱排定，三才次分**：排定四柱后，依天地人三才分层分析。
  - **专以日上天元**：以日柱天干（日元）为论命核心。
  - **配合八字支干**：配合年月日时四柱的天干地支综合分析。
  - **有见不见之形**：既有明显显露的格局，也有隐藏不见的因素。
  - **神煞相绊**：神煞之间相互牵绊作用，需权衡轻重。
  - **时逢七杀**：时柱见七杀，不一定为凶。
  - **月制干强**：月令有制且日干强，七杀反化为权柄。
  - **其杀反为权印**：七杀被制化后，反而成为权力象征。
  - **财官印绶全备**：财星官星印绶三者齐备为佳配。
  - **藏蓄于月季之中**：财官印藏于月令之中，暗中蓄力。

- **规范化释义（primary_lang_explained）**：四柱论命以日干为主配合八字。七杀有制化为权，无制则凶。财官印绶藏于月令为佳。露官藏杀、露杀藏官各有宜忌。格局要纯粹，拱禄拱贵、时上偏财、六阴朝阳等特殊格局各有条件。

- **完整对等诠释（secondary_lang_full）**：Four Pillars analysis uses Day Stem as master coordinating with Eight Characters. Seven Killings with control transforms to authority, without control brings calamity. Wealth-Officer-Seal all hidden in Month Command ideal. Exposed Officer hidden Killing, exposed Killing hidden Officer each has proper applications. Patterns require purity—special patterns like Vaulting Salary, Hour Indirect Wealth, Six Yin Facing Yang each have specific conditions.

- **核心要点**：日干为主配八字；七杀有制化权无制凶；财官印藏月令佳；格局要纯粹；特殊格局各有条件

- **详细解说**：  《喜忌篇》阐述格局喜忌的判断原则与特殊格局的识别条件。开篇"四柱排定，三才次分"强调论命需分层次：先排四柱，再依天地人三才分析。"专以日上天元"重申日干为核心。在喜忌判断上，本篇提出两个重要原则：一是"有见不见之形"——既看显露的格局，也要察隐藏的因素；二是"神煞相绊，轻重较量"——神煞之间相互作用，需权衡轻重而非一概而论。在七杀的判断上，"时逢七杀，见之未必为凶"打破了七杀必凶的刻板印象；"月制干强，其杀反为权印"则说明七杀在有制化且日干强的条件下，反而成为权力象征。"财官印绶全备，藏蓄于月季之中"则指出财官印三者藏于月令为最佳配置。

- **叙事素材（narrative_snippets）**：
  - `[ns_yhzp_297]` `[trigger: 日元为主]` `[factor_trigger: rigan_weizhu AND sancai_cifen AND day_element]` `[role: 主干]` 四柱排定，三才次分，专以日上天元；日干为论命核心。 → 《渊海子平·喜忌篇》
  - `[ns_yhzp_298]` `[trigger: 有见不见]` `[factor_trigger: youjian_bujian AND xian_yin AND caiyin AND caiyin_qing_guansha_zu AND changyin]` `[role: 主干依赖]` 有见不见之形，无时不有；既看显露也察隐藏。 → 《渊海子平·喜忌篇》
  - `[ns_yhzp_299]` `[trigger: 神煞轻重]` `[factor_trigger: shensha_xiangban AND qingzhong AND jiaoliang]` `[role: 条件分支]` 神煞相绊，轻重较量；神煞需权衡轻重。 → 《渊海子平·喜忌篇》
  - `[ns_yhzp_597]` `[trigger: 七杀化权]` `[factor_trigger: qisha_huaquan AND ganqiang_youzhi]` `[role: 条件分支]` 时逢七杀，见之未必为凶；月制干强，其杀反为权印。 → 《渊海子平·喜忌篇》
  - `[ns_yhzp_598]` `[trigger: 财官印藏月]` `[factor_trigger: caiguanyin_quanbei AND cang_yueling AND caiyin AND caiyin_qing_guansha_zu AND changyin]` `[role: 条件分支]` 财官印绶全备，藏蓄于月季之中；三者藏月令为佳配。 → 《渊海子平·喜忌篇》
  - `[ns_yhzp_599]` `[trigger: 喜忌篇纲领]` `[factor_trigger: xiji_pian AND lunming_yuanze]` `[role: 总结]` 喜忌篇以日干为主、七杀化权、财官印藏月为喜忌判断核心原则。 → 《渊海子平·喜忌篇》

- **L2-术语对齐（Term Glossary）**：

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|----------|-----------|--------|
| 七杀有制化为权 | Seven Killings Controlled Transforms Authority | 七杀得制伏则化为权柄 | Seven Killings when controlled transforms to authority | killing_controlled_authority | existing |
| 拱禄拱贵 | Vaulting Salary Vaulting Noble | 两柱拱夹禄位或贵人 | Two pillars vaulting Salary or Noble position | salary | existing |"""
    normalized_text_zh: str = """"""
    subject: str = "喜忌篇"
    factor_refs: list = []
    
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
        book_id="yuanhaiziping",
        chapter="",
        l1_anchor="yhzp_v1.0.0_喜忌篇_001_L1",
    )
    version: str = "1.0.0"
