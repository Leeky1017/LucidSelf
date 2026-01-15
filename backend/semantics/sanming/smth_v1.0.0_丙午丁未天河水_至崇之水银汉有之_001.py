"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228644
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
    semantic_id="smth_v1.0.0_丙午丁未天河水_至崇之水银汉有之_001",
    book_id="sanming",
    engine_id="bazi"
)
class 丙午丁未天河水至崇之水银汉有之(SemanticEntry):
    """
    - **原文（source_text）**：
  丙午、丁未，银汉之水，土不能克，天上之水，地金不能生也。生旺太过，反伤于万物；死绝太多，又不能生万物。五行要论云：丙午至崇之水，体南方温厚之气，禀之者...
    """
    
    original_text: str = """- **原文（source_text）**：
  丙午、丁未，银汉之水，土不能克，天上之水，地金不能生也。生旺太过，反伤于万物；死绝太多，又不能生万物。五行要论云：丙午至崇之水，体南方温厚之气，禀之者，类有道气虚变，颖异有为，魁众出伦。丁未具足三才全数，得冲正之气，禀之者，主精神气全，性根高妙，尽变之道。

- **分字分词释义**：
  - **银汉之水**：银河的水。
  - **天上之水**：天上的水。
  - **地金不能生**：地上的金不能生。
  - **生旺太过**：生旺过度。
  - **死绝太多**：死绝太过。
  - **至崇之水**：最为尊崇的水。
  - **南方温厚之气**：南方温暖深厚的气质。
  - **道气虚变**：道气虚灵变化。
  - **颖异有为**：聪颖奇异有作为。
  - **魁众出伦**：众人之首超出伦常。
  - **三才全数**：天地人三才齐全之数。
  - **冲正之气**：冲和正直的气质。
  - **性根高妙**：性情根基高明玄妙。
  - **尽变之道**：极尽变化之道。

- **规范化释义（primary_lang_explained）**：
  丙午、丁未是银河的水，土不能克制，是天上的水，地上的金不能生。如果生旺过度，反而伤害万物；如果死绝太过，又不能生养万物。五行要论说：丙午是最尊崇的水，包含南方温暖深厚的气质，禀受它的人，大多有道气虚灵变化，聪颖奇异有作为，成为众人之首超出伦常。丁未具备天地人三才齐全之数，得到冲和正直的气质，禀受它的人，主精神气完全，性情根基高明玄妙，极尽变化之道。

- **完整对等诠释（secondary_lang_full）**：
  Bingwu, Dingwei are Milky-Way water, Earth cannot overcome, celestial water, terrestrial Metal cannot generate. Born-prosperous excessive, contrarily harms myriad-things; dead-extinct excessive, again cannot generate myriad-things. Five Elements Essential Discourse says: Bingwu is most-exalted water, embodies southern warm-thick energy. Those receiving it, mostly have Dao-energy virtual-transforming, brilliant-extraordinary accomplished, leading-multitudes surpassing-peers. Dingwei possesses complete three-talents full-number, obtains balanced-upright energy. Those receiving it, govern spirit-energy complete, nature-root elevated-sublime, exhausting transformation-way.

- **核心要点**：
  - 丙午丁未为天河水，银汉之水
  - 天上之水土不克、地金不生
  - 生旺太过伤物、死绝太多不生物
  - 丙午至崇之水、南方温厚、道气虚变
  - 丁未三才全数、冲正之气、精神气全

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_238]` `[trigger: 丙午丁未水性质]` `[factor_trigger: bingwu_dingwei_celestial_river_water AND most_exalted_dao_energy_virtual_transforming AND leading_surpassing_nature_elevated_sublime]` `[role: 主干]` 丙午、丁未，银汉之水，土不能克，天上之水，地金不能生也。生旺太过，反伤于万物；死绝太多，又不能生万物。五行要论云：丙午至崇之水，体南方温厚之气，禀之者，类有道气虚变，颖异有为，魁众出伦。丁未具足三才全数，得冲正之气，禀之者，主精神气全，性根高妙，尽变之道。 → 《三命通会》卷一#丙午丁未水性质

- **详细解说**：
  此条合论丙午、丁未（天河水）的特殊性质。二者为银汉之水，是天上之水，土不能克（天水高悬）、地金不能生（不需地金生）。但要平衡：生旺太过反伤万物、死绝太多又不能生物。五行要论分论：丙午至崇之水，南方温厚，道气虚变、颖异有为、魁众出伦；丁未三才全数，冲正之气，精神气全、性根高妙、尽变之道。这是论述天水的特殊性与神妙格局。

- **校勘与字词辨析（双语）**：
  - **中文**："银汉"指银河。"至崇"指最为尊崇。"道气虚变"指道家虚灵变化的气质。"三才"指天地人。"冲正"指冲和正直。
  - **English**: "Milky-Way" refers to celestial river. "Most-exalted" means most revered. "Dao-energy virtual-transforming" means Daoist ethereal-transforming quality. "Three-talents" refers to heaven-earth-human. "Balanced-upright" means harmonious and upright."""
    normalized_text_zh: str = """"""
    subject: str = "丙午丁未天河水：至崇之水银汉有之"
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
        l1_anchor="smth_v1.0.0_丙午丁未天河水_至崇之水银汉有之_001_L1",
    )
    version: str = "1.0.0"
