"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.755699
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
    semantic_id="zw_v1.0.0_定小儿生时诀_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 定小儿生时诀(SemanticEntry):
    """
    - 分字分词释义：

  - **定小儿生时**：根据新生儿体貌特征反推出生时辰的传统方法，用于记时不精时的辅助校正。
  - **单顶门**：婴儿头顶仅有一个发旋，对应子午卯酉或寅申巳亥时辰，左偏为...
    """
    
    original_text: str = """- 分字分词释义：

  - **定小儿生时**：根据新生儿体貌特征反推出生时辰的传统方法，用于记时不精时的辅助校正。
  - **单顶门**：婴儿头顶仅有一个发旋，对应子午卯酉或寅申巳亥时辰，左偏为四正时，右偏为四隅时。
  - **双顶**：婴儿头顶有两个发旋，对应辰戌丑未四墓时，象征"胞胎受定正时辰"。
  - **偏左边二三分**：单顶旋涡略偏头部左侧，对应四正时（子午卯酉），暗示阳气外展。
  - **偏居右去**：单顶旋涡偏向头部右侧，对应四隅时（寅申巳亥），暗示气机偏侧。
  - **面向天**：婴儿出生时呈仰卧姿态，对应子午卯酉四正时，象征阳气上达。
  - **侧身眠**：婴儿出生时呈侧卧姿态，对应寅申巳亥四隅时，象征气机偏转。
  - **脸伏地**：婴儿出生时呈俯卧姿态，对应辰戌丑未四墓时，象征气沉入里。
  - **临盆当试用心坚**：提醒接生者或记时者须在临产时细心观察，以便事后校正时辰。

- 原文（断句）：

  定小儿生时诀：

  子午卯酉单顶门，或偏左边二三分。寅申巳亥亦单顶，偏居右去始为真。辰戍丑未是双顶，胞胎受定正时辰。

  又子午卯酉面向天，寅申己亥侧身眠，辰戌丑未脸伏地，临盆当试用心坚。

- 规范化释义（primary_lang_explained）：

  本条提供的是一套以婴儿顶门旋向与出生时卧姿为线索、倒推生时地支的民间口诀。第一段以「单顶门」与「双顶」区分：若为子、午、卯、酉四正时生，则多见单顶旋或偏左二三分；寅、申、巳、亥四隅时生，则多见单顶偏向右侧；辰、戌、丑、未四墓时生，则常见双顶，似乎在说「胞胎受定正时辰」，即胎位与头旋在成形时已锁定在相应时支。

  第二段改从婴儿面向与卧姿着眼：子、午、卯、酉四时，多见面向上天；寅、申、巳、亥时，则多呈侧身而卧；辰、戌、丑、未时，则面部伏向地面。古人希望借此在记时不精、产程混乱之际，凭婴儿出生瞬间的体态特征来反证生时，以便安命排盘。现代使用时，应将此视作一种传统经验性的辅佐线索，而非替代准确时刻记录或医学常识的唯一依据。

- 完整对等诠释（secondary_lang_full）：

  This short formula offers a traditional way to back-calculate an infant's
  birth hour from physical signs. The first verse links the pattern of hair
  whorls on the crown to the twelve earthly branches: a single crown slightly
  to the left is associated with the four cardinal hours (Zi, Wu, Mao, You); a
  single crown leaning to the right with the four corner hours (Yin, Shen, Si,
  Hai); and a double crown with the four grave hours (Chen, Xu, Chou, Wei), as
  if the fetus had already "accepted" its allotted time while still in the
  womb. The second verse shifts to posture at the moment of birth, matching a
  face-up baby to the cardinal hours, a side-lying baby to the corner hours and
  a face-down baby to the grave hours.

  In practice these rules are meant as corrective tools for situations where
  the recorded time of birth is rough or disputed. The practitioner first uses
  crown and posture to narrow the birth to one of the three groups of hours,
  then tests specific charts within that range to see which one fits events and
  temperament best. The method is highly experiential and should supplement,
  not replace, proper timekeeping and medical records.

- 核心要点：

  1. 通过婴儿顶门单顶/双顶与偏向左右，分别对应十二时辰中的正、隅、墓三类时支。
  2. 通过婴儿出生瞬间的面向与卧姿（仰卧、侧卧、俯卧），进一步交叉验证生时所属的三合或四正。
  3. 口诀本质上是一套在记时不精的环境下，用体貌与姿态「反推时辰」的经验法门。
  4. 真正安命仍应优先依据尽可能准确的时刻记录，此类口诀只可作参考，不宜孤立使用。
  5. 在实际操作中，须结合其他生理与环境线索，并回看命局整体是否与所推生时相符，避免机械硬套。

- 叙事素材（narrative_snippets）：

  - **头旋定时**："顶门单顶双顶与偏向左右，对应正隅墓三类时支"，以头旋推时辰。
  - **卧姿验证**："仰卧对应正时，侧卧对应隅时，俯卧对应墓时"，以卧姿交叉验证。
  - **经验法门**：本诀是记时不精时代的"反推时辰"经验法，现代应以准确记录为主。
  - **现代应用**：可作为时辰存疑时的辅助参考，但需结合命局整体验证，不宜机械硬套。"""
    normalized_text_zh: str = """"""
    subject: str = "定小儿生时诀"
    factor_refs: list = ['type_dandingmen', 'type_shuangding', 'group_sizheng', 'group_siyu', 'group_simu', 'source_ref', 'rel_shengshi_001', 'type_dandingmen', 'rel_shengshi_002', 'type_dandingmen', 'rel_shengshi_003', 'type_shuangding', 'evi_shengshi_001', 'type_dandingmen', 'rule_shengshi_sizheng', 'evi_shengshi_002', 'type_shuangding', 'rule_shengshi_simu', 'concept_birth_time', 'concept_body_sign']
    
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
        book_id="ziwei",
        chapter="",
        l1_anchor="zw_v1.0.0_定小儿生时诀_001_L1",
    )
    version: str = "1.0.0"
