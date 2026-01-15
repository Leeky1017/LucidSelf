"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.227845
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
    semantic_id="smth_v1.0.0_干支起源与天地人三皇_001",
    book_id="sanming",
    engine_id="bazi"
)
class 干支起源与天地人三皇(SemanticEntry):
    """
    - **原文（source_text）**：
  夫干犹木之干，强而为阳；支犹木之枝，弱而为阴。昔盘古氏明天地之道，达阴阳之变，为三才首君，以天地既分之后，先有天而后有地，由是气化而人生焉。故天皇氏一...
    """
    
    original_text: str = """- **原文（source_text）**：
  夫干犹木之干，强而为阳；支犹木之枝，弱而为阴。昔盘古氏明天地之道，达阴阳之变，为三才首君，以天地既分之后，先有天而后有地，由是气化而人生焉。故天皇氏一姓十三人，继盘古氏以治，是曰天灵，澹泊无为，而俗自化，始制干支之名，以定岁之所在。

- **分字分词释义**：
  - **干犹木之干**：天干如同树木的主干，强壮为阳。
  - **支犹木之枝**：地支如同树木的枝条，柔弱为阴。
  - **三才首君**：天地人三才的首位君主。
  - **气化而人生**：由气化生人类。
  - **澹泊无为**：清静无为而治。
  - **定岁之所在**：确定年岁的位置。

- **规范化释义（primary_lang_explained）**：
  天干就像树木的主干，强壮而属阳；地支就像树木的枝条，柔弱而属阴。远古盘古氏通晓天地之道，洞察阴阳变化，成为天地人三才的首位君主。在天地分开之后，先有天后有地，由此气化而产生人类。因此天皇氏一姓十三人，继承盘古氏治理天下，称为天灵，以清静无为的方式治理，风俗自然化育，开始创制天干地支的名称，用来确定年岁的位置。

- **完整对等诠释（secondary_lang_full）**：
  The Heavenly Stems are like a tree's trunk—strong and yang in nature; the Earthly Branches are like a tree's branches—soft and yin in nature. In ancient times, Pangu understood the way of heaven and earth, comprehended the transformations of yin and yang, and became the first sovereign of the three realms (heaven, earth, humanity). After heaven and earth separated, heaven existed first and then earth, from which qi transformation gave birth to humanity. Thus the Celestial Sovereign lineage, thirteen rulers of one family name, succeeded Pangu in governance. Known as "Heavenly Spirits," they ruled through tranquil non-action, allowing customs to transform naturally. They first created the names of stems and branches to determine the positions of years.

- **核心要点**：
  - 干支取象于树木：干如主干（阳），支如枝条（阴）
  - 盘古氏为三才首君，通达天地阴阳
  - 天皇氏创制干支名称，用于纪年

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_138]` `[trigger: 干支起源]` `[factor_trigger: ganzhi_origin AND three_sovereigns]` `[role: 主干]` 干犹木之干，强而为阳；支犹木之枝，弱而为阴。天皇氏一姓十三人，始制干支之名，以定岁之所在。 → 《三命通会》卷一#干支起源与天地人三皇
  - 天皇氏以无为而治，风俗自化

- **详细解说**：
  此条阐述干支起源的神话传说。首先从象征层面解释：天干如树之主干，强壮为阳；地支如树之枝条，柔弱为阴。这不仅是形象比喻，更揭示了干支的阴阳属性。在时间起源上，盘古氏开天辟地后，天皇氏一姓十三人继承治理。天皇氏以清静无为之道治世，风俗自然化育，并首创天干地支的名称体系，用于确定年岁位置，这是中国历法纪年系统的开端。

- **校勘与字词辨析（双语）**：
  - **中文**："澹泊"通"淡泊"，清静恬淡之意。"天皇氏一姓十三人"指天皇氏世系传十三代。
  - **English**："澹泊" means tranquil and without desire; "one family name, thirteen rulers" indicates a dynastic succession of thirteen generations under the Celestial Sovereign lineage."""
    normalized_text_zh: str = """"""
    subject: str = "干支起源与天地人三皇"
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
        l1_anchor="smth_v1.0.0_干支起源与天地人三皇_001_L1",
    )
    version: str = "1.0.0"
