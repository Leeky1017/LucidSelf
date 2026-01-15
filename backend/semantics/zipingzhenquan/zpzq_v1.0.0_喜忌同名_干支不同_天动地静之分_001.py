"""
Auto-generated semantic module for zipingzhenquan
Generated at: 2025-12-05T13:30:19.492166
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
    semantic_id="zpzq_v1.0.0_喜忌同名_干支不同_天动地静之分_001",
    book_id="zipingzhenquan",
    engine_id="bazi"
)
class 喜忌同名干支不同天动地静之分(SemanticEntry):
    """
    - **原文（source_text）**：
  二十七、论喜忌干支有别。
  命中喜忌，虽支干俱有，而干主天，动而有为，支主地，静以待用，且干主一而支藏多，为福为祸，安不得殊？

  譬如甲用酉官，...
    """
    
    original_text: str = """- **原文（source_text）**：
  二十七、论喜忌干支有别。
  命中喜忌，虽支干俱有，而干主天，动而有为，支主地，静以待用，且干主一而支藏多，为福为祸，安不得殊？

  譬如甲用酉官，逢庚辛则官煞杂，而申酉不作此例。申亦辛之旺地，辛坐申酉，如府官又掌道印也。逢二辛则官犯重，而二酉不作此例。辛坐二酉，如一府而摄二郡也，透丁则伤官，而逢午不作此例。丁动而午静，且丁巳并藏，安知其为财也？

  然亦有支而能作祸福者，何也？如甲用酉官，逢午酉未能伤，而又遇寅遇戌，不隔二位，二者合而火动，亦能伤矣。即此反观，如甲生甲月，午不制煞，会寅会戌，二者清局而火动，亦能矣。然必会有动，是正与干有别也。即此一端，余者可知。

- 原注（原文注解）：
  　　本章说明：**同样是“某神为喜/为忌”，落在天干与落在地支，其作用强弱与表现方式往往不同。**
  - 开篇总论：
    - 命中喜忌，干支中都可能存在；
    - 然而“干主天，动而有为”，在上为显、主主动变化；
    - “支主地，静以待用”，在下为藏、主潜在根气与背景；
    - 干主一而支藏多：天干单线条，地支多藏干，结构更复杂；
    - 因此，同一喜忌之神，落干与落支，对福祸的影响不能一概而论。

  中段以“甲用酉官”为例，详细展示这一差别：
  - 甲日以酉为正官：
    - 若天干再透庚辛，则官煞混杂，官清被破，这是“逢庚辛则官煞杂”；
    - 但遇申酉两支时，情况不同：
      - 申亦辛之旺地，辛坐申酉，如府官兼掌道印，是“官得其所”；
      - 两辛透干则官犯重，而二酉同坐辛气却不算“官犯重”，因为辛在支中为根，不同于天干“另起一头”；
    - 同理：
      - 透丁为伤官，则伤官克官之象明显；
      - 但单见午支，不一定作“伤官论”，因丁火藏于巳午等支，不必皆为“伤官动用”，须视是否透干、会局而定。

  下段指出：
  - 虽然支多“静以待用”，但在一定条件下也能主动成祸福：
    - 如甲用酉官，单见午支未必能伤官；
    - 若又遇寅遇戌，与午不隔二位，会成火局，则火动而能伤金官；
  - 反观“甲生甲月，午不制煞，会寅会戌，火局清成”一例：
    - 午本不制煞，但与寅戌会成火局，则火气动，足以制煞.
  - 结语“然必会有动，是正与干有别”强调：
    - 地支要通过会合、冲动才“活起来”；
    - 与天干自显自动不同，这便是干支在喜忌作用上的根本差异。

- 分字分词释义：
  - 干主天，动而有为：天干主显露之象，易起直接作用.
  - 支主地，静以待用：地支主根基与环境，多为潜在之气，须会合冲动方显.
  - 官煞杂：正官与七煞混杂，官清被破.
  - 府官又掌道印：比喻辛金在申酉之地，如同官员兼掌印信，有权有位.
  - 官犯重：官星过多或遭冲合，使其难以为用.
  - 一府而摄二郡：以一府统辖二郡，比喻辛坐二酉，仍是一神主事，不作“二官”论.
  - 丁动而午静：丁透干则为“动”，午居支则为“静”.
  - 不隔二位：支之间相邻或隔一位，易成会局.

- **规范化释义（primary_lang_explained）**：
  这一章要我们从“空间层级”的角度，重新理解喜忌：
  - 同一个十神，写在天干和埋在地支，效果不同；
  - 同样是“多一个官、多一个伤”，在干上多与在支上多，结论不能画等号.

  作者以甲用酉官为例，说明几点：
  1) 天干之官煞一露，立刻改变结构：
     - 再透庚辛，就不再是单纯清官，而是官煞混杂；
  2) 地支之申酉虽也属辛气，却多在“根与势”的层面：
     - 申酉并临不等于“二辛并列”；
     - 反而像“一个官员兼管多地”，并未另立新官.
  3) 透丁为伤官，是“丁动”；
     - 单见午支，多只是“火的环境”，仍需看是否透丁、会局成火方能实伤官.

  对于“支而能作祸福”的例子：
  - 单个午支不足以动摇官星；
  - 但若寅午戌三支齐来，无隔二位，会成火局，则火局动而伤金官；
  - 这说明：
    - 地支虽静，但一旦会局成功，其威力不逊于天干；
 - **完整对等诠释（secondary_lang_full）**：  
  When the same favourable or unfavourable spirit appears on stems and on branches, it does not operate in the same way. Stems belong to Heaven: they move first, show themselves openly, and their actions are direct and visible. Branches belong to Earth: they are quiet and rooted, storing potential until a full combination is assembled or a stem draws their力量 out. A single Officer on the stem can immediately constrain or support the Day Master, whereas several Officer roots hidden in the branches only begin to act once fire or metal has gathered into a局 and been activated by luck.

  This is why we must distinguish between “root” and “use”: many joys and hates have their根 in the branches, but their effective作用 is expressed through stems and completed patterns. To count every branch root as if it were already an acting useful god, or to treat every stem exposure as if it were only background气, is to confuse potential with actual and to misjudge both blessings and harms.

    - 喜忌之“根”，常在支；喜忌之“用”，常在干与成局.

- 详细解说：
  - 喜忌判断若只看“有无某字”，而不分干支位置，就会出现大量误判：
    - 把支中根气当成“已成之用”；
    - 把干上露神当成“仅是底气”；
  - 本章强调一种层级观：
    - 天干：事情的“表层行为与事件”；
    - 地支：事情的“背景结构与资源土壤”；
    - 相同喜忌之神，在不同层级上出现，其结果不同.
  - 与前一章“成格变格”呼应：
    - 地支会合、藏干透出，往往是“成格变格”的触发点；
    - 若不分干支差异，难以及时捕捉这些结构变化.


- **校勘与字词辨析（双语）**：
  - **中文**：本稿据通行本，经文用字保持原貌，标点现代化处理。
  - **English**: Based on standard edition. Original text preserved, punctuation modernized.

- **叙事素材（narrative_snippets）**：
  - `[ns_zpzy_446]` `[trigger: 建禄月劫]` `[factor_trigger: jianlu_yuejie_wuge AND xu_bie_xun_yongshen]` `[role: 主干]` 建禄月劫无格，须别寻用神。 → 《子平真诠》#下卷第45章
  - `[ns_zpzy_447]` `[trigger: 变格之运]` `[factor_trigger: yun_neng_bian_ge AND jiongxiong_zhuanhuan]` `[role: 主干]` 运能变格，吉凶转换。 → 《子平真诠》#下卷
  - `[ns_zpzy_448]` `[trigger: 阳刃之性]` `[factor_trigger: yangren_weixiong AND xu_guansha_zhi_zhi]` `[role: 主干]` 阳刃为凶，须官煞制之。 → 《子平真诠》#下卷
  - `[ns_zpzy_449]` `[trigger: 支会之力]` `[factor_trigger: xishen_hui_zhi AND liliang_shenhou]` `[role: 主干]` 喜神会支，力量深厚。 → 《子平真诠》#下卷
  - `[ns_zpzy_450]` `[trigger: 正官护印]` `[factor_trigger: guan_feng_yin_sheng AND guiqi_tiancheng]` `[role: 主干]` 官逢印生，贵气天成。 → 《子平真诠》#下卷
  - `[ns_zpzy_451]` `[trigger: 印运逢官]` `[factor_trigger: yinyun_feng_guan AND xueye_youcheng]` `[role: 主干]` 印运逢官，学业有成。 → 《子平真诠》#下卷
  - `[ns_zpzy_452]` `[trigger: 食运逢财]` `[factor_trigger: shiyun_feng_cai AND jingshang_dali]` `[role: 主干]` 食运逢财，经商大利。 → 《子平真诠》#下卷
  - `[ns_zpzy_453]` `[trigger: 煞格行运]` `[factor_trigger: sha_ge AND xi_shizhi_yinhua_yun]` `[role: 主干]` 煞格喜食制印化运。 → 《子平真诠》#下卷
  - `[ns_zpzy_454]` `[trigger: 伤格行运]` `[factor_trigger: shang_ge AND xi_caixing_shengyong_yun]` `[role: 主干]` 伤格喜财星生用运。 → 《子平真诠》#下卷
  - `[ns_zpzy_455]` `[trigger: 五行流通]` `[factor_trigger: wuxing_liutong AND qiji_changda]` `[role: 主干]` 五行流通，气机畅达。 → 《子平真诠》#下卷
  - `[ns_zpzy_456]` `[trigger: 用神无力]` `[factor_trigger: yongshen_wuli=true AND result=pinjian_nanmian]` `[role: 主干]` 用神无力，贫贱难免。 → 《子平真诠》#下卷
  - `[ns_zpzy_457]` `[trigger: 年柱根基]` `[factor_trigger: nianzhu_genji AND zuye_zhigong]` `[role: 条件分支]` 年柱根基，祖业之宫。 → 《子平真诠》#下卷"""
    normalized_text_zh: str = """"""
    subject: str = "喜忌同名，干支不同：天动地静之分"
    factor_refs: list = ['ganzhi_youbie', 'tougan', 'huizhi', 'ganxian_zhicang', 'engine_id', 'shishen_tiangan', 'bazi_rule_engine', 'shishen_dizhi', 'bazi_rule_engine', 'shishen_peidui', 'bazi_rule_engine', 'zhi_jihuo', 'bazi_rule_engine', 'source_ref', 'rel_zpzq_134', 'shishen_tiangan', 'rel_zpzq_135', 'zhi_jihuo', 'evi_zpzq_121', 'ganzhi_youbie', 'rule_ganzhi_youbie', 'concept_manifest', 'concept_latent']
    
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
        l1_anchor="zpzq_v1.0.0_喜忌同名_干支不同_天动地静之分_001_L1",
    )
    version: str = "1.0.0"
