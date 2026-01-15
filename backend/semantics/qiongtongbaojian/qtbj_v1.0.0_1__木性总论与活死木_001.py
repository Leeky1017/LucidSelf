"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.619736
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
    semantic_id="qtbj_v1.0.0_1__木性总论与活死木_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 1木性总论与活死木(SemanticEntry):
    """
    - **原文（source_text）**：
  木性腾上而无所止，气重则欲金任使，有金则有惟高惟敛之德。仍爱土重，则根蟠深固，土少则有枝茂根危之患。木赖水生，少则滋润，多则漂流。
  甲戌、乙亥、木...
    """
    
    original_text: str = """- **原文（source_text）**：
  木性腾上而无所止，气重则欲金任使，有金则有惟高惟敛之德。仍爱土重，则根蟠深固，土少则有枝茂根危之患。木赖水生，少则滋润，多则漂流。
  甲戌、乙亥、木之源。甲寅、乙卯、木之乡。甲辰、乙巳、木之生。皆活木也。
  甲申、乙酉、木受克。甲午、乙未、木自死。甲子、乙丑、金克木。皆死木也。
  生木得火而秀，丙丁相同。死木得金而造，庚辛必利。生木见金自伤，死木得火自焚，无风自止，其势乱也。遇水返化其源，其势尽也。
  金木相等，格谓斲轮。若向秋生，反为伤斧，是秋生忌金重也。

- **分字分词释义**：
  - **腾上**：向上升腾 / 木的生长方向 / 少阳之性
  - **无所止**：没有止境 / 无限生发 / 木的不可抑制性
  - **任使**：使用、驾驭 / 金修剪木 / 成器之功
  - **惟高惟敛**：既高耸又收敛 / 有金则能成形 / 兼具二德
  - **根蟠深固**：根盘结深且牢固 / 土厚护根 / 稳定之象
  - **枝茂根危**：枝叶茂盛但根基危险 / 土薄无依 / 头重脚轻
  - **漂流**：水多木浮 / 失去根基 / 无定之象
  - **活木**：有生气根气的木 / 可生长之木 / 喜火忌金
  - **死木**：无生气的木 / 干枯之材 / 喜金忌火
  - **斲轮**：雕琢车轮 / 金木平衡成大器 / 贵格之名
  - **伤斧**：损伤斧头 / 秋金太强克木 / 反为不吉

- **规范化释义（primary_lang_explained）**：
  木的本性是向上升腾且无止境，如果木气太重，就需要金来修剪约束，有金才能兼具高耸与收敛的美德。木喜爱土厚，这样根基才能盘结深固；若土少，就会有枝叶繁茂但根基危险的隐患。木依赖水生长，水少能滋润，水多则会导致漂流。
  甲戌、乙亥是木的源头（亥为长生、戌包含火土），甲寅、乙卯是木的故乡（临官帝旺），甲辰、乙巳是木的生地（辰为余气、巳为沐浴长生），这些都是活木。
  甲申、乙酉是木受克（绝地），甲午、乙未是木自死（死墓之地），甲子、乙丑是金克木（子中纳音金、丑中金库），这些都是死木。
  活木得到火就能发荣秀气，丙火丁火作用相同。死木得到金就能雕琢成器，庚金辛金必定有利。
  活木见金会损伤自己，死木见火会焚烧自己。如果没有风木却停止不动，其势态是混乱的。若遇到水反而化回源头（水多木漂/腐），其势态就尽绝了。
  金与木力量相当，这种格局叫做“斲轮”（雕琢轮毂，成大器）。但如果是秋天出生，反而会伤损斧头（木坚金缺的变种，或意指秋金太强反伤木），所以秋生忌讳金太重。

- **完整对等诠释（secondary_lang_full）**：
  The nature of Wood is to ascend without limit. If its Qi is heavy, it desires Metal to employ and restrain it; with Metal, it possesses the virtue of being both lofty and disciplined. It loves heavy Earth, which allows its roots to coil deep and firm; if Earth is scarce, it suffers from flourishing branches but endangered roots. Wood relies on Water for birth; a little moistens it, but too much makes it drift.
  Jia-Xu, Yi-Hai are the Source of Wood. Jia-Yin, Yi-Mao are the Hometown of Wood. Jia-Chen, Yi-Si are the Birth of Wood. These are all "Live Wood".
  Jia-Shen, Yi-You are Wood under control. Jia-Wu, Yi-Wei are Wood in self-death. Jia-Zi, Yi-Chou are Metal controlling Wood. These are all "Dead Wood".
  Live Wood obtains Fire and becomes elegant (blooms); Bing and Ding are the same. Dead Wood obtains Metal and is crafted; Geng and Xin are beneficial.
  Live Wood meeting Metal is self-injury; Dead Wood meeting Fire is self-incineration. If it stops without wind, its momentum is chaotic. If it meets Water and reverts to its source, its momentum is exhausted.
  When Metal and Wood are equal, the pattern is called "Carving the Wheel" (Zhuo Lun). If born in Autumn, it turns into "Damaging the Axe", meaning Autumn birth dreads excessive Metal.

- **核心要点**：
  - **活木与死木**：这是本书极重要的区分。有根气、生机者为活木；无根气、死绝者为死木。
  - **活木用法**：喜火（泄秀、开花），怕金（受伤）。
  - **死木用法**：喜金（雕琢成器），怕火（焚化），怕水（腐烂）。
  - **金木平衡**：活木要根固，死木要成器。

- **详细解说**：
  这段提出了《穷通宝鉴》独特的“活木死木”理论。这与《子平真诠》的旺衰论略有不同。
  - 活木（有水生、有根、有土培）：类比为生长中的树，宜见阳光（火）开花，忌见斧头（金）砍伐。
  - 死木（无根、死绝、干燥）：类比为木材，宜见斧头（金）雕琢成栋梁家具，忌见火烧（成灰）或水泡（腐烂）。
  - 特别注意甲子一柱被列为死木（因子水寒冷腐木且纳音金），这在实战中需仔细辨别。

- **校勘与字词辨析**：
  - 原文"无风自止"，语意较晦涩，意指木若无生气（无风）则停止生长。
  - "甲子乙丑金克木"，指纳音海中金，或指子丑合土金之气。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_038]` `[trigger: 木性]` `[factor_trigger: xiang_shaoyang AND element_wood]` `[role: 主干]` 木性腾上而无所止，气重则欲金任使。 → 《穷通宝鉴·论木》#2.1
  - `[ns_qttbj_039]` `[trigger: 木性]` `[factor_trigger: element_wood AND element_metal AND element_earth]` `[role: 主干依赖]` 有金则有惟高惟敛之德，土重则根蟠深固。 → 《穷通宝鉴·论木》#2.1
  - `[ns_qttbj_040]` `[trigger: 木性]` `[factor_trigger: element_wood AND element_water]` `[role: 条件分支]` 木赖水生，少则滋润，多则漂流。 → 《穷通宝鉴·论木》#2.1
  - `[ns_qttbj_041]` `[trigger: 活木]` `[factor_trigger: wood_live]` `[role: 主干]` 甲戌乙亥木之源，甲寅乙卯木之乡，甲辰乙巳木之生，皆活木也。 → 《穷通宝鉴·论木》#2.1
  - `[ns_qttbj_042]` `[trigger: 死木]` `[factor_trigger: wood_dead]` `[role: 主干]` 甲申乙酉木受克，甲午乙未木自死，甲子乙丑金克木，皆死木也。 → 《穷通宝鉴·论木》#2.1
  - `[ns_qttbj_043]` `[trigger: 活木用法]` `[factor_trigger: wood_live AND (live_wood_likes_fire OR live_wood_fears_metal)]` `[role: 条件分支]` 生木得火而秀，丙丁相同；生木见金自伤。 → 《穷通宝鉴·论木》#2.1
  - `[ns_qttbj_044]` `[trigger: 死木用法]` `[factor_trigger: wood_dead AND (dead_wood_likes_metal OR dead_wood_fears_fire)]` `[role: 条件分支]` 死木得金而造，庚辛必利；死木得火自焚。 → 《穷通宝鉴·论木》#2.1
  - `[ns_qttbj_045]` `[trigger: 斲轮格]` `[factor_trigger: pattern_carving_wheel AND season_autumn]` `[role: 例外处理]` 金木相等，格谓斲轮；若向秋生，反为伤斧。 → 《穷通宝鉴·论木》#2.1"""
    normalized_text_zh: str = """"""
    subject: str = "1. 木性总论与活死木"
    factor_refs: list = ['wood_live', 'wood_dead', 'pattern_carving_wheel', 'roots_coiled_deep', 'wood_drifting']
    
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
        l1_anchor="qtbj_v1.0.0_1__木性总论与活死木_001_L1",
    )
    version: str = "1.0.0"
