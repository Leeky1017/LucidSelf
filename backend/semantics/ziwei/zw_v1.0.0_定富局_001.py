"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.778591
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
    semantic_id="zw_v1.0.0_定富局_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 定富局(SemanticEntry):
    """
    - 原文（source_text）：

  财荫夹印，相守命武梁来夹是也。田宅宫亦然。日月夹财，武守命日月来夹也，财帛宫亦然是。财禄夹马，马守命武禄来夹，是也。逢生旺尤妙。荫印拱身，身临田宅，梁相拱冲...
    """
    
    original_text: str = """- 原文（source_text）：

  财荫夹印，相守命武梁来夹是也。田宅宫亦然。日月夹财，武守命日月来夹也，财帛宫亦然是。财禄夹马，马守命武禄来夹，是也。逢生旺尤妙。荫印拱身，身临田宅，梁相拱冲是也。勿坐空亡。日月照璧，日月隋田宅宫是也。喜居墓库。金灿光辉，太阳单守，命在午宫，是也。

- 分字分词释义：
  - **财荫夹印**：以武曲为财星、天梁为荫星，左右夹拱天相及命宫或田宅宫，形成"财星+荫星"护持之局。
  - **日月夹财**：太阳与太阴分处命宫/财帛宫两侧，夹拱守命之武曲，主光明显达之财。
  - **财禄夹马**：武曲与禄存在命宫两侧夹拱天马，象征财源随动、多方奔走而来。
  - **荫印拱身**：天梁、天相在田宅宫与身宫之间拱照，身临田宅，如有长辈庇护与不动产依托。
  - **日月照璧**："璧"指田宅墓库宫，如璧玉之环，喻封闭而可守之财库，日月照临则库满而不腐。
  - **金灿光辉**：太阳居午宫单守命宫，如烈日当空，象征明显、公开且带荣耀感的财富。

- 规范化释义（primary_lang_explained）：

  本条把紫微斗数中常见的富贵格局，归纳为若干"财星+荫星+宫位"的组合：其一，以武曲、天梁、天相夹拱命宫或田宅宫，使财星与庇荫之星共同守护财库与不动产；其二，以日月夹武曲守命或财帛宫，让光明显达之气汇聚于财星之上，更利公开职业与品牌型财富；其三，以武曲、禄存夹天马，使财富随人事往来与地域流动而滚动累积；其四，以天梁、天相拱照身宫与田宅宫，再辅以日月照临墓库，使身家与家业都能得到稳定庇护与长期储蓄；其五，以太阳午宫单守命宫，形成"金灿光辉"之局，主一生名利炽盛、财源显著。总体而言，这些富格都强调财星强而有根、财库稳而不失流动，并以荫星与吉曜加持，使财富既可积累又能承载家族与事业的发展。

- 完整对等诠释（secondary_lang_full）：

  This section summarizes a cluster of wealth configurations in Ziwei Doushu, all built from specific combinations of wealth stars, protective stars and key houses. First, "Wealth‑Shelter Flanking‑Seal" places Wuqu (the main wealth star) and Tianliang (the sheltering star) on the two sides of Tianxiang and the Life or Property House, forming a pattern where wealth and protection jointly guard the native and the estate. Second, "Sun‑Moon Flanking‑Wealth" sets the Sun and Moon on either side of Wuqu at the Life or Wealth House, so that luminous authority flows toward the wealth star. Third, "Wealth‑Salary Flanking‑Horse" has Wuqu and Lucun flanking Tianma, indicating resources that move with travel, mobility and commercial circulation. Fourth, "Shelter‑Seal Arching‑Body" lets Tianliang and Tianxiang arch between the Property and Body houses, while "Sun‑Moon Illuminating‑Wall" lets the Sun and Moon shine onto the tomb‑repository houses, depicting a stable property base and intergenerational accumulation. Finally, "Gold‑Brilliant‑Radiance" describes Taiyang alone in Wu Palace guarding the Life House, symbolizing highly visible, honor‑laden wealth. Taken together, these formations point to a shared logic: wealth must have strong stars with roots, a solid storehouse in Property and Wealth houses, and supporting benefic stars to protect and regulate its flow; only then can riches be both substantial and sustainable across a lifetime.

- 核心要点：
  - 以武曲、禄存等财星为轴，用日月、天梁、天相等吉曜形成夹拱照冲。
  - 重视田宅宫、财帛宫与身命宫之间的三角结构，构成"人—财—库"的闭环。
  - 财富既要有流动性（天马、夹命），又要有沉淀处（墓库、田宅）。
  - 荫星与吉曜决定财富是"可享、可守、可传"还是"暴发易散"。

- 详细解说：

  定富局并非只看单一财星之强弱，而是看财星所处的空间关系与配星结构。财荫夹印强调"财星+荫星"双重防护，使命主不但有赚钱能力，也有长辈庇荫与制度保障；日月夹财则把日月之光汇聚到武曲身上，更适合公开职业、品牌型财富；财禄夹马象征靠流通、贸易、远行而致富，若天马落在迁移宫或事业宫，更见奔波换来的报酬；荫印拱身与日月照璧，则把重点放在田宅与身宫，偏重不动产、家业与长期稳健的财库经营；金灿光辉则是以太阳午宫为主轴，重在个人能见度与名望所带来的财源。实务解盘时，需结合本命盘与大限流年的星曜四化，看这些富格是否成局、是否被冲破，才能判断是"有格不成"还是"富格得用"。

- 校勘与字词辨析（双语）：
  - **中文**："财荫夹印"一语，各本或作"财荫印夹"，本书从便于理解之顺序，仍作"财荫夹印"；"照璧"之"璧"指田宅墓库宫，如璧玉之环，喻封闭而可守之财库。
  - **English**: The term "Wealth‑Shelter Flanking‑Seal" renders *cai yin jia yin*—wealth star and sheltering star flanking the Life or Property house. "Illuminating‑Wall" translates *zhao bi*, likening the Property and repository houses to a jade disc that stores value within a closed boundary.

- 叙事素材（narrative_snippets）：

  - **财荫夹印：稳中有财**：武曲为财、天梁为荫，夹拱命宫或田宅宫，常见有人脉、有靠山、有家业的稳健富局。
  - **日月夹财：带光的收入**：日月夹武曲守命或财帛，多主公开职业、品牌与头衔带来的“体面钱”。
  - **财禄夹马：跑出来的财**：武曲、禄存夹天马，像拖着行李满天下跑的人，忙碌却能越跑越有。
  - **荫印拱身：家业护身**：天梁、天相拱身宫与田宅，往往靠房产、家族资产托起一生底气。
  - **日月照璧：库满而不腐**：日月照临墓库与田宅，如灯照金库，适合做长期、不急于兑现的财富布局。
  - **金灿光辉：光靠自己也能富**：太阳午宫单守命宫，即便没有太多外援，也能凭能见度、能力与声望走出一条富路。"""
    normalized_text_zh: str = """"""
    subject: str = "定富局"
    factor_refs: list = ['combo_caiyinjiayin', 'combo_riyuejiacai', 'combo_cailujiama', 'combo_yinyingongshen', 'combo_riyuezhaopi', 'combo_jincanguanghui', 'source_ref', 'rel_fuju_001', 'fuge_xingyao', 'rel_fuju_002', 'caifu_gongwei', 'rel_fuju_003', 'liudong_jilei', 'evi_fuju_001', 'combo_caiyinjiayin', 'rule_caiyinjiayin', 'evi_fuju_002', 'combo_jincanguanghui', 'rule_jincanguanghui', 'concept_wealth_structure', 'concept_flanking', 'concept_flow_accumulate']
    
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
        l1_anchor="zw_v1.0.0_定富局_001_L1",
    )
    version: str = "1.0.0"
