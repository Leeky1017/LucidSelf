"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:19.008880
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
    semantic_id="dts_v1.0.0_乙木_001",
    book_id="dts",
    engine_id="bazi"
)
class 乙木(SemanticEntry):
    """
    - 原文（source_text）：
  乙木虽柔，刲羊解牛，怀丁抱丙，跨鸡乘猴，虚湿之地，骑马亦忧，藤萝系甲，可春可秋.

- 原注（原文注解）：
  　　乙为枝叶之木，柔如花卉，然坐丑未能制之，（...
    """
    
    original_text: str = """- 原文（source_text）：
  乙木虽柔，刲羊解牛，怀丁抱丙，跨鸡乘猴，虚湿之地，骑马亦忧，藤萝系甲，可春可秋.

- 原注（原文注解）：
  　　乙为枝叶之木，柔如花卉，然坐丑未能制之，（丑未阴土，故乙能制.）如宰羊割牛，只要有一丙丁，则虽申酉之月，亦不畏怯，生于子月，（木叶凋零之时，水多益寒.）而又辛壬癸透者，则虽得午，　亦难发生，（乙虽生午，然午能泄乙，况一火不能敌众水也.）若甲与寅多见，譬之縢萝附乔木，春月秋月皆可.

- 分字分词释义：
  - 乙：天干第二，阴木，象藤蔓、枝叶，性柔和而能曲直.
  - 虽：虽然，转折引入.
  - 柔：柔和、细腻，非刚直之性.
  - 刲：刲割，宰割之义（刲羊）.
  - 解：解体、分解（解牛）.
  - 怀：怀抱、内守（怀丁）.
  - 丁：阴火，为乙之所需之火（温养、成色）.
  - 抱：抱持、相依（抱丙）.
  - 丙：阳火，光烈之火，为乙所借以见明.
  - 跨：跨步、跨依（跨鸡）.
  - 鸡：酉（金），乙木跨酉意在借位或逢金处之态势.
  - 乘：乘势、乘依（乘猴）.
  - 猴：申（金），与上句成对，指金地之从容取位.
  - 虚湿之地：地气虚而湿（如子亥、丑未等湿地）.
  - 骑马：乘“午”，午为火，亦为“马”.
  - 亦忧：亦有忧患，言乙木处午，恐火泄其气而枯焦.
  - 藤萝：柔木之象，须系大木以升.
  - 系：系附、依凭.
  - 甲：阳木，乔木，大干，可为乙之所附.
  - 可春可秋：春得令、秋借助，皆可成其用（条件各异）.

 - 规范化释义（primary_lang_explained）：
  乙木好似藤萝花木，质地柔和，最善于依附他物而生，并非真正软弱。位置得当、火气相帮时，也能像“刲羊解牛”那样发挥精细而有力的作用。它喜欢“怀丁抱丙”，借丁火温养、借丙火显色；“跨鸡乘猴”是说即便身处申酉金地，也能找到自己的立足点，只是必须有水来通关、有土来承托，免得被金硬砍。“虚湿之地”水多益寒，需要火来振发；“骑马亦忧”，指虽得午火温暖，却又担心火过分泄身，这就要靠甲木为依附之干、靠水润泽调候，才能良性循环。最理想的，是像藤萝那样系在甲木大树之上：春天得令，秋天借势，两季都能成用，但用法各有不同。

- **次语种完整诠释（secondary_lang_full）**：  
  Yi Wood is likened to vines and flowering plants: flexible, fine‑grained and highly dependent on what it clings to. On its own it is not built to stand like a great trunk, but when it finds the right support it can cut and penetrate with great precision, “like butchering sheep and dismembering oxen”. Warm fire is its first ally: Ding Fire nourishes and protects, while Bing Fire brings visibility and color. Metal terrain such as Shen and You is not automatically fatal to Yi; if there is water to mediate and earth to receive the impact, harsh cutting can turn into delicate carving. In cold, damp places Yi must first be warmed before it can truly sprout; in blazing heat it must be shielded from being over‑drained. The most favorable pattern is when Yi is tied to a strong Jia trunk, using that structure to rise while still receiving warmth, moisture and mediation from fire, water and earth. Thus Yi Wood’s strength does not lie in brute force, but in choosing the right host, the right climate and the right channels, so that softness becomes accuracy rather than weakness.


- **核心要点**：
  - 乙木为阴木，象藤蔓花卉，质地柔和，善于依附
  - 怀丁抱丙：借丁火温养、借丙火显色，乙木宜得温火
  - 跨鸡乘猴：申酉金地非绝对凶地，有水通关、土承托、火温养则化伐为助
  - 虚湿之地骑马亦忧：水寒须先暖后发，火过则恐泄身焦枯
  - 藤萝系甲：依附甲木大树，春秋两季皆可成用
  - 乙木强在找到合适依托，非独立冲天之象

- **详细解说**：
 乙木为天干第二、阴木之代表，象藤蔓花卉，自身柔细弹性足，适合缠绕依附。其强不在独立，而在找到合适的依托：系甲（依附大树）、抱丙（借阳火显色）、怀丁（借阴火温养），皆为"借势成事"。申酉金地并非绝对凶地，若有水通关、土承托、火温养，可化"金伐"为"金助"（刲羊解牛）。子月水寒重在"先暖后发"，秋月金旺重在"先通关再谈克制"。最理想模式是藤萝系甲：以甲木为主干依托，再配以丙丁火暖、水润土承，春秋两季各有用法。

- **narrative_snippets（叙事片段）**：
  - `[ns_dts_028]` `[trigger: 日主=乙木]` `[factor_trigger: tiangan_yi]` `[role: 主干]` 乙木如藤萝花卉，质柔善依，须找合适依托方能成事。 → 《滴天髓·天干论》#乙木
  - `[ns_dts_029]` `[trigger: 乙木逢申酉]` `[factor_trigger: kuaji_chenghou]` `[role: 条件分支]` 乙木跨鸡乘猴，申酉金地非绝对凶，有水通关火温则化伐为助。 → 《滴天髓·天干论》#乙木
  - `[ns_dts_030]` `[trigger: 乙木系甲]` `[factor_trigger: tengluo_xijia]` `[role: 主干依赖]` 藤萝系甲，乙木得甲木依托，可春可秋，两季皆可成用。 → 《滴天髓·天干论》#乙木
  - `[ns_dts_115]` `[trigger: 虚湿先暖]` `[factor_trigger: yi_warmth_state]` `[role: 条件分支]` 乙木居虚湿之地须先借丙丁温暖，再图生发，否则寒湿困蔓。 → 《滴天髓·天干论》#乙木
  - `[ns_dts_116]` `[trigger: 依附失当]` `[factor_trigger: yi_fragility_risk]` `[role: 例外处理]` 乙木若无甲木为依或久困金地无通关，易成缠绕无成之象。 → 《滴天髓·天干论》#乙木

- **L2-术语对齐（Term Glossary）**：

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|---------|-----------|--------|
| 虽柔 | Though Flexible (Sui Rou) | 质地柔和、善于依附 | Supple quality, adept at attachment | yi_mu_rou | new_candidate |
| 刲羊解牛 | Skillful Butchering (Kui Yang Jie Niu) | 精细而有力的操作能力 | Precision and controlled power in action | yi_precision_action | new_candidate |
| 怀丁抱丙 | Embracing Ding Holding Bing | 借丁火温养、借丙火显色 | Drawing warmth from Ding, brightness from Bing | huaiding_baobing | new_candidate |
| 跨鸡乘猴 | Straddling Rooster Riding Monkey | 在申酉金地找到立足点 | Finding footing in You/Shen Metal territory | kuaji_chenghou | new_candidate |
| 藤萝系甲 | Vine Attaching to Trunk | 如藤萝依附大树而生 | Like vines relying on sturdy trees | tengluo_xijia | new_candidate |
| 可春可秋 | Viable Spring and Autumn | 春秋两季皆可成用 | Functional in both spring and autumn | kechun_keqiu | new_candidate |"""
    normalized_text_zh: str = """"""
    subject: str = "乙木"
    factor_refs: list = ['source_ref', 'rel_dts_yi_001', 'tiangan_yi', 'rel_dts_yi_002', 'tiangan_yi', 'rel_dts_yi_003', 'tiangan_yi', 'rel_dts_yi_004', 'tiangan_yi', 'rel_dts_yi_005', 'yi_attachment_mode', 'rel_dts_yi_006', 'yi_support_profile', 'rel_dts_yi_007', 'yi_warmth_state', 'rel_dts_yi_008', 'yi_moisture_state', 'rel_dts_yi_009', 'yi_precision_potential', 'rel_dts_yi_010', 'yi_fragility_risk', 'rel_dts_yi_011', 'yi_boundary', 'evi_dts_yi_001', 'rule_yi_precision_power', 'evi_dts_yi_002', 'tengluo_xijia', 'rule_yi_jia_attachment', 'evi_dts_yi_003', 'rule_yi_moisture_risk', 'concept_flexible_strength', 'concept_attachment_strategy', 'concept_environment_adaptation', 'engine_id', 'tiangan_yi', 'day_master', 'bazi_calculator', 'yi_attachment_mode', 'attachment_pattern', 'bazi_semantic', 'yi_support_profile', 'support_profile', 'bazi_semantic', 'yi_warmth_state', 'warmth_state', 'bazi_semantic', 'yi_moisture_state', 'moisture_state', 'bazi_semantic', 'yi_precision_potential', 'evaluation', 'bazi_semantic', 'yi_fragility_risk', 'risk_indicator', 'bazi_rule_engine', 'yi_boundary', 'boundary', 'bazi_rule_engine']
    
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
        book_id="dts",
        chapter="",
        l1_anchor="dts_v1.0.0_乙木_001_L1",
    )
    version: str = "1.0.0"
