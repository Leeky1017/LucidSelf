"""
Auto-generated semantic module for zipingzhenquan
Generated at: 2025-12-05T13:30:19.523677
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
    semantic_id="zpzq_v1.0.0_五行干支之说_已详论于干支篇_001",
    book_id="zipingzhenquan",
    engine_id="bazi"
)
class 五行干支之说已详论于干支篇(SemanticEntry):
    """
    - **原文（source_text）**：
  五行干支之说，已详论于干支篇。干动而不息，支静而有常。以每干流行于十二支之月，而生旺墓绝系焉。

- 原注（原文注解）：
  　　此段总提“干支、生旺...
    """
    
    original_text: str = """- **原文（source_text）**：
  五行干支之说，已详论于干支篇。干动而不息，支静而有常。以每干流行于十二支之月，而生旺墓绝系焉。

- 原注（原文注解）：
  　　此段总提“干支、生旺墓绝”的关系：天干主“动而不息”，地支主“静而有常”；每一干在十二支中经历长生、旺、墓、绝等阶段，由此建立“阴阳生死”之说。

- 分字分词释义：
  - 干动而不息：天干在天运行，侧重“气机流行”，不停运动。
  - 支静而有常：地支在地定位，侧重“方位承载”，位置稳定，有其常度。
  - 流行于十二支之月：每一天干在十二个月令中依次经历不同状态。
  - 生旺墓绝：长生、帝旺、入墓、绝等旺衰阶段的总称。

- **规范化释义（primary_lang_explained）**：
  关于五行与干支的基本道理，在前面的“干支篇”里已经讲得很详细了。这里再提出一个关键视角：天干在天上运行不停，属于“动”的一面；地支在地上定位不移，属于“静”的一面。正因为每一天干都要在十二地支所代表的十二个月令中轮流“走一圈”，于是才会有“哪里是长生、哪里是旺、哪里是墓、哪里是绝”等问题，这就统称为“生旺墓绝”的系统，也是本篇所谓“阴阳生死”的背景。

- **完整对等诠释（secondary_lang_full）**：  
  This paragraph restates the basic framework of stems and branches as preparation for the doctrine of "yin–yang life and death". The Heavenly Stems represent the moving aspect of qi: they circulate above and never stand still. The Earthly Branches represent fixed positions: they mark stable locations in which that qi is received and stored. Because every stem in turn "walks a full circle" through the twelve branches that stand for the months of the year, its energy passes through distinct phases of emergence, flourishing, storage and exhaustion. Later writers summarise these phases with the terms "birth", "prosperity", "tomb" and "extinction". The point is that what lives and dies here is not the person in a literal sense, but the strength of the stem's qi as it moves through the twelve earthly positions.

- 详细解说：
  - 阴阳生死，不是指字面上的“生死存亡”，而是指气机在十二支中的旺衰循环。
  - 天干看“动中之气”，地支看“静中之位”；两者合起来，才有具体的“何处为生、何处为死”。
  - 生旺墓绝只是刻画气机节律的一套语言，不能被误解成宿命式的“哪支必凶、哪支必吉”。

- 核心要点：
  - 先有“干支之说”，后有“生旺墓绝”；不可本末倒置，只记口诀不明结构。
  - 生旺墓绝是干在支上的气机阶段，不是静态标签，而是动态循环的一部分。

- 应用推演：
  1) 先弄清每一干在十二支中的长生、临官、帝旺、墓、绝等位置。
  2) 再在具体命局中，结合月令与根气，看日主当前处于哪一阶段。
  3) 配合全局生克通关，判断这个“阶段”是否被加重或缓和。

- 反例与边界：
  - 只背“某干在某支为长生/为墓”的表格，而不理解其背后的气机道理，很容易把“生旺墓绝”当作生硬标签使用。

- 小例（示意）：
  - 同为甲日，生于寅为长生、于卯为禄旺、于未为墓；若局中通根有力，则“入墓”不必一概视为凶，而要看是否成为“藏锋蓄势”。

- 校勘与字词辨析：
  - “干动而不息，支静而有常”：各本文字基本一致，今仅以顿号和逗号略作分句，便于阅读。


- **叙事素材（narrative_snippets）**：
  - `[ns_zpzy_157]` `[trigger: 用神变化]` `[factor_trigger: yongshen_fei_yichengbubian AND sui_xingyun_zhuanyi]` `[role: 主干]` 用神非一成不变，随行运而转移。 → 《子平真诠·论用神变化》#变化
  - `[ns_zpzy_158]` `[trigger: 变中有常]` `[factor_trigger: yongshen_sui_bian AND bianzhong_you_changli]` `[role: 主干]` 用神虽变，变中有常理可循。 → 《子平真诠·论用神变化》#常理
  - `[ns_zpzy_159]` `[trigger: 变化时机]` `[factor_trigger: geju_yuyun AND (cheng OR po) AND xucha_yongshen_dongjing]` `[role: 主干]` 格局遇运，或成或破，须察用神动静。 → 《子平真诠·论用神变化》#时机
  - `[ns_zpzy_160]` `[trigger: 变中求稳]` `[factor_trigger: bianhua_zhizhong AND xu_you_dingjian AND buke_suishi_yaobai]` `[role: 主干]` 变化之中须有定见，不可随势摇摆。 → 《子平真诠·论用神变化》#定见
  - `[ns_zpzy_161]` `[trigger: 天干论命]` `[factor_trigger: tiangan_zhuwai AND dizhi_zhunei]` `[role: 主干]` 天干主外，地支主内。 → 《子平真诠》#上卷
  - `[ns_zpzy_162]` `[trigger: 用神为纲]` `[factor_trigger: bazi_yongshen AND zhuanqiu_yueling]` `[role: 主干]` 八字用神，专求月令。 → 《子平真诠》#论用神
  - `[ns_zpzy_163]` `[trigger: 月令司权]` `[factor_trigger: yueling_siquan AND tigang_zhi_fu]` `[role: 主干]` 月令司权，提纲之府。 → 《子平真诠》#论用神
  - `[ns_zpzy_164]` `[trigger: 用神取法]` `[factor_trigger: yongshen_qufa AND yi_yueling_wei_zhu]` `[role: 主干]` 用神取法，以月令为主。 → 《子平真诠》#论用神
  - `[ns_zpzy_165]` `[trigger: 地支暗藏]` `[factor_trigger: dizhi_ancang AND butou_buxian]` `[role: 主干]` 地支暗藏，不透不显。 → 《子平真诠》#上卷
  - `[ns_zpzy_166]` `[trigger: 根深叶茂]` `[factor_trigger: rigan_yougen AND liliang_beizeng]` `[role: 主干]` 日干有根，力量倍增。 → 《子平真诠》#上卷
  - `[ns_zpzy_167]` `[trigger: 格成格破]` `[factor_trigger: (gecheng=true AND result=ji) OR (gepo=true AND result=xiong)]` `[role: 主干]` 格成则吉，格破则凶。 → 《子平真诠》#上卷
  - `[ns_zpzy_168]` `[trigger: 日主强弱]` `[factor_trigger: rizhu_qiangruo AND ding_geju_zhi_ji]` `[role: 主干]` 日主强弱，定格局之基。 → 《子平真诠》#上卷"""
    normalized_text_zh: str = """"""
    subject: str = "五行干支之说，已详论于干支篇"
    factor_refs: list = ['sheng_wang_mu_jue', 'changsheng', 'diwang', 'rumu', 'jue', 'gan_dong_buxi', 'zhi_jing_youchang']
    
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
        book_id="zipingzhenquan",
        chapter="",
        l1_anchor="zpzq_v1.0.0_五行干支之说_已详论于干支篇_001_L1",
    )
    version: str = "1.0.0"
