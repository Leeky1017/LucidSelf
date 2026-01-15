"""
Auto-generated semantic module for zhouyi
Generated at: 2025-12-05T13:30:19.919158
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
    semantic_id="zy_v1.0.0_咸卦_001",
    book_id="zhouyi",
    engine_id="yijing"
)
class 咸卦(SemanticEntry):
    """
    - **原文（source_text）**：

  【卦辞】
  咸：亨，利贞，取女吉。

  【彖传】
  《彖》曰："咸，感也。柔上而刚下，二气感应以相与。止而说，男下女，是以'亨，利贞，取女吉'...
    """
    
    original_text: str = """- **原文（source_text）**：

  【卦辞】
  咸：亨，利贞，取女吉。

  【彖传】
  《彖》曰："咸，感也。柔上而刚下，二气感应以相与。止而说，男下女，是以'亨，利贞，取女吉'也。天地感而万物化生，圣人感人心而天下和平。观其所感，而天地万物之情可见矣。"

  【象传】
  《象》曰：山上有泽，咸；君子以虚受人。

  【爻辞】
  初六，咸其拇。
  六二，咸其腓，凶，居吉。
  九三，咸其股，执其随，往吝。
  九四，贞吉，悔亡；憧憧往来，朋从尔思。
  九五，咸其脢，无悔。
  上六，咸其辅颊舌。

- 分字分词释义：

  - **咸**：本义为皆、都，引申为感应遍及；卦名指"感应"之道。
  - **亨，利贞，取女吉**：通达、利于守正，并且以"娶女"之事为象，指感应、结合之和谐得宜。
  - **感**：相互感通、被触动，而非单向支配。
  - **柔上而刚下，二气感应以相与**：上卦为兑柔，下卦为艮刚，阴在上、阳在下，二气相互感应、互相成就。
  - **止而说，男下女**：下艮为止，上兑为悦，男下女象征主动者下行而求和，非高压强求。
  - **虚受人**：虚其心以容人之情，保持内在空间，不以己意压人。
  - **咸其拇 / 腓 / 股 / 脢 / 辅颊舌**：从脚趾、腿肚、大腿、背脊到口舌，象征"感"的层级与部位，从外在行动一路上升到言语与表情。
  - **憧憧往来，朋从尔思**：人群往来不绝，朋友顺从你的想法，象征社交感应之盛。

- **规范化释义（primary_lang_explained）**：

  咸卦讲的是"感应之道"，特别是人与人之间、阴与阳之间如何相互感通而达成和谐。卦辞说："咸：亨，利贞，取女吉。"——说明在适当的感应之下，关系可以通达而顺利，利于守正，并且以"娶女"为象，暗示在亲密结合之事上尤须把握感应的和谐与时机。

  彖传从卦象切入：柔在上、刚在下，上兑为悦，下艮为止，构成"止而说、男下女"的图景——主动者放下身段，以恭敬与喜悦的方式接近对方；阴柔在上，保持适度回应。这样，二气才能真正"感应以相与"。进一步说，天地之间也是通过"感"来化生万物，圣人通过感化人心而成就天下和平，因此观察一个系统"所感为何"，便可以洞见它的真实状态。

  象传"山上有泽，咸；君子以虚受人"则把感应落实为修养方法：山在下、泽在上，水气浸润山体，象征内在既稳重又能被滋润。君子因此学会"虚受"——在心中留出空间，听取他人、承接他人的情感与信息，而不是预设立场强行投射。

- **完整对等诠释（secondary_lang_full）**：

  The Hexagram Xian (Influence/Mutual Attraction) represents the principle of resonance and sympathetic response between two parties. The image of a lake above a mountain shows how stillness below receives the moistening influence from above, creating a natural dynamic of mutual influence. The Judgment "Influence: Success, favorable to persist, taking a wife brings fortune" indicates that genuine responsiveness—not control—leads to harmony. The hexagram teaches that in all relationships, from personal intimacy to social connection, the key lies in being receptive without losing one's center, allowing feelings to flow naturally through progressively deeper levels of engagement.

- 核心要点：

  - 咸卦的核心是**"以感通代替强控"**：通过真诚感应与互动，而非单向支配。
  - 从"拇、腓、股、脢、辅颊舌"的层级结构，展示感应从身体末梢到心志、言语的逐层深入。
  - 各爻通过“止而说”“憧憧往来”等象，展示从合宜感应到过度随从、以至失去自我的连续光谱。

- 详细解说：

  卦象上兑下艮：下卦艮为止，如山；上卦兑为泽，为悦。山上有泽，水气从上而下浸润山体，如同外在环境与他人情绪不断渗入我们的内在。若山体坚实而非刚硬，泽水得其所处，则形成健康的"感"结构。

  爻辞以身体部位为序，描绘感应的不同层次：初六"咸其拇"只是脚趾之感，象征动机刚刚萌芽，还停留在表层；六二"咸其腓，凶，居吉"提示：若只是腿肚躁动地想行动，贸然前往会有凶象，但若安居守位则可转吉；九三"咸其股，执其随，往吝"则指出，当感应到了大腿层面，欲随人而动时，若一味执着跟随他人，会导致难堪与后悔。
  九四"贞吉，悔亡；憧憧往来，朋从尔思"是相对理想的社交状态：保持正道，则悔恨可以消除；人来人往、朋友顺从你的想法，但这并非操控，而是建立在可信与共鸣之上。九五"咸其脢，无悔"则象征感应深入到背脊——既非表层情绪，也非单一动作，而是结构性的姿态。上六"咸其辅颊舌"则提醒：当感应到达口舌层面，如果流于滔滔不绝的言语，容易陷入浅薄的共鸣或空洞的说服，需要格外谨慎。

- **校勘与字词辨析（双语）**：
- **叙事素材（narrative_snippets）**：
  - `[ns_zhouyi_281]` `[trigger: 卦=咸 AND 卦辞=亨利贞取女吉]` `[factor_trigger: zhouyi_gua_xian AND zhouyi_guaci]` `[role: 主干]` 咸，亨利贞，取女吉：以感应之道，交感则通。 → 《周易·咸卦·卦辞》
  - `[ns_zhouyi_282]` `[trigger: 卦=咸 AND 彖传]` `[factor_trigger: zhouyi_gua_xian AND zhouyi_tuan AND zhouyi_nannu_xianggan AND zhouyi_xian_result]` `[role: 主干依赖]` 感也。柔上而刚下，二气感应以相与。 → 《周易·咸卦·彖传》
  - `[ns_zhouyi_283]` `[trigger: 卦=咸 AND 象传=山上有泽]` `[factor_trigger: zhouyi_gua_xian AND zhouyi_xiang]` `[role: 主干依赖]` 山上有泽，咸；君子以虚受人：山承泽润，以虚心感物。 → 《周易·咸卦·象传》
  - `[ns_zhouyi_284]` `[trigger: 卦=咸 AND 初六=咸其拇]` `[factor_trigger: zhouyi_gua_xian]` `[role: 条件分支]` 咸其拇：感应始于脚趾，尚在初动。 → 《周易·咸卦·爻辞》
  - `[ns_zhouyi_285]` `[trigger: 卦=咸 AND 六二=咸其腓]` `[factor_trigger: zhouyi_gua_xian]` `[role: 例外处理]` 咸其腓，凶；居吉：感应及腿，躁动则凶。 → 《周易·咸卦·爻辞》
  - `[ns_zhouyi_286]` `[trigger: 卦=咸 AND 九三=咸其股]` `[factor_trigger: zhouyi_gua_xian]` `[role: 条件分支]` 咸其股，执其随：感应及股，随人而动。 → 《周易·咸卦·爻辞》
  - `[ns_zhouyi_287]` `[trigger: 卦=咸 AND 九四=贞吉悔亡]` `[factor_trigger: zhouyi_gua_xian]` `[role: 主干依赖]` 贞吉悔亡，憧憧往来：守正则吉，往来不定则惑。 → 《周易·咸卦·爻辞》
  - `[ns_zhouyi_288]` `[trigger: 卦=咸 AND 九五=咸其脢]` `[factor_trigger: zhouyi_gua_xian]` `[role: 条件分支]` 咸其脢，无悔：感应及背脊，内定而无悔。 → 《周易·咸卦·爻辞》
  - `[ns_zhouyi_289]` `[trigger: 卦=咸 AND 上六=咸其辅颊舌]` `[factor_trigger: zhouyi_gua_xian]` `[role: 总结]` 咸其辅颊舌：感应及面舌，言语过多。 → 《周易·咸卦·爻辞》
  - **中文**：

  - 卦辞"咸：亨，利贞，取女吉"一作"亨，利贞，取女吉"，本稿保留"咸"字后加顿号，以突出卦名与占辞的分界。
  - 爻辞中"拇、腓、股、脢、辅颊舌"等身体部位，本稿在 L1 层仅作直译与位置说明，不提前引申任何心理学或躯体隐喻，留待高阶层处理。
  - "君子以虚受人"中的"虚"解释为"虚心、留白"，本稿不作"空无"式玄学解读。
  - "憧憧往来，朋从尔思"中"憧憧"释为往来不绝之状，非单纯"迷惘"之意。

  - **English**: Based on Wang Bi commentary edition. Punctuation modernized for readability while preserving original characters. Classical terminology maintained without arbitrary modernization."""
    normalized_text_zh: str = """"""
    subject: str = "咸卦（䷞）"
    factor_refs: list = ['zhouyi_gua_031', 'concept_yinyang_resonance_proposal', 'concept_open_reception_proposal', 'relation_male_below_female_proposal', 'symbol_influence_back_proposal']
    
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
        book_id="zhouyi",
        chapter="",
        l1_anchor="zy_v1.0.0_咸卦_001_L1",
    )
    version: str = "1.0.0"
