"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228094
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
    semantic_id="smth_v1.0.0_河图洛书生克之数_001",
    book_id="sanming",
    engine_id="bazi"
)
class 河图洛书生克之数(SemanticEntry):
    """
    - **原文（source_text）**：
  天抵六十甲子，历也。纳音，律也。支干纳音之别也。此天地自然之数。河图生数也。生者左旋，故以中央之土而生西方之金，西方之金而生北方之水，北方之水而生东方...
    """
    
    original_text: str = """- **原文（source_text）**：
  天抵六十甲子，历也。纳音，律也。支干纳音之别也。此天地自然之数。河图生数也。生者左旋，故以中央之土而生西方之金，西方之金而生北方之水，北方之水而生东方之木，东方之木而生南方之火，南方之火而复生中央之土。洛书克数也。克者右转，故以中央之土而克北与西北之水，北与西北之水，而克西与西南之火，西与西南之火而克南与东南之金，南与东南之金而克东与东北之木，东与东北之木，而又克中央之土，无微不通。此纳音之所为妙也，断断乎出自黄帝无疑矣。

- **分字分词释义**：
  - **天抵**：大致、总的来说。
  - **历**：历法。
  - **律**：音律。
  - **支干纳音之别**：地支天干纳音的区别。
  - **天地自然之数**：天地自然的数理。
  - **河图生数**：河图的相生之数。
  - **左旋**：向左旋转。
  - **洛书克数**：洛书的相克之数。
  - **右转**：向右旋转。
  - **无微不通**：无论多细微都通达。

- **规范化释义（primary_lang_explained）**：
  总的来说，六十甲子是历法，纳音是音律，地支天干纳音各有区别。这是天地自然的数理。河图是相生之数。相生的左旋，所以从中央土生西方金，西方金生北方水，北方水生东方木，东方木生南方火，南方火又生中央土。洛书是相克之数。相克的右转，所以从中央土克北方和西北方的水，北方和西北方的水克西方和西南方的火，西方和西南方的火克南方和东南方的金，南方和东南方的金克东方和东北方的木，东方和东北方的木又克中央土，无论多细微都通达。这就是纳音的奥妙，断然是出自黄帝无疑。

- **完整对等诠释（secondary_lang_full）**：
  Generally speaking, Sixty Jiazi is the calendar, Nayin is pitch, Branches-Stems-Nayin each have distinctions. This is Heaven-Earth's natural numbers. Hetu represents generation numbers. Generation rotates leftward, thus Central Earth generates Western Metal, Western Metal generates Northern Water, Northern Water generates Eastern Wood, Eastern Wood generates Southern Fire, Southern Fire returns to generate Central Earth. Luoshu represents restraint numbers. Restraint turns rightward, thus Central Earth restrains Northern and Northwestern Water, Northern and Northwestern Water restrains Western and Southwestern Fire, Western and Southwestern Fire restrains Southern and Southeastern Metal, Southern and Southeastern Metal restrains Eastern and Northeastern Wood, Eastern and Northeastern Wood again restrains Central Earth—penetrating all without exception. This is Nayin's wonder, undoubtedly originating from Yellow Emperor.

- **核心要点**：
  - 六十甲子为历，纳音为律
  - 河图生数左旋：土→金→水→木→火→土
  - 洛书克数右转：土克水→水克火→火克金→金克木→木克土
  - 生克循环，无微不通
  - 纳音妙理出自黄帝

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_171]` `[trigger: 河图洛书生克之数]` `[factor_trigger: hetu_generation AND luoshu_restraint AND five_elements_cycle]` `[role: 主干]` 河图生数也。生者左旋，故以中央之土而生西方之金。洛书克数也。克者右转，故以中央之土而克北与西北之水。无微不通。此纳音之所为妙也。 → 《三命通会》卷一#河图洛书生克之数

- **详细解说**：
  此条总结纳音体系的数理基础——河图洛书。六十甲子代表历法时间，纳音代表音律五行，两者结合形成完整体系。河图代表五行相生（生数），按左旋（逆时针）循环：土生金、金生水、水生木、木生火、火生土。洛书代表五行相克（克数），按右转（顺时针）循环：土克水、水克火、火克金、金克木、木克土。生克两个循环相互交织，"无微不通"，形成复杂精密的纳音体系。最后强调这套体系"断断乎出自黄帝"，确立其权威性和古老性。这是对整个纳音理论的哲学总结。

- **校勘与字词辨析（双语）**：
  - **中文**：河图洛书为上古图式。生数左旋即五行相生顺序，克数右转即五行相克顺序。"天抵"通"大抵"。
  - **English**: Hetu and Luoshu are ancient diagrams; generation numbers rotate left in Five Elements generation order; restraint numbers turn right in Five Elements restraint order; "天抵" means "generally speaking.""""
    normalized_text_zh: str = """"""
    subject: str = "河图洛书生克之数"
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
        l1_anchor="smth_v1.0.0_河图洛书生克之数_001_L1",
    )
    version: str = "1.0.0"
