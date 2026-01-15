"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.227781
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
    semantic_id="smth_v1.0.0_五行生克总论_001",
    book_id="sanming",
    engine_id="bazi"
)
class 五行生克总论(SemanticEntry):
    """
    - **原文（source_text）**：
  五行相生相克，其理昭然。十干十二支、五运六气、岁月日时，皆自此立，更相为用。在天则为气：寒、暑、燥、湿、风；在地则成形：金、木、水、火、土。形气相感而...
    """
    
    original_text: str = """- **原文（source_text）**：
  五行相生相克，其理昭然。十干十二支、五运六气、岁月日时，皆自此立，更相为用。在天则为气：寒、暑、燥、湿、风；在地则成形：金、木、水、火、土。形气相感而化生万物，此造化生成之大纪也。原其妙用，可谓无穷矣。

- **分字分词释义**：
  - **五行相生相克**：金生水、水生木、木生火、火生土、土生金为相生；金克木、木克土、土克水、水克火、火克金为相克。
  - **十干十二支**：天干地支系统。
  - **五运六气**：五运为五行之运，六气为风寒暑湿燥火六种气候。
  - **形气相感**：有形之质与无形之气互相感应。

- **规范化释义（primary_lang_explained）**：
  五行的相生相克，道理十分明显。天干地支、五运六气、年月日时，都是从这套生克关系建立起来的，彼此相互作用。在天上表现为气候（寒、暑、燥、湿、风），在地上凝结成形质（金、木、水、火、土）。形与气相互感应，从而化生出万物，这就是造化生成的根本纲纪。若要追溯其中的奥妙作用，可以说是无穷无尽的。

- **完整对等诠释（secondary_lang_full）**：
  The Five Elements exhibit mutual generation (metal-water-wood-fire-earth cycle) and mutual restriction (metal restricts wood, wood restricts earth, earth restricts water, water restricts fire, fire restricts metal) as self-evident cosmic principles. The Ten Heavenly Stems, Twelve Earthly Branches, Five Movements, Six Qi, and all temporal divisions (year-month-day-hour) are founded upon this system and mutually interact. In heaven, the Five Elements manifest as qi in five climatic forms (cold, heat, dryness, dampness, wind); on earth, they congeal into five material forms (metal, wood, water, fire, earth). The mutual stimulation between form and qi generates all myriad things, constituting the grand cosmological framework with inexhaustible subtle applications. This Five Elements generation-restriction theory establishes the fundamental logic of destiny calculation, coordinating heaven-earth-human fate through form-qi interplay rather than mechanistic rules.

- **核心要点**：
  - 五行生克是天干地支、五运六气、年月日时的共同基础
  - 在天为气（五种气候），在地为形（五种物质）
  - 形气相感是万物化生的根本机制

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_128]` `[trigger: 五行生克总论]` `[factor_trigger: wuxing_shengke AND xingqi_xianggan]` `[role: 主干]` 五行相生相克，其理昭然。十干十二支、五运六气、岁月日时，皆自此立，更相为用。在天则为气：寒、暑、燥、湿、风；在地则成形：金、木、水、火、土。形气相感而化生万物。 → 《三命通会》卷一#五行生克总论

- **详细解说**：
  本段为全书五行生克理论的总纲。强调五行生克并非孤立的数字游戏，而是贯通天地、连接形气的宇宙运行法则。在天上，五行表现为气候的变化（寒暑燥湿风）；在地上，五行凝结为具体的物质形态（金木水火土）。正是通过形与气的相互感应，才化生出世间万物的千变万化。这套理论不仅用于解释自然现象，更是推算人命吉凶的根本依据。

- **校勘与字词辨析（双语）**：
  - **中文**：原文"其理昭然"，"昭然"意为"明白显著"，强调五行生克之理的自明性与普遍性。
  - **English**：The phrase "其理昭然" (its principle is self-evident) emphasizes the universality and clarity of五行shengke theory as foundational cosmological law."""
    normalized_text_zh: str = """"""
    subject: str = "五行生克总论"
    factor_refs: list = ['source_ref']
    
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
        l1_anchor="smth_v1.0.0_五行生克总论_001_L1",
    )
    version: str = "1.0.0"
