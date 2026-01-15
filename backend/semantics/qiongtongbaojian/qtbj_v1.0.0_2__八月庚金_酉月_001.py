"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.578349
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
    semantic_id="qtbj_v1.0.0_2__八月庚金_酉月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 2八月庚金酉月(SemanticEntry):
    """
    - **原文（source_text）**：
  八月庚金，刚锐未退，用丁用甲，丙不可少。若丁甲透，又见一丙，功名显赫，且见羊刃，无刑克，丙杀藏支，名为羊刃驾杀，主出将入相，直介忠臣。
  或丙火重重...
    """
    
    original_text: str = """- **原文（source_text）**：
  八月庚金，刚锐未退，用丁用甲，丙不可少。若丁甲透，又见一丙，功名显赫，且见羊刃，无刑克，丙杀藏支，名为羊刃驾杀，主出将入相，直介忠臣。
  或丙火重重，一丁高透，亦主科甲。丙出丁藏，异路功名。
  或甲藏支，火透而水不透者，亦主清高，衣衿可望。
  或丁藏支内，重见丙火者，此名假杀重重，虽羊刃帖身，却难从杀也。即一丙透，秀而不富。或支见重重甲乙，无用之人。
  总之，旺金木衰，非火莫制，不见丙丁，艺术之辈。

- **分字分词释义**：
  - **刚锐未退**：刚锐之气尚未消退 / 酉月庚金仍旺 / 身强
  - **丙不可少**：丙火不可缺少 / 调候兼制 / 用神
  - **功名显赫**：功名非常显著 / 丁甲丙全 / 贵格
  - **羊刃驾杀**：羊刃制约七杀 / 格局名 / 大贵
  - **出将入相**：出为将军入为宰相 / 文武全才 / 极贵
  - **直介忠臣**：正直刚介的忠臣 / 人品高洁 / 吉象
  - **异路功名**：非正途的功名 / 丙透丁藏 / 次贵
  - **假杀重重**：假七杀太多 / 丙多丁藏 / 凶象
  - **秀而不富**：清秀但不富裕 / 一丙透 / 中平
  - **艺术之辈**：从事技艺的人 / 无丙丁 / 下格

- **规范化释义（primary_lang_explained）**：
  八月（酉月）的庚金，刚锐之气尚未消退，用丁火用甲木，丙火不可少。若丁甲透出，又见一丙火，功名显赫。而且见羊刃（酉中辛金为庚之刃），无刑克，丙杀藏支，名为"羊刃驾杀"，主出将入相，是正直刚介的忠臣。
  如果丙火重重，一个丁火高透，也主科甲。丙火透出丁火藏支，异路功名。
  如果甲木藏支，火透而水不透者，也主清高，秀才可望。
  如果丁火藏在支内，重见丙火者，这名"假杀重重"，虽然羊刃贴身，却难从杀。即使一丙透出，秀而不富。如果地支见重重甲乙木，无用之人。
  总之，旺金木衰，非火莫制，不见丙丁火，艺术之辈。

- **完整对等诠释（secondary_lang_full）**：
  Geng Metal in the 8th Month (Rooster Month): Hard sharpness not yet faded. Use Ding, use Jia, Bing cannot be lacking. If Ding and Jia reveal, plus one Bing, fame is illustrious. Also seeing Sheep Blade, without punishment/destruction, Bing Killing hidden in branch, called "Sheep Blade Riding Killing", implying becoming general or minister, a straight and loyal official.
  If Bing Fire is heavy, one Ding highly revealed, also implies Civil Service. Bing revealed Ding hidden, alternative fame.
  If Jia hidden in branch, Fire revealed Water not revealed, also implies purity and elegance, scholar possible.
  If Ding hidden in branch with heavy Bing Fire, this is "Fake Killing Heavy", though Sheep Blade sticks to body, hard to follow Killing. Even if one Bing reveals, elegant but not rich. If branches see heavy Jia/Yi Wood, a useless person.
  In summary, prosperous Metal weak Wood, without Fire nothing controls. Without Bing/Ding, one of the artisan class.

- **核心要点**：
  - **首要用神**：丁火、甲木、丙火并用。酉月金旺，三者配合最佳。
  - **极贵格**：羊刃驾杀（丙杀藏支+羊刃无冲）。
  - **忌讳**：假杀重重（丙多丁藏），难成大格。

- **详细解说**：
  - 酉月庚金帝旺，气势极旺。
  - 羊刃驾杀：庚以酉为刃（阳刃），丙为七杀。刃杀相配，主武贵。
  - "直介忠臣"：刃杀配合得宜者，性格刚正，能任大事。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_355]` `[trigger: 庚生酉月]` `[factor_trigger: month_you AND tiangan_geng AND tiangan_ding AND tiangan_jia AND tiangan_bing]` `[role: 主干]` 八月庚金，刚锐未退，用丁用甲，丙不可少。 → 《穷通宝鉴·三秋庚金》#32.2
  - `[ns_qttbj_356]` `[trigger: 羊刃驾杀]` `[factor_trigger: month_you AND tiangan_geng AND yangren_pattern AND bing_in_branch]` `[role: 条件分支]` 丙杀藏支，名为羊刃驾杀，主出将入相。 → 《穷通宝鉴·三秋庚金》#32.2
  - `[ns_qttbj_357]` `[trigger: 假杀重重]` `[factor_trigger: month_you AND tiangan_geng AND bing_excessive AND ding_in_branch]` `[role: 例外处理]` 丁藏支内，重见丙火者，此名假杀重重，秀而不富。 → 《穷通宝鉴·三秋庚金》#32.2"""
    normalized_text_zh: str = """"""
    subject: str = "2. 八月庚金（酉月）"
    factor_refs: list = ['yangren_jiasha', 'jiangling_chuxiang', 'fake_killing']
    
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
        l1_anchor="qtbj_v1.0.0_2__八月庚金_酉月_001_L1",
    )
    version: str = "1.0.0"
