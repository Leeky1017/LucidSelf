"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.725461
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
    semantic_id="zw_v1.0.0_斗数发微论总论_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 斗数发微论总论(SemanticEntry):
    """
    - 原文（source_text）：

  白玉蟾先生曰：观天斗数，与五星不同。按此星辰与诸术大异。四正吉星定为贵，三方杀拱少为奇。对照兮详凶详吉，合照兮观贱视荣。吉星入垣则为吉，凶星失地则为凶。命逢...
    """
    
    original_text: str = """- 原文（source_text）：

  白玉蟾先生曰：观天斗数，与五星不同。按此星辰与诸术大异。四正吉星定为贵，三方杀拱少为奇。对照兮详凶详吉，合照兮观贱视荣。吉星入垣则为吉，凶星失地则为凶。命逢紫府，非特寿而且荣；身遇杀星，不但贫而且贱。左右会于紫府，极品之尊；科权陷于凶乡，功名𬧔蹬；行限逢乎弱地，禾必为灾；立命会在强宫，必能降福。羊陀七杀，限运莫逢，逢之定有刑伤；劫空伤使，在内，合断。天哭丧门，流年莫遇，遇之寔防破害。南斗主限必生男，北斗加临，先得女。科星居于陷地，灯火辛勤；昌曲在凶乡，林泉冷淡，奸谋频设。紫微愧遇破军，淫奔大行；红鸾羞逢贪宿。命身相克，则心乱而不闲；玄媪即天姚星，三宫，则邪淫而躭酒。杀临三位，定然妻子不和；巨到二宫，必是兄弟无义；刑杀守子宫，子难奉老；诸凶照财帛，聚散无常。羊陀疾厄，眼目昏肓；火铃到迁移，长途寂寞。尊星列贱位，主人多劳；恶星应八宫，奴仆有助。官禄遇紫府，富而且贵；田宅遇破军，先破后成；福德遇空劫，奔走无力；相貌加刑杀，刑克难免。后学者执此推详，万无一失。

- 原注（原文注解，可无则省略小节）：

  本篇题作“发微”，意在于在前几条纲领与准绳之后，再从实务角度“发明隐微处”，说明如何综合星曜的四正、三方、入垣失地、强弱宫位与限运等条件，来细致评估贵贱荣枯、刑伤灾祸与男女性别、六亲关系等具体应验点。其语言多为口诀式简语，需结合后文星曜诸论一并参看。

- 分字分词释义：

  - **观天斗数**：以“斗数”观天象、观人事，点出本论所依仍是紫微斗数体系，而非传统五行星占。
  - **四正吉星**：指命盘四正（命、迁移、财帛、官禄等关键正宫）上所得之吉星，为判断贵气与格局的骨架。
  - **三方杀拱**：三方四正中凶杀星夹拱或冲照关键宫位，虽有奇局，但多伴随代价与风险。
  - **入垣 / 失地**：星在本垣旺地为“入垣”，力量端正；失其本位、陷弱或空亡为“失地”，多虚、多偏、多耗。
  - **科权陷于凶乡**：科星、权星等本应为荣名、权力之星，若落在凶乡或陷地，则主“灯火辛勤而名利多波折”。
  - **羊陀七杀，限运莫逢**：指羊、陀、七杀等重杀若在限运中重叠触发关键宫位，多主刑伤或重灾，应尽量趋避高风险情境。
  - **天哭丧门**：古人以天哭、丧门为丧葬、哭泣之象，流年与限运遇之，常主忧丧、失亲或重大心理打击。
  - **尊星列贱位**：本应高贵之星（如紫微、天府等）落在相对卑下或劳碌之位，象征“人高而位卑”或“位不称德”。
  - **恶星应八宫**：恶星在奴仆、田宅、迁移等宫应事，虽对命主本身不至绝凶，但往往借由环境与他人而发生。

- 规范化释义（primary_lang_explained）：

  白玉蟾指出：以紫微斗数观人事，与仅以五行推星的传统占法不同，必须兼顾四正、三方、入垣失地与限运强弱等多重结构。四正宫位若得吉星，则格局自然高；三方若多杀拱照，则虽可成奇局，却常伴随风险与代价。吉星入垣，则其吉象较易兑现；凶星失地，则其凶性更为明显。命逢紫微、天府等主星，往往不但寿长而且荣显；身遇杀星，若又失地失垣，则多贫贱与坎坷。

  文中进一步说明：左右辅弼会于紫府，可至极品之尊；若科权陷于凶乡，则功名多蹭蹬、难以久安。行限若逢弱地，多主禾稼受灾、人事不顺；立命会在强宫，则能承福。限运中若逢羊、陀、七杀重叠，刑伤之事难免；劫空伤使，则多主破败、损失。天哭、丧门之流年，应谨防破害与忧丧。又以南斗、北斗之配置论生男、先女之象，以科星、昌曲入陷地与凶乡论“灯火辛勤而境遇冷淡”。

  后段详述诸多具体组合：紫微遇破军，易见淫奔与大起大落；红鸾逢贪狼，多有情欲纠葛；天姚星在三宫，多主邪淫与嗜酒。杀星临三位，妻子不和；巨门到二宫，兄弟无义；刑杀守子宫，子难奉老。诸凶照财帛，则财来财去、聚散无常；羊陀守疾厄，多见眼目昏花；火铃在迁移，主远行寂寞。尊星列贱位，则人多劳而不显；恶星应八宫，则奴仆反能助主。官禄遇紫府，富而且贵；田宅遇破军，先破后成；福德遇空劫，奔走无力；相貌加刑杀，刑克难免。结语“后学者执此推详，万无一失”，强调本条可作为实务推断时的综合检核表。

- 完整对等诠释（secondary_lang_full）：

  This chapter, attributed to Bai Yuchan, describes how Ziwei Doushu should be used in concrete chart reading, beyond abstract principles. It insists that one must read the four cardinal houses, their three‑house supports, whether stars are in their proper enclosures or fallen, and how timing cycles strengthen or weaken them. When the four cardinal houses are well supplied with benefics, the skeleton of the chart is inherently noble; when the three‑house formations are packed with malefics, one may still see striking or "strange" patterns, but these often come with heavy costs. Stars in dignity fulfil their promises more readily, while fallen malefics show their harsher side. Charts with Ziwei or Tianfu strongly placed tend toward honour and longevity; charts where the body is bound up with fallen killing stars tend more toward poverty, danger and repeated setbacks.

  The text then walks through many concrete combinations. Assistants such as Zuo Fu and You Bi flanking Ziwei can mark extremely high rank, while promotion and examination stars trapped in hostile places describe careers that shine for a moment but cannot hold. Weak or afflicted terrain in major periods tends to damage crops and daily affairs; a strong Life palace can nevertheless carry blessings through such times. Overlapping cycles that repeatedly activate Yang, Tuo and Qisha indicate periods of physical danger or legal trouble, especially when combined with Void or depletion stars. Yearly indicators such as Heavenly Cry and Funeral Gate point to seasons of grief or loss. Further examples show how Southern and Northern Dipper stars can be read for the sex of children, and how imperially flavoured configurations like "Golden Hall proclamation" or "Hanlin purity" arise from specific planetary clusters.

  In its later sections, the chapter turns to relational and financial houses: combinations that scatter wealth, patterns that show quarrelsome or estranged siblings, children who cannot care for elders, or marriages that are tested by distance and pressure. Here again the point is not fatalistic certainty but structural alertness: such configurations name areas of life that will demand extra work, boundaries and conscious choice. Finally, clusters such as Ziwei with Pojun or Hongluan with Tanlang are read as sites where desire, volatility and status interact. Without values and responsibility to contain them, these blends can produce scandal, impulsive decisions or reputation loss; with awareness, they can become engines of transformation and creative drive. Taken together, the text offers a dense checklist of micro‑rules that extend the earlier general principles into a practical, multi‑house diagnostic toolkit.

- 核心要点：

  - 通过“四正 + 三方 + 入垣/失地 + 限运”的多维视角，综合评估贵贱荣枯与灾福风险。
  - 将紫府、辅弼、科权等“尊星”，与羊陀、空劫、天哭丧门等“恶星”放在具体宫位与限运中对照，而非孤立看星名。
  - 对婚姻、兄弟、子女、财帛、健康、迁移等具体生活领域，给出一套“凶应优先”的预警结构。
  - 强调“先看结构，再看应期”：本条既看本命星位，又看行限与流年如何触发或缓解其吉凶。

- 详细解说：

  1. **四正吉星与三方杀拱：格局与代价的两面**  
     “四正吉星定为贵，三方杀拱少为奇”表明：真正的高格局，不只是看某一宫位，而是四正宫整体配置。四正得吉，骨架本佳；若三方多杀拱照，则虽有奇局，却常伴随高风险或极端事件，应视为“有代价的光彩”，而非纯粹好运。

  2. **入垣失地与尊星贱位：位置决定发挥方式**  
     吉星入垣，凶星失地，是传统斗数中常见语，但本篇特别提出“尊星列贱位”的概念：紫微、天府、科权、昌曲等若落入劳碌、卑下或被压制之宫，往往表现为“人好而位不称”“有才无位”，需要在现实选择中主动寻找更合适的平台。

  3. **限运、羊陀七杀与天哭丧门：时间与事件的交汇**  
     “羊陀七杀，限运莫逢”“天哭丧门，流年莫遇”点出：某些结构在平时只是潜在风险，一旦在限运或流年中被集中触发，便容易应验为刑伤、官非或丧忧。本条的建议，不是让人恐惧，而是提醒在这些时段避免高风险行为，并加强对健康与家人的关怀。

  4. **六亲与财帛的凶象结构**  
     文中对妻子不和、兄弟无义、子难奉老、财帛聚散无常等，都以“杀临三位”“巨到二宫”“刑杀守子宫”“诸凶照财帛”等结构加以标示。这些结构并非绝对断语，而是指出“需要投入额外心力”的关系领域，可在实际生活中通过沟通、契约与边界设置加以调节。

  5. **紫府破军与红鸾贪宿：情欲与格局的张力**  
     紫微遇破军，红鸾逢贪狼，古书多以“淫奔”相责。本篇在现代解读中，更可理解为：强烈欲望与变动倾向汇聚时，若缺乏价值观与责任感的约束，容易在情感与名誉上付出高代价。通过觉察这类结构，可以提前为自己设定边界与底线。

- 校勘与字词辨析：

  - “功名𬧔蹬”之“𬧔”，诸本亦作“坠”“颠”，皆有跌落、失足之意，本稿据底本录“𬧔”，并在白话中以“功名蹭蹬”释之。
  - “寔防破害”之“寔”，为“实”之异体字，本稿从底本原字，在现代释义中以“务须、防备”说明其强调之意。
  - “昏肓”有本作“昏盲”，皆指眼目昏花、视力衰退，本稿据底本录“肓”，并在释义中以“昏花、模糊”解释。

- 叙事素材（narrative_snippets）：

  - **四正三方**："身命须明四正三方，官禄田财相互流转"，强调四正三方是判断格局的基本骨架。
  - **入垣失地**："入庙则身荣，失地则命贱"，星曜得地与否直接决定吉凶的发挥程度。
  - **煞曜侵凌**："擎羊陀罗同居太岁，必主灾殃"，限运遇煞为凶象集中激发的高危期。
  - **六亲结构**："妻宫太阴失地，主妻难完聚"，六亲宫位的吉凶直接映射现实关系质量。
  - **情欲张力**："紫微遇破军，红鸾逢贪狼"，强欲与变动汇聚时需设定边界底线。
  - **现代应用**：本条可作为命盘"发微细查"的框架——从四正三方到限运，从六亲到财帛，层层深入。"""
    normalized_text_zh: str = """"""
    subject: str = "斗数发微论总论"
    factor_refs: list = ['combo_sizheng_ji', 'combo_sanfang_sha', 'state_ruyuan_shidi', 'combo_zunxing_jianwei', 'combo_yangtuo_qisha', 'star_tianku_sangmen']
    
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
        l1_anchor="zw_v1.0.0_斗数发微论总论_001_L1",
    )
    version: str = "1.0.0"
