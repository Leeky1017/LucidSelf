"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.101529
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
    semantic_id="smth_v1.0.0_德秀本义与取位_001",
    book_id="sanming",
    engine_id="bazi"
)
class 德秀本义与取位(SemanticEntry):
    """
    - **原文（source_text）**：
  论德秀。夫德者，本月生旺之德；秀者，合天地中和之气、五行变化而成者也。又曰：德者，阴阳解凶之神；秀者，天地清秀之气，四时当旺之神。故寅午戌月，丙丁为德...
    """
    
    original_text: str = """- **原文（source_text）**：
  论德秀。夫德者，本月生旺之德；秀者，合天地中和之气、五行变化而成者也。又曰：德者，阴阳解凶之神；秀者，天地清秀之气，四时当旺之神。故寅午戌月，丙丁为德，戊癸为秀；申子辰月，壬癸戊己为德，丙辛甲己为秀；巳酉丑月，庚辛为德，乙庚为秀；亥卯未月，甲乙为德，丁壬为秀。凡人命中得此德秀，无破冲克压者，赋性聪明，温厚和气；若遇学堂，更带财官，主贵；冲克减力。

- **分字分词释义**：
  - **德者，本月生旺之德**：指当月本气所生的厚重之德，偏向「稳住局面、解凶成吉」。
  - **秀者，天地清秀之气**：指在当下四时之中和点汇聚而成的清灵之气，偏向「聪慧才华与气质」。
  - **解凶之神 / 当旺之神**：德多主化解、缓和凶煞；秀多主锦上添花，使气机清亮而不浊。
  - **各月德秀组合**：寅午戌月丙丁为德、戊癸为秀；申子辰月壬癸戊己为德、丙辛甲己为秀；巳酉丑月庚辛为德、乙庚为秀；亥卯未月甲乙为德、丁壬为秀。

- **规范化释义（primary_lang_explained）**：
  德秀二字，分别代表命局中的「德性」与「清秀」：德是本月生旺之气所凝成的厚德，能解凶与扶正；秀是天地中和之气、四时当旺之神所化出的清灵之气，常表聪明、气质与才华。作者按照四季、四三合局，将不同月份对应的德星与秀星列出：火旺之寅午戌月，丙丁为德、戊癸为秀；水旺之申子辰月，壬癸戊己为德、丙辛甲己为秀；金旺之巳酉丑月，庚辛为德、乙庚为秀；木旺之亥卯未月，甲乙为德、丁壬为秀。命局中若德秀俱全且不受破冲压制，多主天性聪慧、为人温厚和气；若再遇学堂、财官等吉神配合，则贵气更显。若德秀遭冲克，则力量削弱。

- **完整对等诠释（secondary_lang_full）**：
  The pair Virtue and Beauty, De and Xiu, summarise two inner qualities: Virtue is the thick stabilising goodness arising from the month main qi, and Beauty is the clear elegant qi formed at the seasonal point of balance.
  By listing for each month group which stems count as Virtue and which as Beauty, the text states that charts holding both without heavy affliction tend to produce people who are intelligent, gentle and well mannered.
  In practice these stars refine the tone of a chart rather than overturning its structure and are best treated as modifiers of character and style.
- **核心要点**：
  - 德秀格主要刻画「品性与才华」两方面的内在品质：德重在厚实与解凶，秀重在聪明与清雅。
  - 德秀须与月令、用神与整体格局相配：单有德秀而局中浊煞横生、空亡冲破者，效果有限；反之，清局逢德秀，多能显出一层「润色」与「提纯」。
  - 在工程化分析中，可将德与秀分别建模为「品行修为潜力」与「才华气质潜力」两个维度，并同时考虑其是否受冲克与是否与学堂、贵人等同见，用以解释命主在德行、名誉与才学上的综合表现。

- **详细解说**：
  1) 在历法与局势特征中，根据出生月与三合局，标注当月对应的德星、秀星集合，并检测命局中是否实际出现，形成 `de_star_present`、`xiu_star_present` 标记及其落宫信息；
   2) 为德星和秀星分别计算「不受冲克压制」的有效度，如被重煞冲克、落空亡则降权，得到 `de_effective_score` 与 `xiu_effective_score`；
   3) 将德、秀在性格层面的作用拆分为「品行修为潜力」与「才华气质潜力」，并与学堂、文昌、贵人等结构联合建模，用于解释现实中的「被信任度」「温厚程度」「审美与表达能力」等维度；
   4) 在解释输出时，将德秀更多用于说明「内在质地」与「气质表现」，而不是直接承诺财富或职级的高度。

 - 反例与边界：
   - 不宜因命局有德秀就断定此人必然「品学兼优」，现实中环境、教育与选择同样重要，德秀更多是潜质与倾向；
   - 若局中煞气极重、结构混浊，即便有德秀，其作用往往只是部分缓和，而非完全扭转，需要在模型中体现其有限性；
   - 工程上若把德秀直接视为「高道德评分」或「高声誉评分」，会引入评价偏见，应通过行为数据和声誉数据进行校准；
   - 反向误区是完全舍弃德秀特征，使模型难以区分「同样格局下更温厚清雅」这类细微差异。

 - 小例（示意）：
   - 某命局德秀俱全且落在用神宫位，又与学堂、文昌同见，现实表现为品行端正、学习稳健、气质清雅，在团队中自然承担协调与润滑角色，系统可用「德秀 + 学堂文昌」结构解释其被信赖与被推举的原因；
  - 另一命局仅见偏弱之秀星且被煞克，德星缺位，现实中则表现为才华有时难以驾驭、情绪波动较大，偶有华而不实的倾向，系统在解释时会提示「需要以稳定结构与长期修为来承托其才气」。"""
    normalized_text_zh: str = """"""
    subject: str = "德秀本义与取位"
    factor_refs: list = ['new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_factor_60', 'bazi_semantic', 'bazi_state_factor_137', 'bazi_semantic', 'bazi_function_factor_11', 'bazi_semantic']
    
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
        l1_anchor="smth_v1.0.0_德秀本义与取位_001_L1",
    )
    version: str = "1.0.0"
