"""
Auto-generated semantic module for zipingzhenquan
Generated at: 2025-12-05T13:30:19.465664
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
    semantic_id="zpzq_v1.0.0_外格的适用边界_月令无用方权用之_001",
    book_id="zipingzhenquan",
    engine_id="bazi"
)
class 外格的适用边界月令无用方权用之(SemanticEntry):
    """
    - **原文（source_text）**：
  二十二、论外格用舍.
  八字用神既专主月令，何以又有外格乎？外格者，盖因月令无用，权而用之，故曰外格也.

  如春木冬水、土生四季之类，日与月同，...
    """
    
    original_text: str = """- **原文（source_text）**：
  二十二、论外格用舍.
  八字用神既专主月令，何以又有外格乎？外格者，盖因月令无用，权而用之，故曰外格也.

  如春木冬水、土生四季之类，日与月同，难以作用，类象、属象、冲财、会禄、刑合、遥迎、井栏、朝阳诸格，皆可用也.若月令自有用神，岂可另寻外格？又或春木冬水，干头已有财官七煞，而弃之以就外格，亦太谬矣.是故干头有财，何用冲财？

  干头有官，何用合禄？书云“提纲有用提纲重”，又曰“有官莫寻格局”，不易之论也.

  然所谓月令无用者，原是月令本无用神，而今人不知，往往以财被劫官被伤之类，用神已破，皆以为月令无取，而弃之以就外格，则谬之又谬矣.

- 原注（原文注解）：
  　　本章讨论“外格”的用与舍，重点有三：
  - 其一：外格并不是主流取用之道，而是“月令无用时的权宜之计”；
  - 其二：若月令本身自有用神，就不应舍主就次，抛弃提纲而去追逐外格名目；
  - 其三：今人常把“用神已被破坏”误当成“月令无用”，从而乱就外格，是“谬之又谬”。

  作者先问：“八字用神既专主月令，何以又有外格？”随即给答案：所谓外格，正是因为某些情况下月令本身难以作为用神，才“权而用之”。例如：
  - 春木、冬水、土生四季之类，日干与月令同气，难以直接以日、月之同气为用；
  - 此时才可以考虑“类象、属象、冲财、会禄、刑合、遥迎、井栏、朝阳”等各种外格，作为权衡取用的参考.

  紧接着，作者立下两条边界：
  1) **月令自有用神，不可另寻外格**：
     - 若月令有明用（财、官、印、食等），格局本身已可成立；
     - 此时再一味去找“类象格”“冲财格”“会禄格”等外格，是舍本逐末.
  2) **干头已有财官七煞，不可抛弃而就外格**：
     - 如春木冬水之命，干头已有财、官、七煞等可用之神，而却弃之不用，专就“冲财会禄”等外格，作者认为“亦太谬矣”。

  最后，作者进一步指出，所谓“月令无用”，应当理解为“月令本来就无可用之神”；
  - 而今人常常见“财被劫、官被伤”等用神受克，就说“月令无取”，乃是把“用神已破”错当成“月令无用”；
  - 在此误解之下，弃月令而就外格，便成“谬之又谬”。

- 分字分词释义：
  - 用神专主月令：指取用神以月令为纲，四柱配之.
  - 外格：不由月令用神立格，而从特定组合（类象、属象、冲财、会禄等）权衡取用的格局.
  - 春木冬水：春木旺、冬水旺，日干与月令同气之局.
  - 土生四季：指四季土局中，日月同属土.
  - 类象、属象：按字面象义、属象等取格，如专看“马星”“羊刃”等类.
  - 冲财、会禄、刑合、遥迎、井栏、朝阳：诸多传统外格名称，皆为特定组合格局的代称.
  - 干头有财 / 有官：天干明透财星或官星.
  - 提纲有用提纲重：指月令提纲一旦有用，则其重要性居首，不可轻弃.
  - 有官莫寻格局：若局中已有明官，便不必再强求“奇格怪局”.
  - 月令无取：月令中无可取之用神.

- **规范化释义（primary_lang_explained）**：
  本章要点很清楚：**外格只是“无奈之选”，不是首选.**

  在正常情况下，八字取用神、立格局，都应以月令提纲为主线：
  - 月令中有什么用神，便以此为纲，再看四柱如何配合；
  - 若月令根本无可用之神，才考虑借助“外格”系统，寻找另一条取用路径.

  作者给出的几个外格类别——类象、属象、冲财、会禄、刑合、遥迎、井栏、朝阳——都是传统术数中常见的一些“特例格局”.这些格局本身并非虚妄，但有一个前提：
  - **只能在月令确实无用之时，才用来“权而用之”**；
  - 一旦月令已有明用、干头已有财官煞印等可以立格之神，就不该舍主就次，用外格来“抢戏”.

  尤其是作者批评今人常犯的错误：
  - 看见“财被劫、官被伤”等用神受克，就说“月令无取”；
  - 于是把原本应该通过“救应”“成败互转”来分析的局，简单归类为“年月日时中有某某组合，故用某外格”；
  - 这种做法等于因为格局有难度，就放弃格局法，转而用外格名目代替思考.

  本章从根本上提醒我们：
  - 外格是“权宜之计”，不是主线方法；
  - 真正需要外格者，是“月令本无用神”的极少数情况；
  - 将“用神已被破坏”误判为“月令无用”，而弃主就次，是最常见的误用.

- **完整对等诠释（secondary_lang_full）**：  
  External patterns belong only to a secondary, provisional layer built on top of the Month-Branch framework and should be considered only when the Month truly holds no usable god at all, not merely because that god has suffered clashes or harm. If the Month already contains Wealth, Officer or another clear useful spirit, one must not abandon it and chase attractive pattern names such as Clash-Wealth or Meeting-Lu. The principles "when the Month has a useful god it takes precedence" and "when Officer is present, do not seek other patterns" mark the hard boundary of this system.

- **详细解说**：
  - 从方法论角度看，本章是对子平体系边界的一个明确划定：
    - 主线：月令用神 + 四柱格局；
    - 辅线：外格系统，仅在主线无从着手时使用；
    - 星辰、外格皆属“辅线”，不可喧宾夺主.
  - 这也提醒命理学习者：
    - 不要为了追求“奇格”“特例”而忽略基本功；
    - 不要用外格名目来逃避对格局本身的深入分析.
  - 结合前一章“星辰无关格局”，可以看到作者一贯强调：
    - 格局为本，星辰与外格为末；
    - 先把本系统用神与格局吃透，再谈“奇格”“外格”.

- 核心要点：
  - 外格使用两大条件：
    1) 月令确实无用神；
    2) 干支中另有清晰且有理可循的外格结构可用.
  - 有用神则用用神，无用神才用外格；
  - 用神已破不等于月令无用，更不等于可以放弃用神系统而改用外格体系.

- 应用推演：
  1) 首先按月令用神体系分析格局，看是否能立格、成格；
  2) 若月令本身无可用之神，再检查是否存在可靠的外格结构（如冲财、会禄等）；
  3) 若月令有用但用神受破，应优先从“成败救应、成中有败、败中有成”等体系中寻找解法，而非直接改用外格；
  4) 在教学与工程实现中，将“外格判定”置于用神与格局分析之后，作为“最后一层”的 fallback，而非第一步.

- 反例与边界：
  - 一见某组合符合书上某外格名，就直接判为外格，而不看月令是否自有用神；
  - 把格局中用神受伤一律视为“月令无用”，进而弃主就次；
  - 将外格与星辰混为一谈，把所有“特别名目”都当主线判断依据.

- 小例（示意）：
  - 一命春木生寅月，月令木旺、干头又透财官，本可按正格处理，却因底本写有“某某外格”，便强行套用，导致判断偏离；
  - 另一命冬水日主与月令同气、月中无财官印食可用，此时借“会禄”“冲财”等外格来立格，则属于本章所说的“权而用之”，是外格的正当用法.

- 校勘与字词辨析：
  - 原文“类象、属象、冲财、会禄、刑合、遥迎、井栏、朝阳诸格”，诸格名在不同命书中写法略有差异，本精校不一一展开，只保留原列举；
  - “提纲有用提纲重”“有官莫寻格局”两句，与前文多处提到的“月令为纲、格局为本”一脉相承，提醒读者不要舍本逐末.
- **叙事素材（narrative_snippets）**：
  - `[ns_zpzy_372]` `[trigger: 四凶亦成]` `[factor_trigger: sha_shang_xiao_ren IN sixiongshen AND shi_zhi_deyi AND yi_cheng_ge]` `[role: 主干]` 煞伤枭刃四凶神，施之得宜亦成格。 → 《子平真诠·论四凶神能成格》#四凶
  - `[ns_zpzy_373]` `[trigger: 凶神成格例]` `[factor_trigger: (yinqing_tousha_weizhu) OR (cai_feng_bijie_shangguan_ke_jie)]` `[role: 主干]` 印轻透煞为助，财逢比劫伤官可解。 → 《子平真诠·论四凶神能成格》#成格例
  - `[ns_zpzy_374]` `[trigger: 凶为良剂]` `[factor_trigger: changqiang_daji_ru_xiongshen AND shi_zhi_deyi_ke_kanluan]` `[role: 条件分支]` 如长枪大戟，本非美具，施之得宜可戞乱。 → 《子平真诠·论四凶神能成格》#比喻
  - `[ns_zpzy_375]` `[trigger: 外格之用]` `[factor_trigger: waige_xu_zhen AND zhen_ze_keyong]` `[role: 主干]` 外格须真，真则可用。 → 《子平真诠》#中卷
  - `[ns_zpzy_376]` `[trigger: 辰戌丑未]` `[factor_trigger: branch IN (chen, xu, chou, wei) AND simu_ku]` `[role: 主干]` 辰戌丑未为四墓库。 → 《子平真诠》#中卷
  - `[ns_zpzy_377]` `[trigger: 冲开库门]` `[factor_trigger: chong_kai_kumen AND caiguan_shi_xian]` `[role: 主干]` 冲开库门，财官始显。 → 《子平真诠》#中卷
  - `[ns_zpzy_378]` `[trigger: 库中藏干]` `[factor_trigger: kuzhong_canggan AND tougan_fang_yong]` `[role: 主干]` 库中藏干，透干方用。 → 《子平真诠》#中卷
  - `[ns_zpzy_379]` `[trigger: 财多身弱忌]` `[factor_trigger: cai_duo_shen_ruo_yi AND fu_wu_pin_ren]` `[role: 主干]` 财多身弱，富屋贫人。 → 《子平真诠》#中卷
  - `[ns_zpzy_380]` `[trigger: 官多为煞忌]` `[factor_trigger: guan_duo_wei_sha_yi AND fan_sui_qi_hai]` `[role: 主干]` 官多为煞，反遭其害。 → 《子平真诠》#中卷
  - `[ns_zpzy_381]` `[trigger: 食旺泄身]` `[factor_trigger: shi_wang_xie_shen AND xiu_qi_liu_lu]` `[role: 主干]` 食旺泄身，秀气流露。 → 《子平真诠》#中卷
  - `[ns_zpzy_382]` `[trigger: 煞旺攻身]` `[factor_trigger: sha_wang_gong_shen AND xu_yao_shi_hua]` `[role: 主干]` 煞旺攻身，须食制印化。 → 《子平真诠》#中卷
  - `[ns_zpzy_383]` `[trigger: 伤旺生财]` `[factor_trigger: shang_wang_sheng_cai AND ji_yi_zhi_fu]` `[role: 主干]` 伤旺生财，技艺致富。 → 《子平真诠》#中卷
  - `[ns_zpzy_384]` `[trigger: 喜神来助]` `[factor_trigger: xishen_laizhu=true AND result=shishi_shunsui]` `[role: 主干]` 喜神来助，事事顺遂。 → 《子平真诠》#中卷
  - `[ns_zpzy_385]` `[trigger: 天干主动]` `[factor_trigger: tiangan_zhu_dong AND ying_su_er_xian]` `[role: 主干]` 天干主动，应速而显。 → 《子平真诠》#中卷
  - `[ns_zpzy_386]` `[trigger: 官多为煞忌]` `[factor_trigger: guan_duo_wei_sha AND fan_zao_qi_hai]` `[role: 主干]` 官多为煞，反遭其害。 → 《子平真诠》#中卷
  - `[ns_zpzy_387]` `[trigger: 食旺泄身]` `[factor_trigger: shi_wang_xie_shen AND xiuqi_liulu]` `[role: 主干]` 食旺泄身，秀气流露。 → 《子平真诠》#中卷
  - `[ns_zpzy_388]` `[trigger: 煞旺攻身]` `[factor_trigger: sha_wang_gong_shen AND xu_shi_zhi_yin_hua]` `[role: 主干]` 煞旺攻身，须食制印化。 → 《子平真诠》#中卷
  - `[ns_zpzy_389]` `[trigger: 伤旺生财]` `[factor_trigger: shang_wang_sheng_cai AND jiyi_zhifu]` `[role: 主干]` 伤旺生财，技艺致富。 → 《子平真诠》#中卷
  - `[ns_zpzy_390]` `[trigger: 忌神来犯]` `[factor_trigger: jishen_laifan=true AND result=zaihuo_nanmian]` `[role: 主干]` 忌神来犯，灾祸难免。 → 《子平真诠》#中卷
  - `[ns_zpzy_391]` `[trigger: 地支主静]` `[factor_trigger: dizhi_zhu_jing AND ying_huan_er_shen]` `[role: 主干]` 地支主静，应缓而深。 → 《子平真诠》#中卷"""
    normalized_text_zh: str = """"""
    subject: str = "外格的适用边界：月令无用方权用之"
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
        book_id="zipingzhenquan",
        chapter="",
        l1_anchor="zpzq_v1.0.0_外格的适用边界_月令无用方权用之_001_L1",
    )
    version: str = "1.0.0"
