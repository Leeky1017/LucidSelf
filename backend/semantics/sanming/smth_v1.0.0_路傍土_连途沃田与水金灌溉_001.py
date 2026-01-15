"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228885
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
    semantic_id="smth_v1.0.0_路傍土_连途沃田与水金灌溉_001",
    book_id="sanming",
    engine_id="bazi"
)
class 路傍土连途沃田与水金灌溉(SemanticEntry):
    """
    - **原文（source_text）**：
  庚午、辛未路傍土。路傍土者，大地连途，平田万顷，禾稼赖以资生，草木由之畅茂。此乃火煖土温，长养万物之土也，故须假水为先，乃灌漑滋润之论。次第尤宜水化为...
    """
    
    original_text: str = """- **原文（source_text）**：
  庚午、辛未路傍土。路傍土者，大地连途，平田万顷，禾稼赖以资生，草木由之畅茂。此乃火煖土温，长养万物之土也，故须假水为先，乃灌漑滋润之论。次第尤宜水化为妙，更得金来相助，则禾稼成实。如庚午见甲申，辛未见乙酉，为禄，若无冲破，主早贵。天上水雨露相滋，庚午喜见丁未，辛未喜见丙午，为官贵禄合之妙。涧下庚午见丁丑，贵禄交驰；辛未见丙子，化水逄生。大溪乙卯，为东震发生之义，单见亦吉。长流大海二水，以其不能浇灌此土，故最忌之，主凶夭。火逢霹雳，庚午见巳丹，贵禄交穿；辛未见戊子，印贵朝阳，皆吉。上火就位相生，太燥则土反不能生物，有水润之始得。若独见主夭，炉中火亦燥，亦主妨寿。灯头有屋土，方应造化名超凡入圣，不然亦凶。见木可以发生，然有贵人禄马则吉，刑煞冲破则凶。只有庚寅木此土逄之，大好，大林不能胜载。如逄土位，见丙辰、丙戊、辛丑、辛未皆吉。若庚午见辛未，辛未见庚午，为二仪贵偶，无有不贵。钗钏砂中二金，可以滋助清水，金水并见，大吉。若命中已见水，无金运，遇此金亦福。乙丑海金可为山论，若得天河清水助之，庚人大好，妙选有金马嘶风格。以庚午、甲午生人，得辛巳时，有马化龙驹格。又以午生人见辰时，有哨风猛虎格。以庚辛生人，得辛巳、乙巳，俱以贵论，而水火土金似不相拘。

- **规范化释义（primary_lang_explained）**：
  庚午、辛未为路傍土。路傍土如连绵大道两旁的土田，平田万顷，禾稼与草木皆赖之而生，是火暖土温、长养万物之土。此土首先需要水来灌溉：适量清水使土壤湿润而不板结，其后再得金来相助，则可使禾稼结实。命局中庚午见甲申、辛未见乙酉，为得禄之象，若无冲破，多主早贵。天河水如雨露相滋，庚午喜见丁未、辛未喜见丙午，构成官贵禄合之妙；涧下水与大溪水在特定配合下亦主贵吉。长流水、大海水因流势过大、难以灌溉路傍田土，反主凶夭。火方面，霹雳火若与路傍土配庚午见巳、辛未见戊子，可成贵禄交映之格；但上火（天上火）与炉中火若无水滋润，则路傍土过燥，反不能生物。灯头火若有屋上土为护，方成"火土入堂"之贵象，否则易成焚灼之患。木可以在路傍土上发生、成林，但需有贵人、禄马等吉神相扶，遇刑冲则为祸。特别是庚寅木，此土所逢极佳，而大林木过重时反有"不胜其载"之忧。金以钗钏金与砂金最宜，与清水并见则大吉；乙丑海中金若为山，再协以天河清水，则对庚午格局尤其有利，妙选称"金马嘶风格"、"马化龙驹格"、"哨风猛虎格"等，皆属高贵之象。

- **完整对等诠释（secondary_lang_full）**：
  Gengwu and Xinwei belong to Roadside Earth. Roadside Earth is like the soil flanking great roadways—vast level fields on which grains rely for growth and through which grasses prosper. It is warm Earth heated by Fire, nurturing all things. This Earth first requires Water for irrigation: appropriate, clean Water moistens without hardening; afterward, when Metal assists, crops ripen fully. In natal charts, Gengwu meeting Jiashen or Xinwei meeting Yiyou signifies stipend and, if unbroken by clashes, early nobility. Heavenly-River Water, as rain and dew, is ideal; Gengwu gladly meets Dingwei, Xinwei meets Bingwu, forming marvelous combinations of office and stipend. Stream-below and Great-Stream Waters in certain arrangements also bring honor. Long-Flowing and Ocean Waters, however, are too forceful to irrigate such soil and tend toward disaster and short life. Concerning Fire, Thunder-Bolt Fire paired with Roadside Earth—Gengwu meeting Sidan or Xinwei meeting Wuzi—can yield patterns where nobility and stipend intersect; yet Sky-Above and Furnace Fires without Water make the Earth overly dry and unable to give life. Covered-Lamp Fire only becomes auspicious when sheltered by Roof-Top Earth, forming "Fire-and-Earth Entering-the-Hall"; otherwise it burns destructively. Wood can sprout and grow along Roadside Earth, but only with nobleman and stipend-horse support; under punishments and clashes it becomes harmful. Gengyin Wood suits this Earth extremely well, while excessive Great-Forest Wood may be too heavy to bear. Among Metals, Hairpin-Gold and Sand-Center Metal best enhance clear Water; when Metal and Water appear together, great fortune follows. Sea-Center Metal at Yichou can act as a mountain; assisted by Heavenly-River Water, it especially benefits Gengwu, inspiring patterns like "Metal Horse Neighing in the Wind", "Horse Transforming into Dragon-Colt", and "Whistling-Wind Fierce-Tiger"—all noble and dynamic configurations. In these combinations, Water, Fire, Earth, and Metal interplay flexibly rather than being rigidly constrained.

- **核心要点**：
  - 路傍土为火暖土温之田土，重在灌溉与载道
  - 喜天河、涧下、大溪等可灌之水，忌长流水与大海水直冲
  - 火以霹雳及适度天上火为用，无水则过燥伤生
  - 钗钏金与砂金配清水最吉，可成金马嘶风等贵格

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_117]` `[trigger: 路傍土]` `[factor_trigger: gengwu_xinwei AND lupang_tu]` `[role: 主干]` 路傍土者，大地连途，平田万顷，禾稼赖以资生，草木由之畅茂。此乃火煖土温，长养万物之土也，故须假水为先，乃灌漑滋润之论。 → 《三命通会》卷一#路傍土

- **详细解说**：
  路傍土比砂中土更实、更有承载力，但仍需水与金的精细配合：水决定是否能"灌溉万顷平田"，金决定是否能"催成禾稼之实"。原文通过不同水火金组合，勾勒出从"路旁干土"到"良田通衢"的多条路径：清水在上、金在下，则为润泽之田；长流水与大海水则像洪水冲路，非但不能灌溉，反有冲毁路堤之忧。火与水则共同定义路傍土的气候环境：天河雨露与霹雳雷火，可理解为适度雨雷，使土暖而不焦；炉火与无水之天火，则让土裂而不生。命理实务中，庚午辛未路傍土若能见路旁土、屋上土、城头土等形成完整建筑—道路结构，再得清水与清金调和，则人多主早贵、行走四方；反之，多火少水、多土相刑，则易成劳碌奔波而不得其位之象。

- **校勘与字词辨析（双语）**：
  - **中文**："金马嘶风格"、"马化龙驹格"、"哨风猛虎格"皆出妙选，用以形容路傍土配金火水所成之贵格。
  - **English**: Patterns like "Metal Horse Neighing in the Wind", "Horse Transforming into Dragon-Colt", and "Whistling-Wind Fierce-Tiger" from Wonderful-Selection denote noble configurations where Roadside Earth interacts with Metal, Fire, and Water."""
    normalized_text_zh: str = """"""
    subject: str = "路傍土：连途沃田与水金灌溉"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate']
    
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
        l1_anchor="smth_v1.0.0_路傍土_连途沃田与水金灌溉_001_L1",
    )
    version: str = "1.0.0"
