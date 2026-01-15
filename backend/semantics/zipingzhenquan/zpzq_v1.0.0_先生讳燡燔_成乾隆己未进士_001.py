"""
Auto-generated semantic module for zipingzhenquan
Generated at: 2025-12-05T13:30:19.523402
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
    semantic_id="zpzq_v1.0.0_先生讳燡燔_成乾隆己未进士_001",
    book_id="zipingzhenquan",
    engine_id="bazi"
)
class 先生讳燡燔成乾隆己未进士(SemanticEntry):
    """
    - **原文（source_text）**：
  先生讳燡燔，成乾隆己未进士，天资颖悟，学业渊邃，其于造化精微，固神而明之，变化从心者矣。观其论用神之成败得失，又用神之因成得败、因败得成，用神之必兼看...
    """
    
    original_text: str = """- **原文（source_text）**：
  先生讳燡燔，成乾隆己未进士，天资颖悟，学业渊邃，其于造化精微，固神而明之，变化从心者矣。观其论用神之成败得失，又用神之因成得败、因败得成，用神之必兼看于忌神，与用神先后生克之别，并用神之透与全、有情无情、有力无力之辨，疑似毫芒，至详且悉。是先生一生心血，生注于是，是安可以淹没哉！君安爰谋付剞劂，为天下谈命者，立至当不易之准，而一切影响游移、管窥蠡测之智，俱可以不惑。此亦谈命家之幸也；且不谈命家之幸，抑亦天下士君子之幸，何则？人能知命，则营竞之可以息，非分之想可以屏，凡一切富贵穷通寿夭之遭，皆听之于天，而循循焉各安于义命，以共勉于圣贤之路，岂非士君子厚幸哉！观于此而君安之不没人善，公诸同好，其功不亦多乎哉？爱乐序其缘起。乾隆四十一年岁丙申初夏，同后学胡焜倬空甫谨识。

- 原注（原文注解）：
  　　此段为胡焜倬对沈孝瞻及章君安之德业与命理贡献的总评，原刻本不另夹注。

- 分字分词释义：
  - 燡燔：沈孝瞻先生之名，二字皆火部，取其火明之象。
  - 造化精微：天地生成变化的微妙之理。
  - 神而明之：以“神解”之悟性洞察其理，又能说得分明。
  - 变化从心：对理法运用纯熟，自然随心而转，不拘于死法。
  - 用神之成败得失：用神是否得力、成格或破格的得失。
  - 因成得败、因败得成：由成局之处招致败象，或由看似败局处转出成局之妙。
  - 兼看于忌神：判断用神时必须同时观察忌神的位置与力量。
  - 先后生克之别：生克发生的前后顺序，对格局影响极大。
  - 透与全：喜用之神是否透出、是否纯全。
  - 有情无情：干支之间是否有真生、真合之情，或只见名义不见实情。
  - 有力无力：某神虽在命局，却是否真有根气与实用之力。
  - 付剞劂：付诸刻版刊印，使之流传。
  - 影响游移：人云亦云、摇摆不定之见。
  - 管窥蠡测：以管窥天、以蠡测海，比喻见识局促。
  - 义命：合乎义理之所当然的命分，区别于侥幸与非分之求。

- **规范化释义（primary_lang_explained）**：
  沈孝瞻先生名燡燔，是乾隆己未科进士，天资聪颖，学问深厚，对于造化精微之理，能以近乎神悟的方式洞察，又能说得分明透彻，运用时几乎可以随心所欲。细看他论述用神，不仅讲到用神本身的成败得失，更指出"因成得败、因败得成"的种种反转之机；又主张论用神时必须一并考察忌神的位置与力度、先后生克的次序、喜用之神是否透出、是否纯全、干支之间有无真情、有无实力等。对这些疑难细微之处，他都剖析得极为详尽。可以说，这是先生一生心血凝注之处，又岂能让它湮没？章君安于是谋划付梓刊刻，为天下学习命理的人树立一个"至当而不易"的标准，使那些随波逐流、见识浅浅的说法，不再足以迷惑世人。这本书的问世，不只是一家谈命之士的幸事，也是天下读书人、讲义命之人的幸事。因为人一旦真正"知命"，便能息掉争竞之心，屏退不合分的妄想，把一切富贵、穷通、寿夭的遭遇，交给天命，同时在可为的范围内，各自安于"义所当然"的命分，共同勉力于圣贤之路。这也是胡焜倬所以特意写下此序，叙述缘起的原因。

- **完整对等诠释（secondary_lang_full）**：  
  This preface portrays Shen Yifan (Shen Xiaozhan) as a scholar of exceptional talent whose life work was to clarify the subtle laws of creation and, above all, the system of the Useful God. He does not stop at listing which stars are favourable or unfavourable; he traces how a Useful God can succeed or fail, how success can gradually contain the seeds of later failure, and how apparent failure can sometimes turn back into success. In doing so he constantly weighs the role of inimical stars, the order in which generating and controlling take place, whether the helpful star is exposed and pure, and whether the relations between stems and branches are genuinely affectionate and effective or only nominally so.

  The author of the preface insists that such painstaking analysis must not be allowed to sink into obscurity. By having Zhang Jun'an carve and print the work, he hopes to provide all students of fate with a standard that is "utterly proper and not easily shaken", so that vague, fashion‑driven opinions will no longer mislead them. At a deeper level, knowing fate correctly is meant to quiet worldly competition and unrealistic desires: once a person understands the limits of wealth, status and longevity that Heaven has assigned, he can place outcomes in Heaven's hands while exerting himself within the bounds of moral duty. In this sense, the publication of 《子平真诠》 is not only a blessing for professionals who read charts, but also for all cultivated people who wish to walk the path of the sages by aligning themselves with "righteous fate".

 - 详细解说：
  - 本书的理论核心，是围绕“用神体系”展开的：不仅看用神本身，更重视与忌神、先后生克、透藏纯杂、有情有力之间的综合判读。
  - “因成得败、因败得成”点出命局之妙不在静态格局名目，而在动态权衡与细致推理。
  - 序末强调“知命而后能安义命”，把命理的终极落点放在德行与人生修养上，而非单纯技巧。

- 核心要点：
  - 用神判断必须成体系：成败、救应、忌神、次序、透藏、有情、有力，缺一不可。
  - 反对“影响游移、管窥蠡测”的断法：不以一两个表象字眼，草率论人一生。
  - 以“义命”为终点：知命之后，回到伦理与自我修养，而不是沉溺于趋吉避凶的算计。

- 应用推演：
  1) 读全书时，以“用神体系八大关键词”（成败、救应、忌神、先后、透全、有情、有力）为总纲。
  2) 遇到具体命例，先看格局大势，再细察这些关键词如何互相作用。
  3) 在给人断命或自我观命时，把“知命以安义命”明确告知为前提，不鼓励宿命与投机心理。

- 反例与边界：
  - 只摘取某条用神口诀，不顾忌神位置与先后次序，极易误判。
  - 把“因成得败”当成随口反转的托词，而不是基于具体生克路线的严密推理。
  - 用命理为人开脱责任，鼓励“命中注定所以不必尽力”，与本序精神完全相反。

- 小例（示意）：
  - 某局本为财官格成，用神得位，但因财过旺、官受损，行运再助财即“因成得败”；若后运转印制财，反能“因败得成”，此类变局，皆须在“用神—忌神—先后—有情有力”的框架下细推。

- 校勘与字词辨析（双语）：
  - **中文**：“有情无情、无力无力之辨”：今据理当作“有情无情、有力无力之辨”。“无力无力”显属传抄讹误，且与前后结构不对称，故从语义与结构一并改为“有力无力”，并在此记下旧文。
  - **中文**：文中“影响游移管窥蠡测之智”，部分版本或作“影响游移，管窥蠡测之见”，义近。今从本书原文，并以逗号略作分读，以便理解。
  - **中文**：末尾署名“乾隆四十一年岁丙申初夏同后学胡焜倬空甫谨识”，各本大体相同，今只略整标点，不改其字。
  - **English**: The phrase "youqing wuqing, wuli wuli" in some copies clearly contains a copying error; on structural and semantic grounds it is corrected here to "youqing wuqing, youli wuli" (with or without genuine affinity, with or without real strength), and the older form is recorded as a variant. The expression "yingxiang youyi, guankui lice zhi zhi" appears in some editions with "zhi jian" (opinion) instead of "zhi" (intelligence); the meanings are similar and we follow the wording of the base text, adding punctuation for clarity. The closing signature "In the forty-first year of Qianlong, early summer of the Bingshen year, respectfully written by the later student Hu Kunzhuo" is consistent across editions; only punctuation has been lightly regularized.


- **叙事素材（narrative_snippets）**：
  - `[ns_zpzy_043]` `[trigger: 合而不合]` `[factor_trigger: tiangan_he AND (deling=true -> zhenhe) OR (deling=false -> jiahe)]` `[role: 条件分支]` 合有真合假合，须察得令失令。 → 《子平真诠·论十干合而不合》#真假
  - `[ns_zpzy_044]` `[trigger: 争合妒合]` `[factor_trigger: tiangan_he AND he_count>=2 AND (zhenghe OR duhe)]` `[role: 条件分支]` 一干合两干，有争有妒，须辨谁得谁失。 → 《子平真诠·论十干合而不合》#争妒
  - `[ns_zpzy_045]` `[trigger: 合处逢冲]` `[factor_trigger: tiangan_he AND (fengchong=true -> san) OR (san_zhong_fuhe -> ning)]` `[role: 条件分支]` 合处逢冲则散，散中复合则凝。 → 《子平真诠·论十干合而不合》#冲散
  - `[ns_zpzy_046]` `[trigger: 水主智]` `[factor_trigger: element=shui AND virtue=zhi AND character=(cong, ling)]` `[role: 主干依赖]` 壬癸水主智，性聪心灵。 → 《子平真诠》#上卷
  - `[ns_zpzy_047]` `[trigger: 春木当令]` `[factor_trigger: season=chun AND mu_dangling AND mu_wang_huo_xiang]` `[role: 主干依赖]` 春木当令，木旺火相。 → 《子平真诠》#上卷
  - `[ns_zpzy_048]` `[trigger: 闲神无用]` `[factor_trigger: xianshen_exists AND function=wuyong AND status=buxi_buji]` `[role: 条件分支]` 闲神无用，不喜不忌。 → 《子平真诠》#上卷
  - `[ns_zpzy_049]` `[trigger: 调候为急]` `[factor_trigger: tiaohou_priority=ji AND condition IN (han, nuan, zao, shi)]` `[role: 条件分支]` 调候为急，寒暖燥湿。 → 《子平真诠》#上卷
  - `[ns_zpzy_050]` `[trigger: 通关为妙]` `[factor_trigger: tongguan_exists AND function=huajie_zhengzhan]` `[role: 主干依赖]` 通关为妙，化解争战。 → 《子平真诠》#上卷
  - `[ns_zpzy_051]` `[trigger: 五行流通]` `[factor_trigger: wuxing_liutong AND qiji_changda]` `[role: 总结]` 五行流通，气机畅达。 → 《子平真诠》#上卷
  - `[ns_zpzy_052]` `[trigger: 用神无力]` `[factor_trigger: yongshen_strength=wuli AND result=pinjian_nanmian]` `[role: 总结]` 用神无力，贫贱难免。 → 《子平真诠》#上卷
  - `[ns_zpzy_053]` `[trigger: 年柱根基]` `[factor_trigger: pillar=nian AND role=genji_zuye]` `[role: 主干依赖]` 年柱根基，祖业之宫。 → 《子平真诠》#上卷"""
    normalized_text_zh: str = """"""
    subject: str = "先生讳燡燔，成乾隆己未进士"
    factor_refs: list = ['source_ref', 'yongshen', 'yin_cheng_de_bai', 'yin_bai_de_cheng', 'jishen', 'youqing_wuqing', 'youli_wuli', 'yiming']
    
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
        l1_anchor="zpzq_v1.0.0_先生讳燡燔_成乾隆己未进士_001_L1",
    )
    version: str = "1.0.0"
