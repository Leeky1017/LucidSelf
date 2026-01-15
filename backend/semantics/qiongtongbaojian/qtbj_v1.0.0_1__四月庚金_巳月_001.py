"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.578305
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
    semantic_id="qtbj_v1.0.0_1__四月庚金_巳月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 1四月庚金巳月(SemanticEntry):
    """
    - **原文（source_text）**：
  四月庚金，长生于巳，巳内有戊。丙不镕金，故不畏火炎，丙亦可作用，但先壬水，方得中和，故曰群金生夏，喜用勾陈。次取戊土，丙火佐之。三者皆全，登科及第，即...
    """
    
    original_text: str = """- **原文（source_text）**：
  四月庚金，长生于巳，巳内有戊。丙不镕金，故不畏火炎，丙亦可作用，但先壬水，方得中和，故曰群金生夏，喜用勾陈。次取戊土，丙火佐之。三者皆全，登科及第，即透一二，亦非白丁。
  或一派丙火，名曰假杀为权，须不见壬制者，此人假作清高，并无仁义，刑妻克子。有壬制者，又主荣华。壬藏支者，有富贵之名，而无其实。
  或支成金局，变弱为强，用丙无力，用丁方妙，故丁透者吉。无丁、无用之人。或丁出三四，煅制太过，其人奔波。
  四月庚金，须用壬丙戊，但非拘执先后，宜分病用药。妻子仝前。
  剑戟成功，入火乡而反害。金逢火已损，再见火必伤。庚辛火旺怕南方，逢辰巳之乡，又为荣断。

- **分字分词释义**：
  - **四月**：巳月 / 农历四月 / 丙火当令
  - **长生于巳**：庚金长生在巳 / 气不绝 / 十二长生
  - **丙不镕金**：丙火不熔庚金 / 长生之金 / 不畏火
  - **勾陈**：戊土 / 土神 / 生身之用
  - **假杀为权**：七杀假借权柄 / 杀重身轻 / 格局名
  - **刑妻克子**：伤害妻子 / 克子息 / 凶象
  - **变弱为强**：身弱转身强 / 金局帮身 / 格局变化
  - **煅制太过**：锻炼过度 / 火多熔金 / 凶象
  - **剑戟成功**：兵器成型 / 金已成器 / 吉象
  - **火乡**：南方火地 / 午未方 / 忌讳

- **规范化释义（primary_lang_explained）**：
  四月（巳月）的庚金，长生在巳，巳中藏有戊土。丙火（七杀）不熔金（因庚金长生），所以不畏火炎，丙火也可以作用，但先用壬水（食神制杀/调候），才能得到中和，所以说“群金生夏，喜用勾陈”（勾陈指土？原文“喜用勾陈”疑指用戊土生身，或指喜土金帮身。通常夏金喜水土）。次取戊土，丙火佐之。壬、戊、丙三者皆全，登科及第，即使透出一二个，也非白丁。
  如果一派丙火，叫“假杀为权”，必须不见壬水制约（杀印相生或从杀？不，原文说“须不见壬制者...假作清高”，意指若杀重无制则假清高。若有壬制，主荣华。这里逻辑有点绕。通常杀重喜食制。原文可能是说：若假杀为权（杀重身轻），若无壬水制杀，则假清高；有壬制则荣华）。有壬水制约者，又主荣华。壬水藏支者，有富贵之名，而无其实。
  如果地支合成金局，变弱为强（身转旺），用丙火无力（火不够炼），用丁火才妙（丁炼顽金），所以丁火透出者吉。无丁火，无用之人。或者丁火透出三四个，锻炼制约太过，这人奔波劳碌。
  四月庚金，须用壬水、丙火、戊土，但不是拘执先后，适宜分辨病症用药。妻子同前。
  （诗云）剑戟成功，入火乡而反害。金逢火已损，再见火必伤。庚辛火旺怕南方，逢辰巳之乡（土金之地），又为荣断。

- **完整对等诠释（secondary_lang_full）**：
  Geng Metal in the 4th Month (Snake Month): Born in Si, which contains Wu. Bing does not melt Metal (as it is Birth place), so it does not fear blazing Fire; Bing can be used. But first use Ren Water to achieve balance. Thus "Group of Metals born in Summer likes using Gouchen" (Earth). Next take Wu Earth, with Bing assisting. If Ren, Wu, and Bing are all present, one passes exams. Even if one or two reveal, one is not a commoner.
  If there is a mass of Bing Fire, it is "Fake Killing wielding Power". If Ren is not seen to control it, the person pretends to be noble/aloof but has no benevolence/righteousness, punishing wife and harming children. If Ren controls it, it implies glory. If Ren is hidden, one has the name of wealth/nobility but not the reality.
  If branches form a Metal Frame, turning Weak into Strong, Bing is powerless; Ding is wondrous. So Ding revealed is auspicious. Without Ding, a useless person. If 3-4 Dings reveal, smelting is excessive, the person wanders.
  4th Month Geng needs Ren/Bing/Wu, but order is not fixed; distinguish disease and medicine.
  (Poem) Swords and Halberds formed, entering Fire land brings harm. Metal damaged by Fire will be hurt by more Fire. Geng/Xin with prosperous Fire fear the South; meeting Chen/Si (Wet Earth/Metal Birth) implies glory.

- **核心要点**：
  - **首要用神**：壬水（调候/制杀）。巳月火旺，喜水润。
  - **配合**：戊土（生身）、丙火（暖/杀）。
  - **假杀为权**：丙多无制，假清高。

- **详细解说**：
  - 巳月庚金虽长生，但巳火本气为丙，实为杀地。
  - 关键在于“调候”与“制杀”。夏金柔弱，喜土生、水润。
  - "喜用勾陈"：勾陈即土，夏金喜土生身泄火。
  - "剑戟成功"：喻金已成器，怕火乡销熔。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_335]` `[trigger: 庚生巳月]` `[factor_trigger: month_si AND tiangan_geng AND tiangan_ren]` `[role: 主干]` 四月庚金，长生于巳，丙不镕金，故不畏火炎，但先壬水，方得中和。 → 《穷通宝鉴·三夏庚金》#31.1
  - `[ns_qttbj_336]` `[trigger: 壬丙戊全]` `[factor_trigger: month_si AND tiangan_geng AND ren_revealed AND bing_revealed AND wu_revealed]` `[role: 条件分支]` 壬丙戊三者皆全，登科及第，即透一二，亦非白丁。 → 《穷通宝鉴·三夏庚金》#31.1
  - `[ns_qttbj_337]` `[trigger: 假杀为权]` `[factor_trigger: month_si AND tiangan_geng AND bing_excessive AND NOT tiangan_ren AND fake_killing_power]` `[role: 条件分支]` 或一派丙火，名曰假杀为权，须不见壬制者，此人假作清高。 → 《穷通宝鉴·三夏庚金》#31.1
  - `[ns_qttbj_338]` `[trigger: 金局用丁]` `[factor_trigger: month_si AND tiangan_geng AND dizhi_metal_frame AND tiangan_ding]` `[role: 条件分支]` 或支成金局，变弱为强，用丁方妙，故丁透者吉。 → 《穷通宝鉴·三夏庚金》#31.1
  - `[ns_qttbj_339]` `[trigger: 剑戟成功]` `[factor_trigger: tiangan_geng AND metal_formed AND fears_fire_luck]` `[role: 总结]` 剑戟成功，入火乡而反害。金逢火已损，再见火必伤。 → 《穷通宝鉴·三夏庚金》#31.1"""
    normalized_text_zh: str = """"""
    subject: str = "1. 四月庚金（巳月）"
    factor_refs: list = ['fake_killing_power', 'sword_halberd_success']
    
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
        book_id="qiongtongbaojian",
        chapter="",
        l1_anchor="qtbj_v1.0.0_1__四月庚金_巳月_001_L1",
    )
    version: str = "1.0.0"
