"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228603
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
    semantic_id="smth_v1.0.0_己亥平地木_自生之木根本繁盛_001",
    book_id="sanming",
    engine_id="bazi"
)
class 己亥平地木自生之木根本繁盛(SemanticEntry):
    """
    - **原文（source_text）**：
  己亥自生之木，根本繁盛，不忌众金，惟嫌辛亥、辛巳、癸酉之金，若见乙卯、丁未水、癸未木，未有不大贵。五行要论云：己亥木自生，挺英才秀拔之德，得之于特达处...
    """
    
    original_text: str = """- **原文（source_text）**：
  己亥自生之木，根本繁盛，不忌众金，惟嫌辛亥、辛巳、癸酉之金，若见乙卯、丁未水、癸未木，未有不大贵。五行要论云：己亥木自生，挺英才秀拔之德，得之于特达处，类皆清贵少达。阎东叟云：己亥之木，得时则清贵，非时则辛苦。

- **分字分词释义**：
  - **自生之木**：自己生长的木。
  - **根本繁盛**：根基繁茂兴盛。
  - **不忌众金**：不忌讳众多的金。
  - **英才秀拔**：英才秀美出众。
  - **特达处**：特别通达之处。
  - **清贵少达**：清高尊贵少有通达。

- **规范化释义（primary_lang_explained）**：
  己亥是自生的木，根基繁茂兴盛，不忌讳众多的金，只忌讳辛亥、辛巳、癸酉的金。如果见到乙卯、丁未水、癸未木，没有不大贵的。五行要论说：己亥木自生，挺拔英才秀美出众的德性，得到它的人在特别通达之处，大多清高尊贵少有通达。阎东叟说：己亥木，得时则清贵，非时则辛苦。

- **完整对等诠释（secondary_lang_full）**：
  Jihai is self-born wood, root-foundation flourishing-prosperous, not fearing many Metals, only avoids Xinhai, Xinsi, Jiyou Metal. If seeing Yimao, Dingwei Water, Guiwei Wood, none not greatly noble. Five Elements Essential Discourse says: Jihai Wood self-born, upright talented-beauty outstanding virtue, obtaining it at specially-accomplished place, mostly pure-noble rarely-reaching. Yan Dongsou says: Jihai Wood, obtaining proper-time then pure-noble, wrong-time then hardship.

- **核心要点**：
  - 己亥为平地木，自生之木
  - 根本繁盛不忌众金
  - 只嫌特定三金
  - 见特定水木大贵
  - 英才秀拔、得时清贵非时辛苦

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_233]` `[trigger: 己亥木性质]` `[factor_trigger: jihai_self_born_wood AND root_foundation_flourishing AND proper_time_noble_wrong_time_hardship]` `[role: 主干]` 己亥自生之木，根本繁盛，不忌众金，惟嫌辛亥、辛巳、癸酉之金，若见乙卯、丁未水、癸未木，未有不大贵。五行要论云：己亥木自生，挺英才秀拔之德，得之于特达处，类皆清贵少达。阎东叟云：己亥之木，得时则清贵，非时则辛苦。 → 《三命通会》卷一#己亥木性质

- **详细解说**：
  此条详论己亥（平地木）的性质。己亥是自生的木（亥为木长生），根本繁盛，一般不忌众金（木气旺），但嫌辛亥（钗钏金）、辛巳（白镴金）、癸酉（剑锋金）等锋锐之金。若见乙卯（大溪水）、丁未（天河水）、癸未（杨柳木），必大贵。五行要论强调己亥木自生，英才秀拔，清贵少达。阎东叟指出得时清贵、非时辛苦。这是论述长生木的繁盛与时节影响。

- **校勘与字词辨析（双语）**：
  - **中文**："自生"指亥为木长生。"根本繁盛"形容木气旺盛。"特达"指特别通达。"清贵少达"指清高但少能通达。
  - **English**: "Self-born" means Hai is wood's longevity position. "Root-foundation flourishing-prosperous" describes vigorous wood energy. "Specially-accomplished" means particularly successful. "Pure-noble rarely-reaching" means noble but rarely achieving widespread success."""
    normalized_text_zh: str = """"""
    subject: str = "己亥平地木：自生之木根本繁盛"
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
        l1_anchor="smth_v1.0.0_己亥平地木_自生之木根本繁盛_001_L1",
    )
    version: str = "1.0.0"
