"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.436596
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
    semantic_id="smth_v1.0.0_六亲取用与亲缘结构_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六亲取用与亲缘结构(SemanticEntry):
    """
    - 原文（source_text）：

  论六亲。

  或问：阴阳何所配合，为夫妇而成六亲？答云：如甲以乙为妹，配以庚金为妻；丙以丁为妹，配以壬水为妻；戊以己配甲；庚以辛配丙；壬以癸配戊。一阴一阳...
    """
    
    original_text: str = """- 原文（source_text）：

  论六亲。

  或问：阴阳何所配合，为夫妇而成六亲？答云：如甲以乙为妹，配以庚金为妻；丙以丁为妹，配以壬水为妻；戊以己配甲；庚以辛配丙；壬以癸配戊。一阴一阳，配成夫妇，有夫妇然后有父子，有父子然后有兄弟。六亲者，父母、兄弟、妻子也。六甲娶己为妻，甲己合而生庚辛为子。男取克干为子，女取干生为息，则己者庚辛之母，庚为父，乙为母，故谓阴干生我为母，我克阳干者为父；克我者为官为子，我克者为财为妻，比和者为兄弟姊妹。其余六亲俱于十干变化取用。

- 分字分词释义：

  - **六亲**：父母、兄弟、妻子四类，连同自己，共构成基本家庭结构。
  - **一阴一阳配成夫妇**：以阴干、阳干相配，象征婚配的阴阳互补。
  - **克我 / 我克 / 生我 / 我生**：以五行生克从日主出发，分别对应父母、妻子、子女与兄弟等不同六亲角色。
  - **十干变化取用**：六亲判断皆从十天干之间的生克合化中推演，而非孤立看某一位。

- **规范化释义（primary_lang_explained）**：

  本节是对“六亲如何从干支中取用”的总纲：

  - 先以阴阳配合说明夫妇的构成，然后引申出父母、兄弟、子女等六亲；
  - 男命以克日主者为子，女命以生日主者为息，进一步说明“父母生我、我生子女”的链条；
  - 由此建立一套：父母——我——配偶——子女——兄弟姊妹，在干支间对应的取用规则。

- **完整对等诠释（secondary_lang_full）**：

  This section lays out how the six close relationships in a family are read from the stems and branches of a chart, always taking the Day Master as the centre. Those who give qi to me are read as parents or protectors; those to whom I give qi are children or works that I bring into the world; those I control are partners and resources that I must shoulder; those who control me are authorities, spouses or offspring who can place demands on me; those who stand equal to me are siblings and peers.

  For a modern reader, this is less a system for judging whether a relative is "good" or "bad" and more a language for mapping flows of care, obligation and pressure within a family network. By following the paths of "gives to me / I give to" and "I control / controls me", we can see where responsibility tends to concentrate, where help is easily available, and where boundaries may be thin. It is a structural map of kinship dynamics, not a moral verdict on filial piety or character.

- 核心要点：

  - 六亲取用以**日主为中心**，通过“生、克、比和”来判定各类亲属象；
  - 阴阳配合出夫妇，再由夫妇生父子、兄弟，是古人对家庭结构的基本想象；
  - 具体推断时，要结合十干生克及合化，不可只记死公式。

- 详细解说：

  1. **以日主为坐标的六亲体系**  
     - 生我者多取为父母；我生者多取为子女；我克者多取为妻财；克我者多取为夫官；比和者多取为兄弟姊妹；  
     - 这样，所有六亲关系都可以在“我与他”的能量流动中找到对应。

  2. **阴阳与性别角色**  
     - 文中仍以“男取克干为子、女取干生为息”等说法区分男女；  
     - 现代阅读不必拘泥于性别角色，而可将其视作“主 / 客”、“主动 / 被动”的关系象随机。

  3. **现代应用的界限**  
     - 六亲取用体系可以帮助我们从命局结构上理解亲缘强弱、支持与压力的大致方向；  
     - 但具体到个体命运、家庭事件，仍需结合现实状况，不宜以此简单断绝婚姻、亲子或孝道。

- 校勘与字词辨析：

  - 原文后文大量举例推演诸干为父母、兄弟等，本稿不一一转录，仅在解说中概括其取用逻辑。
  - “正财为妻、偏财为妾”“正官为夫、七煞为偏夫”等说法，保留为结构性术语，在白话中尽量用中性语言转译。
  - **English**：
    - Translated with neutral language in vernacular.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_07_077]` `[trigger: 六亲总纲]` `[factor_trigger: liuqin_quanyong]` `[role: 主干]` 论六亲。 → 《三命通会》卷七#六亲取用
  - `[ns_smth_07_078]` `[trigger: 阴阳配合]` `[factor_trigger: yinyang_peihe AND fufu_fumu]` `[role: 主干依赖]` 一阴一阳，配成夫妇，有夫妇然后有父子，有父子然后有兄弟。 → 《三命通会》卷七#六亲取用
  - `[ns_smth_07_079]` `[trigger: 生克取用]` `[factor_trigger: ke_wo_wei_guan AND wo_ke_wei_cai]` `[role: 条件分支]` 克我者为官为子，我克者为财为妻，比和者为兄弟姊妹。 → 《三命通会》卷七#六亲取用
  - `[ns_smth_07_080]` `[trigger: 十干变化]` `[factor_trigger: shigan_bianhua_quyong]` `[role: 总结]` 其余六亲俱于十干变化取用。 → 《三命通会》卷七#六亲取用"""
    normalized_text_zh: str = """"""
    subject: str = "六亲取用与亲缘结构"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_factor_107', 'bazi_semantic', 'bazi_state_factor_359', 'bazi_semantic', 'bazi_structure_factor_108', 'bazi_semantic', 'bazi_factor_17', 'bazi_semantic', 'source_ref', 'rel_smth_07_055', 'qinyuan_zhongxin', 'rel_smth_07_056', 'zhichi_yali', 'rel_smth_07_057', 'jiazu_lianjie', 'evi_smth_07_055', 'qinyuan_zhongxin', 'rule_liuqin', 'evi_smth_07_056', 'zhichi_yali', 'rule_shengke', 'evi_smth_07_057', 'jiazu_lianjie', 'rule_shigan', 'map_smth_07_037', 'map_smth_07_038']
    
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
        l1_anchor="smth_v1.0.0_六亲取用与亲缘结构_001_L1",
    )
    version: str = "1.0.0"
