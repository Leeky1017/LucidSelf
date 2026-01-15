"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.458188
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
    semantic_id="smth_v1.0.0_官星坐禄为天福_001",
    book_id="sanming",
    engine_id="bazi"
)
class 官星坐禄为天福(SemanticEntry):
    """
    - **原文（source_text）**：
  谓官星坐处，见禄如人，有官有禄，莫非天福。甲生人以辛为官，辛禄在酉，是以甲人见酉，乙人见申之例。甲用辛官，柱有辛酉，更得福神助之，生旺有气为佳。一名禄...
    """
    
    original_text: str = """- **原文（source_text）**：
  谓官星坐处，见禄如人，有官有禄，莫非天福。甲生人以辛为官，辛禄在酉，是以甲人见酉，乙人见申之例。甲用辛官，柱有辛酉，更得福神助之，生旺有气为佳。一名禄干福神，遇者主科名巍峨，官职尊崇，多掌丝纶文翰之美。

- 分字分词释义：
  - **官星坐禄**：官星所临之地支，正好是此官星的禄位，如辛官禄在酉，庚官禄在申，谓之官星坐禄。
  - **天福贵人**：官星与禄并见，如人既有官职又享俸禄，为天所赐之福，故名天福贵人。
  - **禄干福神**：又名禄干福神，指官星自带禄根、福神相助之格局。
  - **丝纶文翰**：丝纶原指皇帝诏命，文翰指文章翰墨，合指掌诏令、制书等清贵文职。

- **规范化释义（primary_lang_explained）**：
  所谓天福贵人，就是官星落在自己的禄位上，如甲木日主以辛金为官，辛金之禄在酉，若命局中见辛酉，则为官星坐禄，有官有禄，福分极厚。乙木日主以庚金为官，庚禄在申，见庚申同理。此格又称禄干福神，若官星生旺有气、再得其他福神扶助，多主科第高登、官职尊崇，适宜从事文书、诏令、典章制度等带有丝纶文翰性质的清要之职。

- **完整对等诠释（secondary_lang_full）**：
  "Heavenly Fortune Noble" describes the situation where the official star sits on its own salary position in the branches, so that both office and stipend are present together as if granted by Heaven. For a Jia day-master, Xin metal is the official and its salary place is You; when the chart shows Xin in You, or for a Yi day-master Geng in Shen, the official star is said to "sit on salary". If such an official is strong and vital and further helped by fortune spirits, the result is someone with both rank and pay who enjoys thick blessings. This configuration is therefore also called the "salary stem with fortune god", and people who meet it are often marked by distinguished examination success and high, honorable office, especially in refined civil posts that handle edicts, documents and written orders—the realm summed up by the phrase "silk decrees and literary papers".


- 核心要点：
  - 关键在于**官星坐自身禄位**：官星不但有根，而且得地，官禄双美。
  - 需配合日主不弱、官星生旺、有福神扶助，方能成其贵气；若官星坐禄而日主太弱，仍有"不能胜任"之虞。
  - 此格偏重文贵与清职，多见科名、翰林、词章之类，不若偏官、七煞格那样重武权与锋锐。

- 校勘与字词辨析：
  - **"甲人见酉，乙人见申"**：是以甲日辛官禄在酉、乙日庚官禄在申为例，余干可按十干禄位表类推。
  - **"禄干福神"**：有的抄本作"禄干福星"，以本书前后文与他书对照，以"福神"更合常见称呼，故从此写。
  - **"丝纶文翰"**：古代专指掌管起草制诏、诰命之高品文臣，现代理解为文职系统中最接近决策核心的一类岗位。
  - **English**：
    - Positions closest to decision-making core.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_05_009]` `[trigger: 天福贵人定义]` `[factor_trigger: tianfu_guiren_presence]` `[role: 主干]` 官星坐处，见禄如人，有官有禄，莫非天福。 → 《三命通会》卷五#天福贵人
  - `[ns_smth_05_010]` `[trigger: 官禄双美]` `[factor_trigger: guan_lu_shuangmei AND guanxing_shengwang_score=high]` `[role: 主干依赖]` 官星不但有根，而且得地，官禄双美。 → 《三命通会》卷五#天福贵人
  - `[ns_smth_05_011]` `[trigger: 福神助力]` `[factor_trigger: fushen_fuzhu_score=high AND rizhu_shengren_score=high]` `[role: 条件分支]` 柱有辛酉，更得福神助之，生旺有气为佳。 → 《三命通会》卷五#天福贵人
  - `[ns_smth_05_012]` `[trigger: 文贵倾向]` `[factor_trigger: wengui_tendency_flag=on]` `[role: 总结]` 遇者主科名巍峨，官职尊崇，多掌丝纶文翰之美。 → 《三命通会》卷五#天福贵人"""
    normalized_text_zh: str = """"""
    subject: str = "官星坐禄为天福"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'tianfu_guiren_presence', 'bazi_semantic', 'guan_lu_shuangmei', 'bazi_semantic', 'guanxing_shengwang_score', 'bazi_semantic', 'fushen_fuzhu_score', 'bazi_semantic', 'rizhu_shengren_score', 'bazi_semantic', 'wengui_tendency_flag', 'bazi_semantic', 'source_ref', 'rel_smth_05_007', 'tianfu_guiren_presence', 'rel_smth_05_008', 'fushen_fuzhu_score', 'rel_smth_05_009', 'wengui_tendency_flag', 'evi_smth_05_007', 'guan_lu_shuangmei', 'rule_tianfu', 'evi_smth_05_008', 'fushen_fuzhu_score', 'rule_fushen', 'evi_smth_05_009', 'wengui_tendency_flag', 'rule_wengui', 'map_smth_05_005', 'map_smth_05_006']
    
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
        l1_anchor="smth_v1.0.0_官星坐禄为天福_001_L1",
    )
    version: str = "1.0.0"
