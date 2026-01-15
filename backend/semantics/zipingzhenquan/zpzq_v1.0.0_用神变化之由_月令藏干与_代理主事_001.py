"""
Auto-generated semantic module for zipingzhenquan
Generated at: 2025-12-05T13:30:19.523976
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
    semantic_id="zpzq_v1.0.0_用神变化之由_月令藏干与_代理主事_001",
    book_id="zipingzhenquan",
    engine_id="bazi"
)
class 用神变化之由月令藏干与代理主事(SemanticEntry):
    """
    - **原文（source_text）**：
  用神既主月令矣，然月令所藏不一，而用神遂有变化。如十二支中，除子午卯酉外，余皆有藏，不必四库也。即以寅论，甲为本主，如郡之有府；丙其长生，如郡之有同知...
    """
    
    original_text: str = """- **原文（source_text）**：
  用神既主月令矣，然月令所藏不一，而用神遂有变化。如十二支中，除子午卯酉外，余皆有藏，不必四库也。即以寅论，甲为本主，如郡之有府；丙其长生，如郡之有同知；戊亦长生，如郡之有通判。假使寅月为提，不透甲而透丙，则如知府不临郡，而同知得以作主，此变化之由也。故若丁生亥月，本为正官，支全卯未，则化为印。己生申月，本属伤官，藏庚透壬，则化为财。凡此之类，皆用神之变化也。

- 原注（原文注解）：
  　　本段总论“用神变化”的根本原因：
  - 月令为用神之本，但十二支多有藏干，除子午卯酉四正外，余支皆“多头结构”；
  - 当本主不透，而副主或余气透出、会合成局时，原用神的位置与性格会发生“代理主事”的变化；
  - 丁亥、己申两例，分别演示从官化印、从伤化财的典型情形。

- 分字分词释义：
  - 月令所藏不一：
    - 指地支所藏天干不止一位主气，多有长生、余气、库气等陪衬。
  - 不必四库：
    - 变化并不局限于辰戌丑未四墓，普通支如寅申亥未等，只要藏干结构具备，同样可以发生。
  - 甲为本主，如郡之有府：
    - 甲木是寅支的主气，比喻为“知府”，掌一郡大权。
  - 丙其长生，如郡之有同知；戊亦长生，如郡之有通判：
    - 丙火、戊土在寅中为长生，虽非本主，却有实权，比喻为同知、通判，在特定条件下可“代府主事”。
  - 寅月为提：
    - 指月令在寅，寅为一局之纲领。
  - 不透甲而透丙：
    - 天干上不见甲木本主，独见丙火，等于知府不在，只好由同知暂代。
  - 丁生亥月……支全卯未，则化为印：
    - 丁火日主生于亥月，本以亥中壬为官；若地支再有卯未齐全，形成亥卯未木局，原官星壬水被化，转成木印格。
  - 己生申月，本属伤官，藏庚透壬，则化为财：
    - 己土日主生于申月，申中庚为伤官；若庚不透而壬透，则从申藏壬水为财，以财为用，原伤官之性退居次位。

- **规范化释义（primary_lang_explained）**：
  用神的理论以月令为核心，但月令所在的地支并不只有一位“本主”。除了子午卯酉这四个只藏单一主气的支之外，其他地支内部往往同时藏着主气与长生、余气等好几位“角色”。

  以寅支为例：甲木是本主，好比一郡的知府；丙火是甲木的长生，好比协助知府的同知；戊土也是长生，好比郡中通判。正常情况当然是甲木“主事”，命局论用神自然以甲为纲。但如果寅月为提纲之月，天干上偏偏不透甲，反而是丙火或戊土透出并得实权，就等于是知府不在，改由同知或通判暂时执政——此时，原本的甲木用神便会“让位”，用神随之发生变化。

  丁亥、己申两个例子把这种“代理主事”的机制说得更直白：
  - 丁日生亥月，按理亥中壬水为正官，是丁火的官星；但如果地支卯未齐全，构成亥卯未三合木局，则原本的水官被合化成木，木转而为印格，用神由官变印；
  - 己日生申月，申中庚金本为伤官，但若庚不透、壬水透出，壬便从藏中“走到台前”，使原来的伤官退居幕后，格局转成以水财为主.

  这便是“用神变化”的基本原因：月令内部的多重藏干与三合六合等会局，使原来的用神有时不再真正在“当家”，而由其他藏干代理.

- **完整对等诠释（secondary_lang_full）**：  
  This section explains why the Useful God can change even when the Month branch itself remains the same. The Month branch may hide several different stems, and in many branches more than one stem can in principle take charge. Yin, for instance, hides Jia Wood as the primary ruler of the county, with Bing Fire and Wu Earth as its assistants. In ordinary cases Jia, the main Wood, is treated as the Useful God. But if Yin is the Month branch and Jia never appears on the stems while Bing or Wu does surface and gains real influence, it is as if the prefect is absent and the vice-prefect or assistant magistrate temporarily governs in his place. The role of Useful God then shifts from the absent main ruler to the deputy who is actually visible and in power.

  The text illustrates the same logic with Ding day in Hai month and Ji day in Shen month. For Ding in Hai, Ren Water in Hai is originally the Direct Officer, but when Mao and Wei complete a Hai–Mao–Wei Wood combination, the water qi is transformed into Wood and the structure turns into a Resource pattern, so the Useful God moves from Officer to Resource. For Ji in Shen, the hidden Geng Metal is by nature Hurting Officer, yet if Geng stays hidden and Ren Water rises to the stem, the chart takes Wealth as its main line instead. All such cases are examples of ‘Useful God changing’: when the Month’s principal stem remains hidden while a secondary stem comes to the surface and secures the bureau, the effective Useful God must be reassigned to the one that is truly in office.

- 详细解说：
  - 用神虽主月令，但**谁在天干上“执政”**，才是真正的用神：本主不透、而副主透出且会局有力时，格局重心必然随之移动；
  - 藏干不是被动背景，而是潜在的备用用神和破格因素，随时可能在合化中“上位”；
  - 学命不能只看月令字面，更要细察其中藏干结构、透出情况及支间会合.

- 核心要点：
  - **三问用神变化：**
    1) 月令本主是否透出？
    2) 藏干中有无他神透干、得局？
    3) 合会是否已把原主气“挪位”或“化性”？
  - 本主不透而副主透，副主往往转为真正用神；
  - 合局、化局一旦成形，原用神的性质和位置都可能发生根本变化。

- 应用推演：
  1) 解剖月令：列出主气、长生、余气各是谁，分清层级；
  2) 查天干：看哪一个藏干透出，并审其是否得根、得局；
  3) 看支间会合：有无三合、三会、半合，把原主气化掉或扶起；
  4) 据此重定用神：本主不透而副主有权时，承认“代理用神”；
  5) 再按新用神体系，推格局、取喜忌。

- 反例与边界：
  - 只看“寅木主事”，不察寅中丙戊透出与否，忽略“代理主事”的情形；
  - 见丁亥局仍执着看水官，不顾亥卯未成木局而化印；
  - 把“藏干皆有用”理解为“每一藏干都要平均使用”，反失主从。

- 小例（示意）：
  - 某命甲日生寅月，天干丙透而甲不透，地支又成寅午戌火局，此时局中真正“当家”的已是火气，用神宜从火印、火食伤体系入手，而不宜拘泥于“寅为木旺，必用木”。

- 校勘与字词辨析：
  - “不必四库也”：点出变化并不限于辰戌丑未四墓，今本多同，存而释之；
  - “如郡之有府……同知……通判”：此处比喻系统在原书中极为重要，本精校保持原状，并在白话中展开说明。

---




- **叙事素材（narrative_snippets）**：
  - `[ns_zpzy_291]` `[trigger: 用神变化]` `[factor_trigger: yongshen_sui_bian AND bianzhong_you_changli_kexun]` `[role: 主干]` 用神虽变，变中有常理可循。 → 《子平真诠》#上卷
  - `[ns_zpzy_292]` `[trigger: 用神有力]` `[factor_trigger: yongshen_youli=true AND yunzhu_ze_fa]` `[role: 主干]` 用神有力，运助则发。 → 《子平真诠》#上卷
  - `[ns_zpzy_293]` `[trigger: 格成格破]` `[factor_trigger: (gecheng=true AND result=ji) OR (gepo=true AND result=xiong)]` `[role: 主干]` 格成则吉，格破则凶。 → 《子平真诠》#上卷"""
    normalized_text_zh: str = """"""
    subject: str = "用神变化之由：月令藏干与“代理主事”"
    factor_refs: list = ['benzhu', 'fuzhu', 'daili_zhushi', 'canggan_jiegou', 'yongshen_bianhua', 'engine_id', 'canggan_quanli', 'bazi_rule_engine', 'tougan_guishu', 'bazi_rule_engine', 'huihe_yingxiang', 'bazi_rule_engine', 'yongshen_genghuan', 'bazi_rule_engine', 'wupan_fengxian', 'bazi_rule_engine', 'source_ref', 'rel_zpzq_105', 'canggan_quanli', 'rel_zpzq_106', 'tougan_guishu', 'rel_zpzq_107', 'huihe_yingxiang', 'evi_zpzq_099', 'huihe_yingxiang', 'rule_guanhuayin', 'evi_zpzq_100', 'tougan_guishu', 'rule_shanghuacai', 'concept_role_change', 'concept_deputy']
    
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
        l1_anchor="zpzq_v1.0.0_用神变化之由_月令藏干与_代理主事_001_L1",
    )
    version: str = "1.0.0"
