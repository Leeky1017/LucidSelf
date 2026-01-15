"""
Auto-generated semantic module for zhougong
Generated at: 2025-12-05T13:30:19.885276
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
    semantic_id="zgjm_v1.0.0_被害斗伤打骂_001",
    book_id="zhougong",
    engine_id="dream"
)
class 被害斗伤打骂(SemanticEntry):
    """
    - **原文（source_text）**：

  被人杀害者大吉，杀死他人大富贵。持刀自杀者大吉。  
  杀人血污衣得财，被刀刺火出快利。持刀相杀见血吉。  
  刀伤出血主酒食，砍刺见血主大吉。...
    """
    
    original_text: str = """- **原文（source_text）**：

  被人杀害者大吉，杀死他人大富贵。持刀自杀者大吉。  
  杀人血污衣得财，被刀刺火出快利。持刀相杀见血吉。  
  刀伤出血主酒食，砍刺见血主大吉。炙身见血流大吉。  
  刀斧自伤主大吉，持刀斫人自失财。人砍头脑中二吉。  
  被人打者主得力，被人脚踢主求财。打妻妾者主失力。  
  家中人斗主分散，断头而行主大喜。女人相打主病至。  
  兄弟相打大吉利，被妻妾打主凶事。看见杀人主大吉。  
  被人签刺大吉昌，手措折者主子病。向人叩头百事吉。  
  与人相骂者主吉，被骂佯颠大贵至。被人凌辱主得财。  
  杀猪豖者大吉利，杀羊打羊主病凶。杀虎豹主得重印。  
  杀牛鹿者大富贵，杀牛食肉主生财。杀驴骡马有酒食.

- 分字分词释义：

  - **被人杀害、杀死他人**：在梦中被杀或杀人，往往不主真实死亡，而象征旧我消亡、新我重生或冲突解决.
  - **持刀自杀**：自己持刀自尽，象征自我革新或断绝旧缠.
  - **血污衣、见血**：血液沾染衣物或见到鲜血，在梦象中往往主得财或喜事，而非灾祸.
  - **被刀刺火出**：被刀刺中而有火光或快感，象征快速突破或利益到来.
  - **刀斧自伤**：自己用刀斧伤害自己，象征自我革新与断舍离.
  - **被人打、被脚踢**：被他人殴打或踢，往往主得力、得财，体现"以退为进"的逻辑.
  - **打妻妾**：殴打妻妾，则主失力，象征家庭关系失衡.
  - **家中人斗、兄弟相打**：家人或兄弟争斗，有吉有凶，需区分具体情境.
  - **断头而行**：头被砍断仍能行走，象征摆脱束缚或极大喜事.
  - **被骂、被凌辱**：被辱骂或凌辱，往往主得财或大贵，体现"忍辱负重"的反转.
  - **杀猪豖、杀牛鹿等**：杀各种动物，多主富贵、酒食或官印，但杀羊则主病凶.

- **规范化释义（primary_lang_explained）**：

  本类条目围绕"被害斗伤打骂"展开，揭示梦象学中对**暴力、冲突与伤害**的独特解读——大多数情境下，梦中的暴力与伤害并非凶兆，反而主吉利、得财或新生。被人杀害、杀死他人、持刀自杀皆主大吉；血污衣、见血多主得财；被打、被踢主得力、求财；被骂、被凌辱主得财或大贵。但也有例外：打妻妾主失力，家中人斗主分散，女人相打主病至，被妻妾打主凶事。杀动物方面，杀猪豖、牛鹿、虎豹多主吉利富贵，但杀羊打羊主病凶.

- 核心要点：

  - **暴力与伤害多主逆反吉利**：被杀、杀人、自杀、见血、被打、被骂等，往往不主灾祸，反主得财、新生或突破.
  - **血象征财富与喜事**：血污衣、见血、刀伤出血等，多主得财或酒食.
  - **被动受害主得力得财**：被人打、被脚踢、被骂、被凌辱等，体现"以退为进""忍辱负重"的智慧.
  - **主动施暴有吉有凶**：杀他人、杀动物多主吉，但打妻妾主失力，需区分对象.
  - **特殊例外需警惕**：打妻妾、家中人斗、女人相打、被妻妾打等，主凶或分散.

- 详细解说：

  **（一）被害与杀人：旧我消亡与新我重生**

  本类开篇即揭示"被人杀害者大吉，杀死他人大富贵，持刀自杀者大吉"三句，构成梦象学中最强烈的逆反规律：梦中的死亡与杀戮，并非真实的死亡威胁，而是象征"旧我消亡、新我重生"或"冲突解决、障碍清除"。被人杀害象征被外力推动而进入新阶段；杀死他人象征主动清除障碍或竞争对手；持刀自杀则象征自我革新与断绝旧缠.

  **（二）血象征财富：血污衣与见血的正向意义**

  "杀人血污衣得财，被刀刺火出快利，持刀相杀见血吉，刀伤出血主酒食，砍刺见血主大吉，炙身见血流大吉"六句构成"血象征财富"的完整链条：血液在梦象中不主灾祸，反而主财富、喜事或快速利益。血污衣象征财富沾身；见血象征收获显现；刀伤出血主酒食宴请；炙身见血流则主大吉大利.

  **（三）被动受害：得力得财的智慧**

  "被人打者主得力，被人脚踢主求财，被骂佯颠大贵至，被人凌辱主得财"四句揭示"被动受害主得力得财"的智慧：梦中被殴打、被踢、被辱骂、被凌辱，往往不主真实的伤害与屈辱，反而预示现实中将得他人相助、获得财富或通过"以退为进""忍辱负重"而换取更大利益.

  **（四）主动施暴：有吉有凶需区分**

  "刀斧自伤主大吉，持刀斫人自失财，打妻妾者主失力"三句区分不同施暴对象的吉凶：刀斧自伤（自我革新）主大吉；但持刀斫人（主动伤害他人）则主自失财；打妻妾更主失力，象征家庭关系失衡与能量流失.

  **（五）家庭冲突：分散与病凶的警示**

  "家中人斗主分散，女人相打主病至，被妻妾打主凶事"三句揭示家庭冲突的负面象征：家人争斗主分散离析；女人相打主疾病将至；被妻妾殴打则主凶事.But"兄弟相打大吉利"是例外，说明兄弟间的争执反而主吉利.

  **（六）杀动物：富贵与病凶的分野**

  杀猪豖、牛鹿、虎豹、驴骡马等动物多主吉利：杀猪主大吉，杀牛鹿主大富贵，杀虎豹主得官印，杀牛食肉主生财，杀驴骡马主酒食.But"杀羊打羊主病凶"是例外：羊性温顺，杀羊反主病凶.

- 校勘与字词辨析（本类）：

  - "被害斗伤打骂"六字标题按底本录入，涵盖被害、争斗、伤害、殴打、辱骂五大主题.
  - "杀人血污衣得财"一句，"血污衣"指血液沾染衣物，梦象中主得财而非灾祸.
  - "被刀刺火出快利"一句，"火出"指火光或快感，本稿释为"快速利益到来".

- **叙事素材（narrative_snippets）**：

  - `[ns_zgjm_1006]` `[trigger: 梦见被人打者]` `[factor_trigger: dream_beaten]` `[role: 主干]` 被人打者，主得力。 → 《周公解梦·被害斗伤打骂》
  - `[ns_zgjm_1007]` `[trigger: 梦见被人骂者]` `[factor_trigger: dream_scolded]` `[role: 主干]` 被人骂者，主得助。 → 《周公解梦·被害斗伤打骂》
  - `[ns_zgjm_1008]` `[trigger: 梦见被人欺侮]` `[factor_trigger: dream_bullied]` `[role: 主干]` 被人欺侮，主得贵。 → 《周公解梦·被害斗伤打骂》
  - `[ns_zgjm_1009]` `[trigger: 梦见与人相打]` `[factor_trigger: dream_fight_people]` `[role: 主干]` 与人相打，主有理。 → 《周公解梦·被害斗伤打骂》
  - `[ns_zgjm_1010]` `[trigger: 梦见与人相骂]` `[factor_trigger: dream_curse_people]` `[role: 主干]` 与人相骂，主有吉。 → 《周公解梦·被害斗伤打骂》
  - `[ns_zgjm_1011]` `[trigger: 梦见与人斗者]` `[factor_trigger: dream_quarrel]` `[role: 主干]` 与人斗者，主和合。 → 《周公解梦·被害斗伤打骂》
  - `[ns_zgjm_1012]` `[trigger: 梦见被刀刺]` `[factor_trigger: dream_stabbed]` `[role: 主干]` 被刀刺，火出快利。 → 《周公解梦·被害斗伤打骂》
  - `[ns_zgjm_1013]` `[trigger: 梦见杀人血污衣]` `[factor_trigger: dream_kill_blood]` `[role: 主干]` 杀人血污衣，得财。 → 《周公解梦·被害斗伤打骂》
  - `[ns_zgjm_1014]` `[trigger: 梦见被刀枪刺者]` `[factor_trigger: dream_weapon_stab]` `[role: 主干]` 被刀枪刺者，大吉。 → 《周公解梦·被害斗伤打骂》
  - `[ns_zgjm_1015]` `[trigger: 梦见持刀相杀]` `[factor_trigger: dream_knife_kill]` `[role: 主干]` 持刀相杀，主大吉。 → 《周公解梦·被害斗伤打骂》
  - `[ns_zgjm_1016]` `[trigger: 梦见刀落]` `[factor_trigger: dream_knife_fall]` `[role: 主干]` 刀落，主妻产凶。 → 《周公解梦·被害斗伤打骂》
  - `[ns_zgjm_1017]` `[trigger: 梦见身被刀斧伤]` `[factor_trigger: dream_axe_wound]` `[role: 主干]` 身被刀斧伤，大吉。 → 《周公解梦·被害斗伤打骂》
  - `[ns_zgjm_1018]` `[trigger: 梦见刀剑自落]` `[factor_trigger: dream_sword_fall]` `[role: 主干]` 刀剑自落，妻亡凶。 → 《周公解梦·被害斗伤打骂》
  - `[ns_zgjm_1019]` `[trigger: 梦见杀猪]` `[factor_trigger: dream_kill_pig_2]` `[role: 主干]` 杀猪，主大吉利。 → 《周公解梦·被害斗伤打骂》
  - `[ns_zgjm_1020]` `[trigger: 梦见杀牛鹿]` `[factor_trigger: dream_kill_deer]` `[role: 主干]` 杀牛鹿，主大富贵。 → 《周公解梦·被害斗伤打骂》
  - `[ns_zgjm_1021]` `[trigger: 梦见杀虎豹]` `[factor_trigger: dream_kill_tiger]` `[role: 主干]` 杀虎豹，主得官印。 → 《周公解梦·被害斗伤打骂》
  - `[ns_zgjm_1022]` `[trigger: 梦见杀牛食肉]` `[factor_trigger: dream_kill_ox_eat]` `[role: 主干]` 杀牛食肉，主生财。 → 《周公解梦·被害斗伤打骂》
  - `[ns_zgjm_1023]` `[trigger: 梦见杀驴骡马]` `[factor_trigger: dream_kill_donkey]` `[role: 主干]` 杀驴骡马，主酒食。 → 《周公解梦·被害斗伤打骂》
  - `[ns_zgjm_1024]` `[trigger: 梦见杀羊打羊]` `[factor_trigger: dream_kill_sheep]` `[role: 主干]` 杀羊打羊，主病凶。 → 《周公解梦·被害斗伤打骂》
  - `[ns_zgjm_1025]` `[trigger: 梦见杀犬]` `[factor_trigger: dream_kill_dog]` `[role: 主干]` 杀犬，主妻不贞。 → 《周公解梦·被害斗伤打骂》"""
    normalized_text_zh: str = """"""
    subject: str = "被害斗伤打骂"
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
        book_id="zhougong",
        chapter="",
        l1_anchor="zgjm_v1.0.0_被害斗伤打骂_001_L1",
    )
    version: str = "1.0.0"
