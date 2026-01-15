"""
Auto-generated semantic module for zhouyi
Generated at: 2025-12-05T13:30:19.919242
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
    semantic_id="zy_v1.0.0_大壮卦_001",
    book_id="zhouyi",
    engine_id="yijing"
)
class 大壮卦(SemanticEntry):
    """
    - **原文（source_text）**：

  【卦辞】
  大壮：利贞。

  【彖传】
  《彖》曰：大壮，大者壮也。刚以动，故壮。“大壮，利贞”，大者正也。正大而天地之情可见矣。

  【象...
    """
    
    original_text: str = """- **原文（source_text）**：

  【卦辞】
  大壮：利贞。

  【彖传】
  《彖》曰：大壮，大者壮也。刚以动，故壮。“大壮，利贞”，大者正也。正大而天地之情可见矣。

  【象传】
  《象》曰：雷在天上，大壮；君子以非礼弗履。

  【爻辞】
  初九，壮于趾，征凶，有孚。
  九二，贞吉。
  九三，小人用壮，君子用罔，贞厉，羝羊触藩，羸其角。
  九四，贞吉，悔亡，藩决不羸，壮于大舆之輹。
  六五，丧羊于易，无悔。
  上六，羝羊触藩，不能退，不能遂，无攸利；艰则吉。

- 分字分词释义：

  - **大壮**：大而壮盛，指阳刚之气极盛之时。
  - **利贞**：利于守正，不利于恣意扩张或任意妄为。
  - **刚以动，故壮**：以刚健之德而行动，故显出强壮之象。
  - **大者正也**：真正的大，不在于力之大，而在于能守正。
  - **雷在天上**：震为雷在上卦乾天之上，声威远布，象征力量外显而影响广泛。
  - **非礼弗履**：不合礼的事，一步也不踏入，比喻以礼节制强壮。
  - **壮于趾**：仅在脚趾之力强而先动，象征下端躁进、急于出征。
  - **小人用壮，君子用罔**：小人恃强而妄用其力；君子则用“罔”——约束、网住自己的力量。
  - **羝羊触藩，羸其角**：公羊用角撞篱笆，角被缠住，比喻盲目用力反受其累。
  - **藩决不羸**：篱笆冲决而不再缠住，象征突破阻碍后力量得其正用。
  - **丧羊于易**：在边界地带失去羊，暗示因失位而有损失，但可无悔。

- **规范化释义（primary_lang_explained）**：

  大壮卦关注的是“力量极盛时如何自持”。卦辞“ 大壮：利贞。”一句，既肯定了壮盛之时的可贵，也提醒：只有守正，这股力量才真正有利；若恣意妄为，则壮反成灾。

  彖传指出：大壮就是“大者壮也”，阳刚之气以行动表现出来，故显得强壮。但“壮”的价值在于“利贞”——力量必须服务于正大之道，才能看见天地之情，即洞悉事物的真实结构与规律。否则，强壮只是盲力。

- **完整对等诠释（secondary_lang_full）**：

  The Hexagram Da Zhuang (Great Power) portrays a time of overflowing strength and momentum. Thunder above Heaven symbolizes fully manifest yang power spreading its influence far and wide, yet the Judgment "Great Power: favorable to persist in what is right" stresses that only power constrained by correctness is truly auspicious. The hexagram teaches that when resources, status, or influence peak, the key question is not how strong one is, but whether one's actions remain aligned with the Way and do not cross the boundaries of propriety.

- 核心要点：

  - 大壮卦核心是**“强而能制、盛而守正”**。
  - 阳刚盛时，最危险的不是力量不足，而是"用力之处是否合礼"。
  - 爻辞通过"羝羊触藩"的意象，展示盲力与正力的分界。

- 详细解说：

  卦象上乾下震，雷动于天上。初九"壮于趾"提示急于行动有凶象；九二"贞吉"示范守正而行。九三"羝羊触藩"是警钟；九四"藩决不羸"展示力量正用。六五"丧羊于易，无悔"说明反躬自省便可无悔；上六提醒以"艰"自持。

- **校勘与字词辨析（双语）**：
- **叙事素材（narrative_snippets）**：
  - `[ns_zhouyi_308]` `[trigger: 卦=大壮 AND 卦辞=利贞]` `[factor_trigger: zhouyi_gua_dazhuang AND zhouyi_guaci]` `[role: 主干]` 大壮，利贞：阳气壮盛，仍须守正。 → 《周易·大壮卦·卦辞》
  - `[ns_zhouyi_309]` `[trigger: 卦=大壮 AND 彖传]` `[factor_trigger: zhouyi_gua_dazhuang AND zhouyi_tuan AND zhouyi_zhuangda_chengdu]` `[role: 主干依赖]` 大者壮也。刚以动，故壮。 → 《周易·大壮卦·彖传》
  - `[ns_zhouyi_310]` `[trigger: 卦=大壮 AND 象传=雷在天上]` `[factor_trigger: zhouyi_gua_dazhuang AND zhouyi_xiang]` `[role: 主干依赖]` 雷在天上，大壮；君子以非礼弗履：阳壮之时，仍守礼节。 → 《周易·大壮卦·象传》
  - `[ns_zhouyi_311]` `[trigger: 卦=大壮 AND 初九=壮于趾]` `[factor_trigger: zhouyi_gua_dazhuang]` `[role: 例外处理]` 壮于趾，征凶：壮在脚趾，轻举妄动则凶。 → 《周易·大壮卦·爻辞》
  - `[ns_zhouyi_312]` `[trigger: 卦=大壮 AND 九二=贞吉]` `[factor_trigger: zhouyi_gua_dazhuang]` `[role: 条件分支]` 贞吉：居中守正，自然吉祥。 → 《周易·大壮卦·爻辞》
  - `[ns_zhouyi_313]` `[trigger: 卦=大壮 AND 九三=小人用壮]` `[factor_trigger: zhouyi_gua_dazhuang]` `[role: 例外处理]` 小人用壮，君子用罔：小人恃强，君子以智。 → 《周易·大壮卦·爻辞》
  - `[ns_zhouyi_314]` `[trigger: 卦=大壮 AND 九四=贞吉悔亡]` `[factor_trigger: zhouyi_gua_dazhuang]` `[role: 条件分支]` 贞吉悔亡，藩决不缸：守正则吉，障碍可除。 → 《周易·大壮卦·爻辞》
  - `[ns_zhouyi_315]` `[trigger: 卦=大壮 AND 六五=丧羊于易]` `[factor_trigger: zhouyi_gua_dazhuang]` `[role: 条件分支]` 丧羊于易，无悔：失羊于平地，未必可悔。 → 《周易·大壮卦·爻辞》
  - `[ns_zhouyi_316]` `[trigger: 卦=大壮 AND 上六=羝羊触藩]` `[factor_trigger: zhouyi_gua_dazhuang]` `[role: 总结]` 羝羊触藩，不能退，不能遂，无攸利；艰则吉。 → 《周易·大壮卦·爻辞》
  - **中文**：
  - 卦辞"大壮：利贞"依通行王弼本；"大壮"谓阳气壮盛至极，四阳在下而上进，故名大壮。
  - "雷在天上"谓震雷在乾天之上，声威远布，象征阳刚势力极盛之时。
  - "非礼弗履"谓虽当壮盛之时，君子仍须以礼自节，不可恃强妄行。
  - "羝羊触藩"之"羝羊"为公羊，"藩"为篱笆；"羸其角"谓角被困于藩中，进退两难。
  - "小人用壮，君子用罔"中"罔"释为网、约束，君子以智慧约束而非恃力蛮进。
  - "丧羊于易"之"易"释为平地或交易场所，丧羊于平坦之地，非己之过，故无悔。
  - **English**: Based on Wang Bi commentary edition. "大壮" means great strength—four yang lines rising. "羝羊" is a ram. "非礼弗履" advises propriety even in strength. "用罔" means using restraint/wisdom. "丧羊于易" shows loss in open field—not one's fault."""
    normalized_text_zh: str = """"""
    subject: str = "大壮卦（䷡）"
    factor_refs: list = ['zhouyi_gua_034', 'principle_not_step_without_ritual_proposal', 'symbol_ram_hits_fence_proposal', 'method_self_restraint_net_proposal', 'principle_greatness_in_correctness_proposal']
    
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
        l1_anchor="zy_v1.0.0_大壮卦_001_L1",
    )
    version: str = "1.0.0"
