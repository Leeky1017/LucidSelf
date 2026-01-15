"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228128
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
    semantic_id="smth_v1.0.0_十二支对应人生六阶段_001",
    book_id="sanming",
    engine_id="bazi"
)
class 十二支对应人生六阶段(SemanticEntry):
    """
    - **原文（source_text）**：
  何言乎？子丑二位，阴阳始孕，人在胞胎，物藏荄根，未有涯际。寅卯二位，阴阳渐辟，人渐生长，物以拆甲，群葩渐剖，如人将有立身也。辰巳二位，阴阳气盛，物当华...
    """
    
    original_text: str = """- **原文（source_text）**：
  何言乎？子丑二位，阴阳始孕，人在胞胎，物藏荄根，未有涯际。寅卯二位，阴阳渐辟，人渐生长，物以拆甲，群葩渐剖，如人将有立身也。辰巳二位，阴阳气盛，物当华秀，如人三十四十而有立身之地，始有进取之象。午未二位，阴阳彰露，物已成齐，人至五十六十，富贵贫贱可知，凡百兴衰可见。申酉二位，阴阳肃杀，物已收成，人已龟缩，各得其静矣。戌亥二位，阴阳闭塞，物气归根，人当休息，各有归著。

- **分字分词释义**：
  - **始孕**：开始孕育。
  - **荄根**：草根，指植物根部。
  - **未有涯际**：还没有边界形态。
  - **渐辟**：逐渐展开。
  - **拆甲**：破壳而出。
  - **群葩渐剖**：群花逐渐绽放。
  - **立身**：成家立业。
  - **华秀**：开花秀丽。
  - **成齐**：成熟齐备。
  - **肃杀**：收敛凋零。
  - **龟缩**：收缩蜷曲。
  - **归著**：归宿着落。

- **规范化释义（primary_lang_explained）**：
  怎么说呢？子丑两个位置，阴阳开始孕育，人在母腹胞胎中，物藏在草根里，还没有边界形态。寅卯两个位置，阴阳逐渐展开，人渐渐生长，植物破壳而出，群花逐渐绽放，就像人将要成家立业。辰巳两个位置，阴阳之气旺盛，植物正当开花秀丽，就像人三十四十岁有了立身之地，开始有进取的迹象。午未两个位置，阴阳显露彰明，植物已经成熟齐备，人到五十六十岁，富贵贫贱可以知道，各种兴衰都可以看见。申酉两个位置，阴阳收敛凋零，植物已经收成，人已经收缩蜷曲，各得其安静了。戌亥两个位置，阴阳闭塞，植物之气归回根部，人应当休息，各有归宿着落。

- **完整对等诠释（secondary_lang_full）**：
  What does this mean? Zi-Chou two positions: yin-yang begin gestating, humans in mother's womb, plants storing in roots, not yet having boundaries or shape. Yin-Mao two positions: yin-yang gradually opening, humans gradually growing, plants breaking from husks, flower clusters gradually blooming—like humans about to establish themselves. Chen-Si two positions: yin-yang qi flourishing, plants flowering beautifully—like humans at thirty-forty having established ground, beginning to show advancement. Wu-Wei two positions: yin-yang manifest and revealed, plants already mature and complete—humans reaching fifty-sixty, wealth-poverty-nobility-baseness knowable, all rises and declines visible. Shen-You two positions: yin-yang contracting and withering, plants already harvested, humans already withdrawn and curled up, each attaining their quietude. Xu-Hai two positions: yin-yang sealed and blocked, plant qi returning to roots, humans should rest, each having their proper destination.

- **核心要点**：
  - 子丑：胎孕期（未有形态）
  - 寅卯：生长期（破壳绽放）
  - 辰巳：壮年期（30-40岁，立身进取）
  - 午未：成熟期（50-60岁，成败可知）
  - 申酉：收敛期（收成归静）
  - 戌亥：归藏期（归根休息）

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_175]` `[trigger: 十二支对应人生六阶段]` `[factor_trigger: twelve_branches AND life_stages AND yinyang_cycle]` `[role: 主干]` 子丑二位，阴阳始孕，人在胞胎。寅卯二位，阴阳渐辟，人渐生长。辰巳二位，阴阳气盛，如人三十四十。午未二位，物已成齐，人至五十六十。申酉二位，阴阳肃杀。戌亥二位，阴阳闭塞。 → 《三命通会》卷一#十二支对应人生六阶段

- **详细解说**：
  此条用十二地支的六个阶段（每阶段两支）来比喻人生和万物的完整生命周期。子丑对应胎孕期，如种子在土中、胎儿在母腹，形态未显；寅卯对应幼年期，如春天草木破土、人渐长成，准备立身；辰巳对应壮年期（30-40岁），如夏天花开茂盛、人事业有成，开始进取；午未对应成熟期（50-60岁），如秋初果实成熟、人生富贵贫贱已定，兴衰可见；申酉对应收敛期，如秋收冬藏、人老年收缩，各得安静；戌亥对应归藏期，如冬天万物归根、人生休息，各有归宿。这六个阶段构成完整的生命循环，体现"生-长-壮-衰-藏"的自然规律，是纳音象征人生的理论基础。

- **校勘与字词辨析（双语）**：
  - **中文**："荄根"，荄音该，指草根。"涯际"指边界。"拆甲"指种子破壳。"龟缩"比喻老年人身体收缩。"归著"，著音着，指归宿。此段体现了中国古代"天人合一"思想。
  - **English**: "Gai gen" (grass roots), "gai" pronounced like "gai." "Ya ji" means boundaries. "Chai jia" means seeds breaking from husks. "Gui suo" metaphorically describes elderly bodies contracting. "Gui zhu" means proper destination. This passage embodies ancient Chinese "Heaven-Human Unity" philosophy."""
    normalized_text_zh: str = """"""
    subject: str = "十二支对应人生六阶段"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate']
    
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
        l1_anchor="smth_v1.0.0_十二支对应人生六阶段_001_L1",
    )
    version: str = "1.0.0"
