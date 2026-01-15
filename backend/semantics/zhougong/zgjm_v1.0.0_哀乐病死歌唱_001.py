"""
Auto-generated semantic module for zhougong
Generated at: 2025-12-05T13:30:19.885193
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
    semantic_id="zgjm_v1.0.0_哀乐病死歌唱_001",
    book_id="zhougong",
    engine_id="dream"
)
class 哀乐病死歌唱(SemanticEntry):
    """
    - **原文（source_text）**：

  与人哭泣有庆贺，放声大哭欢乐至。身着孝服官禄至。  
  远人来悲泣主凶，床上哭泣主大凶。见歌舞者口舌至。  
  家中欢喜百事吉，怀中琵琶得人助。...
    """
    
    original_text: str = """- **原文（source_text）**：

  与人哭泣有庆贺，放声大哭欢乐至。身着孝服官禄至。  
  远人来悲泣主凶，床上哭泣主大凶。见歌舞者口舌至。  
  家中欢喜百事吉，怀中琵琶得人助。他人与笛有名声。  
  与人拍板有口舌，堂上歌乐主丧事。吹笙者主有更改。  
  吹笛打鼓有吉庆，他人作乐讼有理。露齿哭者有争讼。  
  病卧为人扶加官，病重者主有凶事。自疾病者主有喜。  
  病人歌唱主大凶，病人哭笑疾病除。病人起者必定死。  
  病人装车必死亡，死人哭泣有口舌。死人立者主大凶。  
  死人哭怀者得财，死人复活主有信。见人死自死者吉。  
  子死者有添喜事，见先亡尊长大吉。问吊他人主生子.

- 分字分词释义：

  - **哭泣**：指梦中流泪、悲伤、哭泣的行为，象征情绪释放与吉凶反转.
  - **放声大哭**：大声哭泣，情绪彻底释放，往往象征压力与悲伤的排解，反而预示欢乐将至.
  - **孝服**：丧服，梦中着孝服往往不主丧事，而主官禄进益，体现梦象的逆反特性.
  - **歌舞**：欢乐歌舞，但梦象中有时反主口舌是非或丧事，需结合场景判断.
  - **琵琶、笛、拍板、笙、鼓**：各类乐器，象征音乐、声名、人际关系与变动信号.
  - **病卧、病重、自疾病**：梦中自己或他人患病，往往反主加官、有喜或疾病去除.
  - **病人歌唱、哭笑、起、装车**：病人在梦中的各种行为，往往预示病情转折或生死结局.
  - **死人哭泣、立、哭怀、复活**：梦中死者的各种状态，往往关联口舌、财物、信息或吉凶反转.
  - **见人死、自死、子死**：梦中见他人或自己死亡，往往不主真实死亡，而主吉庆、喜事或长寿.
  - **先亡尊长**：已故的长辈，梦见往往主吉兆或祖先提示.
  - **问吊**：前往吊唁，梦象中反主生育喜事.

- **规范化释义（primary_lang_explained）**：

  本类条目围绕"哭泣""歌乐""病""死"四个核心主题，揭示梦象学中最典型的**逆反逻辑**：哭泣往往不主悲伤而主欢乐庆贺，着孝服反主官禄提升；病重、自疾反主加官有喜；见死人、自己死亡反主吉庆长寿.But也有例外：远人来悲泣、床上哭泣、堂上歌乐等特定场景，仍主凶事或丧事。乐器如琵琶、笛、鼓等，多主人助、名声与吉庆，但拍板则主口舌。病人歌唱、起身、装车等行为，多主病情转为凶险或死亡；而病人哭笑则反主疾病去除。死者在梦中的状态，如哭怀主得财、复活主有信、见死反主吉，体现梦象对"生死边界"的独特解读.

- 核心要点：

  - **哭泣逆反原则**：与人哭泣、放声大哭、着孝服，多主欢乐庆贺与官禄至，而非真实悲伤.
  - **歌乐双面性**：家中欢喜、吹笛打鼓主吉庆，但堂上歌乐、见歌舞者反主丧事或口舌.
  - **病象逆反**：病卧、病重、自疾病多主加官有喜，而病人歌唱、起身、装车则主凶或死亡.
  - **死象逆反**：见人死、自死、子死多主吉庆喜事，死人哭怀主得财，死人复活主有信.
  - **特定场景例外**：远人来悲泣、床上哭泣、死人立者等，仍主凶事，需警惕边界情形.

- 详细解说：

  **（一）哭泣与孝服：情绪释放与官禄进益**

  本类开篇即揭示梦象学最典型的逆反规律："与人哭泣有庆贺，放声大哭欢乐至，身着孝服官禄至."梦中与人共泣或独自放声大哭，往往预示现实中压力释放后的欢乐与庆贺；着孝服则不主丧事，反而象征通过"承担哀荣责任"而获得官禄提升或身份进益。这一逆反逻辑的心理基础在于：梦中的极度悲伤往往是现实中积压情绪的镜像释放，释放完毕则轻松喜悦随之而来.

  但此逆反并非绝对：若"远人来悲泣"或"床上哭泣"，则转为凶兆。前者暗示远方传来噩耗或不利消息；后者"床上哭泣"则意味梦者在卧榻之上悲泣，卧床本已是"病弱""困顿"之象，再加哭泣则凶上加凶，主大凶.

  **（二）歌乐与乐器：声名与变动的双面象征**

  "家中欢喜百事吉，怀中琵琶得人助，他人与笛有名声"三句揭示"家庭欢乐"与"乐器"的正向象征。然而，"与人拍板有口舌，堂上歌乐主丧事，吹笙者主有更改"三句则展现歌乐的负面或变动一面：拍板往往意味争执与口舌；堂上歌乐反主丧事；吹笙则主变动与更改.

  **（三）病象：逆反与边界**

  "病卧为人扶加官，病重者主有凶事，自疾病者主有喜"三句构成"病象逆反"的基本框架."病人歌唱主大凶，病人哭笑疾病除"则针对"病人"这一特定主体，需额外谨慎解读.

  **（四）死象：逆反与财信**

  "死人哭泣有口舌，死人立者主大凶"揭示死者在梦中的状态."死人哭怀者得财，死人复活主有信"则展现死象的正向转化."见人死自死者吉，子死者有添喜事"构成"死亡逆反"的完整链条.

- 校勘与字词辨析（本类）：

  - "哀乐病死歌唱"六字标题按底本录入，涵盖情绪、音乐、疾病、死亡四大主题.
  - "拍板"指古代打击乐器，释义中已明确其"口舌"象征.
  - "吹笙者主有更改"，"更改"指状态变动、环境转换.
  - "病人起者必定死"，原文"起"作起身行走，非康复之意.
  - "问吊他人主生子"，"问吊"作吊唁，梦象中反主生育喜事.

- **叙事素材（narrative_snippets）**：

  - `[ns_zgjm_954]` `[trigger: 梦见与人哭泣]` `[factor_trigger: dream_cry_together]` `[role: 主干]` 与人哭泣，有庆贺。 → 《周公解梦·哀乐病死歌唱》
  - `[ns_zgjm_955]` `[trigger: 梦见放声大哭]` `[factor_trigger: dream_cry_loud]` `[role: 主干]` 放声大哭，欢乐至。 → 《周公解梦·哀乐病死歌唱》
  - `[ns_zgjm_956]` `[trigger: 梦见身着孝服]` `[factor_trigger: dream_mourning_clothes]` `[role: 主干]` 身着孝服，官禄至。 → 《周公解梦·哀乐病死歌唱》
  - `[ns_zgjm_957]` `[trigger: 梦见远人来悲泣]` `[factor_trigger: dream_distant_cry]` `[role: 主干]` 远人来悲泣，主凶。 → 《周公解梦·哀乐病死歌唱》
  - `[ns_zgjm_958]` `[trigger: 梦见床上哭泣]` `[factor_trigger: dream_bed_cry]` `[role: 主干]` 床上哭泣，主大凶。 → 《周公解梦·哀乐病死歌唱》
  - `[ns_zgjm_959]` `[trigger: 梦见歌舞者]` `[factor_trigger: dream_singing_dancing]` `[role: 主干]` 见歌舞者，口舌至。 → 《周公解梦·哀乐病死歌唱》
  - `[ns_zgjm_960]` `[trigger: 梦见家中欢喜]` `[factor_trigger: dream_home_joy]` `[role: 主干]` 家中欢喜，百事吉。 → 《周公解梦·哀乐病死歌唱》
  - `[ns_zgjm_961]` `[trigger: 梦见怀中琵琶]` `[factor_trigger: dream_pipa]` `[role: 主干]` 怀中琵琶，得人助。 → 《周公解梦·哀乐病死歌唱》
  - `[ns_zgjm_962]` `[trigger: 梦见他人与笛]` `[factor_trigger: dream_flute]` `[role: 主干]` 他人与笛，有名声。 → 《周公解梦·哀乐病死歌唱》
  - `[ns_zgjm_963]` `[trigger: 梦见与人拍板]` `[factor_trigger: dream_clapper]` `[role: 主干]` 与人拍板，有口舌。 → 《周公解梦·哀乐病死歌唱》
  - `[ns_zgjm_964]` `[trigger: 梦见堂上歌乐]` `[factor_trigger: dream_hall_music]` `[role: 主干]` 堂上歌乐，主丧事。 → 《周公解梦·哀乐病死歌唱》
  - `[ns_zgjm_965]` `[trigger: 梦见吹笙者]` `[factor_trigger: dream_sheng]` `[role: 主干]` 吹笙者，主有更改。 → 《周公解梦·哀乐病死歌唱》
  - `[ns_zgjm_966]` `[trigger: 梦见吹笛打鼓]` `[factor_trigger: dream_flute_drum]` `[role: 主干]` 吹笛打鼓，有吉庆。 → 《周公解梦·哀乐病死歌唱》
  - `[ns_zgjm_967]` `[trigger: 梦见他人作乐]` `[factor_trigger: dream_others_music]` `[role: 主干]` 他人作乐，讼有理。 → 《周公解梦·哀乐病死歌唱》
  - `[ns_zgjm_968]` `[trigger: 梦见露齿哭者]` `[factor_trigger: dream_teeth_cry]` `[role: 主干]` 露齿哭者，有争讼。 → 《周公解梦·哀乐病死歌唱》
  - `[ns_zgjm_969]` `[trigger: 梦见病卧为人扶]` `[factor_trigger: dream_sick_supported]` `[role: 主干]` 病卧为人扶，加官。 → 《周公解梦·哀乐病死歌唱》
  - `[ns_zgjm_970]` `[trigger: 梦见病重者]` `[factor_trigger: dream_seriously_ill]` `[role: 主干]` 病重者，主有凶事。 → 《周公解梦·哀乐病死歌唱》
  - `[ns_zgjm_971]` `[trigger: 梦见自疾病者]` `[factor_trigger: dream_self_sick]` `[role: 主干]` 自疾病者，主有喜。 → 《周公解梦·哀乐病死歌唱》
  - `[ns_zgjm_972]` `[trigger: 梦见病人歌唱]` `[factor_trigger: dream_patient_sing]` `[role: 主干]` 病人歌唱，主大凶。 → 《周公解梦·哀乐病死歌唱》
  - `[ns_zgjm_973]` `[trigger: 梦见病人哭笑]` `[factor_trigger: dream_patient_laugh]` `[role: 主干]` 病人哭笑，疾病除。 → 《周公解梦·哀乐病死歌唱》
  - `[ns_zgjm_974]` `[trigger: 梦见病人起者]` `[factor_trigger: dream_patient_rise]` `[role: 主干]` 病人起者，必定死。 → 《周公解梦·哀乐病死歌唱》
  - `[ns_zgjm_975]` `[trigger: 梦见病人装车]` `[factor_trigger: dream_patient_cart]` `[role: 主干]` 病人装车，必死亡。 → 《周公解梦·哀乐病死歌唱》
  - `[ns_zgjm_976]` `[trigger: 梦见死人哭泣]` `[factor_trigger: dream_dead_cry]` `[role: 主干]` 死人哭泣，有口舌。 → 《周公解梦·哀乐病死歌唱》
  - `[ns_zgjm_977]` `[trigger: 梦见死人立者]` `[factor_trigger: dream_dead_stand]` `[role: 主干]` 死人立者，主大凶。 → 《周公解梦·哀乐病死歌唱》
  - `[ns_zgjm_978]` `[trigger: 梦见死人哭怀者]` `[factor_trigger: dream_dead_embrace]` `[role: 主干]` 死人哭怀者，得财。 → 《周公解梦·哀乐病死歌唱》
  - `[ns_zgjm_979]` `[trigger: 梦见死人复活]` `[factor_trigger: dream_dead_revive]` `[role: 主干]` 死人复活，主有信。 → 《周公解梦·哀乐病死歌唱》
  - `[ns_zgjm_980]` `[trigger: 梦见见人死自死者]` `[factor_trigger: dream_see_death]` `[role: 主干]` 见人死自死者，吉。 → 《周公解梦·哀乐病死歌唱》
  - `[ns_zgjm_981]` `[trigger: 梦见子死者]` `[factor_trigger: dream_child_die]` `[role: 主干]` 子死者，有添喜事。 → 《周公解梦·哀乐病死歌唱》
  - `[ns_zgjm_982]` `[trigger: 梦见先亡尊长]` `[factor_trigger: dream_ancestor]` `[role: 主干]` 见先亡尊长，大吉。 → 《周公解梦·哀乐病死歌唱》
  - `[ns_zgjm_983]` `[trigger: 梦见问吊他人]` `[factor_trigger: dream_condolence]` `[role: 主干]` 问吊他人，主生子。 → 《周公解梦·哀乐病死歌唱》"""
    normalized_text_zh: str = """"""
    subject: str = "哀乐病死歌唱"
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
        l1_anchor="zgjm_v1.0.0_哀乐病死歌唱_001_L1",
    )
    version: str = "1.0.0"
