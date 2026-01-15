"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.725575
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
    semantic_id="zw_v1.0.0_8_太阴星_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 8太阴星(SemanticEntry):
    """
    - 原文（source_text）：

  问：太阴星所主若何？

  答曰：太阴乃水之精，为田宅主，化富与日为配，天之仪表，有上弦、下弦之用。黄道黑道，分势尚好亏。数定庙乐，其为人也聪明俊秀，其禀性...
    """
    
    original_text: str = """- 原文（source_text）：

  问：太阴星所主若何？

  答曰：太阴乃水之精，为田宅主，化富与日为配，天之仪表，有上弦、下弦之用。黄道黑道，分势尚好亏。数定庙乐，其为人也聪明俊秀，其禀性也端雅纯祥。上弦为要之机，下弦减威之论。男为妻宿，又作母星。

- 原注（原文注解，可无则省略小节）：

  希夷先生曰：太阴化禄，与日为配，以卯辰巳午未为陷地，以酉戌亥子丑为得垣，酉为西出之门，子为东潜之所，嫌巨曜以来缠，怕羊陀以同度。廉囚相犯，七杀相冲，恐非得意之垣，定作伤残之论。此星属水，为田宅宫，主有辉为福，失陷必凶。男女得之，皆为母星，又作妻宿。若在身命庙乐吉集，主富贵。

- 分字分词释义：

  - **田宅主**：在斗数中主管房产、不动产与居住环境的主星。
  - **得垣 / 失陷**：太阴在不同宫位的旺衰状态，“得垣”光辉充足，“失陷”则光弱受损。
  - **上下弦**：借月相比喻太阴力量的开启与衰减，上弦偏向机会与起势，下弦主收缩与减力。
  - **母星妻宿**：在六亲系统中，太阴既代表母亲，又代表伴侣（特别是妻子），体现稳定照拂与亲密关系。
  - **巨曜羊陀廉囚七杀**：一系列与太阴相冲相缠的凶星组合，多主眼目、身心或田宅方面的损伤与不安。

- 规范化释义（primary_lang_explained）：

  本条把太阴描写成“水之精”“田宅主”，是一颗与居所、安全感、照拂与内在情感关系最为密切的星曜。落在得垣之地时，太阴如同一轮光辉柔和的明月，可以为命盘提供稳定的物质基础与温润的情感氛围：田宅有根、住处安定，人与人之间的关照细腻周到。若又与太阳形成良好的日月配合，则一动一静、一明一柔，既有对外发展的能力，也有对内安顿的空间，常见“家业殷实、内外相济”之象。

  但太阴也极其在意“得垣失陷”与“上下弦”的细微差别：失陷或处于不利月相时，其柔和就可能转为敏感与脆弱。原文所提巨暗、羊陀、廉囚、七杀等凶星缠绕，多半反映在眼目、睡眠、情绪与田宅上的不安——如居住环境频繁变动、家宅维修不断、与母亲或伴侣关系反复波动等。男人命盘中，太阴偏向妻宿；女命中，则往往强化母性与照料角色，因此太阴失衡时，也常带来夫妻间的疏离、角色压力与“照顾他人却难以被照顾”的内在感受。整体来说，太阴提醒命师：判断财与宅，不只是看数量与面积，更要看这一轮“内在之月”是否真正照亮了心与家。

- 完整对等诠释（secondary_lang_full）：

  This section presents Taiyin, the Moon, as the refined essence of Water and the lord of property and dwelling. When strong and well placed, it describes not only real estate and material shelter, but also the atmosphere of a home: how safe, gentle and emotionally nourishing a space feels. In such charts, a bright Moon in its "strong walls" suggests stable housing, accumulated property and a capacity to create environments where people can rest, heal and reconnect. When harmoniously paired with the Sun, Taiyang, the combination of day and night, outer activity and inner repose, points to lives that can balance career or public demands with genuine refuge.

  The text, however, pays close attention to phases and positions—whether the Moon is in an advancing or waning phase, and whether it stands in signs where its light is supported or undermined. Entanglements with dark stars like Jumen, harsh companions such as Yang and Tuo, or killing forces like Qisha and Lian can manifest through eye strain, disturbed sleep, chronic worry, repeated moves or ongoing repairs to property. In family symbolism, Taiyin often represents the mother and, in many charts, the spouse, so afflictions here may show as complicated mother–child dynamics, emotional distance in partnership or the burden of caretaking without sufficient support. Overall, Taiyin does not merely quantify assets; it points to the quality of inner and outer dwelling—how well a person is housed in both body and psyche, and how vulnerable that shelter is to erosion or sudden disruption.

- 核心要点：

  1. **太阴化富**：水之精，田宅主，化富与日为配。
  2. **得垣失陷**：酉戌亥子丑为得垣，卯辰巳午未为陷地。
  3. **上下弦论**：上弦为要之机，下弦减威之论。
  4. **母星妻宿**：男女皆为母星，又作妻宿。
  5. **忌凶星**：嫌巨曜、怕羊陀、忌廉囚七杀。

- 叙事素材（narrative_snippets）：

  - **太阴化富**："太阴水之精，为田宅主，化富与日为配"，太阴主田宅财富。
  - **得垣失陷**："酉戌亥子丑为得垣，卯辰巳午未为陷地"，太阴的旺衰关键在宫位。
  - **上下弦**："上弦为要之机，下弦减威之论"，月相影响太阴力量的发挥。
  - **母妻双宿**："男女皆为母星，又作妻宿"，太阴兼具母亲与伴侣的象征。
  - **现代应用**：太阴可作为评估"田宅安全感"的核心指标——内在之月需照亮心与家。"""
    normalized_text_zh: str = """"""
    subject: str = "8 太阴星"
    factor_refs: list = ['star_taiyin', 'state_deyuan_shixian', 'state_shangxian_xiaxian', 'role_muxing_qisu', 'combo_riyue_peihe']
    
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
        book_id="ziwei",
        chapter="",
        l1_anchor="zw_v1.0.0_8_太阴星_001_L1",
    )
    version: str = "1.0.0"
