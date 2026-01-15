"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228247
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
    semantic_id="smth_v1.0.0_大驿土与屋上土_001",
    book_id="sanming",
    engine_id="bazi"
)
class 大驿土与屋上土(SemanticEntry):
    """
    - **原文（source_text）**：
  戊申己酉，气以归息，物当收敛，龟缩退闲，美而无事，乃曰大驿土。丙戌丁亥，气成物府，事以美圆，阴阳历遍，势得期闲，乃曰屋上土也。

- **分字分词释义...
    """
    
    original_text: str = """- **原文（source_text）**：
  戊申己酉，气以归息，物当收敛，龟缩退闲，美而无事，乃曰大驿土。丙戌丁亥，气成物府，事以美圆，阴阳历遍，势得期闲，乃曰屋上土也。

- **分字分词释义**：
  - **大驿土**：大驿站道路的土。
  - **气以归息**：气归于休息。
  - **物当收敛**：事物应当收敛。
  - **龟缩退闲**：收缩退守安闲。
  - **美而无事**：完美而无事可做。
  - **气成物府**：气成为事物的府库。
  - **事以美圆**：事情完美圆满。
  - **阴阳历遍**：阴阳经历遍了。
  - **势得期闲**：势头得到安闲时期。

- **规范化释义（primary_lang_explained）**：
  戊申己酉，气归于休息，事物应当收敛，收缩退守安闲，完美而无事可做，就叫大驿土。丙戌丁亥，气成为事物的府库，事情完美圆满，阴阳经历遍了，势头得到安闲时期，就叫屋上土。

- **完整对等诠释（secondary_lang_full）**：
  Wushen-Jiyou: qi returning to rest, things should contract, withdrawing to leisurely repose, perfect yet with nothing to do, thus called Great-Station Earth. Bingxu-Dinghai: qi becoming storehouse of things, affairs perfectly complete, yin-yang having traversed all, momentum gaining leisurely period, thus called Rooftop Earth.

- **核心要点**：
  - 戊申己酉：大驿土（气以归息，美而无事）
  - 丙戌丁亥：屋上土（气成物府，事以美圆）
  - 大驿土为土的收敛归息
  - 屋上土为土的圆满归藏

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_190]` `[trigger: 大驿土与屋上土]` `[factor_trigger: great_station_earth AND rooftop_earth AND nayin_earth_final]` `[role: 主干]` 戊申己酉，气以归息，物当收敛，龟缩退闲，美而无事，乃曰大驿土。丙戌丁亥，气成物府，事以美圆，阴阳历遍，势得期闲，乃曰屋上土也。 → 《三命通会》卷一#大驿土与屋上土

- **详细解说**：
  此条完成土纳音的解释。戊申己酉为"大驿土"：申酉属秋季金旺，土气归息，事物收敛，如大驿站的道路之土，承载完毕归于安闲，美而无事，这是土的收敛状态。丙戌丁亥为"屋上土"：戌亥为秋冬之交，土气成为府库，阴阳历遍，事情圆满完成，势得安闲，如屋顶之土（房屋最后的覆盖），这是土的圆满归藏。六种土纳音：壁上土（封闭）→城头土（育物）→沙中土（润泽）→路旁土（承载）→大驿土（归息）→屋上土（圆满），完整呈现土的一生。命理上，大驿土命格安闲收敛，屋上土命格圆满归藏。至此，六十甲子纳音三十种（金木水火土各六种）全部解释完毕。

- **校勘与字词辨析（双语）**：
  - **中文**："大驿土"指驿站道路之土，承载往来后归于平静。"美而无事"指完美但无事可做了。"屋上土"指屋顶之土，房屋最后的覆盖。"气成物府"指气成为万物的府库。
  - **English**: "Great-Station Earth" refers to station road earth, after bearing travelers returns to tranquility. "Perfect yet nothing to do" means perfect but no more tasks. "Rooftop Earth" refers to roof earth, final covering of buildings. "Qi becoming storehouse" means qi becoming repository of all things."""
    normalized_text_zh: str = """"""
    subject: str = "大驿土与屋上土"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate']
    
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
        l1_anchor="smth_v1.0.0_大驿土与屋上土_001_L1",
    )
    version: str = "1.0.0"
