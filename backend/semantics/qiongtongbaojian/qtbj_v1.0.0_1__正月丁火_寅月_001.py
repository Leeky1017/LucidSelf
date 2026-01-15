"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.596842
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
    semantic_id="qtbj_v1.0.0_1__正月丁火_寅月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 1正月丁火寅月(SemanticEntry):
    """
    - **原文（source_text）**：
  正月丁火，甲木当权，乃为母旺，非庚不能噼甲，何以引丁，姑用庚金。
  或一派甲木，无庚制之，非贫即夭。或只一甲木，多见乙木者，必离乡之客，焉问妻儿。或...
    """
    
    original_text: str = """- **原文（source_text）**：
  正月丁火，甲木当权，乃为母旺，非庚不能噼甲，何以引丁，姑用庚金。
  或一派甲木，无庚制之，非贫即夭。或只一甲木，多见乙木者，必离乡之客，焉问妻儿。或见甲乙，生庚子时，又主妻早子早，且可采芹。
  得壬化木，弱极复生，合此必主大贵，但此化合，反以不见庚破格为妙。
  或有庚金壬癸，得己土出干制之，此命不由科甲，亦有异途。
  或一派壬癸，不得寅时，又无庚金，必主穷困。
  或丁年、壬月、丁日、壬时，男主大贵；女则不宜。此格以土为妻、金为子。但子女艰难。女命合此，淫贱，刑夫克子。
  或支火局，无滴水解，僧道之命。见甲出略可。总不可无水。水多亦不宜。

- **分字分词释义**：
  - **甲木当权**：甲木掌握权柄 / 寅月 / 印旺
  - **噼甲引丁**：劈开甲木引燃丁火 / 庚金功能 / 核心机制
  - **母旺**：印星旺盛 / 甲木 / 印格
  - **木多火塞**：木太多火被塞住 / 甲多无庚 / 凶象
  - **离乡之客**：离开家乡的客人 / 乙多 / 孤苦
  - **采芹**：采摘芹菜 / 中秀才代称 / 功名
  - **弱极复生**：弱到极点又复活 / 化格 / 大贵
  - **刑夫克子**：刑克丈夫和儿子 / 女命凶 / 大忌

- **规范化释义（primary_lang_explained）**：
  正月（寅月）的丁火，甲木当权，这是母旺（印旺），没有庚金就不能劈甲木，怎能引燃丁火呢（劈甲引丁）？所以暂且用庚金。
  如果一派甲木，没有庚金制约，不是贫穷就是夭折（木多火塞）。或者只有一个甲木，多见乙木，必定是离乡背井的客人，还问什么妻儿呢（孤苦）。如果见到甲木乙木，生在庚子时（庚制甲、子水润），又主娶妻早、生子早，而且可以中秀才（采芹）。
  如果得到壬水（丁壬合）化木，弱极复生（从化格），符合此格必定大贵，但这种化合格，反而以不见庚金破格（金克木）为妙。
  如果有庚金和壬癸水（官杀），得到己土出干制水（食神制杀），这命不由科甲，也有异途功名。
  如果一派壬癸水（杀重），没有得到寅时（归禄/印长生），又没有庚金（生水？此处疑为印化杀或食制杀，庚金生水反助杀，但庚能劈甲引丁，可能有救），必主穷困。
  如果是丁年、壬月、丁日、壬时（两丁两壬），男命主大贵（化气格或争合不忌）；女命则不宜（争合官星）。这个格局以土为妻、金为子。但子女艰难。女命符合此格，淫贱，刑夫克子。
  如果地支合成火局，没有一点水来解炎，是僧道之命。见到甲木出干稍微好一点。总不可无水，但水多也不适宜。

- **完整对等诠释（secondary_lang_full）**：
  Ding Fire in the 1st Month (Tiger Month): Jia Wood holds power; the Mother is Prosperous. Without Geng to split Jia, how can Ding be ignited? Thus tentatively use Geng Metal.
  If there is a mass of Jia Wood without Geng to control it, it means either poverty or premature death (Wood chokes Fire). If there is only one Jia but much Yi, one is a guest leaving home; don't even ask about wife and children. If Jia/Yi are seen and born in Geng-Zi Hour, it implies early marriage and children, and passing the Xiucai exam.
  Obtaining Ren to transform into Wood (Ding-Ren combine), "Weak Extreme Revives", this pattern implies great nobility. But for this transformation, it is best not to see Geng breaking the pattern.
  If Geng/Ren/Gui are present, and Ji Earth reveals to control them, fame comes from alternative paths, not exams.
  If a mass of Ren/Gui appears, not born in Yin Hour, and without Geng, it implies poverty.
  If Ding Year, Ren Month, Ding Day, Ren Hour, a man is greatly noble; not suitable for a woman. This pattern takes Earth as Wife, Metal as Child. But children are difficult. A woman with this pattern is lewd/lowly, punishing husband and harming children.
  If branches form a Fire Frame without a drop of Water, it is a monk/Taoist life. Seeing Jia reveal is slightly better. Generally, Water cannot be absent, but excessive Water is also not suitable.

- **核心要点**：
  - **劈甲引丁**：寅月甲旺，湿木无焰，必用庚劈。
  - **木多火塞**：甲乙多无庚，贫夭/离乡。
  - **化木格**：丁壬化木，生于寅月当令，大贵，忌庚。
  - **争合**：男命两丁两壬大贵，女命淫贱。

- **详细解说**：
  - 丁火柔中，寅月印旺。
  - 正常格局喜庚金财星破印，实为劈甲引丁。
  - 丁壬合化木，在寅月最易成格（化神当令）。若成化格，则最忌金（克化神）。
  - “两丁两壬”：男命作“化气”或“清奇”论，女命则为“多夫/争妒”论。
- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_263]` `[trigger: 寅月丁火]` `[factor_trigger: month_yin AND tiangan_ding AND tiangan_jia AND tiangan_geng AND split_jia_ignite_ding]` `[role: 主干]` 正月丁火，甲木当权，乃为母旺，非庚不能噼甲，何以引丁，姑用庚金。 → 《穷通宝鉴·三春丁火》#16.1
  - `[ns_qttbj_264]` `[trigger: 木多火塞]` `[factor_trigger: month_yin AND tiangan_ding AND jia_multiple AND NOT tiangan_geng AND wood_chokes_fire]` `[role: 例外处理]` 一派甲木，无庚制之，非贫即夭。 → 《穷通宝鉴·三春丁火》#16.1
  - `[ns_qttbj_265]` `[trigger: 丁壬化木]` `[factor_trigger: month_yin AND tiangan_ding AND tiangan_ren AND ding_ren_transform_wood AND NOT tiangan_geng]` `[role: 条件分支]` 得壬化木，弱极复生，合此必主大贵，但此化合，反以不见庚破格为妙。 → 《穷通宝鉴·三春丁火》#16.1
  - `[ns_qttbj_266]` `[trigger: 女命刑夫]` `[factor_trigger: tiangan_ding AND tiangan_ren AND ding_ren_multiple AND female_chart AND punish_husband_harm_child]` `[role: 例外处理]` 丁年壬月丁日壬时，男主大贵，女则不宜。女命合此，淫贱，刑夫克子。 → 《穷通宝鉴·三春丁火》#16.1"""
    normalized_text_zh: str = """"""
    subject: str = "1. 正月丁火（寅月）"
    factor_refs: list = ['split_jia_ignite', 'wood_chokes_fire', 'plucking_celery']
    
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
        book_id="qiongtongbaojian",
        chapter="",
        l1_anchor="qtbj_v1.0.0_1__正月丁火_寅月_001_L1",
    )
    version: str = "1.0.0"
