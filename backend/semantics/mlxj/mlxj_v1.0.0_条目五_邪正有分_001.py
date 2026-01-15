"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.850579
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
    semantic_id="mlxj_v1.0.0_条目五_邪正有分_001",
    book_id="mlxj",
    engine_id="dream"
)
class 条目五邪正有分(SemanticEntry):
    """
    ### 原文（source_text）

邪正有分，凶人获吉梦，梦则吉矣，德不足以当之，虽吉亦凶，胡可幸也。吉人获凶梦，梦则凶矣，天必有以佑之，虽凶亦吉，犹可避也。至如中怀恶意，梦得吉占，是必所以速其...
    """
    
    original_text: str = """### 原文（source_text）

邪正有分，凶人获吉梦，梦则吉矣，德不足以当之，虽吉亦凶，胡可幸也。吉人获凶梦，梦则凶矣，天必有以佑之，虽凶亦吉，犹可避也。至如中怀恶意，梦得吉占，是必所以速其祸；寔抱仁心而反罹凶兆，是必所以玉其成。君子当察人之为邪为正，为邪中之正，正中之邪，则吉凶如列了，祸福如随影也。

### 规范化释义（primary_lang_explained）

占梦的第五条核心原则是「邪正有分」——必须分辨做梦者的道德品性是邪是正。

凶恶之人获得吉梦，梦象虽然是吉的，但其德行不足以承当这份吉祥，所以虽吉亦凶，不可侥幸。善良之人获得凶梦，梦象虽然是凶的，但上天必定会保佑他，所以虽凶亦吉，凶祸可以避免。

进一步说，心怀恶意之人梦得吉占，这反而是加速其祸患的征兆；真正怀抱仁心之人反遭凶兆，这反而是上天磨砺其成就的方式。

君子占梦应当详察做梦者是邪是正、是邪中藏正还是正中藏邪，如此则吉凶分明如列举、祸福相随如影子。

### 完整对等诠释（secondary_lang_full）

The fifth principle is "Distinction between Evil and Righteous" — one must discern whether the dreamer's moral character is wicked or virtuous.

When an evil person receives an auspicious dream, though the dream appears fortunate, their virtue is insufficient to warrant such blessing — thus fortune becomes misfortune, and they should not count on luck. When a good person receives an ominous dream, though the dream appears unfortunate, Heaven will surely protect them — thus misfortune becomes fortune, and calamity can be avoided.

Furthermore, when one harbors malicious intent yet dreams of good omens, this actually accelerates their disaster. When one truly embraces benevolence yet encounters bad omens, this is Heaven's way of refining their eventual success.

The gentleman interpreting dreams should carefully examine whether the dreamer is wicked or righteous, whether wickedness hides within righteousness or righteousness within wickedness. Thus fortune and misfortune become as clear as itemized lists, and blessing and calamity follow like shadows.

### 核心要点

- 邪正有分是占梦第五核心原则
- 凶人得吉梦，德不当之，虽吉亦凶
- 吉人得凶梦，天必佑之，虽凶亦吉
- 恶意得吉占，反速其祸
- 仁心遭凶兆，反玉其成
- 需辨邪中之正、正中之邪

### 叙事素材（narrative_snippets）

- `[ns_mlxj_016]` `[trigger: 德行判断]` `[factor_trigger: dreamer_virtue]` `[role: 核心原则]` 凶人获吉梦，德不足以当之，虽吉亦凶。 → 《梦林玄解·卷之首》#邪正有分
- `[ns_mlxj_017]` `[trigger: 德行判断]` `[factor_trigger: dreamer_virtue]` `[role: 核心原则]` 吉人获凶梦，天必有以佑之，虽凶亦吉。 → 《梦林玄解·卷之首》#邪正有分"""
    normalized_text_zh: str = """"""
    subject: str = "条目五：邪正有分"
    factor_refs: list = ['dreamer_virtue']
    
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
        book_id="mlxj",
        chapter="",
        l1_anchor="mlxj_v1.0.0_条目五_邪正有分_001_L1",
    )
    version: str = "1.0.0"
