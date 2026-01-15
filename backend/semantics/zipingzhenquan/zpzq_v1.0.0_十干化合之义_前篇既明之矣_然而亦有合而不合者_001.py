"""
Auto-generated semantic module for zipingzhenquan
Generated at: 2025-12-05T13:30:19.523757
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
    semantic_id="zpzq_v1.0.0_十干化合之义_前篇既明之矣_然而亦有合而不合者_001",
    book_id="zipingzhenquan",
    engine_id="bazi"
)
class 十干化合之义前篇既明之矣然而亦有合而不合者(SemanticEntry):
    """
    - **原文（source_text）**：
  十干化合之义，前篇既明之矣，然而亦有合而不合者，何也？盖隔于有所间也。譬如人彼此相好，而有人从中间之，则交必不能成。譬如甲与己合，而甲己中间，以庚间隔...
    """
    
    original_text: str = """- **原文（source_text）**：
  十干化合之义，前篇既明之矣，然而亦有合而不合者，何也？盖隔于有所间也。譬如人彼此相好，而有人从中间之，则交必不能成。譬如甲与己合，而甲己中间，以庚间隔之，则甲岂能越克我之庚而合己？此制于势然也，合而不敢合也，有若无也。又有隔位太远，如甲在年干，己在时上，心虽相契，地则相远，如人天南地北，不能相合一般。然于有所制而不敢合者，亦稍有差，合而不能合也，半合也，其为祸福得十之二三而已。

- 原注（原文注解）：
  　　本段指出：
  - 十干虽有合化之理，但并非凡见两干即可论合；
  - 中间有他干隔制，或位置太远，皆可使“合而不合”；
  - 有的情况只是“半合”，作用程度有限。

- 分字分词释义：
  - 合而不合：形式上有合的条件，但实质上不能发挥合化或合去之力。
  - 隔于有所间：中间有他干插入、阻隔，造成“有若无”的状态。
  - 交必不能成：比喻两人本欲交好，却被第三者从中阻隔，关系难成。
  - 制于势然：受形势所制，自然如此，并非主观所能强为。
  - 隔位太远：甲在年干、己在时干，位置极远，如天南地北。
  - 半合：合力不全，只发挥一部分作用，对祸福影响有限（十分之二三）。

- **规范化释义（primary_lang_explained）**：
  十干有合化之理，但并不是只要看到两干同现，就可以简单说“必合”。如果两干之间夹着一个强有力的他干（比如甲、庚、己三干并列，其中庚居中），甲本来要去合己，却必须先面对中间这颗能克自己的庚金——甲不可能无视庚而越过去合己，因此这种状况虽然有“甲己同现”的形式，却是“合而不敢合，有若无也”。再比如甲在年干、己在时干，中间隔着月干与日干，位置相去太远，如同两人在天南地北，虽有契意，却难以真正会合，这就是“隔位太远”。与中间有强制之干不同，这类“隔位”仍有一点点合的意味，所以作者称其为“半合”，在祸福上的实际影响只有大势的两三成。

- **完整对等诠释（secondary_lang_full）**：  
  Even when a pair of stems that could combine are present together, circumstances may prevent the combination from really taking effect. One common situation is when a strong intervening stem stands between them. The text likens this to two people who wish to become friends but are constantly blocked by a third person standing in the way. In stem terms, if Jia and Ji both appear but Geng sits between them, Jia cannot simply ignore the Metal that restrains it and reach across to embrace Ji; the controlling relationship with Geng dominates, so the apparent Jia–Ji pair is a combination in name only. Another situation arises when the potential partners are placed so far apart in the four pillars that they are like people living at opposite ends of the earth: Jia in the Year stem and Ji in the Hour stem may share an affinity, but the distance and intervening stems prevent them from forming a true centre together.

  The author calls this latter case a "half‑combination": there is a slight tendency to combine, but its ability to change fortune, for good or ill, is only a small fraction of what a close, unimpeded conjunction would achieve. In both types of pattern, the form of combination seems to be present, yet the real combining power is weak or absent.

- 详细解说：
  - 合化之判断，要同时看位置与中间是否有“制隔之神”。
  - 形式上的“二干同现”并不足以判断“格局已经改变”；要看合力能否真正连通。
  - “半合”这一概念提醒我们，许多格局变化并非“有/无”的二元，而有程度差异。

- 核心要点：
  - 判断合化，必须考虑：
    - 中间有无克制之干；
    - 位置是否相距过远；
    - 合力是否足以左右大局。
  - 合而不合、半合之说，是防止我们在实际占断中过度夸大“合格、化格”的作用。

- 应用推演：
  1) 看到两干成对（如甲己、乙庚等）时，先画出它们在四柱中的位置。
  2) 检查中间是否夹有能克一方的干，若有，则多为“合而不敢合”。
  3) 若在年与时两端相对，中间隔两干且无特别牵联，多视作“半合”，不宜夸大影响。

- 反例与边界：
  - 只要看见“甲与己共现”就直接论合土，忽视中间庚的强力阻隔，是对本段精神的违背。
  - 把一切略有合意的组合都当作“全合”，导致格局与用神被频繁“强行改写”。

- 小例（示意）：
  - 甲日年干、己日时干，中间月日多有比劫与官杀，且庚在月干，甲先要应对庚之克，甲己合化的力量很有限，只能作为辅助参考，而不能据此重构全局格局。

- 校勘与字词辨析：
  - 原文“则郊必不能成”，据义当作“交必不能成”，今在精校中以“交”解读，并在此记明。

---
- **叙事素材（narrative_snippets）**：
  - `[ns_zpzy_217]` `[trigger: 相神紧要]` `[factor_trigger: xiangshen_fu_yongshen AND jinyao_zhi_dier]` `[role: 主干]` 相神辅用神，紧要之第二。 → 《子平真诠·论相神紧要》#紧要定义
  - `[ns_zpzy_218]` `[trigger: 相辅用神]` `[factor_trigger: xiangshen_fuyong AND geju_yuqing]` `[role: 主干]` 相神辅用，格局愈清。 → 《子平真诠·论相神紧要》#辅用
  - `[ns_zpzy_219]` `[trigger: 相神作用]` `[factor_trigger: (yongshen_you_xiang AND result=yuqing) OR (yongshen_wu_xiang AND result=shigu)]` `[role: 主干]` 用神有相则愈清，无相则势孤。 → 《子平真诠·论相神紧要》#作用
  - `[ns_zpzy_220]` `[trigger: 相神选取]` `[factor_trigger: xiangshen_xu_yu_yongshen_youqing AND fang_neng_ji_qi_buzu]` `[role: 主干]` 相神须与用神有情，方能济其不足。 → 《子平真诠·论相神紧要》#选取
  - `[ns_zpzy_221]` `[trigger: 刑害之论]` `[factor_trigger: xinghai_sui_xiong AND xu_kan_peihe]` `[role: 主干]` 刑害虽凶，须看配合。 → 《子平真诠》#上卷
  - `[ns_zpzy_222]` `[trigger: 相神得力]` `[factor_trigger: xiangshen_deli=true AND result=fugui_keqi]` `[role: 主干]` 相神得力，富贵可期。 → 《子平真诠》#论相神紧要
  - `[ns_zpzy_223]` `[trigger: 杂气概念]` `[factor_trigger: zaqi_yu_zhongqi AND zaqi_yu_yongshen]` `[role: 主干]` 辰戌丑未为杂气，内藏多神须择用。 → 《子平真诠·论杂气如何取用》#概念
  - `[ns_zpzy_224]` `[trigger: 库中取用]` `[factor_trigger: zaqi_ku_zhong AND zaqi_qu_yong]` `[role: 主干]` 杂气透干，库中取用。 → 《子平真诠·论杂气如何取用》#取用
  - `[ns_zpzy_225]` `[trigger: 透干为用]` `[factor_trigger: zaqi_tou_gan AND zaqi_wei_yong]` `[role: 主干]` 杂气透干者先用，不透则看会合。 → 《子平真诠·论杂气如何取用》#透干
  - `[ns_zpzy_226]` `[trigger: 冲开库门]` `[factor_trigger: zaqi_chong_kai AND zaqi_ku_men]` `[role: 主干]` 杂气逢冲则库开，财官印食各有用。 → 《子平真诠·论杂气如何取用》#冲开
  - `[ns_zpzy_227]` `[trigger: 空亡之说]` `[factor_trigger: kongwang_yu_zhongqi AND kongwang_yu_yongshen]` `[role: 主干]` 空亡不必尽信。 → 《子平真诠》#上卷
  - `[ns_zpzy_228]` `[trigger: 杂气月令]` `[factor_trigger: zaqi_yue_ling AND zaqi_yu_zhongqi]` `[role: 主干]` 杂气月令，透干会支。 → 《子平真诠》#论杂气如何取用
  - `[ns_zpzy_229]` `[trigger: 病重药重]` `[factor_trigger: bingzhong_yaoyong AND bingqing_yaoliang]` `[role: 主干]` 病重药重，病轻药轻。 → 《子平真诠》#上卷
  - `[ns_zpzy_230]` `[trigger: 忌神来犯]` `[factor_trigger: jishen_laifan=true AND result=zaihuo_nanmian]` `[role: 主干]` 忌神来犯，灾祸难免。 → 《子平真诠》#上卷"""
    normalized_text_zh: str = """"""
    subject: str = "十干化合之义，前篇既明之矣，然而亦有合而不合者"
    factor_refs: list = ['he_er_buhe', 'banhe', 'ge_yu_suojian', 'gewei_taiyuan', 'engine_id', 'ganzhi_distance', 'bazi_rule_engine', 'kezhi_jiegan', 'bazi_rule_engine', 'hehua_lidu', 'bazi_rule_engine', 'hehua_impact', 'bazi_rule_engine', 'source_ref', 'rel_zpzq_054', 'ganzhi_distance', 'rel_zpzq_055', 'kezhi_jiegan', 'evi_zpzq_054', 'kezhi_jiegan', 'rule_jiegan_blocking', 'evi_zpzq_055', 'ganzhi_distance', 'rule_distance_banhe', 'concept_blocked_union', 'concept_partial_effect']
    
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
        book_id="zipingzhenquan",
        chapter="",
        l1_anchor="zpzq_v1.0.0_十干化合之义_前篇既明之矣_然而亦有合而不合者_001_L1",
    )
    version: str = "1.0.0"
