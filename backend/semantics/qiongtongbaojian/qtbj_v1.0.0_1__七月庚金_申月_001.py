"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.578339
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
    semantic_id="qtbj_v1.0.0_1__七月庚金_申月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 1七月庚金申月(SemanticEntry):
    """
    - **原文（source_text）**：
  七月庚金，刚锐极矣。专用丁火煅炼，次取甲木引丁，故曰：秋金锐锐最为奇，壬癸相逢总不宜，如逢木火来成局，试看福寿与天齐。
  如得丁甲两透，定步青云。若...
    """
    
    original_text: str = """- **原文（source_text）**：
  七月庚金，刚锐极矣。专用丁火煅炼，次取甲木引丁，故曰：秋金锐锐最为奇，壬癸相逢总不宜，如逢木火来成局，试看福寿与天齐。
  如得丁甲两透，定步青云。若有丁无甲为俊秀。有甲无丁是平人。丁甲两无无用物，只堪门下作闲人。
  或支成水局，乏丁用丙，柱中即有丙火，不见甲木者，必主愚懦。何也？当时金水两旺，金生水以制火，何能发达。或见甲出引丁，可云生监。甲弱者、衣食充盈。
  或支成土局，先甲后丁。支成火局，富贵中人。金刚木明，行商坐贾之人。金备申酉戌之地，富贵无疑。金神入火乡，逢羊刃，富贵荣华。

- **分字分词释义**：
  - **刚锐极矣**：刚硬锐利到极点 / 申月庚金当令 / 身强
  - **煅炼**：锻炼加工 / 丁火炼金 / 用神作用
  - **秋金锐锐**：秋金锋利 / 当权得令 / 诗诀
  - **壬癸不宜**：水不适宜 / 金生水泄气 / 忌讳
  - **木火成局**：木火合力 / 财官配合 / 吉象
  - **步青云**：平步青云 / 仕途顺利 / 贵格
  - **俊秀**：才华出众 / 有丁无甲 / 中贵
  - **平人**：普通人 / 有甲无丁 / 平格
  - **门下闲人**：无用之人 / 丁甲两无 / 下格
  - **生监**：监生 / 国子监学生 / 中等功名
  - **金刚木明**：金强木显 / 身财两停 / 商贾之命

- **规范化释义（primary_lang_explained）**：
  七月（申月）的庚金，刚硬锐利到了极点（当令得势）。专门用丁火锻炼，其次取甲木引出丁火，所以说："秋金锐锐最为奇，壬癸相逢总不宜，如逢木火来成局，试看福寿与天齐。"
  如果得到丁火甲木两透，必定平步青云。若有丁无甲为俊秀。有甲无丁是平人。丁甲两无是无用之物，只堪在门下作闲人。
  如果地支合成水局，缺丁火而用丙火，柱中即使有丙火，不见甲木者，必主愚懦。为什么？因为当时金水两旺，金生水以制火，怎能发达。如见甲木透出引丁，可说是监生。甲木弱者，衣食充盈。
  如果地支合成土局，先甲后丁。地支合成火局，富贵中人。金刚木明，行商坐贾之人。金备申酉戌之地（西方全金），富贵无疑。金神入火乡，逢羊刃，富贵荣华。

- **完整对等诠释（secondary_lang_full）**：
  Geng Metal in the 7th Month (Monkey Month): Extremely hard and sharp. Exclusively use Ding Fire to temper; next take Jia Wood to draw Ding. The poem says: "Autumn Metal sharp and keen is most marvelous, Ren/Gui encountering is always unsuitable, if meeting Wood/Fire forming pattern, see how fortune and longevity match Heaven."
  If Ding and Jia both reveal, one surely rises to high clouds. With Ding but no Jia, talented and elegant. With Jia but no Ding, an ordinary person. Without both Ding and Jia, a useless thing, only fit to idle under someone's gate.
  If branches form Water Frame, lacking Ding use Bing. Even if Bing Fire is present but no Jia Wood, one is certainly timid and weak. Why? Because at this time Metal and Water are both prosperous, Metal generating Water to control Fire, how can one prosper?
  If branches form Earth Frame, first Jia then Ding. If branches form Fire Frame, a wealthy and noble person. Metal hard Wood bright, a merchant trader. Metal complete in Shen-You-Xu territory, wealth and nobility certain.

- **核心要点**：
  - **首要用神**：丁火（煅炼）。秋金刚锐，必须丁炼方能成器。
  - **配合**：甲木（引丁）。甲木生火，引出丁火之用。
  - **忌讳**：壬癸水（泄金）。秋金喜炼不喜泄。
  - **格局配置**：丁甲两透为上，有一为中，两无为下。

- **详细解说**：
  - 申月庚金建禄，气势最旺。
  - 旺金须炼，丁火为炉火，能炼顽金成器。
  - 甲木引丁：甲木生火，使丁火有源而持久。
  - "金神入火乡"：金旺见火运，反成大器。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_350]` `[trigger: 庚生申月]` `[factor_trigger: month_shen AND tiangan_geng AND tiangan_ding AND tiangan_jia]` `[role: 主干]` 七月庚金，刚锐极矣，专用丁火煅炼，次取甲木引丁。 → 《穷通宝鉴·三秋庚金》#32.1
  - `[ns_qttbj_351]` `[trigger: 丁甲两透]` `[factor_trigger: month_shen AND tiangan_geng AND ding_revealed AND jia_revealed]` `[role: 条件分支]` 如得丁甲两透，定步青云。 → 《穷通宝鉴·三秋庚金》#32.1
  - `[ns_qttbj_352]` `[trigger: 有丁无甲]` `[factor_trigger: month_shen AND tiangan_geng AND ding_revealed AND NOT jia_revealed]` `[role: 条件分支]` 若有丁无甲为俊秀。 → 《穷通宝鉴·三秋庚金》#32.1
  - `[ns_qttbj_353]` `[trigger: 丁甲两无]` `[factor_trigger: month_shen AND tiangan_geng AND NOT ding_revealed AND NOT jia_revealed]` `[role: 例外处理]` 丁甲两无无用物，只堪门下作闲人。 → 《穷通宝鉴·三秋庚金》#32.1
  - `[ns_qttbj_354]` `[trigger: 金神入火乡]` `[factor_trigger: tiangan_geng AND metal_prosperous AND fire_luck AND yangren]` `[role: 条件分支]` 金神入火乡，逢羊刃，富贵荣华。 → 《穷通宝鉴·三秋庚金》#32.1"""
    normalized_text_zh: str = """"""
    subject: str = "1. 七月庚金（申月）"
    factor_refs: list = ['metal_sharpness', 'tempering_metal', 'drawing_ding', 'metal_fire_luck']
    
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
        book_id="qiongtongbaojian",
        chapter="",
        l1_anchor="qtbj_v1.0.0_1__七月庚金_申月_001_L1",
    )
    version: str = "1.0.0"
