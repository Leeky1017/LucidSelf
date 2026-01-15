"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228710
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
    semantic_id="smth_v1.0.0_壬戌癸亥大海水_气归休绝伏逆需济_001",
    book_id="sanming",
    engine_id="bazi"
)
class 壬戌癸亥大海水气归休绝伏逆需济(SemanticEntry):
    """
    - **原文（source_text）**：
  壬戌偏库之水，癸亥临官之水，名曰大海水。盖支干纳音皆水，忌见众水，虽壬辰水库，亦不能当，不忌他土，死绝则吉，生旺则泛滥而无所归也。玉霄宝鉴云：亥子水之...
    """
    
    original_text: str = """- **原文（source_text）**：
  壬戌偏库之水，癸亥临官之水，名曰大海水。盖支干纳音皆水，忌见众水，虽壬辰水库，亦不能当，不忌他土，死绝则吉，生旺则泛滥而无所归也。玉霄宝鉴云：亥子水之正位，壬戌气伏而不顺，惟以火土损益之，乃成大器。癸亥具纯阳之数，内体至仁，禀之者，天资夷旷，志气浩然，发为功业利泽。日时带煞，则凶狡之流。

- **分字分词释义**：
  - **偏库之水**：偏库的水。
  - **临官之水**：临官位的水。
  - **支干纳音皆水**：地支天干纳音都是水。
  - **不能当**：不能承受。
  - **泛滥而无所归**：泛滥而没有归宿。
  - **气伏而不顺**：气伏藏而不顺畅。
  - **损益之**：损减增益调和。
  - **纯阳之数**：纯阳的数理。
  - **内体至仁**：内在本体极其仁德。
  - **天资夷旷**：天资平和开阔。
  - **志气浩然**：志气浩大。
  - **功业利泽**：功业和利益泽被。
  - **凶狡之流**：凶恶狡猾之辈。

- **规范化释义（primary_lang_explained）**：
  壬戌是偏库的水，癸亥是临官的水，名叫大海水。因为地支天干纳音都是水，忌讳见到众多水，即使壬辰水库，也不能承受，不忌讳其他土，死绝则吉利，生旺则泛滥而没有归宿。玉霄宝鉴说：亥子是水的正位，壬戌气伏藏而不顺畅，只有用火土损减增益调和，才能成就大器。癸亥具备纯阳的数理，内在本体极其仁德，禀受它的人，天资平和开阔，志气浩大，表现为功业和利益泽被。如果日时带煞，则是凶恶狡猾之辈。

- **完整对等诠释（secondary_lang_full）**：
  Renxu is partial-storage water, Guihai is official-position water, named Great-Sea Water. Since stems-branches-nayin all water, avoids seeing many Waters. Even Renchen water-repository cannot withstand. Not avoiding other Earths. Dead-extinct then auspicious, born-prosperous then flooding without-destination. Jade-Sky Treasure-Mirror says: Hai-Zi water's proper-position, Renxu energy concealed not-flowing, only using Fire-Earth diminishing-augmenting, then achieves great-vessel. Guihai possesses pure-yang number, internally embodies ultimate-benevolence. Those receiving it, natural-talent peaceful-expansive, aspiration-spirit vast. Manifesting as achievement-benefit spreading. Day-time carrying sha, then vicious-cunning class.

- **核心要点**：
  - 壬戌癸亥为大海水，偏库临官
  - 支干纳音皆水、忌见众水
  - 不忌他土、死绝吉生旺凶（反常）
  - 壬戌气伏不顺、需火土损益
  - 癸亥纯阳至仁、天资夷旷志气浩然
  - 功业利泽或带煞凶狡

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_246]` `[trigger: 壬戌癸亥水性质]` `[factor_trigger: renxu_guihai_great_sea_water AND dead_extinct_auspicious_born_prosperous_inauspicious AND fire_earth_aid_achievement_benefit_spreading]` `[role: 主干]` 壬戌偏库之水，癸亥临官之水，名曰大海水。盖支干纳音皆水，忌见众水，虽壬辰水库，亦不能当，不忌他土，死绝则吉，生旺则泛滥而无所归也。玉霄宝鉴云：亥子水之正位，壬戌气伏而不顺，惟以火土损益之，乃成大器。癸亥具纯阳之数，内体至仁，禀之者，天资夷旷，志气浩然，发为功业利泽。日时带煞，则凶狡之流。 → 《三命通会》卷一#壬戌癸亥水性质

- **详细解说**：
  此条详论壬戌、癸亥（大海水）的性质与格局。二者支干纳音皆水（壬癸为水、戌亥近水、纳音水），忌众水（水太多泛滥），连壬辰水库也不能当，不忌他土。反常地死绝吉、生旺凶（水太多无归）。玉霄宝鉴指出壬戌气伏不顺需火土损益成器，癸亥纯阳至仁天资夷旷志气浩然，功业利泽但带煞凶狡。这是论述海水的汇聚特性与反常格局。

- **校勘与字词辨析（双语）**：
  - **中文**："大海水"为六十甲子纳音之最后，象征水的归宿。"气伏不顺"，壬戌水气伏藏受戌土影响。"纯阳之数"，癸亥为六十甲子之末，阴极生阳。"夷旷"指平和开阔。
  - **English**: "Great-Sea Water" is last of sixty Jiazi Nayin, symbolizing water's destination. "Energy concealed not-flowing" means Renxu water energy concealed affected by Xu earth. "Pure-yang number" means Guihai is end of sixty Jiazi, extreme yin generating yang. "Peaceful-expansive" means calm and broad."""
    normalized_text_zh: str = """"""
    subject: str = "壬戌癸亥大海水：气归休绝伏逆需济"
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
        l1_anchor="smth_v1.0.0_壬戌癸亥大海水_气归休绝伏逆需济_001_L1",
    )
    version: str = "1.0.0"
