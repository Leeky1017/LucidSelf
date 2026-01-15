"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.412869
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
    semantic_id="smth_v1.0.0_金白水清与金水文贵之象_001",
    book_id="sanming",
    engine_id="bazi"
)
class 金白水清与金水文贵之象(SemanticEntry):
    """
    - **原文（source_text）**：

  赋云：金白水清，此辈宜登科第。此象乃庚申、辛酉日生秋月令，引到时上遇亥子水乡，以金则白，以水则清，无刑冲破害，主富厚。切忌夏生，则不入格，春金二三月...
    """
    
    original_text: str = """- **原文（source_text）**：

  赋云：金白水清，此辈宜登科第。此象乃庚申、辛酉日生秋月令，引到时上遇亥子水乡，以金则白，以水则清，无刑冲破害，主富厚。切忌夏生，则不入格，春金二三月，运行西北亦可。如庚辰、庚子、癸巳、癸酉、癸丑等日，生秋冬月令，无火伤，无土制，见金水相停成局，亦是。诗曰：金清水白主荣贵，秀丽文章定出群，更无火土来刑制，声誉掀腾翰苑人。

- 分字分词释义：

  - **金白水清**：以金之纯白、水之清澈比喻格局气质清正、不杂浊气，主文章清秀、名誉出众。
  - **庚申、辛酉日生秋月令**：庚申、辛酉本属金旺之地，再逢秋令（金当令），金气尤盛。
  - **时上遇亥子水乡**：时支落在亥子等水地，水来承接金气，使金水相生，成“金白水清”之象。
  - **无刑冲破害，主富厚**：若四柱中无严重刑冲破害，则此清金清水之局易主富贵厚实。
  - **切忌夏生，则不入格**：夏月火旺，火克金、蒸水，破坏金水清润之象，故夏生多难成此格。
  - **春金二三月，运行西北亦可**：春金虽不及秋金之旺，若行西北金水之运，亦可成就一部分金白水清之象。

- **规范化释义（primary_lang_explained）**：

  金白水清格，是以庚申、辛酉等金日生于秋月，再在时上遇亥子水乡为典型的金水清润之局。秋金当令，金性坚明；亥子之水清而不浊，得金所生而益显其清光。金白水清，象征一个人的才情与气质既刚正而不偏激，又清朗而不混浊，故原文说“此辈宜登科第”，多主文章清秀、科名之贵。

  原文强调：成格之要在于“金水相停而不受火土破害”。若火来伤金、土来浊水，则清气减损，难以论为上乘；若生于夏令，火旺克金，水被煎熬，更不入格。相对地，即便不是秋月，只要金水之气仍能相生、且行运多在西北金水之乡，也可得“次一等”的金白水清之象，主富厚与文名兼具。

- 核心要点：

  - 以**秋金日 + 时上亥子水**为典型，金旺而不杂，水清而不浊。
  - 忌火土过重破坏金水之清气，尤其夏令与火土混杂之局。
  - 行运得西北金水之乡，则更能发挥文章、科名与富贵之象。

- 详细解说：

  从格局结构看，金白水清兼具“刚与柔、收与流”的双重特性：金主收敛与裁决，水主流动与通达。秋金得令时，人的性格多偏理性、严谨；若再得清水相助，则严谨中有灵动，理性中有通融，容易在学术、文字、法律、策划等领域表现出色。

  若金旺而无水，则易成过度刚硬、偏于刻薄之象；若水多而金弱，则易流于漂浮、缺乏原则。金白水清格正是借由金水相停，达到“有准绳而不拘泥，有灵动而不散乱”的平衡。火土若介入过多，一则伤金，一则浊水，破坏这一平衡，故原文屡言“忌火土刑制”。

- **校勘与字词辨析（双语）**：

  - “金白水清，此辈宜登科第”一句，本稿在白话中理解为“文章清秀、科名利学”的象意，而非局限于科举制度本身。
  - “无刑冲破害，主富厚”一句，本稿将其展开为对“少刑冲、少破害”的结构要求，并在详细解说中以性格与职业倾向的方式呈现。
  - 诗句“金清水白主荣贵，秀丽文章定出群，更无火土来刑制，声誉掀腾翰苑人”，本稿提炼为“文章清丽、名誉隆起”的总评，而不逐句拆译。
  - **English**：
    - Overall assessment provided without sentence-by-sentence translation.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_06_201]` `[trigger: 金白水清]` `[factor_trigger: jinbaishuiqing_presence AND qiujin_shuiqing]` `[role: 主干]` 金白水清，此辈宜登科第。 → 《三命通会》卷六#金白水清
  - `[ns_smth_06_202]` `[trigger: 秋金入格]` `[factor_trigger: gengshenxinyou_qiuyue AND haiziwater]` `[role: 主干依赖]` 庚申、辛酉日生秋月令，引到时上遇亥子水乡。 → 《三命通会》卷六#金白水清
  - `[ns_smth_06_203]` `[trigger: 忌夏生]` `[factor_trigger: qieji_xiasheng AND buruge]` `[role: 条件分支]` 切忌夏生，则不入格。 → 《三命通会》卷六#金白水清
  - `[ns_smth_06_204]` `[trigger: 文章出群]` `[factor_trigger: wuhuotu_xingzhi AND shenyu_hanyuan]` `[role: 总结]` 秀丽文章定出群，声誉掀腾翰苑人。 → 《三命通会》卷六#金白水清"""
    normalized_text_zh: str = """"""
    subject: str = "金白水清与金水文贵之象"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_metal_water_marker', 'bazi_semantic', 'bazi_structure_metal_water_config', 'bazi_semantic', 'bazi_state_degree_34', 'bazi_semantic', 'bazi_state_factor_33', 'bazi_semantic', 'bazi_condition_factor_214', 'bazi_semantic', 'bazi_condition_fire_earth_4', 'bazi_semantic', 'source_ref', 'rel_smth_06_178', 'jinbaishuiqing_presence', 'rel_smth_06_179', 'xiuqi_chengdu', 'rel_smth_06_180', 'xiasheng_buruge_risk', 'evi_smth_06_178', 'jinbaishuiqing_presence', 'rule_jinbaishuiqing', 'evi_smth_06_179', 'wengui_fadadu', 'rule_dengke', 'evi_smth_06_180', 'xiasheng_buruge_risk', 'rule_xiasheng', 'map_smth_06_119', 'map_smth_06_120']
    
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
        l1_anchor="smth_v1.0.0_金白水清与金水文贵之象_001_L1",
    )
    version: str = "1.0.0"
