"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.619906
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
    semantic_id="qtbj_v1.0.0_1__七月甲木_申月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 1七月甲木申月(SemanticEntry):
    """
    - **原文（source_text）**：
  三秋甲木，木性枯藁，金土乘旺，先丁后庚，丁庚两全，将甲造为画戟。七月甲堪为戟，非丁火不能造庚，非庚不能造甲，丁庚两透，科甲定然。
  庚禄居申，杀印相...
    """
    
    original_text: str = """- **原文（source_text）**：
  三秋甲木，木性枯藁，金土乘旺，先丁后庚，丁庚两全，将甲造为画戟。七月甲堪为戟，非丁火不能造庚，非庚不能造甲，丁庚两透，科甲定然。
  庚禄居申，杀印相生，运行金水，身伴明君。
  或庚透无丁，一富而已，主为人操心太重，不能坐享。或丁透庚藏，亦主青衿小富。或庚多无丁，残疾之人，若为僧道，灾厄可免。

- **分字分词释义**：
  - **木性枯藁**：木的性质枯槁干燥 / 秋木衰死 / 气势衰退
  - **金土乘旺**：金和土正当旺相 / 秋气肃杀 / 甲木受克
  - **画戟**：古代兵器 / 喻成材成器 / 贵器
  - **科甲定然**：科举功名一定能取得 / 大贵之象 / 庚丁配合
  - **庚禄居申**：庚金的禄位在申 / 申月庚旺 / 杀气旺盛
  - **杀印相生**：七杀生印、印生身 / 申藏壬水 / 贵格
  - **身伴明君**：在皇帝身边辅佐 / 大官之象 / 运走金水
  - **操心太重**：忧虑太多 / 庚透无丁之象 / 劳碌

- **规范化释义（primary_lang_explained）**：
  秋季三个月的甲木，木性枯槁，金和土乘旺。首先用丁火（炼金），其次用庚金（劈甲/成器）。如果丁火和庚金两者齐全，能将甲木打造成画戟（兵器）。七月的甲木堪当画戟的材料，没有丁火就不能锻炼庚金，没有庚金就不能雕琢甲木，丁火庚金都透出，科甲功名是一定的。
  庚金的禄位在申，申中藏壬水，构成“杀印相生”（庚生壬，壬生甲）。如果运行金水之地，能身伴明君（做大官）。
  如果庚金透出而没有丁火，只是富人而已，而且主为人操心太重，不能坐享其成。如果丁火透出而庚金藏支，也是秀才（青衿）或小富。如果庚金太多而没有丁火制约，是残疾之人，如果出家为僧道，灾厄可以免除。

- **完整对等诠释（secondary_lang_full）**：
  Jia Wood in the Three Autumn Months is withered in nature, while Metal and Earth are prospering. First use Ding Fire (to refine Metal), then Geng Metal (to carve Wood). If both Ding and Geng are complete, they forge Jia into a Painted Halberd (Weapon). Jia in the 7th Month is suitable to be a Halberd; without Ding, Geng cannot be refined; without Geng, Jia cannot be crafted. If both Ding and Geng are revealed, Civil Service success is certain.
  Geng's Lu (Prosperity) is in Shen, forming "Killing Generating Seal" (as Shen contains Ren Water). If Luck runs through Metal/Water, one accompanies a wise ruler.
  If Geng is revealed without Ding, it is merely wealth, denoting a person who worries too much and cannot enjoy leisure. If Ding is revealed and Geng is hidden, it denotes a scholar (Qingjin) or small wealth. If Geng is excessive without Ding, one becomes disabled; if one becomes a monk or Taoist, disaster can be avoided.

- **核心要点**：
  - **首要用神**：丁火（炼庚）。
  - **配合用神**：庚金（成器）。
  - **格局**：庚丁双透（大贵/科甲）。
  - **杀印相生**：申月特有（申藏壬水），利金水运。
  - **忌讳**：庚多无丁（残疾/操劳）。

- **详细解说**：
  申月甲木为死绝之地，且申金七杀当令，气势肃杀。
  - “死木”原则：死木得金而造。但金太顽，需火炼。
  - 丁庚配合是申月甲木的最佳配置（劈甲引丁，火炼真金）。
  - 申月独特之处在于“杀印相生”，因为申中壬水长生。若无丁，用印化杀也可（身伴明君），但不如用丁制杀格高（科甲画戟）。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_129]` `[trigger: 三秋甲木]` `[factor_trigger: season_autumn AND tiangan_jia AND tiangan_ding AND tiangan_geng]` `[role: 主干]` 三秋甲木，木性枯藁，金土乘旺，先丁后庚。 → 《穷通宝鉴·三秋甲木》#5.1
  - `[ns_qttbj_130]` `[trigger: 申月甲木]` `[factor_trigger: month_shen AND tiangan_jia AND ding_revealed AND geng_revealed]` `[role: 主干依赖]` 七月甲堪为戟，非丁火不能造庚，非庚不能造甲，丁庚两透，科甲定然。 → 《穷通宝鉴·三秋甲木》#5.1
  - `[ns_qttbj_131]` `[trigger: 杀印相生]` `[factor_trigger: month_shen AND tiangan_jia AND pattern_killing_gen_seal AND dayun_metal_water]` `[role: 条件分支]` 庚禄居申，杀印相生，运行金水，身伴明君。 → 《穷通宝鉴·三秋甲木》#5.1
  - `[ns_qttbj_132]` `[trigger: 庚多无丁]` `[factor_trigger: month_shen AND tiangan_jia AND metal_excessive AND NOT tiangan_ding]` `[role: 例外处理]` 庚多无丁，残疾之人，若为僧道，灾厄可免。 → 《穷通宝鉴·三秋甲木》#5.1"""
    normalized_text_zh: str = """"""
    subject: str = "1. 七月甲木（申月）"
    factor_refs: list = ['painted_halberd', 'pattern_killing_gen_seal', 'qingjin_scholar', 'accompanying_wise_ruler']
    
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
        l1_anchor="qtbj_v1.0.0_1__七月甲木_申月_001_L1",
    )
    version: str = "1.0.0"
