"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228693
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
    semantic_id="smth_v1.0.0_戊午己未天上火_自旺衰火刚柔有别_001",
    book_id="sanming",
    engine_id="bazi"
)
class 戊午己未天上火自旺衰火刚柔有别(SemanticEntry):
    """
    - **原文（source_text）**：
  戊午自旺之火，己未偏库之火，居离明之方，旺相之地，其气极盛，他水无伤。忌丙午、丁未天上之水。阎东叟云：戊午自旺，火含离明炎上之气，无情治物，动违于众。...
    """
    
    original_text: str = """- **原文（source_text）**：
  戊午自旺之火，己未偏库之火，居离明之方，旺相之地，其气极盛，他水无伤。忌丙午、丁未天上之水。阎东叟云：戊午自旺，火含离明炎上之气，无情治物，动违于众。秋冬得之，济以水土旺气，则豁达高明，福力坚壮。春夏乘之以金木，虽腾光迅速，命非久常。五行要论云：己未衰火，含余藏宝之气，春夏之月，运入沉潜之乡，则明达峻敏，福庆深远。

- **分字分词释义**：
  - **自旺之火**：自己旺盛的火。
  - **偏库之火**：偏库的火。
  - **居离明之方**：居于离卦光明之方。
  - **旺相之地**：旺盛得势的地方。
  - **其气极盛**：其气极其旺盛。
  - **无情治物**：无情地管治事物。
  - **动违于众**：动辄违背众人。
  - **豁达高明**：豁达高明。
  - **福力坚壮**：福德力量坚强壮大。
  - **腾光迅速**：光芒腾飞迅速。
  - **命非久常**：命运不能长久。
  - **余藏宝**：残余藏宝。
  - **沉潜之乡**：沉潜的地方。
  - **明达峻敏**：明达峻猛敏锐。
  - **福庆深远**：福庆深厚久远。

- **规范化释义（primary_lang_explained）**：
  戊午是自己旺盛的火，己未是偏库的火，居于离卦光明之方，旺盛得势的地方，其气极其旺盛，其他水无法伤害。只忌讳丙午、丁未天上的水。阎东叟说：戊午自旺火，包含离卦光明炎上的气质，无情地管治事物，动辄违背众人。秋冬得到它，用水土旺气来帮助，就豁达高明，福德力量坚强壮大。春夏遇到它配以金木，虽然光芒腾飞迅速，命运不能长久。五行要论说：己未衰火，包含残余藏宝的气质，春夏之月，运入沉潜的地方，就明达峻猛敏锐，福庆深厚久远。

- **完整对等诠释（secondary_lang_full）**：
  Wuwu is self-prosperous fire, Jiwei is partial-storage fire, residing at Li-bright direction, prosperous-favorable location, their energy extremely-vigorous, other Waters cannot harm. Only fears Bingwu, Dingwei celestial water. Yan Dongsou says: Wuwu self-prosperous fire contains Li-bright flaming-upward energy, ruthlessly governs things, moving violates multitudes. Autumn-winter obtaining it, aided by Water-Earth prosperous energy, then magnanimous elevated-bright, blessing-power firm-robust. Spring-summer riding it with Metal-Wood, although radiance soaring swift, destiny not long-lasting. Five Elements Essential Discourse says: Jiwei declining fire, contains remnant treasure-storing energy. Spring-summer months, fate entering submerged-latent location, then brilliant-penetrating steep-keen, blessing-celebration deep-distant.

- **核心要点**：
  - 戊午己未为天上火，自旺偏库
  - 居离明方旺相地气极盛
  - 他水无伤、忌天河水
  - 戊午自旺火：离明炎上、无情治物、动违于众
  - 秋冬济以水土豁达高明、春夏金木腾光不久
  - 己未衰火：余藏宝气、运入沉潜明达峻敏

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_244]` `[trigger: 戊午己未火性质]` `[factor_trigger: wuwu_self_prosperous_fire AND li_bright_flaming_ruthlessly_governs AND autumn_winter_aided_magnanimous_spring_summer_not_lasting]` `[role: 主干]` 戊午自旺之火，己未偏库之火，居离明之方，旺相之地，其气极盛，他水无伤。忌丙午、丁未天上之水。阎东叟云：戊午自旺，火含离明炎上之气，无情治物，动违于众。秋冬得之，济以水土旺气，则豁达高明，福力坚壮。春夏乘之以金木，虽腾光迅速，命非久常。五行要论云：己未衰火，含余藏宝之气，春夏之月，运入沉潜之乡，则明达峻敏，福庆深远。 → 《三命通会》卷一#戊午己未火性质

- **详细解说**：
  此条详论戊午、己未（天上火）的性质与格局。戊午自旺火、己未偏库火，居离明方旺相地气极盛，他水无伤（火太旺），只忌丙午丁未天河水。阎东叟分析戊午：离明炎上无情治物动违于众，秋冬水土济豁达高明福力坚壮，春夏金木腾光迅速命不久长。五行要论指出己未衰火余藏宝气，运入沉潜明达峻敏福庆深远。这是论述旺火与衰火的刚柔差异与季节影响。

- **校勘与字词辨析（双语）**：
  - **中文**："自旺"指午为火帝旺。"离明"指离卦为火、为光明。"无情治物"形容火势太旺无情。"沉潜"指收敛潜藏。
  - **English**: "Self-prosperous" means Wu is fire's emperor-prosperity. "Li-bright" means Li trigram is fire and brightness. "Ruthlessly governs things" describes fire too vigorous and ruthless. "Submerged-latent" means restraining and hiding."""
    normalized_text_zh: str = """"""
    subject: str = "戊午己未天上火：自旺衰火刚柔有别"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate']
    
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
        l1_anchor="smth_v1.0.0_戊午己未天上火_自旺衰火刚柔有别_001_L1",
    )
    version: str = "1.0.0"
