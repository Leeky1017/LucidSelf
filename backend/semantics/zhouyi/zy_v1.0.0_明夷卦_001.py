"""
Auto-generated semantic module for zhouyi
Generated at: 2025-12-05T13:30:19.919274
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
    semantic_id="zy_v1.0.0_明夷卦_001",
    book_id="zhouyi",
    engine_id="yijing"
)
class 明夷卦(SemanticEntry):
    """
    - **原文（source_text）**：

  【卦辞】
  明夷：利艰贞。

  【彖传】
  《彖》曰：明入地中，明夷。内文明而外柔顺，以蒙大难，文王以之。“利艰贞”，晦其明也；内难而能正其志...
    """
    
    original_text: str = """- **原文（source_text）**：

  【卦辞】
  明夷：利艰贞。

  【彖传】
  《彖》曰：明入地中，明夷。内文明而外柔顺，以蒙大难，文王以之。“利艰贞”，晦其明也；内难而能正其志，箕子以之。

  【象传】
  《象》曰：明入地中，明夷；君子以莅众，用晦而明。

  【爻辞】
  初九，明夷于飞，垂其翼；君子于行，三日不食。有攸往，主人有言。
  六二，明夷，夷于左股；用拯马壮，吉。
  九三，明夷于南狩，得其大首，不可疾贞。
  六四，入于左腹，获明夷之心，于出门庭。
  六五，箕子之明夷，利贞。
  上六，不明晦；初登于天，后入于地。

- 分字分词释义：

  - **明夷**：明，为光明；夷，有伤、损之意。明夷即“光明受伤”“文明受创”。
  - **利艰贞**：在艰难中守正才有利，强调“明在困境中更须守道”。
  - **明入地中**：光明藏入地底，比喻贤者或正道被压抑、不见其光。
  - **内文明而外柔顺**：内在有文明之德，外在示人以柔顺，以承受大难。
  - **晦其明**：刻意收敛光明，不轻易显露锋芒，以保全自身与道统。
  - **用晦而明**：在表面上显得晦暗、退隐，实则是另一种守明之方式。
  - **于飞，垂其翼**：本可飞扬，却垂翼而行，象征主动收敛锋芒。
  - **夷于左股 / 入于左腹**：从外在受伤到深入腹地，象征亲身感受明夷之难，并寻求其内在意义。
  - **箕子之明夷**：以箕子自喻，指在亡国之难下仍守其明而不失节。

- **规范化释义（primary_lang_explained）**：

  明夷卦讲的是“光明在黑暗时代如何自处”。卦辞说：“明夷：利艰贞。”——在光明受伤、黑暗当道之时，只有在艰难中坚守正道才有利；若只求安逸或逞一时之勇，反会灭明。

  彖传以“明入地中”定全卦大象：光明不再高悬，而是沉入大地深处，外表看似昏暗无光，内里却仍有文明与柔顺之德。“内文明而外柔顺，以蒙大难，文王以之”指文王在囚禁中，外表柔顺以承大难，内心文明不灭；“利艰贞，晦其明也；内难而能正其志，箕子以之”则以箕子为例，说明在内外交困之境，晦明、守志才是真正的“利”。

  象传“君子以莅众，用晦而明”把这一结构应用到治理层面：当时代不容光明直露，君子治理众人时不以锐气示之，而是以“晦”藏明，避免锋芒过露反遭毁伤。

- **完整对等诠释（secondary_lang_full）**：

  The Hexagram Ming Yi (Darkening of the Light) depicts a time when brightness is forced underground. Fire sinks beneath the earth, symbolizing talent, virtue, or clarity being suppressed by adverse conditions. The Judgment "Darkening of the Light: favorable to persist in hardship" teaches that when the age does not allow direct radiance, the wise preserve the light by dimming its surface expression, accepting outer difficulty in order to keep inner integrity intact. Rather than burning out in futile confrontation, one shelters the flame until a more fitting time.

- 核心要点：

  - 明夷的核心是**“在晦暗中守住光明，而不是逞一时之亮”**。
  - “利艰贞”强调：困难是试验明德的场域，守正才是唯一有利的选择。
  - 文王与箕子的两种明夷，分别展示“外柔内明”与“晦明守志”的典型路径。

- 详细解说：

  卦象为上地下火：地上无光，火入地中，是光明被覆盖的图景。与晋卦“明出地上”相对，晋是光明升出、受人看见；明夷则是光明被打压、不得不下潜。

  初九“明夷于飞，垂其翼；君子于行，三日不食。有攸往，主人有言”描写的是初入明夷之境的君子：本可以高飞，但因局势不利而垂翼低飞，甚至三日未食；若此时仍勉强有所往，则必遭责言，提醒切勿逞强。六二“明夷，夷于左股；用拯马壮，吉”则是从身体受创与拯救入手：左股受伤，仍需努力拯救“马壮”，象征在受损之中仍要拯救有用之才与资源。

  九三“明夷于南狩，得其大首，不可疾贞”展示的是在外处事的君子：身处狩猎之时，虽得大首，亦不可急于定贞或行动过速，以免因胜而失道。六四“入于左腹，获明夷之心，于出门庭”则转向内在：进入腹地，体会到明夷之真正用意，再走出门庭，带着对黑暗局势的深刻理解而行事。

  六五“箕子之明夷，利贞”把箕子作为典型：在极端艰难中，以沉默、装疯等方式“晦其明”，实则守其贞；上六“不明晦；初登于天，后入于地”则描述从极盛之光到彻底昏暗的过程，提醒人们警惕从“过度高调”到“全然沉没”的剧烈反差。


- **校勘与字词辨析（双语）**：
- **叙事素材（narrative_snippets）**：
  - `[ns_zhouyi_326]` `[trigger: 卦=明夷 AND 卦辞=利艰贞]` `[factor_trigger: zhouyi_gua_mingyi AND zhouyi_guaci AND zhouyi_qingshe_fengxian]` `[role: 主干]` 明夷，利艰贞：光明受伤之时，宜坚守艰难之正道。 → 《周易·明夷卦·卦辞》
  - `[ns_zhouyi_327]` `[trigger: 卦=明夷 AND 彖传]` `[factor_trigger: zhouyi_gua_mingyi AND zhouyi_tuan AND zhouyi_mingshang_chengdu]` `[role: 主干依赖]` 明入地中。内文明而外柔顺。 → 《周易·明夷卦·彖传》
  - `[ns_zhouyi_328]` `[trigger: 卦=明夷 AND 象传=明入地中]` `[factor_trigger: zhouyi_gua_mingyi AND zhouyi_xiang]` `[role: 主干依赖]` 明入地中，明夷；君子以莉众，用晦而明：韬光养晦以治众。 → 《周易·明夷卦·象传》
  - `[ns_zhouyi_329]` `[trigger: 卦=明夷 AND 初九=明夷于飞]` `[factor_trigger: zhouyi_gua_mingyi]` `[role: 条件分支]` 明夷于飞，垂其翼：光明受伤，如飞鸟垂翼。 → 《周易·明夷卦·爻辞》
  - `[ns_zhouyi_330]` `[trigger: 卦=明夷 AND 六二=明夷夷于左股]` `[factor_trigger: zhouyi_gua_mingyi]` `[role: 条件分支]` 明夷，夷于左股：伤及左股，仍可行走。 → 《周易·明夷卦·爻辞》
  - `[ns_zhouyi_331]` `[trigger: 卦=明夷 AND 九三=明夷于南狩]` `[factor_trigger: zhouyi_gua_mingyi]` `[role: 条件分支]` 明夷于南狩，得其大首：南征而获大收。 → 《周易·明夷卦·爻辞》
  - `[ns_zhouyi_332]` `[trigger: 卦=明夷 AND 六四=入于左腹]` `[factor_trigger: zhouyi_gua_mingyi]` `[role: 主干依赖]` 入于左腹，获明夷之心：深入腹地，知其伤心之由。 → 《周易·明夷卦·爻辞》
  - `[ns_zhouyi_333]` `[trigger: 卦=明夷 AND 六五=箕子之明夷]` `[factor_trigger: zhouyi_gua_mingyi]` `[role: 主干依赖]` 箕子之明夷，利贞：如箕子韬光，守正而利。 → 《周易·明夷卦·爻辞》
  - `[ns_zhouyi_334]` `[trigger: 卦=明夷 AND 上六=不明晦]` `[factor_trigger: zhouyi_gua_mingyi]` `[role: 总结]` 不明晦，初登于天，后入于地：先明后暗，由盛转衰。 → 《周易·明夷卦·爻辞》
  - **中文**：
  - 卦辞"明夷：利艰贞"依通行王弼本；"明夷"谓光明受伤，离日入于坤地之下。
  - "明入地中"谓离火入坤土之中，日落地下，象征光明隐没、处境艰难。
  - "用晦而明"谓君子在暗世中以韬晦为手段，而内心保持光明，不失其正。
  - "文王以之""箕子以之"引周文王与商末箕子为典范，皆处明夷之世而能守正避祸。
  - "明夷于飞，垂其翼"以受伤飞鸟为喻，垂翼而行，不敢高飞。
  - "初登于天，后入于地"描写由盛转衰之轨迹，先极盛而后沉沦。
  - **English**: Based on Wang Bi commentary edition. "明夷" means brightness injured. King Wen and Jizi are historical exemplars. "用晦而明" means using obscurity to preserve inner light. "垂其翼" depicts wounded bird imagery."""
    normalized_text_zh: str = """"""
    subject: str = "明夷卦（䷣）"
    factor_refs: list = ['zhouyi_gua_036', 'method_dimming_light_proposal', 'principle_bright_through_darkness_proposal', 'exemplar_jizi_darkening_proposal', 'principle_benefit_hardship_proposal']
    
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
        book_id="zhouyi",
        chapter="",
        l1_anchor="zy_v1.0.0_明夷卦_001_L1",
    )
    version: str = "1.0.0"
