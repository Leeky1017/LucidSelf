"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228736
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
    semantic_id="smth_v1.0.0_不畏鬼不嫌鬼_之丑之土戊戌之木等化鬼格局总论_001",
    book_id="sanming",
    engine_id="bazi"
)
class 不畏鬼不嫌鬼之丑之土戊戌之木等化鬼格局总论(SemanticEntry):
    """
    - **原文（source_text）**：
  戊子水中之火，神龙有之，即六气之君火也。得之者，自神而明，沉几先物，二气兼得，尤妙绝。其余诸气，准此详之。之丑之土不嫌于木，戊戌之木，不怕于金。何以辨...
    """
    
    original_text: str = """- **原文（source_text）**：
  戊子水中之火，神龙有之，即六气之君火也。得之者，自神而明，沉几先物，二气兼得，尤妙绝。其余诸气，准此详之。之丑之土不嫌于木，戊戌之木，不怕于金。何以辨之？丑中金库，木不为鬼；戊中有火，金反受其殃。若戊戌之木，二土在上，一木在下，埋在二土之内，尚未萌芽，不见其形，是土盛木弱，余皆仿此。庚寅木、丁巳土，不嫌金木之鬼。金至寅宫，虽为鬼，而金绝在寅，故不为鬼。木至巳宫，而巳有生金克木，故不为鬼。若庚寅木逢壬申金，相冲受克，余皆仿此。庚午之土，乘南方旺火，以养其形。戊申之土自生，庚子之土自盈，不忌木鬼。盖木至午死，申绝子败，又自强之土何伤？余皆仿此。壬申、癸酉、庚戌、辛亥四金气壮，不嫌于鬼。戊子之火，不畏其鬼。

- **分字分词释义**：
  - **君火**：六气之一，主导之火。
  - **沉几先物**：沉静机心而先知万物。
  - **二气兼得**：两种气机同时具备。
  - **不嫌鬼/不畏鬼**：不害怕平常所说的"鬼"（克我之神）。
  - **金库**：金的库藏之地（丑）。
  - **木不为鬼**：木虽克土，但因有金库反制，不成鬼害。
  - **金反受其殃**：金反而受到火的伤害。
  - **土盛木弱**：土多木少，木力微弱。
  - **气壮**：气势旺盛强健。

- **规范化释义（primary_lang_explained）**：
  戊子水中之火，是六气中的君火，只有神龙格局才有，得到它的人，自然神明，沉静机心而先知万物，两种气机兼得，极为玄妙。其余各种气机，都可以依此类推。之丑之土不怕木鬼，戊戌之木不怕金鬼。为什么？因为丑中藏金库，木来克土却因金库存在而不成鬼；戊中有火，金来反而受火伤害。戊戌之木，上有二土，下有一木，木埋在二土之内，尚未萌芽，不见其形，是土盛木弱，其余情况都可以这样类推。庚寅木、丁巳土，也不怕金木之鬼。金到寅宫虽为鬼，但金在寅位已绝，所以不成鬼；木到巳宫，巳中有生金克木之气，所以不成鬼。但若庚寅木遇到壬申金，则相冲受克，其余情况类推。庚午之土乘南方旺火以养其形，戊申之土自生，庚子之土自盈，都不忌木鬼，因为木到午死、到申绝、到子败，而这些土本身又自强，木怎能伤害？其余类推。壬申、癸酉、庚戌、辛亥四金气势旺盛，不怕鬼。戊子之火，也不畏其鬼。

- **完整对等诠释（secondary_lang_full）**：
  Wuzi Fire-within-Water is the Sovereign Fire among the Six Qi, possessed only by divine-dragon configurations. Those who obtain it are naturally spiritual and enlightened, quiet in intent yet preceding things, endowed with two streams of qi, extremely marvelous. Chou-earth does not mind Wood-ghosts; Wuxu Wood does not fear Metal-ghosts. Because within Chou is Metal-repository; when Wood comes it controls Earth yet does not become ghost. Within Wu is Fire; when Metal comes it instead receives Fire's harm. For Wuxu Wood, two Earths above and one Wood below, the Wood is buried within two Earths—Earth abundant and Wood weak; the rest follow by analogy.

- **核心要点**：
  - 戊子水中火为君火，神龙有之，沉几先物、二气兼得
  - 提出一系列"名有鬼而实不为鬼"的特例
  - 关键在于：藏干库气改变表面克制关系、鬼方之气已绝已败、本体之气自强
  - 具体例证：之丑土（金库化木鬼）、戊戌木（土盛木弱）、庚寅木丁巳土（鬼气已绝）、庚午戊申庚子土（自强不畏木鬼）、四金气壮不嫌鬼

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_249]` `[trigger: 不畏鬼不嫌鬼格局]` `[factor_trigger: no_fear_ghost_structural_conditions AND strong_qi_not_fearing_ghost AND sovereign_fire_quiet_preceding]` `[role: 主干]` 戊子水中之火，神龙有之，即六气之君火也。得之者，自神而明，沉几先物，二气兼得，尤妙绝。之丑之土不嫌于木，戊戌之木，不怕于金。丑中金库，木不为鬼；戊中有火，金反受其殃。庚寅木、丁巳土，不嫌金木之鬼。庚午之土，乘南方旺火，以养其形。戊申之土自生，庚子之土自盈，不忌木鬼。壬申、癸酉、庚戌、辛亥四金气壮，不嫌于鬼。戊子之火，不畏其鬼。 → 《三命通会》卷一#不畏鬼不嫌鬼格局

- **详细解说**：
  本段是对"鬼"与"鬼神格局"的系统修正。命理中常以"克我者为鬼"，但在具体干支与藏干结构中，往往存在"名为鬼而实不为鬼"的情况。例如：丑中金库使木不为鬼、戊中有火使金反受其殃；金到寅宫名为鬼而气已绝、木到巳宫反被生金克制；或土气自强而木在死绝败地，木鬼难以为害。又列出壬申、癸酉、庚戌、辛亥四金与戊子之火，皆因气壮不畏鬼。实务判断时，应综合纳音、藏干、长生死绝与强弱，而不能只按"某支为鬼"一条规则机械下断。同时强调戊子水中火为君火，神龙格局，具有特殊的精神灵动特质。

- **校勘与字词辨析（双语）**：
  - **中文**："鬼"在命理中指"克我之神"或不利之神，并非迷信鬼怪；"不嫌鬼""不畏鬼"指格局能化解。"君火"为六气之一，主导性之火。
  - **English**: "Ghost" here means harmful controlling star, not literal spirits. "Not minding ghosts" or "not fearing ghosts" means the configuration neutralizes such harm. "Sovereign Fire" is one of the Six Qi, the governing fire."""
    normalized_text_zh: str = """"""
    subject: str = "不畏鬼不嫌鬼：之丑之土戊戌之木等化鬼格局总论"
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
        l1_anchor="smth_v1.0.0_不畏鬼不嫌鬼_之丑之土戊戌之木等化鬼格局总论_001_L1",
    )
    version: str = "1.0.0"
