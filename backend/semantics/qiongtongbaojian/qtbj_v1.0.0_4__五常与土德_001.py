"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.619691
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
    semantic_id="qtbj_v1.0.0_4__五常与土德_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 4五常与土德(SemanticEntry):
    """
    - **原文（source_text）**：
  夫五行之性，各致其用。水者其性智，火者其性礼，木其性仁，金其性义，惟土主信，重宽厚博，无所不容：以之水，即水附之而行；以之木，则木托之而生；金不得土，...
    """
    
    original_text: str = """- **原文（source_text）**：
  夫五行之性，各致其用。水者其性智，火者其性礼，木其性仁，金其性义，惟土主信，重宽厚博，无所不容：以之水，即水附之而行；以之木，则木托之而生；金不得土，则无自出；火不得土，则无自归。必损实以为通，致虚以为明，故五行皆赖土也。

- **分字分词释义**：
  - **性**：本性、天性 / 内在特质 / 五行固有的属性
  - **智**：智慧 / 水之德 / 灵动变通
  - **礼**：礼仪、礼节 / 火之德 / 光明照耀、文明教化
  - **仁**：仁爱 / 木之德 / 生发慈爱
  - **义**：正义、义理 / 金之德 / 决断裁制
  - **信**：信用、诚信 / 土之德 / 厚重承载、言出必行
  - **宽厚博**：宽广、厚实、博大 / 土的包容性 / 承载万物
  - **附之而行**：依附土而流动 / 水的流转需土承载 / 水土关系
  - **托之而生**：依托土而生长 / 木的生长需土培养 / 木土关系
  - **损实以为通**：减损实滞使之通畅 / 调节土的方法 / 疏土的必要性
  - **致虚以为明**：达到虚灵才能明澈 / 土的理想状态 / 虚则灵动

- **规范化释义（primary_lang_explained）**：
  五行的本性，各自发挥其作用。水性主智，火性主礼，木性主仁，金性主义。只有土主信，厚重宽博，无所不包容：水依附土才能流转，木寄托土才能生长，金没有土就无法生出，火没有土就无处归宿。必须减损土的实滞使之通透，达致虚灵才算明澈，所以五行都依赖土。

- **完整对等诠释（secondary_lang_full）**：
  The natures of the Five Elements each have their function. Water corresponds to Wisdom, Fire to Propriety, Wood to Benevolence, and Metal to Righteousness. Only Earth corresponds to Trustworthiness; it is heavy, broad, thick, and vast, containing everything. Water relies on it to flow; Wood relies on it to root and grow; Metal cannot be produced without Earth; Fire cannot return (store) without Earth. One must reduce its solidity to allow flow, and reach emptiness to achieve clarity; thus, all Five Elements depend on Earth.

- **核心要点**：
  - 五常对应：水智、火礼、木仁、金义、土信。
  - 土的核心地位：万物之母，四行皆赖土（载水、培木、生金、藏火）。
  - 土的修炼：忌实滞，贵虚通。

- **详细解说**：
  此段将五行上升到儒家五常（仁义礼智信）。特别强调了土的"载体"功能。土不仅是信，更是平台。最后一句"损实以为通，致虚以为明"是修身也是论命的高阶心法，土太重则滞，需疏通（如木疏土）方能灵动。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_015]` `[trigger: 五常]` `[factor_trigger: wuxing_five_virtues]` `[role: 主干]` 水者其性智，火者其性礼，木其性仁，金其性义，惟土主信。 → 《穷通宝鉴·五行总论》#1.4
  - `[ns_qttbj_016]` `[trigger: 土德]` `[factor_trigger: virtue_trust AND earth_carries_all]` `[role: 主干依赖]` 土重宽厚博，无所不容，五行皆赖土也。 → 《穷通宝鉴·五行总论》#1.4
  - `[ns_qttbj_017]` `[trigger: 土载水]` `[factor_trigger: earth_carries_all AND element_water]` `[role: 主干依赖]` 以之水，即水附之而行。 → 《穷通宝鉴·五行总论》#1.4
  - `[ns_qttbj_018]` `[trigger: 土培木]` `[factor_trigger: earth_carries_all AND element_wood]` `[role: 主干依赖]` 以之木，则木托之而生。 → 《穷通宝鉴·五行总论》#1.4
  - `[ns_qttbj_019]` `[trigger: 土生金]` `[factor_trigger: interaction_generation AND element_earth AND element_metal]` `[role: 主干依赖]` 金不得土，则无自出。 → 《穷通宝鉴·五行总论》#1.4
  - `[ns_qttbj_020]` `[trigger: 土藏火]` `[factor_trigger: earth_carries_all AND element_fire]` `[role: 主干依赖]` 火不得土，则无自归。 → 《穷通宝鉴·五行总论》#1.4
  - `[ns_qttbj_021]` `[trigger: 调土心法]` `[factor_trigger: principle_balance AND earth_variable_nature]` `[role: 总结]` 损实以为通，致虚以为明。 → 《穷通宝鉴·五行总论》#1.4"""
    normalized_text_zh: str = """"""
    subject: str = "4. 五常与土德"
    factor_refs: list = ['wuchang_system', 'virtue_benevolence', 'virtue_righteousness', 'virtue_propriety', 'virtue_wisdom', 'virtue_trust']
    
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
        l1_anchor="qtbj_v1.0.0_4__五常与土德_001_L1",
    )
    version: str = "1.0.0"
