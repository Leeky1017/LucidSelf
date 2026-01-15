"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.619765
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
    semantic_id="qtbj_v1.0.0_4__秋季之木_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 4秋季之木(SemanticEntry):
    """
    - **原文（source_text）**：
  秋月之木，气渐凄凉，形渐凋败。初秋之时，火气未除，尤喜水土以相滋。中秋之令，果以成实，欲得刚金而修削。霜降后不宜水盛，水盛则木漂。寒露节又喜火炎，火炎...
    """
    
    original_text: str = """- **原文（source_text）**：
  秋月之木，气渐凄凉，形渐凋败。初秋之时，火气未除，尤喜水土以相滋。中秋之令，果以成实，欲得刚金而修削。霜降后不宜水盛，水盛则木漂。寒露节又喜火炎，火炎则木实。木多有多材之美，土厚无自任之能。

- **分字分词释义**：
  - **气渐凄凉**：生气逐渐萧瑟 / 秋木衰退 / 金气当令
  - **形渐凋败**：形态逐渐凋零衰败 / 秋木失令 / 死绝之象
  - **火气未除**：夏天的火气还没消退 / 初秋气候 / 申月特征
  - **相滋**：互相滋养 / 水土护根 / 化解金气
  - **果以成实**：果实已经结成 / 中秋成熟 / 酉月特征
  - **刚金**：刚强的金（庚金） / 修剪成器 / 死木喜金
  - **木漂**：水多木浮 / 晚秋木虚怕水 / 戌月忌讳
  - **木实**：木变得坚实 / 火暖成材 / 寒露后喜火
  - **多材之美**：多才多艺或材料丰富 / 木多的好处 / 但需金剪
  - **无自任之能**：没有能力胜任财星 / 身弱财多 / 土厚之患

- **规范化释义（primary_lang_explained）**：
  秋天的木，生气逐渐凄凉，形态逐渐凋零衰败。初秋（申月）的时候，夏天的火气还没完全消除，特别喜欢水和土来滋润和培养（土生金、水泄金气养木）。中秋（酉月）的时候，果实已经结成，希望能得到刚强的金来修剪（成器）。霜降（戌月）以后，不宜水太盛，水盛了木就会漂浮（因为此时木已虚）。寒露节（戌月）又喜欢火来温暖，火暖则木变得结实（实木成材）。木多有作为多才多艺或材料丰富的美意，土太厚则木无力克土（无法胜任财星）。

- **完整对等诠释（secondary_lang_full）**：
  Wood in Autumn has gradually desolated Qi and fading form. In Early Autumn (Shen month), the Fire energy is not yet gone, so it especially likes Water and Earth for nourishment. In Mid-Autumn (You month), fruits have formed; it desires rigid Metal for pruning. After Frost Descent (Xu month), abundant Water is not suitable; if Water is abundant, Wood drifts. In the Cold Dew solar term, it likes blazing Fire; Fire makes the Wood solid. Abundant Wood has the beauty of plentiful materials, but if Earth is too thick, Wood lacks the capability to handle it.

- **核心要点**：
  - 秋木凋零，分三阶段论。
  - 初秋（申）：喜水土（化金气）。
  - 中秋（酉）：喜刚金（修剪成器/死木原理）。
  - 晚秋（戌）：忌水盛（木漂），喜火（制金暖木）。
  - 财多身弱：土厚则木无力胜任。

- **详细解说**：
  秋木（申酉戌月）总体处于死绝之地。
  - 申月：虽金旺，但申中藏壬水，有生机，故"火气未除"时用水土护根。
  - 酉月：金气最纯，木气最死，此时适用"死木喜金"理论，修剪成器。
  - 戌月：进冬，水气进气，但木根枯，怕水多漂木，喜火暖身防冻，同时火能炼金制金。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_058]` `[trigger: 秋木状态]` `[factor_trigger: season_autumn AND element_wood]` `[role: 主干]` 秋月之木，气渐凄凉，形渐凋败。 → 《穷通宝鉴·论木》#2.4
  - `[ns_qttbj_059]` `[trigger: 初秋木]` `[factor_trigger: month_shen AND element_wood AND element_water AND element_earth]` `[role: 条件分支]` 初秋之时，火气未除，尤喜水土以相滋。 → 《穷通宝鉴·论木》#2.4
  - `[ns_qttbj_060]` `[trigger: 中秋木]` `[factor_trigger: month_you AND element_wood AND tiangan_geng]` `[role: 条件分支]` 中秋之令，果以成实，欲得刚金而修削。 → 《穷通宝鉴·论木》#2.4
  - `[ns_qttbj_061]` `[trigger: 晚秋木忌水]` `[factor_trigger: month_xu AND element_wood AND water_excessive]` `[role: 例外处理]` 霜降后不宜水盛，水盛则木漂。 → 《穷通宝鉴·论木》#2.4
  - `[ns_qttbj_062]` `[trigger: 晚秋木喜火]` `[factor_trigger: month_xu AND element_wood AND element_fire]` `[role: 主干依赖]` 寒露节又喜火炎，火炎则木实。 → 《穷通宝鉴·论木》#2.4
  - `[ns_qttbj_063]` `[trigger: 秋木财多]` `[factor_trigger: season_autumn AND element_wood AND earth_excessive]` `[role: 总结]` 土厚无自任之能，身弱不能胜财。 → 《穷通宝鉴·论木》#2.4"""
    normalized_text_zh: str = """"""
    subject: str = "4. 秋季之木"
    factor_refs: list = ['vitality_fading', 'tiangan_geng', 'wood_drifting', 'cannot_handle_wealth']
    
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
        l1_anchor="qtbj_v1.0.0_4__秋季之木_001_L1",
    )
    version: str = "1.0.0"
