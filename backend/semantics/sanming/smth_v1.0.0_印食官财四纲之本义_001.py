"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.458131
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
    semantic_id="smth_v1.0.0_印食官财四纲之本义_001",
    book_id="sanming",
    engine_id="bazi"
)
class 印食官财四纲之本义(SemanticEntry):
    """
    - **原文（source_text）**：
  徐子平论格局，独以印、食、官、财四者为纲。其立名之义云何？盖造化流行天地间，不过阴阳五行而已。阴阳五行，交相为用，不过生克制化而已。今指甲乙为例，以日...
    """
    
    original_text: str = """- **原文（source_text）**：
  徐子平论格局，独以印、食、官、财四者为纲。其立名之义云何？盖造化流行天地间，不过阴阳五行而已。阴阳五行，交相为用，不过生克制化而已。今指甲乙为例，以日干论甲乙，在五行属木，甲阳而乙阴也。如人命得甲乙，生谓之日主属我，生我者壬癸水，我生者丙丁火，克我者庚辛金，我克者戊己土，而十干尽之矣。
  
  生我者，有父母之义，故立名印绶。印，荫也。绶，受也。譬父母有恩德荫庇子孙，子孙得受其福。朝廷设官分职，畀以印绶，使之掌管。官而无印，何所凭据？人无父母，何所怙恃？其理通一无二，故曰印绶。
  
  我生者，有子孙之义，故立名食神。食者，如虫之食物，盖伤之也。虫得食物，则饱；人得食，则益；被食，则损造化。以子成而致养，即人子致养父母之道也，故曰食神。
  
  克我者，我受制于人之义，故立名官煞。官者，官也；煞者，害也。朝廷以官与人，以身属之公家，任其驱使，赴汤蹈火，不敢有违，至于盖棺而后已，是官害之也。凡人梦棺而得官，亦是此义，故曰官煞。
  
  我克者，是人受制于我之义，故立名妻财。如人成家立产，须得妻室内助，故曰妻财。是四者，术家立名之大义。然生近乎身，克隔乎位，造化喜生恶煞，乃自然之理也。
  
  中间阴阳从类，阴阳配合，各有至理存焉。生我、我生，如壬生甲、癸生乙，甲食丙、乙食丁，是阴生阴，阳生阳，阴食阴，阳食阳，为阴阳各从其类，故甲喜壬生死，木滋死水中，则多年不坏；不喜癸生死，木被雨水淋漓，不逾所，则朽。甲喜食丙，以丙能制庚煞，而甲始得安其身；不喜食丁，以丁能伤官，而甲不得成其材，以其义也。
  
  克我、我克，如辛克甲，庚克乙，甲克己，乙克戊，是阴克阳，阳克阴，阴匹阳，阳匹阴，取相制而有情。故甲以辛为官，以己为妻，顺也；甲以庚为煞，以戊为财，逆也。如甲逢庚，则阳遇阳，刚遇刚，无制伏，则力足相伤，故庚不能作甲官，而反为煞；甲逢戊，则阳见阳，不能为室家相依，故戊不能为甲妻，而反为财矣。他干仿此。是以五行生克制化之妙，不过顺逆相成而已。

- 分字分词释义：
  - **印、食、官、财四纲**：以"生我、我生、克我、我克"四类五行关系，分别命名为印绶、食神、官煞、妻财，是子平格局体系的总纲。
  - **印绶**："印"本指官印，"绶"为系印之带，引申为父母、长辈、制度之荫庇与凭据，象征生我者之恩德。
  - **食神**："食"本有"啖食、损物"之意，原文以"虫得食则饱，人得食则益，被食则损造化"说明"我生"本耗我之气，再升华为子孙奉养父母之义。
  - **官煞**：统称克我之星，"官"为有制之权柄，"煞"为无制之害力；有制则为官，无制则为煞，皆由克我之五行而来。
  - **妻财**：我所克者，一方面为财物可制，另一方面比附为妻室内助，故曰妻财，兼具经济与婚姻之象。
  - **阴阳从类**：阴生阴、阳生阳，阴食阴、阳食阳，为同类相生相食，力量纯一；与阴阳配合（阴克阳、阳克阴）相比，作用与吉凶有别。
  - **顺逆相成**：阴阳配合、克生有情者谓之顺，如甲以辛为官、己为妻；同性相见、刚柔失中者谓之逆，如甲以庚为煞、戊为财。

- **规范化释义（primary_lang_explained）**：
  本段说明子平命理为什么以"印、食、官、财"四者为纲。天地间的一切变化，归根结底不过阴阳与五行的流行，而五行之间又不过"生我、我生、克我、我克"四种基本关系。以甲乙木日主为例：生我者壬癸水，好比父母生养子女，所以叫印绶；我生者丙丁火，好比子孙奉养父母，所以叫食神；克我者庚辛金，好比官府约束、驱使我，所以叫官煞；我克者戊己土，好比妻室与财产，是我可以支配、经营的对象，所以叫妻财。四种关系既对应五行，又对应人伦，构成命理立名的根本。
  
  但作者并不止步于此，而进一步强调阴阳的精细分化：同为"生我"，壬生甲、癸生乙在阴阳上有从类与不从类之别；同为"我生"，甲食丙、乙食丁在阴阳上也有差异；同为"克我"，辛克甲、庚克乙的阴阳配合亦不同。甲木喜壬水生而不喜癸水过润，喜食丙火以制庚煞而不喜丁火伤官，说明同类之生未必尽善，配合得当才是真正的"有情"。由此推出：甲以辛为官、己为妻，是顺中有节；甲以庚为煞、戊为财，是逆而易伤。这就是"顺逆相成"在印食官财四纲中的具体体现。
  - **English**：
    - Pattern (格局) terms explained systematically; classical judgments contextualized with conditional logic.

- **完整对等诠释（secondary_lang_full）**：
  Xu Ziping builds his whole pattern system on four key relations called Seal, Food, Official and Wealth. They are not arbitrary labels but names drawn from how the five elements generate and restrain one another around the day-stem. Taking Jia-Yi wood as the example, the day-master itself is "me"; the water that gives birth to it (Ren and Gui) stands for parents and benefactors and so is called Seal; the fire that it in turn produces (Bing and Ding) stands for children, enjoyment and output and so is called Food God; the metal that restrains it (Geng and Xin) stands for public authority and constraint and so is called Official or Killing; the earth that it can control (Wu and Ji) stands for resources and partners and so is called Wife and Wealth. In this way the four movements "generates me, I generate, restrains me, I restrain" are mapped to four human relationships and made into the backbone of all later pattern names.
  He then refines this simple scheme with yin-yang nuance. When yin gives birth to yin and yang to yang—such as Ren nurturing Jia or Gui nurturing Yi, Jia "eating" Bing or Yi "eating" Ding—the force is of one kind and therefore pure; when yin and yang meet in mutual restraint—such as Xin restraining Jia, Geng restraining Yi, Jia restraining Ji or Yi restraining Wu—the outcome depends on whether the relationship is gentle and "affectionate" or hard and excessive. Thus Jia taking Xin as Proper Official and Ji as Wife is a smooth, well-matched configuration, whereas Jia taking Geng as Killing and Wu as Wealth is a contrary, potentially damaging one. From this perspective, all the subtleties of later patterns—Proper Official, Seven Killing, Seal, Food, Wealth structures and so on—are different ways in which these four basic ties of generation and restraint, in their yin-yang harmony or conflict, cooperate to produce fortune or misfortune.

- 核心要点：
  - **一切格局皆从四纲出**：印绶、食神、官煞、妻财四者，囊括所有"生我、我生、克我、我克"关系，是全书格局体系的总纲。
  - **人伦比附是命名之本**：以父母、子孙、官府、妻室四种人伦形象，比附四种五行关系，使抽象的生克化为可理解的社会角色。
  - **阴阳与顺逆决定吉凶层次**：同一五行关系，在不同阴阳配合下有"顺"与"逆"之别。顺者多成正格，逆者或为偏格，或需更多制化调剂。
  - **"造化喜生恶煞"**：自然之理偏向于生扶，不喜过度克害。判盘时，应先看生我与我生之结构，再审官煞与妻财之强弱与得失。

- 详细解说：
  此节实为卷五乃至全书格局篇的总序。作者一开始就把"印、食、官、财"提到"四纲"的高度，说明后面所有"正官、偏官、正财、偏财、印格、食神格"等无数变格，都只是围绕这四个角色做组合与权衡。其精妙之处在于：一方面以极简的五行生克关系为出发点，另一方面又通过人伦类比，将抽象的数学结构嵌入深厚的文化语境中，使读者一见"印"便知其为父母之恩，一见"官"便知其为制约之力，一见"食"便知其为子孙、享受与耗泄，一见"财"便知其为资源、妻室与现实利益。
  
  同时，作者在这一节就埋下了"阴阳从类"与"顺逆相成"两条主线。无论是壬生甲、癸生乙，还是甲食丙、乙食丁，抑或辛克甲、庚克乙、甲克己、乙克戊，都是在用具体组合告诉读者：命理不是简单看"谁生谁、谁克谁"，而要看阴阳是否相配、力量是否均衡、关系是否有情。后文论正官、偏官、弃命从煞等格局时，反复用到"有制则贵、无制则凶"、"顺逆得当"等原则，皆以此节为理论根基。

- 校勘与字词辨析：
  - "印，荫也"：此处"荫"作"庇护"解，古书常用同音假借字，现代整理时保留原字，并在释义中点明。
  - "梦棺而得官"：古人占梦，梦见棺材主得官，因"棺"与"官"音近，并取"盖棺论定"之意，此处用来说明"官煞"之内在联系。
  - "造化喜生恶煞"：原文指出自然之理偏向"生我、我生"而不喜过度"克我"，为后文许多格局的价值判断埋下伏笔。
  - "他干仿此"：指甲乙之外，丙丁戊己庚辛壬癸诸干，皆可按同样思路推演其印、食、官、财的阴阳顺逆结构。
  - **English**：
    - Yin-yang forward-reverse structure of Food, Official, Wealth.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_05_001]` `[trigger: 四纲立名]` `[factor_trigger: shishen_four_pillars_framework]` `[role: 主干]` 印绶、食神、官煞、妻财四者，囊括所有"生我、我生、克我、我克"关系，是全书格局体系的总纲。 → 《三命通会》卷五#印食官财
  - `[ns_smth_05_002]` `[trigger: 阴阳从类]` `[factor_trigger: yinyang_congzhu_profile]` `[role: 主干依赖]` 阴生阴、阳生阳，阴食阴、阳食阳，为同类相生相食，力量纯一。 → 《三命通会》卷五#印食官财
  - `[ns_smth_05_003]` `[trigger: 顺逆相成]` `[factor_trigger: shun_ni_xiangcheng_axis]` `[role: 主干依赖]` 甲以辛为官、己为妻，顺也；甲以庚为煞、戊为财，逆也。 → 《三命通会》卷五#印食官财
  - `[ns_smth_05_004]` `[trigger: 造化喜生]` `[factor_trigger: zaohua_xisheng_principle]` `[role: 总结]` 造化喜生恶煞，乃自然之理也。 → 《三命通会》卷五#印食官财"""
    normalized_text_zh: str = """"""
    subject: str = "印食官财四纲之本义"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'shishen_four_pillars_framework', 'bazi_semantic', 'wuxing_sheng_ke_to_shishen', 'bazi_semantic', 'yinyang_congzhu_profile', 'bazi_semantic', 'shun_ni_xiangcheng_axis', 'bazi_semantic', 'zaohua_xisheng_principle', 'bazi_semantic', 'renlun_bifu_framework', 'bazi_semantic', 'yinyang_youqing_condition', 'bazi_semantic', 'source_ref', 'rel_smth_05_001', 'shishen_four_pillars_framework', 'rel_smth_05_002', 'zaohua_xisheng_principle', 'rel_smth_05_003', 'yinyang_youqing_condition', 'evi_smth_05_001', 'shishen_four_pillars_framework', 'rule_four_pillars', 'evi_smth_05_002', 'zaohua_xisheng_principle', 'rule_xisheng', 'evi_smth_05_003', 'yinyang_youqing_condition', 'rule_youqing', 'map_smth_05_001', 'map_smth_05_002']
    
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
        book_id="sanming",
        chapter="",
        l1_anchor="smth_v1.0.0_印食官财四纲之本义_001_L1",
    )
    version: str = "1.0.0"
