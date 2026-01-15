"""
Auto-generated semantic module for yuanhaiziping
Generated at: 2025-12-05T13:30:19.559418
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
    semantic_id="yhzp_v1.0.0_相心赋_001",
    book_id="yuanhaiziping",
    engine_id="bazi"
)
class 相心赋(SemanticEntry):
    """
    - **原文（source_text）**：
  人居六合，心相五行，欲晓一生，辩形察性。
  官星恺悌，贵气轩昂，性优游而仁慈宽大、怀豁达而和畅声音、丰姿美而秀丽、性格敏而聪明。
  印绶主多智慧、...
    """
    
    original_text: str = """- **原文（source_text）**：
  人居六合，心相五行，欲晓一生，辩形察性。
  官星恺悌，贵气轩昂，性优游而仁慈宽大、怀豁达而和畅声音、丰姿美而秀丽、性格敏而聪明。
  印绶主多智慧、丰身自在心慈。
  食神善能饮食、体厚而喜讴歌。
  偏官七杀，势压三公，喜酒色而偏争好斗、爱轩昂而扶弱欺强、情性如虎、急躁如风。
  枭印当权，使心机而始勤终惰、好学艺而多学少成。
  偏印劫刃，出祖离家，外象谦和尚义、内实狠毒无知、有刻剥之意、无慈惠之心。
  偏正财露，轻财好义，爱人趋奉、好说是非、嗜酒贪花，亦系如此。
  伤官伤尽，多艺多能，使心机而傲物气高、多谲诈而侮人志大、颧高骨俊、眼大眉粗。
  日德心善稳厚、而作事慈祥。
  魁罡性严有操持、而为人聪敏。
  日贵夜贵，朝荣暮荣，为人纯粹而有姿色、作仁德而不骄奢。
  金神贵格，火地奇哉！有刚断明敏之才、无刻剥欺瞒之心。
  乙巳鼠贵，遇午冲，贫如颜子。
  壬骑龙背，逢丁破，欲比申枨。
  井栏飞天，其心傲物。
  刑合趋艮（寅），智足多仁。
  六甲趋干（亥），主仁慈而刚介心平。（六甲趋干格）
  五阴会局，为人佛口蛇心。
  二德印生，作事施恩布德。
  五行有化，看何气而推。
  四柱无情，取元干而论也。
  且，火炎土燥，必声洪而好礼；水清润下，主言悟而施仁。
  金白水清，质黑肥圆。
  土气厚重，信在四时。
  汇合如然，失时反此；事则举其大略，须要察其细微。欲识情理，学者用心于此。

- **分字分词释义**：
  - **人居六合心相五行**：人生天地间，心性与五行相应。
  - **官星恺悌贵气轩昂**：正官主性情和乐，气度轩昂。
  - **偏官七杀势压三公**：七杀主威严刚猛，势可压倒高官。
  - **枭印当权始勤终惰**：偏印掌权，做事虎头蛇尾。
  - **伤官伤尽多艺多能**：伤官旺主才艺出众但傲慢。
  - **日德心善稳厚**：日德格主心地善良稳重。
  - **魁罡性严有操持**：魁罡格主性格严厉有操守。
  - **五阴会局佛口蛇心**：五阴全聚，主外柔内毒。
  - **金白水清质黑肥圆**：金水旺主肤白体圆。
  - **火炎土燥声洪而好礼**：火土旺主声音洪亮重礼节。

- **规范化释义（primary_lang_explained）**：
  本篇名为《相心赋》，专门通过八字五行神煞来推断人的心性与外貌：
  - **十神心性**：
    - **官星**：恺悌仁慈，声音和畅，相貌秀丽。
    - **印绶**：智慧慈祥，丰身自在。
    - **食神**：体厚（微胖），喜饮食歌唱。
    - **七杀**：急躁如虎，好斗争强，喜酒色，扶弱欺强。
    - **枭印**：心机多，始勤终惰，学而不成。
    - **劫刃**：外谦内毒，刻薄无情。
    - **财星**：轻财好义，嗜酒贪花，好说是非。
    - **伤官**：多艺多能，傲物气高，颧高骨俊（面部特征）。
  - **神煞性情**：
    - **日德/天月德**：心善稳厚。
    - **魁罡**：性严聪敏。
    - **金神**：刚断明敏。
    - **五阴会局**：佛口蛇心（外柔内阴）。
  - **五行体象**：火炎土燥声洪好礼；金白水清体圆；土气厚重主信。

- **完整对等诠释（secondary_lang_full）**：
  **Ode on Physiognomy and Mind (Xiang Xin Fu)**:
  - **Ten Gods & Character**:
    - **Officer**: Benevolent, dignified, harmonious voice, beautiful features.
    - **Seal**: Wise, charitable, comfortable physique.
    - **Eating God**: Plump, loves food and song.
    - **Killing**: Aggressive ("Like a tiger"), argumentative, loves alcohol/lust, bullies the strong/helps the weak (or vice versa depending on context).
    - **Owl (Indirect Seal)**: Scheming, lazy ending, learns much but masters little.
    - **Rob/Blade**: Externally humble, internally poisonous/cruel.
    - **Wealth**: Generous with money, loves flattery/alcohol/lust, gossipy.
    - **Injury**: Talented but arrogant, high cheekbones, large eyes/thick brows.
  - **Stars & Nature**:
    - **Day Virtues**: Kind and steady.
    - **Kui Gang**: Strict and intelligent.
    - **Jin Shen (Metal Spirit)**: Decisive and sharp.
    - **Five Yin Gathering**: "Buddha's mouth, Snake's heart" (Hypocritical).
  - **Elemental Constitution**: Fire/Earth dry = Loud voice, polite. Metal/Water clear = Round physique. Earth heavy = Trustworthy.

- **核心要点**：
  - **相由心生**：命局决定心性，心性影响外貌（如伤官颧高）
  - **善恶两端**：官印食德为善，杀伤劫枭为恶（需制化）
  - **五行表征**：金主义/肃杀，木主仁/慈爱，水主智/圆通，火主礼/声宏，土主信/厚重

- **详细解说**：  《相心赋》专论命局与心性外貌的关系，开篇"人居六合，心相五行"点明命理与心性的相应关系。**十神心性**——"官星恺悌，贵气轩昂"主仁慈宽大；"印绶主多智慧，丰身自在心慈"主智慧慈祥；"食神善能饮食，体厚而喜讴歌"主体态丰厚；"偏官七杀，势压三公"主刚猛好斗；"枭印当权，始勤终惰"主虎头蛇尾；"伤官伤尽，多艺多能"主才华傲慢。**神煞性情**——"日德心善稳厚"主善良；"魁罡性严有操持"主严厉聪敏；"金神贵格，火地奇哉"主刚断明敏；"五阴会局，为人佛口蛇心"主外柔内毒。**五行体象**——"火炎土燥必声洪而好礼"主声宏重礼；"金白水清，质黑肥圆"主体圆肤白；"土气厚重，信在四时"主诚信厚道。末句"欲识情理，学者用心于此"点明相心之学需细致体会。

- **叙事素材（narrative_snippets）**：
  - `[ns_yhzp_711]` `[trigger: 心相五行]` `[factor_trigger: xinxiang_wuxing AND mingju_xinxing_waimao]` `[role: 主干]` 人居六合，心相五行；命局决定心性外貌。 → 《渊海子平·相心赋》
  - `[ns_yhzp_712]` `[trigger: 官星恺悌]` `[factor_trigger: guanxing_kaiti AND guiqi_xuanang AND renci_kuanda AND anchong_qugui AND angui]` `[role: 条件分支]` 官星恺悌贵气轩昂，性优游而仁慈宽大。 → 《渊海子平·相心赋》
  - `[ns_yhzp_713]` `[trigger: 七杀虎性]` `[factor_trigger: qisha_pianguan AND shiyan_sangong AND jizao_rufeng AND hu_xing]` `[role: 条件分支]` 偏官七杀势压三公，情性如虎急躁如风。 → 《渊海子平·相心赋》
  - `[ns_yhzp_714]` `[trigger: 枭印始勤终惰]` `[factor_trigger: xiaoyin_dangquan AND shiqin_zhongduo AND duoxue_shaocheng AND caiyin AND caiyin_qing_guansha_zu AND changyin]` `[role: 条件分支]` 枭印当权，使心机而始勤终惰，好学艺而多学少成。 → 《渊海子平·相心赋》
  - `[ns_yhzp_715]` `[trigger: 伤官多艺]` `[factor_trigger: shangguan_shangjin AND duoyi_duoneng AND aowu_qigao AND duoyi_aowu AND injury_officer]` `[role: 条件分支]` 伤官伤尽多艺多能，使心机而傲物气高。 → 《渊海子平·相心赋》
  - `[ns_yhzp_716]` `[trigger: 五阴佛口蛇心]` `[factor_trigger: wuyin_huiju AND fokou_shexin AND wairou_neidu AND caiyin AND caiyin_qing_guansha_zu AND changyin AND five_yin]` `[role: 例外处理]` 五阴会局，为人佛口蛇心；外柔内毒之象。 → 《渊海子平·相心赋》
  - `[ns_yhzp_717]` `[trigger: 五行体象]` `[factor_trigger: huoyan_tuzao_shenghong AND jinbai_shuiqing AND tuqi_houzhong AND fire_earth]` `[role: 条件分支]` 火炎土燥必声洪而好礼；金白水清质黑肥圆；土气厚重信在四时。 → 《渊海子平·相心赋》
  - `[ns_yhzp_718]` `[trigger: 相心赋纲领]` `[factor_trigger: xiangxin_fu AND shishen_xinxing AND wuxing_tixiang]` `[role: 总结]` 相心赋以十神心性、神煞性情、五行体象推断人的心性与外貌。 → 《渊海子平·相心赋》"""
    normalized_text_zh: str = """"""
    subject: str = "相心赋"
    factor_refs: list = ['physiognomy_mind_ode', 'benevolent_brotherly', 'buddha_mouth_snake_heart', 'start_diligent_end_lazy']
    
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
        book_id="yuanhaiziping",
        chapter="",
        l1_anchor="yhzp_v1.0.0_相心赋_001_L1",
    )
    version: str = "1.0.0"
