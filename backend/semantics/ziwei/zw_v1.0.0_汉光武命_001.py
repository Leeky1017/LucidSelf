"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699476
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
    semantic_id="zw_v1.0.0_汉光武命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 汉光武命(SemanticEntry):
    """
    - 分字分词释义：

  - **马头带箭**：特定格局主带兵用武、镇守疆场之象。
  - **权禄生逢**：命主生年即逢权星与禄星同会，主既握实权又享厚禄。
  - **则宫双美**：权宫与禄宫皆美...
    """
    
    original_text: str = """- 分字分词释义：

  - **马头带箭**：特定格局主带兵用武、镇守疆场之象。
  - **权禄生逢**：命主生年即逢权星与禄星同会，主既握实权又享厚禄。
  - **则宫双美**：权宫与禄宫皆美，主位登九五。
  - **限行吉地**：二十四岁后大限多行吉地，一路高升。
  - **大限入地劫之宫**：五十四岁大限入地劫宫，主基础被侵蚀。
  - **小限天伤不吉**：小限遇天伤凶曜，主身体衰退或收束阶段。
  - **阳男金四局**：汉光武命盘的五行局数，金四局主刚断武勇。

- **原文（source_text）**：  
  汉光武命。阳男金四局。马头带箭，镇御□疆，权禄生逢，则宫双美。二十四岁后，限行吉地，位登九五，直到五十四，大限入于地劫之宫，小限天伤不吉，损寿。

- **规范化释义（primary_lang_explained）**：  
  汉光武命为阳男金四局，命宫成「马头带箭」之格，主带兵用武、镇守疆场之象；再得权星、禄星同来，形成「权禄生逢，则宫双美」，预示其既握实权又享厚禄。二十四岁之后，大限多行吉地，借助此格一路高升，终于「位登九五」，以帝王之身统一山河。  
  然而，原文也标出寿命节点：至五十四岁时，大限入地劫之宫，小限又遇天伤凶曜，「损寿」之语，表明此时虽仍在高位，却因结构被地劫、天伤侵蚀，而难以再长久维持。此命例展示「武勋帝王」一类命局：前半生在马头带箭的推动下奋起建功，后期则受到灾星与消耗星限制，寿命略短于本可达到的极限。

- **完整对等诠释（secondary_lang_full）**：  
  The chart of Emperor Guangwu of Han belongs to a Yang Metal native of the Fourth Configuration. The Life palace exhibits the "horse‑head with arrow" pattern, emblematic of leading troops and defending frontiers. When joined by stars of power and stipends, this becomes a configuration where both authority and income are exceptionally strong—"both palaces made beautiful by power and lu." After the age of twenty‑four his major periods traverse favourable terrain, allowing him to rise steadily until he "ascends the Nine‑Five," the throne itself.  
  Yet the text also marks a limit to this ascent. Around fifty‑four the major period moves into the house of Di Jie, the Earth Robber, while the minor period meets the wounding star Tian Shang. The note that this "cuts the lifespan" indicates that even for a victorious emperor the combination of erosion and injury eventually brings his life to a somewhat shortened close. The case exemplifies a martial ruler whose early and middle years are driven by conquest and consolidation, while later years are constrained by the accumulated toll of malefic forces.

- **核心要点**：  
  1. 马头带箭配合权禄生逢，构成「带兵建国、位登九五」的武勋帝王格。  
  2. 二十四岁后大限多行吉地，使命主得以顺势完成从将帅到帝王的跃迁。  
  3. 五十四岁大限入地劫、小限逢天伤，成为寿元略减、盛极而收的关键年份。

- **叙事素材（narrative_snippets）**：
  - **马头带箭**："马头带箭，镇御□疆"，汉光武命主以用兵安边、镇御四方著称。
  - **权禄双美**："权禄生逢，则宫双美"，权星、禄星同会，使其既握兵权又享帝王俸禄。
  - **位登九五**："二十四岁后，限行吉地，位登九五"，二十四岁之后行吉地，完成从将帅到帝位的跃迁。
  - **现代应用**：强烈「马头带箭」格局在现代多见于高压管理者或创业者，前半生冲锋陷阵、拼杀市场；当运势转入地劫天伤之年，应当学会收兵与治理内部，把精力从对外开拓转向稳健经营与自我修复。"""
    normalized_text_zh: str = """"""
    subject: str = "汉光武命"
    factor_refs: list = ['pattern_matou_daijian', 'pattern_quanlu_shengfeng', 'pattern_zegong_shuangmei', 'result_weideng_jiuwu', 'malefic_dijie_gong', 'malefic_tianshang_buji']
    
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
        book_id="ziwei",
        chapter="",
        l1_anchor="zw_v1.0.0_汉光武命_001_L1",
    )
    version: str = "1.0.0"
