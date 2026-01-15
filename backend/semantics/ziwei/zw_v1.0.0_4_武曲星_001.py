"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.725538
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
    semantic_id="zw_v1.0.0_4_武曲星_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 4武曲星(SemanticEntry):
    """
    - 原文（source_text）：

  问：武曲星所主若何？

  答曰：武曲北斗第六星，属金，乃财帛宫，主财，与天府同宫有寿，其施权于十二宫，分其临地有庙旺陷宫，主于人性切果决，有喜有怒，可福可...
    """
    
    original_text: str = """- 原文（source_text）：

  问：武曲星所主若何？

  答曰：武曲北斗第六星，属金，乃财帛宫，主财，与天府同宫有寿，其施权于十二宫，分其临地有庙旺陷宫，主于人性切果决，有喜有怒，可福可灾。若耗囚会于震宫，必为破祖，淹晋之辈与。禄马交驰，发财于远郡；若贪狼同度，悭吝之人；破军同财，乡财到手而成空。诸凶聚而作祸，吉集以成祥。

- 分字分词释义：

  - **武曲**：北斗第六星，五行属金，专司财帛田宅，是命盘中主管财富权力的核心星曜。
  - **北斗第六星**：属北斗星系第六位，在斗数中地位仅次于紫微，为财星之首。
  - **财帛宫主财**：武曲为财帛宫的主星，主管一切与金钱、资产、收入相关的事务。
  - **性切果决**：性情刚烈果断，做事不拖泥带水，有决断力但也有暴躁倾向。
  - **有喜有怒，可福可灾**：情绪起伏明显，顺境则大喜，逆境则大怒；配合吉凶而成祸福。
  - **耗囚会于震宫**：耗星与囚星同聚于震宫（寅卯位），主消耗破败、祖业难守。
  - **淹晋**：仕途淹滞、功名不进，或泛指事业受阻之人。
  - **禄马交驰**：禄存与天马同会，象征因远行、异地经商或外派而得财。
  - **发财于远郡**：在外地或远方发展能获得财富，宜离乡求财。
  - **贪狼同度**：武曲与贪狼同宫同度，主人悭吝、算计、小气。
  - **悭吝**：吝啬小气，对钱财斤斤计较。
  - **破军同财**：武曲与破军同居财帛宫或同度，财来财去难聚守。
  - **乡财到手而成空**：财富到手后很快消散，难以积累。

- 核心要点：

  1. **武曲主财**：北斗第六星，属金，主财帛田宅。
  2. **性刚果决**：性切果决，有喜有怒，可福可灾。
  3. **禄马交驰**：会禄马则发财远郡，宜远方求财。
  4. **贪狼同度**：若贪狼同度则悭吝，少年不利。
  5. **七杀火星**：同宫则因财被劫，需有制化。

- 规范化释义（primary_lang_explained）：

  武曲为北斗第六星，五行属金，专司财帛田宅，是命盘中的财星核心。武曲之人性情刚强果决，有喜有怒，可福可灾，全看配合吉凶而定。若与禄存、天马同会，则"禄马交驰"，主发财于远郡，宜远方经营求财。若与贪狼同度，则主悭吝之性，少年不利。若破军同居财帛宫，则财来财去，难以聚守。若七杀、火星同宫，则易因财被劫，需有吉星制化方可化解。总体而言，武曲之吉凶全看是否得禄马吉曜之助，还是受贪破杀星之制。

- 完整对等诠释（secondary_lang_full）：

  Wuqu, the sixth star of the Northern Dipper, belongs to Metal and governs the Wealth Palace. It presides over financial capacity, assets, and the power to acquire and manage money. Its nature is firm, decisive, capable of both blessing and disaster depending on configuration. When Wuqu shares space with Lucun and Tianma ("Lu-and-Horse galloping together"), wealth comes through distant ventures, foreign trade, or relocation. When joined by Tanlang, the native tends toward miserliness and calculating behavior, with youth often marked by difficulty. When Pojun shares the Wealth sector, money arrives only to slip away. When Qisha and Fire Star converge with Wuqu, the native risks robbery, high-stakes gambling, or violent loss connected to money. Overall, Wuqu charts must be read through the lens of whether the fiscal star is supported by auspicious factors or besieged by draining and confining influences.

- 叙事素材（narrative_snippets）：

  - **武曲主财**："武曲北斗第六星，属金，乃财帛宫主财"，武曲为命盘中的财星核心。
  - **性刚果决**："性切果决，有喜有怒，可福可灾"，武曲性情刚强果断。
  - **禄马交驰**："禄马交驰，发财于远郡"，武曲会禄马宜远方求财。
  - **贪狼悭吝**："贪狼同度，悭吝之人"，武贪同度主吝啬。
  - **现代应用**：武曲可作为评估"财帛能力"的核心指标，需关注其配合（禄马吉、贪破凶）。"""
    normalized_text_zh: str = """"""
    subject: str = "4 武曲星"
    factor_refs: list = ['star_wuqu', 'role_caibo_zhu', 'combo_luma_jiaochi', 'combo_haoqiu', 'combo_wutan', 'combo_wusha_huo']
    
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
        l1_anchor="zw_v1.0.0_4_武曲星_001_L1",
    )
    version: str = "1.0.0"
