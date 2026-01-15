"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.101448
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
    semantic_id="smth_v1.0.0_天德与月德本义与取位_001",
    book_id="sanming",
    engine_id="bazi"
)
class 天德与月德本义与取位(SemanticEntry):
    """
    - **原文（source_text）**：
  论天月德。夫德者，利物济人、掩凶作善之谓也。天德者，谓周天有三百六十五度二十五分半：除十二宫分野，每宫各占三十度，共计三百六十度，外有五度二十五分半，...
    """
    
    original_text: str = """- **原文（source_text）**：
  论天月德。夫德者，利物济人、掩凶作善之谓也。天德者，谓周天有三百六十五度二十五分半：除十二宫分野，每宫各占三十度，共计三百六十度，外有五度二十五分半，散在十二佐宫甲、庚、丙、壬、乙、辛、丁、癸、乾、坤、艮、巽，谓之神藏煞没。每宫各得四十四分，所以子午卯酉中有甲庚丙壬，辰戌丑未中有乙辛丁癸，寅申巳亥中有乾坤艮巽，此十二位宫能回凶作善，乃曰天德也。月德者，乃三合所照之方、日月会合之辰：申子辰会酉出，庚入垣于壬；亥卯未会乾出，丙入垣于甲；寅午戌会卯出，甲入垣于丙；巳酉丑会子出，壬入垣于庚。故壬、甲、丙、癸谓之月德，而辰、未、戌、丑四月，天德亦同属焉。

- **分字分词释义**：
  - **德者利物济人、掩凶作善**：德的核心是化恶为善、护佑众生。
  - **天德**：按周天度数分配于十二佐宫的福德之辰，能回凶作善。
  - **月德**：依三合局与日月会合位置确定的德星，亦能化解部分凶煞。

- **规范化释义（primary_lang_explained）**：
  天德、月德都是用来「转凶为吉」的福德之神。天德从天象布局出发：将周天 365 度余数分配于十二佐宫，从而在子午卯酉、辰戌丑未、寅申巳亥各宫安置不同的德星；月德则从三合与日月会合的角度划分，在申子辰、亥卯未、寅午戌、巳酉丑四局各自对应特定干位，由此形成壬甲丙癸为月德之说。在特定月份，天德与月德可以同宫出现，增强其化煞之力。

- **完整对等诠释（secondary_lang_full）**：
  Heaven Virtue and Moon Virtue are both virtue stars whose defining function is to benefit beings and turn harsh indications into milder outcomes.
  Heaven Virtue is derived from the distribution of the remaining celestial degrees into twelve auxiliary palaces, while Moon Virtue comes from the directions illuminated by the triad bureaux and the Sun Moon meeting points.
  Together they mark sectors where severe indications can be softened, so they are best modelled as strong mitigation factors on existing afflictions rather than as direct wealth or status indicators.
- **核心要点**：
  - 天德偏重「天象所赐」的福德，月德偏重「日月会合」所带来的柔和之光，两者合临时效果最好。
  - 在系统建模中，可将天德、月德视为对凶煞权重的折扣因子，并允许两者叠加产生更大的缓冲效果。

- **详细解说**：
  1) 在历法与节气模块中预先计算出每个年份、月份所对应的天德、月德位置，并以表格形式供命盘计算调用；
  2) 在生成命局特征时，根据出生年、月、日、时所属的宫位，标注命盘中是否同时落在天德、月德所在宫，形成 `tian_de_flag`、`yue_de_flag` 及其叠加标记；
  3) 对于落在德星宫位的凶煞（如劫煞、官符、网罗类神煞），在风险评分时按一定比例下调其权重，将「有名无实」的可能性反映到模型输出中；
  4) 在解释层，将天德、月德主要用于说明「为何命盘多煞而现实仍然能守住底线」这类现象，而不是直接提升财富或地位的预测值。

- 反例与边界：
  - 不宜把天德、月德视为可以「彻底抹去一切凶象」的绝对吉神，在现实中多表现为风险被减轻、事件被软化，而非完全消失；
  - 若命局本身凶煞极重、结构高度失衡，仅凭一两个德星就断定「一生安逸无祸」，会与现实经验严重不符；
  - 工程上若简单使用「有德/无德」二值特征，而不考虑德星所落宫位、所临十神及是否受克制，会导致德星效果被高估或失真；
  - 反向误区是完全忽略德星，只统计凶煞总量，使模型难以解释「同样多煞却有人较为平顺」的差异。

- 小例（示意）：
  - 某命局官煞重重，却恰好日支、月支同见天德、月德，现实中虽多有压力与波折，但总能逢凶化吉、关头有人相助，系统可用「德星折减风险」来解释这种「高压但不至极端」的轨迹；
  - 另一命局仅有一星月德且落在边缘宫位，命局又见多重刑冲合网，现实中仍发生过严重事故，系统则将月德视为仅提供部分缓冲，而不会据此否认既有创伤经历。"""
    normalized_text_zh: str = """"""
    subject: str = "天德与月德本义与取位"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_factor_50', 'bazi_semantic', 'bazi_structure_factor_51', 'bazi_semantic', 'bazi_function_factor_2', 'bazi_semantic', 'bazi_state_marker_14', 'bazi_semantic']
    
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
        l1_anchor="smth_v1.0.0_天德与月德本义与取位_001_L1",
    )
    version: str = "1.0.0"
