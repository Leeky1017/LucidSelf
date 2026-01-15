"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228159
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
    semantic_id="smth_v1.0.0_桑柘木与松柏木_001",
    book_id="sanming",
    engine_id="bazi"
)
class 桑柘木与松柏木(SemanticEntry):
    """
    - **原文（source_text）**：
  壬子癸丑，何以取象桑柘木？盖气居盘屈，形状未伸，居于水地，蚕衰之月，桑柘受气，取其时之生也。庚寅辛卯，则气已乘阳，得栽培之势力，其为状也，柰居金下，凡...
    """
    
    original_text: str = """- **原文（source_text）**：
  壬子癸丑，何以取象桑柘木？盖气居盘屈，形状未伸，居于水地，蚕衰之月，桑柘受气，取其时之生也。庚寅辛卯，则气已乘阳，得栽培之势力，其为状也，柰居金下，凡金与霜素坚，木居下得其旺，岁寒后凋，取其性之坚也，故曰松柏木。

- **分字分词释义**：
  - **桑柘木**：桑树和柘树。
  - **气居盘屈**：气处在盘曲屈折状态。
  - **形状未伸**：形状还未伸展。
  - **蚕衰之月**：蚕将衰落的月份（指冬季）。
  - **受气**：接受生气。
  - **取其时之生**：取其时令的生发。
  - **气已乘阳**：气已经乘着阳气。
  - **栽培之势力**：栽培的力量。
  - **柰居金下**：却处在金克之下。
  - **金与霜素坚**：金属和霜冻本来坚硬。
  - **岁寒后凋**：严寒之后才凋零。
  - **取其性之坚**：取其性质的坚韧。

- **规范化释义（primary_lang_explained）**：
  壬子癸丑，为什么取象为桑柘木？因为气处在盘曲屈折状态，形状还未伸展，处在水地，蚕将衰落的月份，桑柘树接受生气，取其时令的生发。庚寅辛卯，气已经乘着阳气，得到栽培的力量，其形状却处在金克之下，凡是金属和霜冻本来坚硬，木在下面反而得其旺盛，严寒之后才凋零，取其性质的坚韧，所以叫松柏木。

- **完整对等诠释（secondary_lang_full）**：
  Renzi-Guichou, why symbolize Mulberry-Cudrania Wood? Because qi dwells in coiled and bent state, form not yet extended, residing in Water ground, silkworm-waning months, Mulberry-Cudrania receive qi, taking their seasonal generation. Gengyin-Xinmao: qi already riding yang, gaining cultivation's force, yet their condition is beneath Metal—whenever Metal and frost are inherently firm, Wood beneath actually gains prosperity, withering only after year's cold passes, taking their nature's resilience, thus called Pine-Cypress Wood.

- **核心要点**：
  - 壬子癸丑：桑柘木（气居盘屈，蚕衰之月）
  - 庚寅辛卯：松柏木（岁寒后凋，性质坚韧）
  - 桑柘木处水地，形未伸
  - 松柏木耐寒霜，坚韧不凋

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_179]` `[trigger: 桑柘木与松柏木]` `[factor_trigger: mulberry_cudrania_wood AND pine_cypress_wood AND nayin_wood_resilience]` `[role: 主干]` 壬子癸丑，何以取象桑柘木？盖气居盘屈，形状未伸，居于水地，取其时之生也。庚寅辛卯，岁寒后凋，取其性之坚也，故曰松柏木。 → 《三命通会》卷一#桑柘木与松柏木

- **详细解说**：
  此条开始解释木纳音。壬子癸丑为"桑柘木"：子丑属冬季水旺之地，木气盘曲未伸展，正是养蚕时节桑柘树（桑树和柘树）接受生气的时候，取其时令的生发之意。这是木的初生阶段，柔弱盘曲。庚寅辛卯为"松柏木"：寅卯本是木旺之地，得阳气和栽培之力，但天干庚辛属金，木处金克之下，反而如松柏般坚韧——金霜虽坚但松柏更强，"岁寒知松柏之后凋"，取其坚韧不屈之性。从桑柘木（柔弱盘曲）到松柏木（坚韧耐寒），体现了木从初生到坚强的转变。

- **校勘与字词辨析（双语）**：
  - **中文**："桑柘木"，桑树供养蚕，柘树也是桑科植物。"蚕衰之月"指冬季。"柰"通"奈"，表示却、反而。"岁寒后凋"出自《论语》，形容松柏坚贞。
  - **English**: "Mulberry-Cudrania Wood"—mulberry feeds silkworms, cudrania is also Moraceae family. "Silkworm-waning months" refers to winter. "Nai" means "yet" or "however." "Withering after year's cold" from Analects, describing pine-cypress integrity."""
    normalized_text_zh: str = """"""
    subject: str = "桑柘木与松柏木"
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
        l1_anchor="smth_v1.0.0_桑柘木与松柏木_001_L1",
    )
    version: str = "1.0.0"
