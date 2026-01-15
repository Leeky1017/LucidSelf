"""
Auto-generated semantic module for zipingzhenquan
Generated at: 2025-12-05T13:30:19.523816
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
    semantic_id="zpzq_v1.0.0_是故十干不论月令休囚_只要四柱有根_001",
    book_id="zipingzhenquan",
    engine_id="bazi"
)
class 是故十干不论月令休囚只要四柱有根(SemanticEntry):
    """
    - **原文（source_text）**：
  是故十干不论月令休囚，只要四柱有根，便能受财官食神而当伤官七煞。长生禄旺，根之重者也；墓库余气，根之轻者也。得一比肩，不如得支中一墓库，如甲逢未、丙逢...
    """
    
    original_text: str = """- **原文（source_text）**：
  是故十干不论月令休囚，只要四柱有根，便能受财官食神而当伤官七煞。长生禄旺，根之重者也；墓库余气，根之轻者也。得一比肩，不如得支中一墓库，如甲逢未、丙逢戌之类。乙逢戌、丁逢丑、不作此论，以戌中无藏木，丑中无藏火也。得二比肩，不如得一余气，如乙逢辰、丁逢未之类。得三比肩，不如得一长生禄刃，如甲逢亥子寅卯之类。阴长生不作此论，如乙逢午、丁逢酉之类，然亦为明根，比得一余气。盖比劫如朋友之相扶，通根如室家之可住；干多不如根重，理固然也。

- 原注（原文注解）：
  　　此段承前提出"四柱有根"的核心判断标准，明确根气轻重次序（长生禄旺>墓库余气>比肩），以甲乙丙丁为例说明通根的具体判定规则，强调"通根如室家可住"而"比劫如朋友相扶"的本质区别，为身强身弱判断提供精确量化工具。

- 分字分词释义：
  - 是故十干不论月令休囚：所以，无论天干在月令中是旺是衰。
  - 只要四柱有根：只要在年月日时四柱的地支中有根气。
  - 便能受财官食神而当伤官七煞：就能承受财官食神的吉力，抵挡伤官七煞的凶力。
  - 长生禄旺，根之重者也：长生、禄位、帝旺，是根气中最重的。
  - 墓库余气，根之轻者也：墓库、余气（如辰戌丑未中的藏干），是根气中较轻的。
  - 得一比肩，不如得支中一墓库：得到一个比肩（天干），不如得到地支中一个墓库。
  - 如甲逢未、丙逢戌之类：例如甲木遇到未土（木之墓库）、丙火遇到戌土（火之墓库）。
  - 乙逢戌、丁逢丑、不作此论：乙木遇戌、丁火遇丑，不能算作墓库通根。
  - 以戌中无藏木，丑中无藏火也：因为戌土中不藏木，丑土中不藏火。
  - 得二比肩，不如得一余气：得到两个比肩，不如得到一个余气根。
  - 如乙逢辰、丁逢未之类：例如乙木遇到辰土（辰中藏乙木余气）、丁火遇到未土（未中藏丁火余气）。
  - 得三比肩，不如得一长生禄刃：得到三个比肩，不如得到一个长生、禄位或羊刃。
  - 如甲逢亥子寅卯之类：例如甲木遇到亥（长生）、子（沐浴）、寅（禄）、卯（帝旺/羊刃）。
  - 阴长生不作此论：阴干的长生不能这样论（因为阴干长生理论有争议）。
  - 如乙逢午、丁逢酉之类：例如乙木长生在午、丁火长生在酉（按阴干逆行长生表）。
  - 然亦为明根，比得一余气：但这些也算是明确的根气，相当于一个余气根。
  - 盖比劫如朋友之相扶：因为比劫就像朋友的扶持。
  - 通根如室家之可住：通根就像有自己的房屋可以居住。
  - 干多不如根重，理固然也：天干多不如地支根重，这是当然的道理。

- 核心要点：
  - **根气重于比劫**：得一墓库胜过一比肩，得一余气胜过二比肩，得一长生禄刃胜过三比肩。
  - **通根即是力量**：比劫如朋友相扶，通根如有室家可住，本质不同。
  - **根气有轻重之分**：长生禄旺>墓库余气>无根；阴干长生不如阳干，但也算明根。

- **规范化释义（primary_lang_explained）**：
 - 所以，无论天干在月令中是旺是衰，只要在年月日时四柱的地支中有根气，就能承受财官食神的吉力，抵挡伤官七煞的凶力。根气有轻重之分：长生、禄位、帝旺，是根气中最重的；墓库、余气，是根气中较轻的。得到一个比肩（天干），不如得到地支中一个墓库，例如甲木遇到未土（木之墓库）、丙火遇到戌土（火之墓库）。但要注意，乙木遇戌、丁火遇丑，不能算作墓库通根，因为戌土中不藏木，丑土中不藏火。得到两个比肩，不如得到一个余气根，例如乙木遇到辰土（辰中藏乙木余气）、丁火遇到未土（未中藏丁火余气）。得到三个比肩，不如得到一个长生、禄位或羊刃，例如甲木遇到亥（长生）、寅（禄）、卯（羊刃）。阴干的长生理论有争议，不能完全按这个论法，例如乙木长生在午、丁火长生在酉，但这些也算是明确的根气，相当于一个余气根。为什么根气这么重要？因为比劫就像朋友的扶持，而通根就像有自己的房屋可以居住；天干多不如地支根重，这是当然的道理。

- **完整对等诠释（secondary_lang_full）**：  
  From this angle, the decisive question is not simply whether the Day stem enjoys the Month, but whether it has solid roots somewhere in the four branches. As long as it does, it can carry Wealth, Officer and Food God and stand up to Hurting Officer and Seven Killings. Among all forms of rooting, the heaviest are the positions of Longevity, rank and prosperity; tomb branches and residual‑qi branches provide lighter but still useful roots. One single Companion stem in the heavens is worth less than one proper tomb in the branches: for example, Jia meeting Wei, or Bing meeting Xu, gains more from those storehouses than from an extra Jia or Bing in the stems. By contrast, Yi meeting Xu or Ding meeting Chou cannot be counted as tomb roots, because those branches do not actually contain Wood or Fire.

  Two Companion stems are still inferior to one residual root, such as Yi meeting Chen or Ding meeting Wei; three Companions are less valuable than one position of Longevity, rank or Yang Blade, such as Jia finding roots in Hai, Zi, Yin or Mao. For yin stems, the so‑called Longevity positions are weaker and more controversial, but they still count as clear roots roughly comparable to a residual qi. The underlying image is that Companions are like friends lending a hand, whereas rooting in the branches is like having a house of one's own to live in. External help is welcome, but it cannot replace a secure home base: many stems in the sky can never compensate for the absence of deep roots below.

- 详细解说：
  - 身强身弱的判断核心是"通根"，而非"比劫多"。
  - 通根提供的是"立足之地"（室家），比劫提供的是"外援"（朋友），前者更根本。
  - 根气有明确的轻重量化标准：1长生禄刃 = 3比肩，1墓库 = 1比肩，1余气 = 2比肩。
  - 阴干与阳干在根气判定上有细微差异，需区别对待。

- 核心要点：
  - 判断身强身弱，首要看地支通根，其次才看天干透比劫。
  - 根气轻重次序：长生禄旺 > 墓库余气 > 比肩透干 > 无根。
  - 墓库通根的条件：该墓库中必须藏有该干的同类五行（如甲逢未可以，乙逢戌不行）。
  - 阴干长生虽有争议，但仍可作为"明根"，相当于余气的力量。

- 应用推演：
  1) 列出日主在年月日时四支的根气分布。
  2) 按轻重赋值：长生/禄/刃=3分，墓库=1分，余气=0.5分，阴干长生=0.5分。
  3) 统计天干比劫数量：每个比肩=1分。
  4) 综合评分：根气总分 + 比劫分，判断身强身弱。
  5) 特别注意：墓库必须中藏该干，否则不算。

- 反例与边界：
  - 只数天干比劫，不看地支通根，是最常见的机械错误。
  - 机械套用"乙逢戌为墓库"，不知戌中无木，导致误判。
  - 忽视阴干长生的特殊性，与阳干混为一谈。

- 小例（示意）：
  - 甲木日主，地支有未（墓库）= 1分，天干无比劫 = 0分，总分1分，身偏弱但有根。
  - 甲木日主，地支有寅（禄）= 3分，天干有一甲 = 1分，总分4分，身强。
  - 乙木日主，地支有戌（无木）= 0分，天干有三乙 = 3分，总分3分，身弱（虚浮）。

- 校勘与字词辨析：
  - "得一比肩，不如得支中一墓库"：各本大致相同，强调通根重于透干。
  - "阴长生不作此论"：指阴干长生理论有争议，不如阳干长生明确有力。
  - "干多不如根重，理固然也"：经典命理判语，强调地支根气的根本性。


- **叙事素材（narrative_snippets）**：
  - `[ns_zpzy_251]` `[trigger: 解法要诀]` `[factor_trigger: xingchong_you_jie AND huihe_you_san AND xu_cha_quanju]` `[role: 主干]` 刑冲有解，会合有散，须察全局。 → 《子平真诠·论刑冲会合解法》#解法
  - `[ns_zpzy_252]` `[trigger: 会合解法]` `[factor_trigger: xingchong_huihe_ge_you_jiefa AND xu_cha_qingzhong_huanji]` `[role: 主干]` 刑冲会合各有解法，须察轻重缓急。 → 《子平真诠·论刑冲会合解法》#解法
  - `[ns_zpzy_253]` `[trigger: 实践要领]` `[factor_trigger: duanming_shijian AND yaoling_zonghe]` `[role: 主干]` 断命实践要领。 → 《子平真诠》#上卷
  - `[ns_zpzy_254]` `[trigger: 边界条件]` `[factor_trigger: shiyong_tiaojian AND bianjie_xianzhi]` `[role: 条件分支]` 适用条件与边界。 → 《子平真诠》#上卷
  - `[ns_zpzy_255]` `[trigger: 太过不及]` `[factor_trigger: (taiguo=true OR buji=true) AND result=fei_zhonghe]` `[role: 主干]` 太过不及，皆非中和。 → 《子平真诠》#上卷"""
    normalized_text_zh: str = """"""
    subject: str = "是故十干不论月令休囚，只要四柱有根"
    factor_refs: list = ['sizhu_yougen', 'changshen_luwang', 'muku_yuqi', 'tonggen', 'gan_duo_gen_zhong']
    
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
        l1_anchor="zpzq_v1.0.0_是故十干不论月令休囚_只要四柱有根_001_L1",
    )
    version: str = "1.0.0"
