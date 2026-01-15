"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.619936
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
    semantic_id="qtbj_v1.0.0_4__八月甲木_酉月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 4八月甲木酉月(SemanticEntry):
    """
    - **原文（source_text）**：
  八月甲木，木囚金旺。丁火为先，次用丙火，庚金再次。
  一丁一庚，科甲定显。癸水一透，科甲不全。
  丙庚两透，富大贵小。丙丁全无，僧道之命。
  丙...
    """
    
    original_text: str = """- **原文（source_text）**：
  八月甲木，木囚金旺。丁火为先，次用丙火，庚金再次。
  一丁一庚，科甲定显。癸水一透，科甲不全。
  丙庚两透，富大贵小。丙丁全无，僧道之命。
  丙透无癸，富贵双全。有癸制丙，寻常之人。

- **分字分词释义**：
  - **木囚金旺**：木被囚禁、金正旺盛 / 酉月状态 / 官杀当令
  - **丁火为先**：丁火是首选用神 / 炼金成器 / 优先
  - **次用丙火**：其次用丙火 / 暖局调候 / 次选
  - **科甲定显**：科举功名一定显赫 / 丁庚配合 / 贵象
  - **科甲不全**：科举功名不完整 / 癸伤丁 / 减等
  - **富大贵小**：富气大贵气小 / 丙庚配合 / 食神制杀
  - **僧道之命**：出家为僧道的命 / 无火 / 孤寒
  - **寻常之人**：普通平凡的人 / 癸制丙 / 下格

- **规范化释义（primary_lang_explained）**：
  八月（酉月）的甲木，木处于囚地，金处于旺地（官星当令）。首先用丁火（制杀/炼金），其次用丙火（调候/暖局），庚金再次之（此时金已极旺，不缺金，但需透出成格）。
  如果透出一个丁火和一个庚金（火炼真金），科甲功名一定显赫。如果透出一个癸水（伤丁），科甲就不完全（或难成）。
  如果丙火和庚金两透（食神制杀），富气大而贵气小。如果丙火丁火全无（金旺木寒无火），是僧道（孤独贫寒）的命。
  如果丙火透出且没有癸水，富贵双全。如果有癸水制丙，只是寻常普通人。

- **完整对等诠释（secondary_lang_full）**：
  Jia Wood in the 8th Month (Rooster Month) is imprisoned while Metal is prosperous. First use Ding Fire, then Bing Fire, and lastly Geng Metal.
  If one Ding and one Geng are revealed, Civil Service success is certain. If one Gui Water is revealed (hurting Fire), success is incomplete.
  If both Bing and Geng are revealed (Food controlling Killing), wealth is great but nobility is small. If neither Bing nor Ding is present, it is a life of a monk or Taoist.
  If Bing is revealed without Gui, wealth and nobility are complete. If Gui appears to control Bing, one is an ordinary person.

- **核心要点**：
  - **首要用神**：丁火（炼金）。酉月金旺，无火则顽，有火则贵。
  - **次要用神**：丙火（暖局）。秋深气寒，丙火解冻。
  - **格局高低**：丁庚（贵） > 丙庚（富）。
  - **忌讳**：癸水（灭火）。

- **详细解说**：
  酉月甲木，正官当令，但此官气太重（金旺木囚），实则为杀。
  - 必须用火。丁火炼金为上，叫“铸印”；丙火暖局制金为次，叫“制杀”。
  - 这里的“庚金再次”意思不是不需要庚，而是金本身已旺，不需要刻意生扶，只需要透干成格。
  - 无火之局，金寒木冷，死气沉沉，故为僧道。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_140]` `[trigger: 酉月甲木]` `[factor_trigger: month_you AND tiangan_jia AND tiangan_ding]` `[role: 主干]` 八月甲木，木囚金旺，丁火为先，次用丙火，庚金再次。 → 《穷通宝鉴·三秋甲木》#5.4
  - `[ns_qttbj_141]` `[trigger: 酉月科甲]` `[factor_trigger: month_you AND tiangan_jia AND ding_revealed AND geng_revealed]` `[role: 主干依赖]` 一丁一庚，科甲定显。癸水一透，科甲不全。 → 《穷通宝鉴·三秋甲木》#5.4
  - `[ns_qttbj_142]` `[trigger: 酉月富贵]` `[factor_trigger: month_you AND tiangan_jia AND bing_revealed AND geng_revealed]` `[role: 条件分支]` 丙庚两透，富大贵小。丙透无癸，富贵双全。 → 《穷通宝鉴·三秋甲木》#5.4
  - `[ns_qttbj_143]` `[trigger: 酉月僧道]` `[factor_trigger: month_you AND tiangan_jia AND NOT tiangan_bing AND NOT tiangan_ding]` `[role: 例外处理]` 丙丁全无，僧道之命。 → 《穷通宝鉴·三秋甲木》#5.4"""
    normalized_text_zh: str = """"""
    subject: str = "4. 八月甲木（酉月）"
    factor_refs: list = ['wood_imprisoned_metal_prosperous', 'incomplete_success']
    
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
        l1_anchor="qtbj_v1.0.0_4__八月甲木_酉月_001_L1",
    )
    version: str = "1.0.0"
