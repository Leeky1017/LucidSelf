"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.264308
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
    semantic_id="smth_v1.0.0_接甲运分类与一气相连_001",
    book_id="sanming",
    engine_id="bazi"
)
class 接甲运分类与一气相连(SemanticEntry):
    """
    - **原文（source_text）**：  
  若寅卯辰、巳午未、申酉戌、亥子丑，一气相连，皆非接木之说，总遇接甲，亦无大祸。假如甲乙传寅卯运，名曰劫财败财，主克父母及克财败财争斗之事。丙丁巳午...
    """
    
    original_text: str = """- **原文（source_text）**：  
  若寅卯辰、巳午未、申酉戌、亥子丑，一气相连，皆非接木之说，总遇接甲，亦无大祸。假如甲乙传寅卯运，名曰劫财败财，主克父母及克财败财争斗之事。丙丁巳午运各伤官运，主克子女讼事囚系。庚辛申酉运七煞官乡，主得名发越，太过则灾病恶疾。壬癸亥子生气、印绶运，主吉庆增产；辰戌丑未、戊巳财运，主名利皆通。此乃死法，须随格局喜忌推之。干旺宜衰运，正所谓干弱则求气旺之藉，有余则欲不足之营，须要通变，更兼流年诸神煞推之，其验如神。

- **分字分词释义**：
  - **一气相连**：寅卯辰等三支属同一气势，运在本气之内流转，不作“接木”论。
  - **劫财败财运**：甲乙日主行寅卯运，比劫旺而财受损，多主兄弟争财、父母受损。
  - **伤官运**：丙丁日主行巳午，食神伤官极旺，易克子女、惹诉讼囚系。
  - **七煞官乡**：庚辛日主行申酉，七煞与正官得地，可发名权，太过则生灾病恶疾。
  - **死法须通变**：这里列举的是静态口诀，必须结合格局喜忌、身强身弱与流年神煞灵活运用。

- **规范化释义（primary_lang_explained）**：  
  承接前文“接木”之说，作者先指出：若大运仍在同一三合局内轮转（如寅卯辰一气、巳午未一气等），只是本气内部的循环，不算前文所说那种根本换气的“接木”，一般不会引发换根式的大祸。随后他按日干类别，对典型运性作了一个“死法”式的分类表：甲乙日主行寅卯，为比劫兴旺之运，名“劫财败财”，多应在克父母、克财与争夺财物上；丙丁日主行巳午，为伤官旺运，容易在子女、口舌官司乃至囚系上出事；庚辛日主行申酉，为七煞官乡，有制化则得名发越、权力上升，太过则以疾病恶疾报应；壬癸日主行亥子，为生气与印绶运，多主吉庆增产；辰戌丑未及戊巳等多为财运之乡，主名利两通。最后作者提醒：这些只是“死法”，真正判断时必须结合日干强弱与格局喜忌：日干太旺宜行泄耗之衰运，日干太弱反而要行旺运资扶，“干弱则求气旺之藉，有余则欲不足之营”，再叠加流年诸神煞综合推断，方能“其验如神”。

- **完整对等诠释（secondary_lang_full）**：  
  Building on the earlier discussion of grafting‑type transitions, the text first carves out an exception: when major luck stays within the same triplicity of branches—Yin‑Mao‑Chen, Si‑Wu‑Wei, Shen‑You‑Xu, or Hai‑Zi‑Chou—this is called "one continuous qi" and does not belong to the grafting category. Such movements usually do not create a fundamental root change or catastrophic disruption. It then lays out a schematic classification by Day Stem: for Jia and Yi, running Yin‑Mao luck is termed Robbing‑and‑Losing‑Wealth luck, where Parallels are strong and Wealth is harmed, often manifesting as damage to parents and financial disputes. For Bing and Ding, running Si‑Wu luck is Hurting‑Officer luck, with overly strong Eating God/Hurting Officer leading to harm to children, lawsuits and even imprisonment. For Geng and Xin, running Shen‑You luck is the realm of Seven Killings and Officers; if properly controlled and supported, this brings fame and advancement, but in excess it produces illness and severe misfortune. For Ren and Gui, running Hai‑Zi luck is a phase of Vital Qi and Seals, indicating auspicious celebrations and increase in assets. The branches Chen‑Xu‑Chou‑Wei and combinations with Wu and Si are broadly classed as Wealth luck, where reputation and profit are accessible. Yet all of this is explicitly labelled "dead method": one must always adjust these rules to the chart's喜忌 and the strength or weakness of the Day Stem. A strong Day Stem prefers declining luck to drain excess, while a weak Day Stem needs旺氣 to compensate deficiency. When this principle of adaptation is applied together with annual stars, the author claims, predictions become "accurate like a spirit." 

- **核心要点**：
  - 同一三合气内轮转属于“一气相连”，不作接木之大祸看。
  - 依日干分类：甲乙行寅卯为劫财败财，丙丁行巳午为伤官，庚辛行申酉为七煞官乡，壬癸行亥子为生气印绶，辰戌丑未与戊巳多属财运。
  - 这些只是静态口诀，实际运用必须结合格局喜忌、身强身弱与流年神煞“通变”来看。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_10_073]` `[trigger: 一气相连]` `[factor_trigger: yiqi_xianglian AND fei_jiemu_shuo]` `[role: 主干]` 若寅卯辰、巳午未、申酉戌、亥子丑，一气相连，皆非接木之说。 → 《三命通会》卷十#接甲运分类与一气相连
  - `[ns_smth_10_074]` `[trigger: 劫财败财]` `[factor_trigger: jiecai_baicai AND ke_fumu_zhengcai]` `[role: 主干依赖]` 假如甲乙传寅卯运，名曰劫财败财，主克父母及克财败财争斗之事。 → 《三命通会》卷十#接甲运分类与一气相连
  - `[ns_smth_10_075]` `[trigger: 干旺宜衰运]` `[factor_trigger: ganwang_yishuaiyun AND ganruo_yiwangyun]` `[role: 条件分支]` 干旺宜衰运，正所谓干弱则求气旺之藉，有余则欲不足之营。 → 《三命通会》卷十#接甲运分类与一气相连
  - `[ns_smth_10_076]` `[trigger: 死法通变]` `[factor_trigger: sifa_tongbian AND geju_xiji_tuizhi]` `[role: 总结]` 此乃死法，须随格局喜忌推之。 → 《三命通会》卷十#接甲运分类与一气相连"""
    normalized_text_zh: str = """"""
    subject: str = "接甲运分类与一气相连"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate']
    
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
        l1_anchor="smth_v1.0.0_接甲运分类与一气相连_001_L1",
    )
    version: str = "1.0.0"
