"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.101258
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
    semantic_id="smth_v1.0.0_甲禄寅_001",
    book_id="sanming",
    engine_id="bazi"
)
class 甲禄寅(SemanticEntry):
    """
    - **原文（source_text）**：
  甲禄寅。如甲见丙寅，甲见丙寅，克丙为财，为福星禄；戊寅火土相生，为伏马禄，俱吉。庚寅，谓之破禄，半吉半凶。壬寅，谓之正禄，带截路空亡，必为僧道。甲寅，...
    """
    
    original_text: str = """- **原文（source_text）**：
  甲禄寅。如甲见丙寅，甲见丙寅，克丙为财，为福星禄；戊寅火土相生，为伏马禄，俱吉。庚寅，谓之破禄，半吉半凶。壬寅，谓之正禄，带截路空亡，必为僧道。甲寅，谓之长生禄，大吉。

- **分字分词释义**：
  - **福星禄**：禄位上兼得财星相生，多主富裕与福厚。
  - **伏马禄**：禄中带驿马，主流动中得禄，奔波而有成。
  - **破禄**：禄上见克制或矛盾之神，禄力被损，吉凶参半。
  - **截路空亡**：与空亡、截路并见，多主禄位有缺口，易走异途，如僧道之路。

- **规范化释义（primary_lang_explained）**：
  甲木的禄在寅。若命中甲日干见丙寅，则甲克丙为财，寅为禄地，财禄并临，被称为「福星禄」，多主福厚而有财。若见戊寅，火土相生，寅中兼有驿马之象，为「伏马禄」，主奔走中得禄，宜动不宜静。若见庚寅，金克甲木，称「破禄」，禄位受损，吉凶参半。壬寅为「正禄」但带截路空亡，多主走出常规之路，如出家、清修等。甲寅则为「长生禄」，甲木得寅为长生，禄根深厚，大吉。

- **完整对等诠释（secondary_lang_full）**：
  Jia Wood has its Lu in the branch Yin. When Jia meets Bing-Yin, Jia controls Bing as wealth while standing on its own Lu position, so this is called the "Fortune-Star Lu" and usually signals blessings and material support.
  When Jia is joined with Wu-Yin, Fire and Earth generate one another and the Horse star is present, forming the "Crouching-Horse Lu" that points to gaining benefits through movement and travel. Meeting Geng-Yin is called "Broken Lu": Metal cuts Wood and the power of Lu is damaged, so the outcome is mixed.
  Ren-Yin is the "Proper Lu" but carries the configuration known as "Cut-Path Void", meaning that the ordinary worldly road is blocked and the person is inclined to walk an unusual path, traditionally compared to leaving home for religious life. Jia-Yin itself is the "Longevity Lu"; Jia Wood is in its growth phase in Yin, the Lu root is deep and strong, and the configuration is highly auspicious.
- **核心要点**：
  - 判断甲禄寅时，不仅看有无禄支，还要看禄支上坐何干、藏何神，决定禄之性质：财禄、马禄、破禄等。
  - 「截路空亡」等结构提示：纵有禄位，若路径不畅，往往不走常规职业路线，在现代可类比为非典型职业、出世路线。
  - 工程建模时，可将「禄 + 财」视作资源富集、「禄 + 马」视作流动性高、「破禄」视作不稳定标签，用于细化职业与路径预测。

- **详细解说**：
  1) 判盘时，先确认日主是否为甲木，再检查命局中是否出现寅支：日坐寅为「坐禄」，他柱寅为「见禄」；
  2) 若寅支上透丙、戊、庚、壬、甲等不同天干，则按原文分类为福星禄、伏马禄、破禄、正禄、长生禄，并在系统中特征化编码（如 `lu_type=FUXING/FUMA/PO/MAIN/CHANGSHENG`）；
  3) 将不同禄型与行业、生活方式标签关联：福星禄偏重「稳中有财」、伏马禄偏重「奔波中得」、破禄偏「高波动」、正禄/长生禄偏「稳长线」；
  4) 行运推演中，当流年或大运再度触发寅位或相关天干时，提高与晋升、出行、转轨相关事件的概率，但需区分不同禄型的风险收益比。

- 反例与边界：
  - 不可将「壬寅必为僧道」机械照搬到现代环境，系统应将其理解为「路径非典型、易走非主流」的结构，而非字面职业；
  - 不宜认为「破禄」就必然一生贫困或无成，更合理的解释是：发展路径起伏大、需要承担更多不确定性；
  - 工程上若把 `lu_type` 直接映射为「成功/失败」二元标签，会放大误差，应只作为影响趋势的中层特征；
  - 反向误区是忽视「马」象对于空间流动的提示，把一切奔波简单视为坏事，而不看到其中的成长空间。

- 小例（示意）：
  - 某甲日命，日坐寅，年柱丙寅，系统可标记为「坐禄 + 福星禄」，在职业推荐中偏向「有稳定组织、又能在组织内获取实在回报」的路径，如大机构内部的业务拓展，而不必强行创业；
  - 另一甲日命，命中仅见庚寅一支，且行运多逢金水，系统则提示其「禄位受制、路径高波动」，适合通过阶段性项目、自由职业等形式吸收这种不稳定性，而不是过度追求单一铁饭碗。"""
    normalized_text_zh: str = """"""
    subject: str = "甲禄寅"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_jia_yin', 'bazi_semantic', 'bazi_state_marker_1', 'bazi_semantic', 'bazi_state_yima_marker', 'bazi_semantic', 'bazi_state_marker_2', 'bazi_semantic']
    
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
        l1_anchor="smth_v1.0.0_甲禄寅_001_L1",
    )
    version: str = "1.0.0"
