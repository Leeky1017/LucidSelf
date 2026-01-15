"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.042720
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
    semantic_id="smth_v1.0.0_属相相胜与胜负局限_001",
    book_id="sanming",
    engine_id="bazi"
)
class 属相相胜与胜负局限(SemanticEntry):
    """
    - **原文（source_text）**：
  寅，木也，其禽虎；戌，土也，其禽犬。丑、未亦土也，丑禽牛，未禽羊：木胜土，故犬与牛羊为虎所服。亥，水也，其禽豕；巳，火也，其禽蛇；子亦水也，其禽鼠；午...
    """
    
    original_text: str = """- **原文（source_text）**：
  寅，木也，其禽虎；戌，土也，其禽犬。丑、未亦土也，丑禽牛，未禽羊：木胜土，故犬与牛羊为虎所服。亥，水也，其禽豕；巳，火也，其禽蛇；子亦水也，其禽鼠；午亦火也，其禽马：水胜火，故豕食蛇，火为水所害，故马食鼠屎而腹胀。然亦有不相胜者：午，马也；子，鼠也；酉，鸡也；卯，兔也：水胜火，鼠何不逐马？金胜木，鸡何不啄兔？亥，豕也；未，羊也；丑，牛也：土胜水，牛羊何不杀豕？巳，蛇也；申，猴也：火胜金，蛇何不食猕猴？猕猴畏鼠者也，啮猕猴者犬也：鼠，水，猕猴，金也——水不胜金，猕猴何故畏鼠？戌，土也；申，猴也：土不胜金，猴何故畏犬？十二辰之禽，以气性相克，则尤不相应。大凡含血之虫相服，至于相啖食者，以齿牙钝利、筋力优劣，自相胜服也。

- **分字分词释义**：
  - **其禽**：这里的「禽」泛指所取之象，动物不必限于飞禽。
  - **相服 / 不相胜**：有的动物按五行相生相克可推服从关系，有的则并不符合简单克胜逻辑。
  - **气性相克不相应**：动物真实气性与五行抽象克制关系并不总能一一对应。

- **规范化释义（primary_lang_explained）**：
  本段借具体动物关系说明：若按五行「木克土、水克火、土克水、火克金、金克木」去套用属相，会得到一套「谁胜谁、谁服谁」的列表，例如虎克犬牛羊、豕食蛇、马受水害等。但作者马上指出，现实中还有许多并不符合这种简单克胜的情形：如水胜火，却见不着老鼠到处驱逐马；金胜木，鸡也未必啄兔；许多动物之间的强弱，更取决于牙齿锋钝、筋骨强弱等具体条件，而非单一的五行关系。由此说明：属相之象虽可借以联想，但绝不能被当作现实物理世界的因果解释。

- **完整对等诠释（secondary_lang_full）**：
  Here the text uses concrete animal pairings to warn against over‑reading the zodiac. If we naively apply the Five Elements—Wood controlling Earth, Water controlling Fire, Earth controlling Water, Fire controlling Metal, Metal controlling Wood—we can construct an impressive chart of “who overcomes whom”: tigers subdue dogs, oxen and goats; pigs eat snakes; water harms fire so horses suffer; and so on. But the author immediately points out many cases that do not fit such neat schemes: if Water defeats Fire, why do mice not routinely drive off horses? If Metal defeats Wood, why do chickens not reliably peck down rabbits? In reality, who dominates whom depends more on teeth, strength and temperament than on any abstract elemental label. The point is that zodiac images are tools for analogy and story‑telling, not literal causal laws. They can help us remember and explain patterns, but they must not replace careful reasoning about structure, context and scale."""
    normalized_text_zh: str = """"""
    subject: str = "属相相胜与胜负局限"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'zodiac_control_limitation', 'wuxing_control_mapping', 'bazi_semantic', 'zodiac_story_template', 'stereotype_risk_flag', 'source_ref', 'rel_smth_xss_001', 'shuxiang_keshi', 'rel_smth_xss_002', 'wuxing_ke', 'rel_smth_xss_003', 'biyu', 'evi_smth_xss_001', 'shuxiang_juxian', 'rule_xss', 'concept_analogy_limit']
    
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
        l1_anchor="smth_v1.0.0_属相相胜与胜负局限_001_L1",
    )
    version: str = "1.0.0"
