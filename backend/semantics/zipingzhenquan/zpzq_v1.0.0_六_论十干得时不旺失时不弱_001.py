"""
Auto-generated semantic module for zipingzhenquan
Generated at: 2025-12-05T13:30:19.523804
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
    semantic_id="zpzq_v1.0.0_六_论十干得时不旺失时不弱_001",
    book_id="zipingzhenquan",
    engine_id="bazi"
)
class 六论十干得时不旺失时不弱(SemanticEntry):
    """
    - **原文（source_text）**：
  书云，得时俱为旺论，失时便作衰看，虽是至理，亦死法也。然亦可活看。夫五行之气，流行四时，虽日干各有专令，而其实专令之中，亦有并存者在。假若春木司令，甲...
    """
    
    original_text: str = """- **原文（source_text）**：
  书云，得时俱为旺论，失时便作衰看，虽是至理，亦死法也。然亦可活看。夫五行之气，流行四时，虽日干各有专令，而其实专令之中，亦有并存者在。假若春木司令，甲乙虽旺，而此时休囚之戊己，亦尝艳于天地也。特时当退避，不能争先，而其实春土何尝不生万物，冬日何尝不照万国乎？况八字虽以月令为重，而旺相休囚，年月日时，亦有损益之权，故生月即不值令，而年时如值禄旺，岂便为衰？不可执一而论。犹如春木虽强，金太重而木亦危。干庚辛而支酉丑，无火制而晃富，逢土生而必夭，是以得时而不旺也。秋木虽弱，木根深而木亦强。干甲乙而支寅卯，遇官透而能受，逢水生而太过，是失时不弱也。

- 原注（原文注解）：
  　　此段批判机械论旺衰的"死法"，提出"活看"原则，强调月令虽重，年日时三柱同样有损益之权，以春木秋木为例说明"得时不旺、失时不弱"的辩证关系，为后文"四柱有根"论打下理论基础。

- 分字分词释义：
  - 书云，得时俱为旺论：坊间命书说，得月令就算旺。
  - 失时便作衰看：失月令就算衰。
  - 虽是至理，亦死法也：这虽是基本道理，但也是死板的教条。
  - 然亦可活看：但也可以灵活地看待。
  - 五行之气，流行四时：五行之气流转于四季之中。
  - 日干各有专令：每个天干在某个月令中当权（如甲乙在春、丙丁在夏）。
  - 专令之中，亦有并存者在：即使某干当令，其他干也并非完全不存在。
  - 春木司令，甲乙虽旺：春天木当令，甲乙木虽然强旺。
  - 此时休囚之戊己，亦尝艳于天地：但此时休囚的戊己土，也同样存在于天地之间。
  - 时当退避，不能争先：只是时机要求它退避，不能争夺主导权。
  - 春土何尝不生万物：春天的土何尝不在生养万物？
  - 冬日何尝不照万国：冬天的太阳何尝不在照耀天下？
  - 八字虽以月令为重：八字虽然以月令为最重要的判断依据。
  - 旺相休囚，年月日时，亦有损益之权：但旺衰的判断，年日时三柱也有增损的权力。
  - 生月即不值令，而年时如值禄旺，岂便为衰：即使生月不当令，但年时如果遇到禄旺，怎能简单断为衰？
  - 不可执一而论：不能拘泥于一点而下判断。
  - 犹如春木虽强，金太重而木亦危：就像春木虽强，但金太重了木也危险。
  - 干庚辛而支酉丑：天干有庚辛，地支有酉丑。
  - 无火制而晃富：没有火制金，则晃（通"恍"，虚有其表）富。
  - 逢土生而必夭：遇到土生金，则必然夭折。
  - 得时而不旺：这就是得月令而实际不旺的情况。
  - 秋木虽弱，木根深而木亦强：秋天木虽弱，但如果木根深厚，木也能强。
  - 干甲乙而支寅卯：天干有甲乙，地支有寅卯。
  - 遇官透而能受：遇到正官透出能够承受（因为身强）。
  - 逢水生而太过：遇到水生反而太过（因为木已经足够强了）。
  - 失时不弱：这就是失月令而实际不弱的情况。

- 核心要点：
  - **月令非唯一标准**：虽以月令为重，但年日时三柱同样有损益之权。
  - **得时未必真旺**：春木虽强，若金太重而无火制，木反危。
  - **失时未必真弱**：秋木虽弱，若木根深而支多寅卯，木反强。

- **规范化释义（primary_lang_explained）**：
 - 坊间命书说，得月令就算旺，失月令就算衰，这虽然是基本道理，但也是死板的教条，其实可以灵活地看待。五行之气流转于四季之中，虽然每个天干在某个月令中当权（如春天木当令），但即使某干当令，其他干也并非完全不存在。比如春天木当令，甲乙木虽然强旺，但此时休囚的戊己土，也同样存在于天地之间，只是时机要求它退避，不能争夺主导权罢了。春天的土何尝不在生养万物？冬天的太阳何尝不在照耀天下？何况八字虽然以月令为最重要的判断依据，但旺衰的判断，年日时三柱也有增损的权力。所以即使生月不当令，但年时如果遇到禄旺，怎能简单断为衰？不能拘泥于一点而下判断。就像春木虽强，但金太重了（天干庚辛、地支酉丑），没有火制金，则虚有其表；遇到土生金，则必然夭折。这就是"得时而不旺"的情况。反过来，秋天木虽弱，但如果木根深厚（天干甲乙、地支寅卯），遇到正官透出能够承受（因为身强），遇到水生反而太过（因为木已经足够强了）。这就是"失时不弱"的情况。

- **完整对等诠释（secondary_lang_full）**：  
  Traditional manuals often say that any stem that "gets the Season" must be judged strong, and any that "misses the Season" must be judged weak. The author accepts this as a rough principle but warns that it becomes a dead rule if applied mechanically. The qi of the Five Elements circulates through all four seasons: each stem has a month in which it is formally in command, yet in that very month the other elements have not vanished; they have only yielded precedence. In spring, Wood is certainly dominant and the Wood stems are vigorous, but the Earth that receives and nourishes growth is still there, and the winter Sun still shines upon the whole world. In chart terms this means that, although the Month Branch is weighty, the Year, Day and Hour branches also have the power to increase or reduce a stem's real strength.

  A Wood Day Master that is born in spring may nevertheless be in danger if Metal is piled up heavily in stems and branches and there is no Fire to restrain it: the chart then shows "timely yet not truly strong". Conversely, an autumn Wood Day Master, though out of season, may in fact be robust if there are deep Wood roots in Yin and Mao and the stem receives proper Officer support; in such a case further Water generation only makes it excessive—"out of season yet not truly weak". The lesson is that we must weigh timing together with rooting and the overall pattern of generating and controlling, rather than letting the Month alone dictate our verdict on strength and weakness.

- 详细解说：
  - 旺衰不是月令一家说了算，而是四柱综合平衡的结果。
  - "得时"只是表面条件，实际强弱要看整体配置：得时若无根、或被过度克制，反而不旺；失时若有深根、或得多方生助，反而不弱。
  - 这是对"月令决定论"的重要修正，为后文"四柱有根"理论铺垫。

- 核心要点：
  - 判断身强身弱不能只看月令，必须综合年日时三柱的根气、透干、生克配置。
  - "得时"是加分项但非充分条件，"失时"是减分项但非致命弱点。
  - 实战中要避免"见春木就断旺、见秋木就断弱"的机械错误。

- 应用推演：
  1) 先看月令，确定日主在月令中的旺衰状态（得令、失令）。
  2) 再看年日时三柱，统计日主在各支的根气（长生、禄、旺、库、余气等）。
  3) 综合天干透干情况（比劫、印绶生助）与克制情况（财官煞食伤）。
  4) 综合判断：得令但克重则"得时不旺"，失令但根深则"失时不弱"。

- 反例与边界：
  - 只看月令就断旺衰，是最常见的机械错误，本段明确批判为"死法"。
  - 把"活看"理解成"随意看"，不遵守基本的旺衰判断规则，也是误读。

- 小例（示意）：
  - 甲木生于春月（得令），但天干庚辛重重、地支酉丑金局，无火制金，则木虽得令却危，是"得时不旺"。
  - 甲木生于秋月（失令），但地支寅卯木局、天干甲乙透干，则木虽失令却强，是"失时不弱"。

- 校勘与字词辨析：
  - "晃富"：各本多作"晃"字，通"恍"，虚有其表之意。
  - "休囚之戊己，亦尝艳于天地"："艳"字各本同，指存在、显现之意。


- **叙事素材（narrative_snippets）**：
  - `[ns_zpzy_244]` `[trigger: 十干论命]` `[factor_trigger: shigan_ge_you_xingqing AND lunming_xu_shi_qi_ben]` `[role: 主干]` 十干各有性情，论命须识其本。 → 《子平真诠·论十干十二支》#十干
  - `[ns_zpzy_245]` `[trigger: 实践要领]` `[factor_trigger: duanming_shijian AND yaoling_zonghe]` `[role: 主干]` 断命实践要领。 → 《子平真诠》#上卷
  - `[ns_zpzy_246]` `[trigger: 边界条件]` `[factor_trigger: shiyong_tiaojian AND bianjie_xianzhi]` `[role: 条件分支]` 适用条件与边界。 → 《子平真诠》#上卷
  - `[ns_zpzy_247]` `[trigger: 天干地支]` `[factor_trigger: tiangan_dizhi AND yinyang_zhi_xiang]` `[role: 主干]` 天干地支，阴阳之象也。 → 《子平真诠》#论十干十二支
  - `[ns_zpzy_248]` `[trigger: 干支配合]` `[factor_trigger: ganzhi_peihe AND shengke_zhihua_zhi_li]` `[role: 主干]` 干支配合，生克制化之理。 → 《子平真诠》#论十干十二支
  - `[ns_zpzy_249]` `[trigger: 甲乙属木]` `[factor_trigger: (jiayi=mu) AND (bingding=huo) AND (wuji=tu) AND (gengxin=jin) AND (rengui=shui)]` `[role: 主干]` 甲乙属木，丙丁属火，戊己属土，庚辛属金，壬癸属水。 → 《子平真诠》#论十干十二支
  - `[ns_zpzy_250]` `[trigger: 无病无药]` `[factor_trigger: wubing=true AND wuyao=true AND result=pingchang_zhiren]` `[role: 主干]` 无病无药，平常之人。 → 《子平真诠》#上卷"""
    normalized_text_zh: str = """"""
    subject: str = "六．论十干得时不旺失时不弱"
    factor_refs: list = ['deshi_buwang', 'shishi_buruo', 'yueling', 'sizhu_yougen', 'huokan']
    
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
        l1_anchor="zpzq_v1.0.0_六_论十干得时不旺失时不弱_001_L1",
    )
    version: str = "1.0.0"
