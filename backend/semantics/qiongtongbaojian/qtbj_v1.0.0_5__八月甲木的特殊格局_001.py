"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.619946
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
    semantic_id="qtbj_v1.0.0_5__八月甲木的特殊格局_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 5八月甲木的特殊格局(SemanticEntry):
    """
    - **原文（source_text）**：
  支成火局，可许假贵，戊己一透，可作富翁。
  或支成金局，干露庚金，为木被金伤，必主残疾，得丙丁破金，亦主老来暗疾。
  或支成木局，干透比劫，反取庚...
    """
    
    original_text: str = """- **原文（source_text）**：
  支成火局，可许假贵，戊己一透，可作富翁。
  或支成金局，干露庚金，为木被金伤，必主残疾，得丙丁破金，亦主老来暗疾。
  或支成木局，干透比劫，反取庚金为先，次用丁火。

- **分字分词释义**：
  - **支成火局**：地支合成火局 / 伤官局 / 巳午戌或寅午戌
  - **假贵**：虚假的贵气 / 非正途功名 / 伤官见官
  - **富翁**：富有之人 / 土财生发 / 伤官生财
  - **木被金伤**：木被金克伤 / 金局庚透 / 残疾之象
  - **暗疾**：隐藏的疾病 / 慢性病 / 余患
  - **支成木局**：地支合成木局 / 亥卯未 / 身旺
  - **比劫**：比肩劫财 / 同类 / 身旺之象
  - **反取庚金**：反过来取庚金为用 / 制比劫 / 身旺喜杀

- **规范化释义（primary_lang_explained）**：
  如果地支合成火局（伤官局），可以许诺假贵（非正途功名），如果戊己土一透出（伤官生财），可以做富翁。
  如果地支合成金局，天干透出庚金，这叫“木被金伤”，必主残疾。如果得到丙丁火破金救应，也主老来有暗疾（金克木之根，终有伤）。
  如果地支合成木局，天干透出比劫，这叫“身旺”，反过来取庚金为先（制劫），次用丁火（泄秀/炼金）。

- **完整对等诠释（secondary_lang_full）**：
  If branches form a Fire frame, it promises false nobility; if Wu/Ji Earth is revealed, one can be a rich man.
  If branches form a Metal frame and Geng Metal is revealed on stems, it is "Wood Injured by Metal", implying certain disability. If Bing/Ding Fire is obtained to break the Metal, it still implies hidden diseases in old age.
  If branches form a Wood frame and Parallel/Rob Wealth are revealed, conversely take Geng Metal first, then Ding Fire.

- **核心要点**：
  - **火局（伤官）**：假贵（火克官贵气损），富翁（生财）。
  - **金局（官杀）**：极凶（木被金伤），残疾。火虽能救，难免暗疾。
  - **木局（比劫）**：身旺变格，喜金（反取庚金）。

- **详细解说**：
  - 八月金旺，若再成金局，甲木必死。此时火是唯一的救药，但即使有救，金木交战，筋骨必伤（木主筋骨，金主刀兵）。
  - 若成木局（如亥卯未），甲木由弱转强，此时不忌金，反而喜金制身，这叫“身杀两停”或“羊刃驾杀”的变种。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_144]` `[trigger: 酉月火局]` `[factor_trigger: month_you AND tiangan_jia AND dizhi_fire_frame AND (tiangan_wu OR tiangan_ji)]` `[role: 主干]` 支成火局，可许假贵，戊己一透，可作富翁。 → 《穷通宝鉴·三秋甲木》#5.5
  - `[ns_qttbj_145]` `[trigger: 木被金伤]` `[factor_trigger: month_you AND tiangan_jia AND dizhi_metal_frame AND geng_revealed]` `[role: 例外处理]` 支成金局，干露庚金，为木被金伤，必主残疾。 → 《穷通宝鉴·三秋甲木》#5.5
  - `[ns_qttbj_146]` `[trigger: 酉月木局]` `[factor_trigger: month_you AND tiangan_jia AND dizhi_wood_frame AND shishen_parallel_revealed]` `[role: 条件分支]` 支成木局，干透比劫，反取庚金为先，次用丁火。 → 《穷通宝鉴·三秋甲木》#5.5"""
    normalized_text_zh: str = """"""
    subject: str = "5. 八月甲木的特殊格局"
    factor_refs: list = ['false_nobility', 'hidden_disease']
    
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
        l1_anchor="qtbj_v1.0.0_5__八月甲木的特殊格局_001_L1",
    )
    version: str = "1.0.0"
