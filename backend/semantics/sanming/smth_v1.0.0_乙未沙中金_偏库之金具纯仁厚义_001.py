"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228580
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
    semantic_id="smth_v1.0.0_乙未沙中金_偏库之金具纯仁厚义_001",
    book_id="sanming",
    engine_id="bazi"
)
class 乙未沙中金偏库之金具纯仁厚义(SemanticEntry):
    """
    - **原文（source_text）**：
  乙未偏库之金，亦火制而土生之，则福壮气聚。忌己未、丙申、丁酉之火。五行要论云：乙未金在数为木库，又为天将，具纯仁厚义之德，无往不吉。贵格得之，是不世之...
    """
    
    original_text: str = """- **原文（source_text）**：
  乙未偏库之金，亦火制而土生之，则福壮气聚。忌己未、丙申、丁酉之火。五行要论云：乙未金在数为木库，又为天将，具纯仁厚义之德，无往不吉。贵格得之，是不世之英杰，魁镇士伦。常格得之，带煞冲犯，亦作小人中之君子，眉寿人也。

- **分字分词释义**：
  - **偏库之金**：偏于入库的金。
  - **火制而土生**：火锻炼而土生养。
  - **福壮气聚**：福气壮大气势凝聚。
  - **木库**：木的库藏。
  - **天将**：天将星。
  - **纯仁厚义之德**：纯粹仁爱深厚道义的德性。
  - **不世之英杰**：世间少有的英杰。
  - **魁镇士伦**：魁首镇压士人伦理。
  - **眉寿人**：长寿之人。

- **规范化释义（primary_lang_explained）**：
  乙未是偏库的金，也是由火锻炼而土生养的，则福气壮大气势凝聚。忌讳己未、丙申、丁酉的火。五行要论说：乙未金在数理上为木库，又为天将星，具有纯粹仁爱深厚道义的德性，无论何处都吉利。如果贵格得到它，是世间少有的英杰，成为士人的魁首。即使常格得到它，纵然带煞冲犯，也能成为小人中的君子，是长寿之人。

- **完整对等诠释（secondary_lang_full）**：
  Yiwei is partial-storage metal, also fire-refining earth-generating, then blessing-robust energy-gathering. Avoids Jiwei, Bingshen, Dingyou fire. Five Elements Essential Discourse says: Yiwei Metal in numerology as wood-repository, also as Heaven-General, possesses pure-benevolence thick-righteousness virtue, auspicious wherever going. Noble pattern obtaining it, is world-rare hero-talent, chief-commanding scholar-ethics. Common pattern obtaining it, even carrying sha conflicting, also becomes gentleman among petty-men, longevity person.

- **核心要点**：
  - 乙未为沙中金，偏库之金
  - 火制土生则福壮气聚
  - 在数为木库、为天将
  - 具纯仁厚义之德
  - 贵格为英杰魁首，常格亦长寿

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_230]` `[trigger: 乙未金性质]` `[factor_trigger: yiwei_partial_storage_metal AND pure_benevolence_thick_righteousness AND noble_hero_common_gentleman]` `[role: 主干]` 乙未偏库之金，亦火制而土生之，则福壮气聚。忌己未、丙申、丁酉之火。五行要论云：乙未金在数为木库，又为天将，具纯仁厚义之德，无往不吉。贵格得之，是不世之英杰，魁镇士伦。常格得之，带煞冲犯，亦作小人中之君子，眉寿人也。 → 《三命通会》卷一#乙未金性质

- **详细解说**：
  此条详论乙未（沙中金）的特殊性质与格局。乙未是偏库的金（未为木库，但纳音为金），由火锻炼土生养则福壮气聚，但忌己未（天上火）、丙申（山下火）、丁酉（山下火）。五行要论强调乙未金在数为木库又为天将星，具纯仁厚义之德，无往不吉。贵格得之为英杰魁首，即使常格带煞也能成君子长寿。这是论述偏库金的德性与格局转化。

- **校勘与字词辨析（双语）**：
  - **中文**："偏库"指非正库，未为木库而非金库。"火制土生"指火炼金、土生金。"魁镇士伦"指成为士人的领袖楷模。"眉寿"指长寿，眉毛长为长寿象征。
  - **English**: "Partial-storage" means non-primary repository, Wei is wood repository not metal. "Fire-refining earth-generating" means fire refines metal, earth generates metal. "Chief-commanding scholar-ethics" means becoming leader and model of scholars. "Longevity" refers to long life, long eyebrows symbolize longevity."""
    normalized_text_zh: str = """"""
    subject: str = "乙未沙中金：偏库之金具纯仁厚义"
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
        l1_anchor="smth_v1.0.0_乙未沙中金_偏库之金具纯仁厚义_001_L1",
    )
    version: str = "1.0.0"
