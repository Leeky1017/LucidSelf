"""
Auto-generated semantic module for zipingzhenquan
Generated at: 2025-12-05T13:30:19.523691
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
    semantic_id="zpzq_v1.0.0_阳主聚_以进为进_阴主散_以退为退_001",
    book_id="zipingzhenquan",
    engine_id="bazi"
)
class 阳主聚以进为进阴主散以退为退(SemanticEntry):
    """
    - **原文（source_text）**：
  阳主聚，以进为进，故主顺；阴主散，以退为退，故主逆。此生沐浴等项，所以有阳顺阴逆之殊也。四时之运，功成者去，等用者进，故每流行于十二支之月，而生旺墓绝...
    """
    
    original_text: str = """- **原文（source_text）**：
  阳主聚，以进为进，故主顺；阴主散，以退为退，故主逆。此生沐浴等项，所以有阳顺阴逆之殊也。四时之运，功成者去，等用者进，故每流行于十二支之月，而生旺墓绝，又有一定。阳之所生，即阴之所死；彼此互换，自然之运也。即以甲乙论，甲为木之阳，木之枝枝叶叶，受天生气，既收藏饱足，可以为来克发泄之机，此其所以生于亥也。木当午月，正枝叶繁盛之候，而甲何以死？却不是外虽繁盛，而内之生气发泄已尽，此其所以死于午也。乙木反是，午月枝叶繁盛，即为之生；亥月枝叶剥落，即为之死。以质而论，自与气殊也。以甲乙为例，余可知矣。

- 原注（原文注解）：
  　　此段从“阳主聚、阴主散”讲起，说明为什么阳干的长生等位在顺行、阴干则在逆行，由是引出“阳顺阴逆”的序列。再以甲乙为例，说明同是木，甲以“气”为主，乙以“质”为主，因此在午亥两地的“生与死”恰好相反。

- 分字分词释义：
  - 阳主聚：阳气有向外聚合、向前推进之性。
  - 以进为进，故主顺：以“向前推进”的方向为进，所以其长生等位顺行排列。
  - 阴主散：阴气有收敛、散解、回撤之性。
  - 以退为退，故主逆：以“回撤”的方向为进，所以在十二支中是逆行排列。
  - 阳顺阴逆：阳干按地支顺行定长生等位，阴干按地支逆行定长生等位。
  - 功成者去，等用者进：四时运转中，功用既尽的气退出，新一轮气机接替进入。
  - 甲为木之阳，木之枝枝叶叶：甲偏在木的外在枝叶、生发表现。
  - 受天生气，既收藏饱足，可以为来克发泄之机：枝叶饱满之后，反而有被“克去外张之气”的需求。
  - 生于亥、死于午：对甲木而言，亥为长生，午为死地。
  - 乙木反是：乙以“形质”为主，午月旺、生于午、死于亥。

- **规范化释义（primary_lang_explained）**：
  阳气的特征是向前聚合、推进，所以在看阳干的长生、沐浴、冠带等位时，是按地支顺着排过去；阴气的特征是回收、散解，所以阴干的长生等位则是按地支逆着排回来，这就是常说的“阳顺阴逆”。四季运行的原则是：功用完成的气退下去，新的气补上来，所以每一个天干在十二支中都有固定的“生旺墓绝”，并且阳干与阴干的次第并不相同。以甲乙为例：甲是木的阳面，偏在枝叶的外张生发，当它在亥水这一步开始长生，等到午火时外张已极，枝叶繁盛，看似最旺，其实内部生气已经发泄殆尽，因此视为“死地”；乙木则恰好相反，它偏在形质与实木，本身需要火来助成其质，所以在午月反而视为“生”，到了亥水枝叶凋零、形质剥落，反而为“死”。同样是木，因为一偏“气”、一偏“质”，所以长生与死地在午、亥之间刚好倒置。

- **完整对等诠释（secondary_lang_full）**：  
  This section explains why the life-cycle of the stems is counted forward for yang stems but backward for yin stems, and illustrates it with the pair Jia Wood and Yi Wood. Yang qi tends to gather and press forward, so when we mark the stages of a yang stem – birth, bathing, coronet, assuming office, peak power and so on – we assign them by running through the branches in the same direction as the seasonal flow. Yin qi tends to withdraw and return, so for yin stems the same labels are assigned by running the twelve branches in reverse. For Jia, which stands for the outward, leafy expression of Wood, life begins when the hidden water at Hai first awakens the sap; by the time the calendar reaches Wu, at the height of summer, the foliage is externally luxuriant but the inner generative force has already been spent, so Wu is counted as Jia's "death" position. Yi, which emphasises the solid body and form of Wood, tells a different story: it needs fire to ripen and harden its substance, so the fiery fullness of Wu is treated as its birth, while the bleak, water-soaked state symbolised by Hai – when branches strip away and form collapses – is taken as its death. Even within one element, then, the yin and yang sides reach their peak and their exhaustion at opposite points in the cycle. The life-and-death labels track the condition of the underlying qi, not simply the surface greenness or barrenness.

- 详细解说：
  - “阳顺阴逆”并非死记的口诀，而是根源于“阳主聚进、阴主散退”的气机特性。
  - 同行之内，阴阳侧面不同，长生与死地的位置也会不同，不能想当然地用一套表去套所有干。
  - 从甲乙的对比可知：判断生死旺衰，不能只看外表旺衰（枝叶繁盛与否），更要看内部气机是否尚有余力。

- 核心要点：
  - 阳干：长生等位顺行；阴干：长生等位逆行。
  - 甲木：重在气与枝叶，亥为生、午为死；乙木：重在质与形体，午为生、亥为死。
  - 判断“生死”，必须联系阴阳与“气/质”的不同侧面，不能仅看表面时令。

- 应用推演：
  1) 对每一干，先区分阴阳，再按“阳顺阴逆”标出长生等位。
  2) 分析该干在局中偏重“气”还是“质”，再看其在当前支位到底是“已发泄”还是“方成形”。
  3) 在判断身强身弱时，把“表面旺（外张）”与“内里旺（根气足）”区分开来。

- 反例与边界：
  - 见午就说“木旺”，不分甲乙，不看其长生死墓的不同，是对本段精神的违背。
  - 只按“阳顺阴逆”机械顺排或逆排，而不结合具体干、具体行，容易死板。

- 小例（示意）：
  - 甲日生午月，看似木火通明；若无根、无水，又行火土运，多属“枝叶外张而根枯”的象。
  - 乙日生午月，有辰未等湿土载之，反而是枝叶得光、质成器。

- 校勘与字词辨析：
  - “阳主聚，以进为进，故主顺；阴主散，以退为退，故主逆”：今依语气加分号与逗号，以示阴阳两段对举。


- **叙事素材（narrative_snippets）**：
  - `[ns_zpzy_169]` `[trigger: 纯杂之辨]` `[factor_trigger: yongshen_yi_chun AND buyi_za AND za_ze_lifen_ersan]` `[role: 主干]` 用神宜纯不宜杂，杂则力分而散。 → 《子平真诠·论用神纯杂》#纯杂
  - `[ns_zpzy_170]` `[trigger: 杂而能制]` `[factor_trigger: za_er_neng_zhi AND yi_ke_chengge]` `[role: 主干]` 杂而能制，亦可成格。 → 《子平真诠·论用神纯杂》#制杂
  - `[ns_zpzy_171]` `[trigger: 杂中取纯]` `[factor_trigger: zazhong_yike_quchun AND xucha_shili_qingzhong]` `[role: 主干]` 杂中亦可取纯，须察势力之轻重。 → 《子平真诠·论用神纯杂》#取纯
  - `[ns_zpzy_172]` `[trigger: 纯杂得宜]` `[factor_trigger: (chun_er_bupian=weishang) OR (za_er_youzhi=yike_yong)]` `[role: 主干]` 纯而不偏为上，杂而有制亦可用。 → 《子平真诠·论用神纯杂》#得宜
  - `[ns_zpzy_173]` `[trigger: 地支藏干]` `[factor_trigger: dizhi_canggan AND anzhong_quyong]` `[role: 主干]` 地支藏干，暗中取用。 → 《子平真诠》#上卷
  - `[ns_zpzy_174]` `[trigger: 用神为纲]` `[factor_trigger: bazi_yongshen AND zhuanqiu_yueling]` `[role: 主干]` 八字用神，专求月令。 → 《子平真诠》#论用神
  - `[ns_zpzy_175]` `[trigger: 月令司权]` `[factor_trigger: yueling_siquan AND tigang_zhi_fu]` `[role: 主干]` 月令司权，提纲之府。 → 《子平真诠》#论用神
  - `[ns_zpzy_176]` `[trigger: 用神取法]` `[factor_trigger: yongshen_qufa AND yi_yueling_wei_zhu]` `[role: 主干]` 用神取法，以月令为主。 → 《子平真诠》#论用神
  - `[ns_zpzy_177]` `[trigger: 无根飘浮]` `[factor_trigger: rigan_wugen AND xufu_wuli]` `[role: 主干]` 日干无根，虚浮无力。 → 《子平真诠》#上卷
  - `[ns_zpzy_178]` `[trigger: 得令当权]` `[factor_trigger: yueling_deling AND qishi_qiangsheng]` `[role: 主干]` 月令得令，气势强盛。 → 《子平真诠》#上卷
  - `[ns_zpzy_179]` `[trigger: 用神有力]` `[factor_trigger: yongshen_youli AND result=fugui_keqi]` `[role: 主干]` 用神有力，富贵可期。 → 《子平真诠》#上卷
  - `[ns_zpzy_180]` `[trigger: 月令当权]` `[factor_trigger: yueling_dangquan AND yongshen_zhi_fu]` `[role: 主干]` 月令当权，用神之府。 → 《子平真诠》#上卷"""
    normalized_text_zh: str = """"""
    subject: str = "阳主聚，以进为进；阴主散，以退为退"
    factor_refs: list = ['yang_shun_yin_ni', 'yang_zhu_ju', 'yin_zhu_san', 'gongcheng_zhe_qu', 'dengyong_zhe_jin', 'jia_sheng_hai', 'jia_si_wu', 'yi_sheng_wu']
    
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
        l1_anchor="zpzq_v1.0.0_阳主聚_以进为进_阴主散_以退为退_001_L1",
    )
    version: str = "1.0.0"
