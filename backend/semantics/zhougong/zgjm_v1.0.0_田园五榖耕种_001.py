"""
Auto-generated semantic module for zhougong
Generated at: 2025-12-05T13:30:19.885320
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
    semantic_id="zgjm_v1.0.0_田园五榖耕种_001",
    book_id="zhougong",
    engine_id="dream"
)
class 田园五榖耕种(SemanticEntry):
    """
    - **原文（source_text）**：

  田中生草主得财，种田广大有禄位。自种田禾主出行。  
  见种田者禄位至，教人耕种远行至。使人种田地大吉。  
  买人田宅主进职，身在禾中大吉利。...
    """
    
    original_text: str = """- **原文（source_text）**：

  田中生草主得财，种田广大有禄位。自种田禾主出行。  
  见种田者禄位至，教人耕种远行至。使人种田地大吉。  
  买人田宅主进职，身在禾中大吉利。破败田地主大吉。  
  割收田禾家居安，屋上生禾官位吉。禾苗豊熟富贵长。  
  见麦稻主得大财，粳精米者有财吉。五谷茂盛主得财。  
  谷穗齐秀大吉利，米谷堆吉散主凶。大小麦主妻私心。  
  大豆苗叶子孙凶，米麦相排大吉利。坐卧米麦主大吉。  
  手中把榖主福禄，得禾榖者主大吉。得禾忽失主得志。  
  粟米必有献物至，种菜主长命大吉。乔麦面饼官事迁。  
  面糠相交家欲俭，涓麹必主枉屈事。萌芽者主恶事连。  
  麻丛身者主疾至，麻生如林大吉利。

- 分字分词释义：

  - **田中生草**：田地中长出草木，象征土地生机旺盛，财源自然滋生。
  - **种田广大**：大面积耕种田地，象征事业版图扩张，获得禄位与权责。
  - **自种田禾**：亲自耕种田地，主将有外出、迁移或旅行之事。
  - **见种田者**：梦见他人耕种，主禄位将至或职位提升。
  - **割收田禾**：收割庄稼，象征收获成果，家居安稳。
  - **禾苗丰熟**：庄稼长势良好、成熟饱满，主富贵长久。
  - **米谷堆散**：粮食堆积为吉，四散为凶。
  - **大小麦**：大麦小麦，原文特别指出主"妻私心"，暗示家庭内部隐情。
  - **萌芽**：种子发芽，但原文说"主恶事连"，提示初生之事可能带来麻烦。
  - **麻丛身、麻生如林**：麻围绕身体主疾病，麻成林则主大吉利，呈现两极。

- **规范化释义（primary_lang_explained）**：

  本类条目围绕"田园五谷耕种"展开，揭示梦象学中对**农耕、土地与收成**的解读——大多数情境下，田地茂盛、禾苗丰收、粮食堆积皆主吉利，象征财富积累、事业扩张与家业兴旺。田中生草主得财，种田广大主禄位，割收田禾主家居安，禾苗丰熟主富贵长。然而也有例外：米谷散失为凶，大小麦主妻有私心，萌芽主恶事连，麻丛身主疾病。

- 核心要点：

  - **田地与耕种多主财富与事业**：种田、收割、粮食堆积皆为财富与成果的象征。
  - **丰收与成熟主长久富贵**：禾苗丰熟、五谷茂盛、谷穗齐秀等，皆主富贵与长久兴旺。
  - **粮食聚散有别**：堆积为吉（财富聚集），散失为凶（财富流失）。
  - **特殊作物有特殊含义**：大小麦主妻私心，萌芽主恶事连，麻的吉凶两极。
  - **亲自耕种与见他人耕种有别**：自种主出行，见他人种田主禄位至。

- 详细解说：

  **（一）田地与耕种：财富与事业的根基**

  本类开篇即揭示"田中生草主得财，种田广大有禄位"，构成梦象学中对田地的基本理解：田地象征财富的根基与事业的版图，田中生机旺盛（生草）则财源自然滋生；广大耕种则象征事业扩张与权责增加。

  **（二）亲自耕种与见他人耕种**

  "自种田禾主出行，见种田者禄位至，教人耕种远行至，使人种田地大吉"四句揭示耕种主体的差异：自己亲手耕种，多主将有外出或迁移；见他人耕种或指导他人耕种，则主禄位提升或有远行机会；派遣他人耕种，则为大吉，象征事业有人代劳、资源得以扩张。

  **（三）收割与丰收：成果与安稳**

  "割收田禾家居安，禾苗丰熟富贵长，五谷茂盛主得财，谷穗齐秀大吉利"四句构成"丰收"的完整象征：收割象征成果落袋、家居安定；禾苗丰熟象征长久富贵；五谷茂盛与谷穗齐秀象征全面丰收与大吉。

  **（四）粮食的聚散：财富流向**

  "米谷堆吉散主凶，坐卧米麦主大吉，手中把谷主福禄，得禾谷者主大吉"揭示粮食的聚散吉凶：粮食堆积、坐卧其中、手中握谷，皆主财富聚集与福禄临身；反之，粮食四散则主财富流失。

  **（五）特殊作物的特殊含义**

  原文特别提出"大小麦主妻私心"，提示大小麦在梦象中与家庭内部隐情有关；"萌芽者主恶事连"，说明初生之事可能带来连续麻烦；"麻丛身者主疾至，麻生如林大吉利"，呈现麻的两极吉凶——围身为疾，成林为吉。

  **（六）其他细节**

  "买人田宅主进职"，象征通过购置资产而获得职位提升；"破败田地主大吉"，属逆反之象，破败反而主吉；"屋上生禾官位吉"，象征非常规之地长出庄稼，反主官位提升；"得禾忽失主得志"，象征先得后失反而使志向得以实现。

- 校勘与字词辨析（本类）：

  - "田园五榖耕种"五字标题按底本录入，涵盖田园、五谷与耕种三大主题。
  - "种田广大"一句，"广大"指大面积耕种，本稿释为"事业版图扩张"。
  - "大小麦主妻私心"一句较为特殊，原文未详解，本稿据常见解梦传统释为"家庭内部隐情"。
  - "萌芽者主恶事连"一句，与一般"萌芽主生机"的理解相反，提示初生之事可能带来麻烦。
  - "涓麹"一词，疑为"酒麹"或"发酵物"，原文说"必主枉屈事"，本稿保留原文。

- **叙事素材（narrative_snippets）**：

  - `[ns_zgjm_1046]` `[trigger: 梦见田中生草]` `[factor_trigger: dream_grass_field_2]` `[role: 主干]` 田中生草，主得财。 → 《周公解梦·田园五榖耕种》
  - `[ns_zgjm_1047]` `[trigger: 梦见种田广大]` `[factor_trigger: dream_large_field_2]` `[role: 主干]` 种田广大，有禄位。 → 《周公解梦·田园五榖耕种》
  - `[ns_zgjm_1048]` `[trigger: 梦见自种田禾]` `[factor_trigger: dream_plant_grain_2]` `[role: 主干]` 自种田禾，主出行。 → 《周公解梦·田园五榖耕种》
  - `[ns_zgjm_1049]` `[trigger: 梦见见种田者]` `[factor_trigger: dream_see_farmer_2]` `[role: 主干]` 见种田者，禄位至。 → 《周公解梦·田园五榖耕种》
  - `[ns_zgjm_1050]` `[trigger: 梦见教人耕种]` `[factor_trigger: dream_teach_farm_2]` `[role: 主干]` 教人耕种，远行至。 → 《周公解梦·田园五榖耕种》
  - `[ns_zgjm_1051]` `[trigger: 梦见使人种田地]` `[factor_trigger: dream_hire_farm_2]` `[role: 主干]` 使人种田地，大吉。 → 《周公解梦·田园五榖耕种》
  - `[ns_zgjm_1052]` `[trigger: 梦见买人田宅]` `[factor_trigger: dream_buy_land_2]` `[role: 主干]` 买人田宅，主进职。 → 《周公解梦·田园五榖耕种》
  - `[ns_zgjm_1053]` `[trigger: 梦见身在禾中]` `[factor_trigger: dream_in_grain_2]` `[role: 主干]` 身在禾中，大吉利。 → 《周公解梦·田园五榖耕种》
  - `[ns_zgjm_1054]` `[trigger: 梦见破败田地]` `[factor_trigger: dream_ruined_field_2]` `[role: 主干]` 破败田地，主大吉。 → 《周公解梦·田园五榖耕种》
  - `[ns_zgjm_1055]` `[trigger: 梦见割收田禾]` `[factor_trigger: dream_harvest_2]` `[role: 主干]` 割收田禾，家居安。 → 《周公解梦·田园五榖耕种》
  - `[ns_zgjm_1056]` `[trigger: 梦见屋上生禾]` `[factor_trigger: dream_roof_grain_2]` `[role: 主干]` 屋上生禾，官位吉。 → 《周公解梦·田园五榖耕种》
  - `[ns_zgjm_1057]` `[trigger: 梦见禾苗豊熟]` `[factor_trigger: dream_crops_ripe_2]` `[role: 主干]` 禾苗豊熟，富贵长。 → 《周公解梦·田园五榖耕种》
  - `[ns_zgjm_1058]` `[trigger: 梦见见麦稻]` `[factor_trigger: dream_wheat_rice_2]` `[role: 主干]` 见麦稻，主得大财。 → 《周公解梦·田园五榖耕种》
  - `[ns_zgjm_1059]` `[trigger: 梦见五谷茂盛]` `[factor_trigger: dream_grains_flourish_2]` `[role: 主干]` 五谷茂盛，主得财。 → 《周公解梦·田园五榖耕种》
  - `[ns_zgjm_1060]` `[trigger: 梦见谷穗齐秀]` `[factor_trigger: dream_grain_ears_2]` `[role: 主干]` 谷穗齐秀，大吉利。 → 《周公解梦·田园五榖耕种》
  - `[ns_zgjm_1061]` `[trigger: 梦见米谷堆吉散凶]` `[factor_trigger: dream_grain_pile_2]` `[role: 主干]` 米谷堆吉，散主凶。 → 《周公解梦·田园五榖耕种》
  - `[ns_zgjm_1062]` `[trigger: 梦见大豆苗叶]` `[factor_trigger: dream_bean_leaves_2]` `[role: 主干]` 大豆苗叶，子孙凶。 → 《周公解梦·田园五榖耕种》
  - `[ns_zgjm_1063]` `[trigger: 梦见种菜]` `[factor_trigger: dream_plant_vegetable_2]` `[role: 主干]` 种菜主长命大吉。 → 《周公解梦·田园五榖耕种》
  - `[ns_zgjm_1064]` `[trigger: 梦见萌芽者]` `[factor_trigger: dream_sprout_2]` `[role: 主干]` 萌芽者，主恶事连。 → 《周公解梦·田园五榖耕种》
  - `[ns_zgjm_1065]` `[trigger: 梦见麻生如林]` `[factor_trigger: dream_hemp_forest_2]` `[role: 主干]` 麻生如林，大吉利。 → 《周公解梦·田园五榖耕种》"""
    normalized_text_zh: str = """"""
    subject: str = "田园五榖耕种"
    factor_refs: list = []
    
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
        book_id="zhougong",
        chapter="",
        l1_anchor="zgjm_v1.0.0_田园五榖耕种_001_L1",
    )
    version: str = "1.0.0"
