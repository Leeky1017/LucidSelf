"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.850558
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
    semantic_id="mlxj_v1.0.0_条目三_审三辰之象_001",
    book_id="mlxj",
    engine_id="dream"
)
class 条目三审三辰之象(SemanticEntry):
    """
    ### 原文（source_text）

审三辰之象，如宿舍轮转，及五星所行合散、犯、守、陵历、斗拍，彗孛飞流，与日月薄蚀、晕适、背𫔎、抱珥、虫霓之类也。宿舍者，正月日躔娵訾，于辰在亥，二月日躔降娄，...
    """
    
    original_text: str = """### 原文（source_text）

审三辰之象，如宿舍轮转，及五星所行合散、犯、守、陵历、斗拍，彗孛飞流，与日月薄蚀、晕适、背𫔎、抱珥、虫霓之类也。宿舍者，正月日躔娵訾，于辰在亥，二月日躔降娄，于辰在戍之类，而二十八宿轮环于日辰，历七元而始周也。五星同舍曰合，变为妖星曰散，寸以内光芒相及曰犯，居其宿曰守，相冒而过曰陵，经之曰历，相击曰斗，相逼曰拍，光芒偏指曰彗，气四出曰孛，自下而升曰飞，自上而降曰流也。日月无光曰薄，亏毁为食，日旁祲气曰晕，将食先黑曰适，形如背字曰背，形如玉𫔎曰𫔎，气向日曰抱，形点黑曰珥，虹雄曰虹，雌曰霓也。占梦者必探宿舍所临，而五星之变，日月之异，皆不可不精察以为推者也。

### 分字分词释义

- **三辰**：日、月、星/天上三种发光体/天文观测的核心对象
- **宿舍**：二十八宿的宫位/太阳所躔之星宿/月建对应的星宿位置
- **五星**：金木水火土五大行星/岁星、荧惑、填星、太白、辰星
- **合**：五星同舍一宿/会合
- **散**：变为妖星/异常离散
- **犯**：光芒相及/寸内相触/星体相侵
- **守**：居其宿不去/停留驻守
- **陵**：相冒而过/越界凌犯
- **历**：经过/历行
- **斗**：相击/星体相撞之象
- **拍**：相逼/紧迫相近
- **彗**：扫帚星/光芒偏指一方
- **孛**：彗星类/气四出散发
- **飞**：自下而升之流星
- **流**：自上而降之流星
- **薄**：日月无光/光弱
- **食**：日月蚀/亏损
- **晕**：日旁祲气/光晕
- **适**：将食先黑/食前之象
- **背𫔎抱珥**：日月周围各种光象/气象天文现象
- **虹霓**：虹为雄/霓为雌/雨后彩虹

### 规范化释义（primary_lang_explained）

占梦的第三条核心原则是「审三辰之象」——必须审察日、月、星三种天体的运行状态和异象。这包括二十八宿的轮转、五大行星的各种运行状态（合、散、犯、守、陵、历、斗、拍）、彗星孛星的飞流，以及日月的各种异象（薄蚀、晕适、背𫔎、抱珥、虹霓）等。

所谓「宿舍」，指太阳所躔之星宿与月建的对应关系：正月太阳躔于娵訾宿、月建在亥位，二月太阳躔于降娄宿、月建在戌位，以此类推。二十八宿环绕日辰运行，历经七元（二百五十二年）而完成一个大周期。

五星运行状态的术语：同居一宿叫「合」，变异为妖星叫「散」，光芒相及在寸内叫「犯」，停留某宿叫「守」，相冒越过叫「陵」，经行过去叫「历」，相互撞击叫「斗」，紧迫相逼叫「拍」。彗星光芒偏指一方叫「彗」，气息四散叫「孛」，从下往上升叫「飞」，从上往下落叫「流」。

日月异象的术语：光芒暗淡叫「薄」，亏损缺损叫「食」，日旁有祲气叫「晕」，将食之前先黑叫「适」，形如背字叫「背」，形如玉𫔎叫「𫔎」，气向日聚叫「抱」，有黑点叫「珥」，虹为雄、霓为雌。

占梦者必须探究宿舍所临的位置，精察五星的变化、日月的异象，将这些天文现象作为推断梦境的重要依据。

### 完整对等诠释（secondary_lang_full）

The third principle is "Examining the Phenomena of the Three Luminaries" — one must carefully examine the movements and anomalies of the Sun, Moon, and Stars. This encompasses the rotation of the Twenty-Eight Lunar Mansions, the various planetary movements (Conjunction, Dispersion, Violation, Guarding, Transgression, Transit, Clash, Pressure), cometary phenomena, and solar-lunar anomalies (Dimming, Eclipse, Halo, Pre-eclipse Darkening, various Corona formations, Rainbow phenomena).

The "Lunar Mansion positions" refer to the correspondence between the Sun's location in the mansions and the monthly branches: in the first month, the Sun is in Zouzi mansion with the branch at Hai; in the second month, the Sun is in Jianglou mansion with the branch at Xu, and so forth. The Twenty-Eight Mansions cycle around the Sun's position, completing a grand cycle every seven epochs (252 years).

Planetary movement terminology: when five planets share a mansion, it's "Conjunction"; when they transform into ominous stars, it's "Dispersion"; when light rays touch within an inch, it's "Violation"; when stationed at a mansion, it's "Guarding"; when crossing over, it's "Transgression"; when passing through, it's "Transit"; when colliding, it's "Clash"; when pressing close, it's "Pressure." For comets: when rays point sideways, it's "Hui-comet"; when energy radiates in all directions, it's "Bo-comet"; when rising from below, it's "Flying"; when descending from above, it's "Flowing."

Solar-lunar anomaly terminology includes various technical terms for eclipses, halos, coronae, and rainbow phenomena, each with specific divinatory significance.

Dream interpreters must investigate the mansion positions and meticulously observe planetary changes and solar-lunar anomalies as crucial references for dream interpretation.

### 核心要点

- 审三辰之象是占梦第三核心原则
- 三辰指日、月、星三种天体
- 二十八宿轮转，历七元（252年）一周
- 五星八种状态：合、散、犯、守、陵、历、斗、拍
- 彗孛四象：彗（偏指）、孛（四出）、飞（上升）、流（下降）
- 日月异象：薄、食、晕、适、背、𫔎、抱、珥、虹、霓
- 必须将天文现象与梦境对应分析

### 叙事素材（narrative_snippets）

- `[ns_mlxj_011]` `[trigger: 天文占梦]` `[factor_trigger: dream_celestial_sign AND dream_tianxiang AND dream_xingdou AND dream_liuxing AND dream_symbol_wenchangxing AND dream_riyue]` `[role: 主干]` 占梦者必探宿舍所临，而五星之变，日月之异，皆不可不精察以为推者也。 → 《梦林玄解·卷之首》#审三辰之象
- `[ns_mlxj_012]` `[trigger: 五星合]` `[factor_trigger: dream_planet_conjunction]` `[role: 条件分支]` 五星同舍曰合，变为妖星曰散。 → 《梦林玄解·卷之首》#审三辰之象
- `[ns_mlxj_013]` `[trigger: 日月食]` `[factor_trigger: dream_eclipse_sign]` `[role: 条件分支]` 日月无光曰薄，亏毁为食。 → 《梦林玄解·卷之首》#审三辰之象"""
    normalized_text_zh: str = """"""
    subject: str = "条目三：审三辰之象"
    factor_refs: list = ['dream_celestial_sign', 'dream_lunar_mansion', 'dream_planet_conjunction']
    
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
        book_id="mlxj",
        chapter="",
        l1_anchor="mlxj_v1.0.0_条目三_审三辰之象_001_L1",
    )
    version: str = "1.0.0"
