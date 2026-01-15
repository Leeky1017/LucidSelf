"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.439711
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
    semantic_id="dvd_v1.0.0_arm_手臂_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Arm手臂(SemanticEntry):
    """
    ### Source Text

> **General Meaning**: The arm is a picture of security, strength and favor.

**Dre...
    """
    
    original_text: str = """### Source Text

> **General Meaning**: The arm is a picture of security, strength and favor.

**Dreams - Positive**: Arm speaks of your abilities and strengths. "Right hand" speaks of position of authority. Being surrounded by strong arms = protection and security. Dreaming of being held securely = Lord reassuring He's taking care of you.

**Dreams - Negative**: Arm causing damage with negative emotion = things that hinder or block spiritual life. Weak arm = weakness being exposed. Unable to use arm = trying to do things in own strength instead of trusting God. Arm being damaged = attack causing weakness and loss of favor.

**Visions - Positive** (Deut 9:29): "Your stretched out arm"—the arm of the Lord is a tower of strength and deliverance. An embrace from the Lord speaks of acceptance regardless of what you've done.

**Visions - Negative** (2 Chron 32:8): "Arm of flesh"—represents fleshly strength, human and not comparable to God's. Trying to do something in own strength that God can do better.

**See also**: Hand, Back, Body

### Key Terms

| Term | Definition | Significance |
|------|------------|--------------|
| Arm | Strength, ability, security | Action capacity |
| Right hand | Position of authority | Leadership |
| Arm of Lord | Divine strength/deliverance | God's power |
| Arm of flesh | Human strength | Self-reliance |

### English Paraphrase

Arm = security, strength, favor. **Positive**: Your abilities and strengths. Right hand = authority position. Strong arms surrounding you = protection. Being held = Lord's reassurance. Lord's stretched out arm (Deut 9:29) = tower of strength, deliverance, acceptance. **Negative**: Arm causing damage = hindrances in spiritual life. Weak arm = exposed weakness. Unable to use arm = relying on self instead of God. Arm of flesh (2 Chron 32:8) = human strength, not comparable to God's—let Him do what you're trying to do yourself.

### Chinese Interpretation（完整对等诠释）

手臂 = 安全、力量、恩惠。**正面**：你的能力和长处。右手 = 权柄位置。强壮的手臂环绕 = 保护。被抱着 = 主的安慰。耶和华伸出的膀臂（申9:29）= 力量的塔楼、拯救、接纳。**负面**：手臂造成伤害 = 灵命中的阻碍。软弱的手臂 = 暴露的软弱。无法使用手臂 = 靠自己而非信靠神。肉体的膀臂（代下32:8）= 人的力量，无法与神相比——让祂做你试图自己做的事。

### Narrative Snippets

- `[ns_dav_a041]` `[trigger: 梦手臂]` `[factor_trigger: dream_symbol_arm]` `[role: 主干]` Arm = security, strength, favor—your abilities and action capacity. → Dreams Dictionary #Arm
- `[ns_dav_a042]` `[trigger: 神的膀臂]` `[factor_trigger: dream_symbol_arm AND strength_source]` `[role: 条件分支]` Arm of the Lord = tower of strength, deliverance, acceptance (Deut 9:29). → Dreams Dictionary #Arm
- `[ns_dav_a043]` `[trigger: 肉体膀臂]` `[factor_trigger: dream_symbol_arm AND strength_source]` `[role: 条件分支]` Arm of flesh = human strength, self-reliance—let God do what you're trying to do yourself. → Dreams Dictionary #Arm"""
    normalized_text_zh: str = """"""
    subject: str = "Arm 手臂"
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
        book_id="dreams_visions_dict",
        chapter="",
        l1_anchor="dvd_v1.0.0_arm_手臂_001_L1",
    )
    version: str = "1.0.0"
