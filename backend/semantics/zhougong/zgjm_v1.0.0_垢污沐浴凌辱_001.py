"""
Auto-generated semantic module for zhougong
Generated at: 2025-12-05T13:30:19.885364
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
    semantic_id="zgjm_v1.0.0_垢污沐浴凌辱_001",
    book_id="zhougong",
    engine_id="dream"
)
class 垢污沐浴凌辱(SemanticEntry):
    """
    - **原文（source_text）**：

  尿屎污身主得财，大便满地主富贵。处厕中得官禄位。  
  落厕出吉不出凶，厕屋上卧主得财。厕中干者主家破。  
  架厕屋主有财喜，挑粪回家大吉利。...
    """
    
    original_text: str = """- **原文（source_text）**：

  尿屎污身主得财，大便满地主富贵。处厕中得官禄位。  
  落厕出吉不出凶，厕屋上卧主得财。厕中干者主家破。  
  架厕屋主有财喜，挑粪回家大吉利。在泥中所求不成。  
  失大小便主失财，污泥衣裳主产凶。泥污衫衣主身辱。  
  男女沐浴上床凶，沐浴尘土疾病安。洗头迁居疾病除。  
  被辱骂惹人词讼。

- 分字分词释义：

  - **尿屎污身、大便满地**：排泄物污染身体或满地，在梦象中反主得财与富贵（逆反之象）。
  - **处厕中**：在厕所中，反主得官禄位。
  - **落厕出吉不出凶**：跌入厕所能出来为吉，出不来为凶。
  - **厕屋上卧**：在厕所屋顶躺卧，反主得财。
  - **厕中干者**：厕所干燥无污秽，反主家破（逆反之象）。
  - **架厕屋、挑粪回家**：建造厕所或挑粪回家，皆主财喜与吉利。
  - **失大小便**：失禁或无法控制排泄，主失财。
  - **污泥衣裳、泥污衫衣**：泥土污染衣服，主产凶与身辱。
  - **沐浴尘土**：洗去尘土污垢，主疾病安定。
  - **洗头**：洗头清洁，主迁居与疾病除去。
  - **被辱骂**：被人辱骂，主惹人词讼。

- **规范化释义（primary_lang_explained）**：

  本类条目围绕"垢污沐浴凌辱"展开，揭示梦象学中对**污秽、清洁与尊严**的独特解读——其中最显著的特点是"污秽主财"的逆反逻辑：尿屎污身主得财，大便满地主富贵，处厕中得官禄位，厕屋上卧主得财，架厕屋、挑粪回家皆主财喜。然而，厕中干燥反主家破，失大小便主失财，体现"有污则财聚、无污则财散"的特殊象征。清洁与沐浴则主健康与迁移：沐浴尘土主疾病安，洗头主迁居疾病除。污泥衣裳主产凶与身辱，被辱骂主词讼。

- 核心要点：

  - **污秽主财的逆反逻辑**：尿屎污身、大便满地、处厕中、架厕屋、挑粪回家皆主得财富贵。
  - **厕所干燥反主凶**：厕中干者主家破，体现"有污则聚、无污则散"。
  - **出入自如为吉**：落厕能出为吉，不能出为凶。
  - **失控主失财**：失大小便（失去控制）主失财。
  - **清洁主健康与迁移**：沐浴尘土主疾病安，洗头主迁居疾病除。
  - **泥污衣裳主凶辱**：污泥衣裳主产凶，泥污衫衣主身辱。

- 详细解说：

  **（一）污秽主财：最强的逆反象征**

  本类最显著的特点是"污秽主财"的逆反逻辑，构成周公解梦中最极端的逆反象征之一："尿屎污身主得财，大便满地主富贵，处厕中得官禄位，厕屋上卧主得财，架厕屋主有财喜，挑粪回家大吉利"六句，皆将最污秽、最不雅之物转化为财富与官位的象征。

  这种逆反逻辑的背后，蕴含着古代农耕文明对粪肥的实用价值认知：粪便是最重要的肥料，直接关系到土地肥沃与收成好坏，因此在潜意识层面被视为"财富之源"。同时，污秽与黄金、土地的颜色相近，在象征层面也产生联系。

  **（二）厕所干燥反主凶：有污则聚、无污则散**

  "厕中干者主家破"一句，与前述"污秽主财"构成对比：厕所本应有污秽，若厕所干燥无物，反主家破。这体现"有污则聚、无污则散"的逻辑——污秽象征财富聚集，干燥象征财富散失。

  **（三）出入自如与失控**

  "落厕出吉不出凶"与"失大小便主失财"两句，揭示"控制"的重要性：跌入厕所能自如出来为吉（保持控制），出不来为凶（失去控制）；失大小便（失去控制）主失财。这体现对"自主与失控"的深层焦虑。

  **（四）清洁主健康与迁移**

  "沐浴尘土疾病安，洗头迁居疾病除"两句，揭示清洁的正向功能：洗去尘土污垢主疾病安定，洗头主迁居与疾病除去。这与"污秽主财"的逆反逻辑不同，清洁在健康与迁移层面仍保持正向象征。

  **（五）泥污衣裳与身辱**

  "污泥衣裳主产凶，泥污衫衣主身辱"两句，提示泥土污染衣服（而非排泄物）主凶与辱。这是因为泥土污染象征"形象受损""尊严丧失"，与排泄物的"财富象征"不同。

  **（六）被辱骂主词讼**

  "被辱骂惹人词讼"一句，直接揭示语言侵犯与法律纠纷的联系，提示梦者在现实中需注意言语冲突可能升级为诉讼。

- 校勘与字词辨析（本类）：

  - "垢污沐浴凌辱"六字标题按底本录入，涵盖污秽、清洁与尊严三大主题。
  - "尿屎污身主得财，大便满地主富贵"两句为典型逆反之象，本稿在释义中特别标注其背后的农耕文明逻辑。
  - "厕中干者主家破"一句，与"污秽主财"构成对比，体现"有污则聚、无污则散"。
  - "男女沐浴上床凶"一句，原文未详解，本稿据常见解梦传统释为"异性共浴主情色纠纷"。
  - "被辱骂惹人词讼"一句，直接揭示语言侵犯与法律纠纷的联系。

- **叙事素材（narrative_snippets）**：

  - `[ns_zgjm_1086]` `[trigger: 梦见尿屎污身]` `[factor_trigger: dream_feces_body_2]` `[role: 主干]` 尿屎污身，主得财。 → 《周公解梦·垢污沐浴凌辱》
  - `[ns_zgjm_1087]` `[trigger: 梦见大便满地]` `[factor_trigger: dream_feces_ground_2]` `[role: 主干]` 大便满地，主富贵。 → 《周公解梦·垢污沐浴凌辱》
  - `[ns_zgjm_1088]` `[trigger: 梦见处厕中]` `[factor_trigger: dream_in_latrine_2]` `[role: 主干]` 处厕中，得官禄位。 → 《周公解梦·垢污沐浴凌辱》
  - `[ns_zgjm_1089]` `[trigger: 梦见落厕出吉不出凶]` `[factor_trigger: dream_fall_latrine_2]` `[role: 主干]` 落厕出吉，不出凶。 → 《周公解梦·垢污沐浴凌辱》
  - `[ns_zgjm_1090]` `[trigger: 梦见厕屋上卧]` `[factor_trigger: dream_lie_latrine_2]` `[role: 主干]` 厕屋上卧，主得财。 → 《周公解梦·垢污沐浴凌辱》
  - `[ns_zgjm_1091]` `[trigger: 梦见厕中干者]` `[factor_trigger: dream_dry_latrine_2]` `[role: 主干]` 厕中干者，主家破。 → 《周公解梦·垢污沐浴凌辱》
  - `[ns_zgjm_1092]` `[trigger: 梦见架厕屋]` `[factor_trigger: dream_build_latrine_2]` `[role: 主干]` 架厕屋，主有财喜。 → 《周公解梦·垢污沐浴凌辱》
  - `[ns_zgjm_1093]` `[trigger: 梦见挑粪回家]` `[factor_trigger: dream_carry_manure_2]` `[role: 主干]` 挑粪回家，大吉利。 → 《周公解梦·垢污沐浴凌辱》
  - `[ns_zgjm_1094]` `[trigger: 梦见在泥中]` `[factor_trigger: dream_in_mud_2]` `[role: 主干]` 在泥中，所求不成。 → 《周公解梦·垢污沐浴凌辱》
  - `[ns_zgjm_1095]` `[trigger: 梦见失大小便]` `[factor_trigger: dream_lose_excrement_2]` `[role: 主干]` 失大小便，主失财。 → 《周公解梦·垢污沐浴凌辱》
  - `[ns_zgjm_1096]` `[trigger: 梦见污泥衣裳]` `[factor_trigger: dream_mud_clothes_2]` `[role: 主干]` 污泥衣裳，主产凶。 → 《周公解梦·垢污沐浴凌辱》
  - `[ns_zgjm_1097]` `[trigger: 梦见泥污衫衣]` `[factor_trigger: dream_dirty_shirt_2]` `[role: 主干]` 泥污衫衣，主身辱。 → 《周公解梦·垢污沐浴凌辱》
  - `[ns_zgjm_1098]` `[trigger: 梦见男女沐浴上床]` `[factor_trigger: dream_bathe_bed_2]` `[role: 主干]` 男女沐浴上床，凶。 → 《周公解梦·垢污沐浴凌辱》
  - `[ns_zgjm_1099]` `[trigger: 梦见沐浴尘土]` `[factor_trigger: dream_dust_bath_2]` `[role: 主干]` 沐浴尘土，疾病安。 → 《周公解梦·垢污沐浴凌辱》
  - `[ns_zgjm_1100]` `[trigger: 梦见洗头迁居]` `[factor_trigger: dream_wash_head_2]` `[role: 主干]` 洗头迁居，疾病除。 → 《周公解梦·垢污沐浴凌辱》
  - `[ns_zgjm_1101]` `[trigger: 梦见被辱骂惹人]` `[factor_trigger: dream_humiliated_2]` `[role: 主干]` 被辱骂惹人，词讼。 → 《周公解梦·垢污沐浴凌辱》"""
    normalized_text_zh: str = """"""
    subject: str = "垢污沐浴凌辱"
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
        l1_anchor="zgjm_v1.0.0_垢污沐浴凌辱_001_L1",
    )
    version: str = "1.0.0"
