"""
Auto-generated semantic module for zhouyi
Generated at: 2025-12-05T13:30:19.919461
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
    semantic_id="zy_v1.0.0_震卦_001",
    book_id="zhouyi",
    engine_id="yijing"
)
class 震卦(SemanticEntry):
    """
    - **原文（source_text）**：

  【卦辞】
  震，亨。震来虩虩，笑言哑哑。震惊百里，不丧匕鬯。

  【彖传】
  《彖》曰：“震，亨。震来虩虩，恐致福也。笑言哑哑，后有则也。震惊...
    """
    
    original_text: str = """- **原文（source_text）**：

  【卦辞】
  震，亨。震来虩虩，笑言哑哑。震惊百里，不丧匕鬯。

  【彖传】
  《彖》曰：“震，亨。震来虩虩，恐致福也。笑言哑哑，后有则也。震惊百里，惊远而惧迩也。出可以守宗庙社稷，以为祭主也。”

  【象传】
  《象》曰：洊雷，震；君子以恐惧修身。

  【爻辞】
  初九，震来虩虩，后笑言哑哑，吉。
  六二，震来厉，亿丧贝，跻于九陵，勿逐，七日得。
  六三，震苏苏，震行无眚。
  九四，震遂泥。
  六五，震往来厉，亿无丧，有事。
  上六，震索索，视矍矍，征凶；震不于其躬，于其邻，无咎；婚媾有言。

- 分字分词释义：

  - **震**：本义为雷动、震动，引申为惊惧、变动、警策。
  - **虩虩**：读作“戏（xì）”，形容惊惧战栗之状。
  - **笑言哑哑**：惊惧过后，人们笑语连连、声音和悦，表示从恐惧转入安定。
  - **震惊百里，不丧匕鬯**：雷声可以震动百里之远，却不至于让手持祭器的人失手掉落，象征大震之中尚能持守本分。
  - **洊雷**：“洊”有重叠、连绵之意，“洊雷”即雷声一阵接一阵，比喻连续的震动与警示。
  - **亿丧贝 / 亿无丧**：“亿”作“揣度、估量”解，卦中多解为“多”“众”，整体指财物有失、无失之度量与估计。
  - **跻于九陵**：跻，升；九陵，重丘高陵。指仓皇中登高避险，不必强行追回丧失财物。
  - **苏苏 / 索索**：皆为形声叠字，“苏苏”偏于动而未定，“索索”偏于战栗不安。
  - **无眚**：“眚”为小灾小过，“无眚”即无灾无过。
  - **矍矍**：目光急速转动、四顾不安之状。
  - **震不于其躬，于其邻**：震灾不在自己身上，而发于邻里，比喻外在事件带来间接警示。

- **规范化释义（primary_lang_explained）**：

  震卦讲的是“在骤然震动与恐惧中，如何守住分寸而转危为安”。卦辞说：“震，亨。震来虩虩，笑言哑哑。震惊百里，不丧匕鬯。”——雷声骤至，最初人人惊惧战栗；但当人们明白其中规律、懂得雷雨将带来雨泽时，又能谈笑如常，震动虽广及百里，却仍不至于打翻手中的祭器，这正是“在惊惧中仍能守持礼度”的图景。

  彖传强调：震可以“恐致福”——适当的恐惧有助于防患未然；“笑言哑哑，后有则也”则说明：一旦在震动中建立起法则与节奏，惊惧就会化为安心。君王在“震惊百里”的威势中出行，由长子守宗庙社稷，以为祭主，象征在外在变动中，内在秩序必须有人镇守。

- **完整对等诠释（secondary_lang_full）**：

  The Hexagram Zhen (Thunder) addresses 震动惊惧. This hexagram emphasizes the importance of understanding natural patterns and human responses in specific life situations.

- 核心要点：

  - 震卦的核心是**“以敬畏之心应对突然变动，在震动中保持礼与度”**。
  - 恐惧本身并非坏事，关键在于是否借此修身、整肃，而不是被恐惧牵着走。
  - 卦辞“震惊百里，不丧匕鬯”提示：即便声势浩大，只要内在手中之器不落，根本秩序仍可维持。

- 详细解说：

  卦象为震上震下：两震相重，雷声连绵不绝，是典型的“洊雷”之象。与前卦鼎的“内煮而化”不同，震重在外在事件的突发与心理上的波动。君子“以恐惧修身”，并非时时自惊，而是在大震之时，反求诸己。

  初九“震来虩虩，后笑言哑哑，吉。”描述的是第一次遭遇大震的历程：先惊惧后释然，只要最后能恢复日常言笑，即为“吉”。六二“震来厉，亿丧贝，跻于九陵，勿逐，七日得。”则提出在震动中对于损失的态度：雷来为厉，财物似乎丧失，但若能先登高避险，不急于追逐，时间一过，自有可回收之机。

  六三“震苏苏，震行无眚。”强调处于中层者在长时间震荡中的行事之道：虽心神未定（苏苏），但行事若能谨慎守度，终可“无眚”。九四“震遂泥。”是一幅“雷电激荡终归泥淖”的图景：外在行动若陷于泥中，说明震动虽大，却未必带来实质跃迁，需要警觉“雷声大、步子小”的局面。

  六五“震往来厉，亿无丧，有事。”描绘的是居中之人在震动中承担事务的状态：往来奔走虽有危险，但只要估算得当，终不至失去根本，反而应有事可办。上六“震索索，视矍矍，征凶；震不于其躬，于其邻，无咎；婚媾有言。”则收束全卦：若一味索索矍矍，在震中仓皇出征，必有凶险；然而若能明白“震不在己而在邻”，将之视作提醒而非仅是灾难，对自身尚可“无咎”。“婚媾有言”则暗示：即便是喜事，也应在震动之时多留一分谨慎之言。


#### L2 语义提取

- **主题**：震动惊惧，如何在此情境中顺应天道、把握时机、实现人生目标。

- **校勘与字词辨析（双语）**：
- **叙事素材（narrative_snippets）**：
  - `[ns_zhouyi_461]` `[trigger: 卦=震 AND 卦辞=亨震来虩虩]` `[factor_trigger: zhouyi_gua_zhen AND zhouyi_guaci]` `[role: 主干]` 震，亨；震来虩虩，笑言哑哑：雷震之后，惊惧转为安乐。 → 《周易·震卦·卦辞》
  - `[ns_zhouyi_462]` `[trigger: 卦=震 AND 彖传]` `[factor_trigger: zhouyi_gua_zhen AND zhouyi_tuan AND zhouyi_zhendong_chengdu]` `[role: 主干依赖]` 亨。震来虩虩，恐致福也。 → 《周易·震卦·彖传》
  - `[ns_zhouyi_463]` `[trigger: 卦=震 AND 象传=洊雷震]` `[factor_trigger: zhouyi_gua_zhen AND zhouyi_xiang]` `[role: 主干依赖]` 洊雷，震；君子以恐惧修省：重雷震动，君子因惧而自省。 → 《周易·震卦·象传》
  - `[ns_zhouyi_464]` `[trigger: 卦=震 AND 初九=震来虩虩]` `[factor_trigger: zhouyi_gua_zhen]` `[role: 条件分支]` 震来虩虩，后笑言哑哑：初惧后安。 → 《周易·震卦·爻辞》
  - `[ns_zhouyi_465]` `[trigger: 卦=震 AND 六二=震来厉]` `[factor_trigger: zhouyi_gua_zhen]` `[role: 条件分支]` 震来厉，亿丧贝：雷震将至，或有财损。 → 《周易·震卦·爻辞》
  - `[ns_zhouyi_466]` `[trigger: 卦=震 AND 六三=震苏苏]` `[factor_trigger: zhouyi_gua_zhen]` `[role: 条件分支]` 震苏苏，震行无眚：惊惧而醒，无灾眚。 → 《周易·震卦·爻辞》
  - `[ns_zhouyi_467]` `[trigger: 卦=震 AND 九四=震遂泥]` `[factor_trigger: zhouyi_gua_zhen]` `[role: 例外处理]` 震遂泥：震惧而陷于泥中。 → 《周易·震卦·爻辞》
  - `[ns_zhouyi_468]` `[trigger: 卦=震 AND 六五=震往来厉]` `[factor_trigger: zhouyi_gua_zhen]` `[role: 主干依赖]` 震往来厉，亿无丧：往来皆厉，但无大损。 → 《周易·震卦·爻辞》
  - `[ns_zhouyi_469]` `[trigger: 卦=震 AND 上六=震索索]` `[factor_trigger: zhouyi_gua_zhen]` `[role: 总结]` 震索索，视矍矍：惧而索缩，目光惊惧。 → 《周易·震卦·爻辞》
  - **中文**：
  - 卦辞"震：亨。震来虩虩，笑言哑哑。震惊百里，不丧匕鬯"依通行王弼本；"虩虩"释为恐惧战栗貌，"哑哑"为笑声。
  - "匕鬯"为祭祀用具，匕为勺，鬯为香酒；"不丧匕鬯"谓虽惊百里而主祭者不失其器，比喻临危不乱。
  - "洊雷"之"洊"释为重复、再三，上下皆震，故曰"洊雷"。
  - "震苏苏"之"苏苏"释为惊醒貌，非"苏醒"之现代义；"震遂泥"谓震惧而陷于泥中，失去行动力。
  - "震索索，视矍矍"中"索索"为瑟缩貌，"矍矍"为惊视貌，形容极度惊恐之态。
  - **English**: Based on Wang Bi commentary edition. "虩虩/哑哑" describe fear then laughter. "匕鬯" are ritual implements—not losing them shows composure. "洊雷" means repeated thunder. "苏苏/索索/矍矍" are onomatopoeia for states of fear and alertness."""
    normalized_text_zh: str = """"""
    subject: str = "震卦（䷲）"
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
        book_id="zhouyi",
        chapter="",
        l1_anchor="zy_v1.0.0_震卦_001_L1",
    )
    version: str = "1.0.0"
