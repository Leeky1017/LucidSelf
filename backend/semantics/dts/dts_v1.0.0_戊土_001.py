"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:19.008947
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
    semantic_id="dts_v1.0.0_戊土_001",
    book_id="dts",
    engine_id="bazi"
)
class 戊土(SemanticEntry):
    """
    - 原文（source_text）：
  戊土固重，既中且正，静翕动辟，万物司命，水旺物生，火燥喜润，若在坤艮，怕冲宜静。

- 原注（原文注解）：
  　　戊为山冈之土，非城墙之谓，较己土特高厚刚燥...
    """
    
    original_text: str = """- 原文（source_text）：
  戊土固重，既中且正，静翕动辟，万物司命，水旺物生，火燥喜润，若在坤艮，怕冲宜静。

- 原注（原文注解）：
  　　戊为山冈之土，非城墙之谓，较己土特高厚刚燥，乃己土之发源地也，得乎中气，而且正，大春夏则气辟而生万物，秋冬则气翕而成万物，故为司命，其气属阳，喜润下恶燥，坐寅怕申，坐申怕寅，盖冲则根动，非地道之正也，故宜静。

- 分字分词释义：
  - 戊：阳土，山冈之土，厚重刚燥。
  - 固重：稳固厚重，如山岳之势。
  - 中正：居中而正，不偏不倚，为五行之中枢。
  - 静翕动辟：静时收藏（翕），动时开辟（辟），随季节呼吸吐纳。
  - 万物司命：主宰万物生成，为造化之枢纽。
  - 水旺物生：得水滋润则生机盎然。
  - 火燥喜润：火多燥烈时需水润调候。
  - 坤艮：坤为西南（未申），艮为东北（丑寅），皆土之本位。
  - 怕冲宜静：坐本位而逢冲则根基动摇，宜安静守正。

- 规范化释义（primary_lang_explained）：
  戊土如山冈大地，厚重稳固，居五行之中枢，为万物生成之根基。其特点在于"中正司命"：春夏开辟以生万物，秋冬收翕以成万物，一呼一吸间主宰造化节律。戊土虽属阳刚，却喜水润而恶火燥——水旺则生机蓬勃，火烈则干燥枯竭。若戊土坐于坤艮本位（如丑未寅申等土地），最忌逢冲，因冲则根基动摇、地道失正，故宜安静守成，不可妄动。

- **次语种完整诠释（secondary_lang_full）**：  
  Wu Earth is the image of mountain ridges and highland soil—solid, heavy, and central. Unlike Ji Earth which is soft field soil, Wu represents the elevated source from which Ji derives. Its nature is "central and upright" (Zhong Qie Zheng): in spring and summer, it opens up (Pi) to give birth to all things; in autumn and winter, it contracts (Xi) to complete and store them. This breathing rhythm makes Wu the "commander of myriad things" (Wanwu Siming)—the pivot around which creation cycles. Although yang in nature, Wu Earth thrives with water's moisture and suffers from fire's dryness: when water is abundant, life flourishes on its surface; when fire is excessive, it becomes parched and barren. The critical caution concerns positional stability: when Wu sits in its home quarters (Kun direction in southwest or Gen direction in northeast), it must avoid being clashed by opposing branches. Clash destabilizes the root, violating the earth's principle of stillness and proper foundation. Therefore, the prescription for Wu Earth is "fear clash, favor quietude" (Pa Chong Yi Jing)—maintain stability rather than seeking constant movement.

- **核心要点**：
  - 戊为阳土，如山冈大地，厚重刚燥
  - 中正之位：居五行中枢，不偏不倚
  - 静翕动辟：随季节呼吸，春夏开辟生物，秋冬收翕成物
  - 万物司命：为造化之枢纽，主宰生成节律
  - 水旺物生：得水滋润则生机盎然
  - 火燥喜润：火多燥烈需水润调候
  - 怕冲宜静：坐本位逢冲则根基动摇，宜守正安静

- **详细解说**：
  戊土为阳土之代表，如山冈高地，厚重稳固而刚燥。与己土的"卑湿柔顺"形成对照，戊土的精髓在于"中正司命"——居于五行中央，为万物生成之根基与枢纽。春夏之时戊土"气辟"而开放生育，秋冬之时戊土"气翕"而收藏成就，这种呼吸吐纳的节律使其成为"万物司命"。判断戊土命局时，关键看水火调候：水旺则土润而生机蓬勃，火烈则土燥而需水润。另一要点是位置稳定性：戊土若坐于坤艮本位（丑未寅申等），最忌逢冲，因为"冲则根动，非地道之正"。实占时，戊土日主宜安静守成，不可妄动躁进，方能发挥其厚载万物的本质功能。

- **narrative_snippets（叙事片段）**：
  - `[ns_dts_037]` `[trigger: 日主=戊土]` `[factor_trigger: tiangan_wu]` `[role: 主干]` 戊土如山冈大地，厚重中正，为万物司命之枢纽. → 《滴天髓·天干论》#戊土
  - `[ns_dts_038]` `[trigger: 戊土见水旺]` `[factor_trigger: wu_tu_water_moisture]` `[role: 主干依赖]` 戊土得水滋润则生机盎然，水旺物生之理. → 《滴天髓·天干论》#戊土
  - `[ns_dts_039]` `[trigger: 戊土见火燥]` `[factor_trigger: wu_tu_fire_dryness]` `[role: 条件分支]` 戊土火多燥烈需水润调候，否则干枯失养. → 《滴天髓·天干论》#戊土
  - `[ns_dts_121]` `[trigger: 戊土坐本位逢冲]` `[factor_trigger: wu_tu_clash_risk]` `[role: 例外处理]` 戊土坐坤艮本位逢冲则根基动摇，宜静不宜动. → 《滴天髓·天干论》#戊土
  - `[ns_dts_122]` `[trigger: 静翽动辟]` `[role: 总结]` 戊土随季节呼吸：春夏开辟生物，秋冬收翕成物. → 《滴天髓·天干论》#戊土"""
    normalized_text_zh: str = """"""
    subject: str = "戊土"
    factor_refs: list = ['wu_guzhong', 'tiangan_wu_zhong_zheng', 'new_candidate', 'wu_wanwu_siming', 'wu_shuiwang_sheng', 'wu_pachong_yijing']
    
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
        book_id="dts",
        chapter="",
        l1_anchor="dts_v1.0.0_戊土_001_L1",
    )
    version: str = "1.0.0"
