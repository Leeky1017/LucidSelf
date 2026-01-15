"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.850545
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
    semantic_id="mlxj_v1.0.0_条目二_辨二气之乘_001",
    book_id="mlxj",
    engine_id="dream"
)
class 条目二辨二气之乘(SemanticEntry):
    """
    ### 原文（source_text）

辨二气之乘。如制、伐、荫、义、专及王相死休囚也。干克支曰制，支克干曰伐，干生支曰荫，支生干曰义，干支比和曰专。王所胜者死，相所胜者囚。故春则木王，火相土死，水...
    """
    
    original_text: str = """### 原文（source_text）

辨二气之乘。如制、伐、荫、义、专及王相死休囚也。干克支曰制，支克干曰伐，干生支曰荫，支生干曰义，干支比和曰专。王所胜者死，相所胜者囚。故春则木王，火相土死，水休金囚；夏则火王，土相金死，木休水囚。秋则金王，水相木死，土休火囚；冬则水王，木相火死，金休土囚也。王者，旺也。占梦者，必究干支生克之情，五行胜败之实，而后可迎其气以详之。

### 分字分词释义

- **二气**：阴阳二气/天干地支所代表的气/五行生克之气
- **乘**：驾驭、运行/阴阳消长的态势/五行生克的动态关系
- **制**：天干克地支/主动制约/上克下
- **伐**：地支克天干/反克/下伐上
- **荫**：天干生地支/庇荫/上生下
- **义**：地支生天干/义助/下生上
- **专**：干支比和/专一/阴阳同气
- **王（旺）**：当令得时/气势最盛/主导力量
- **相**：次旺/得生气/辅助力量
- **死**：被克制/无生气/衰败状态
- **休**：休息/生出后的疲态/退休状态
- **囚**：受困/被克且无助/最弱状态

### 规范化释义（primary_lang_explained）

占梦的第二条核心原则是「辨二气之乘」——必须辨明阴阳二气运行的生克态势。具体包括制、伐、荫、义、专五种干支关系，以及旺、相、死、休、囚五种五行状态。

天干克地支叫做「制」，是上对下的主动制约；地支克天干叫做「伐」，是下对上的反克。天干生地支叫做「荫」，是上对下的庇护滋养；地支生天干叫做「义」，是下对上的义助扶持。天干地支五行相同叫做「专」，是阴阳同气的专一状态。

在五行旺衰方面：旺者所克者为死，相者所克者为囚。因此：春季木旺、火相、土死、水休、金囚；夏季火旺、土相、金死、木休、水囚；秋季金旺、水相、木死、土休、火囚；冬季水旺、木相、火死、金休、土囚。旺就是当令得时、气势最盛之意。

占梦者必须深入研究干支生克的内在关系，明辨五行旺衰的真实状态，然后才能顺应气机、详细推断梦境的吉凶。

### 完整对等诠释（secondary_lang_full）

The second principle of dream interpretation is "Discerning the Movement of the Two Energies" — one must clearly distinguish the generating and controlling dynamics of Yin-Yang energies. This includes five types of Stem-Branch relationships (Control, Attack, Shelter, Righteousness, Unity) and five states of the Five Elements (Prosperous, Prime, Dead, Resting, Imprisoned).

When the Heavenly Stem controls the Earthly Branch, it is called "Control" — the superior actively restraining the inferior. When the Earthly Branch controls the Heavenly Stem, it is called "Attack" — the inferior counter-attacking the superior. When the Heavenly Stem generates the Earthly Branch, it is called "Shelter" — the superior nurturing the inferior. When the Earthly Branch generates the Heavenly Stem, it is called "Righteousness" — the inferior righteously supporting the superior. When Stem and Branch share the same element, it is called "Unity" — unified Yin-Yang energy.

Regarding the Five Elements' strength cycles: what the Prosperous element controls becomes Dead; what the Prime element controls becomes Imprisoned. Therefore: in Spring, Wood is Prosperous, Fire is Prime, Earth is Dead, Water is Resting, Metal is Imprisoned. In Summer, Fire is Prosperous, Earth is Prime, Metal is Dead, Wood is Resting, Water is Imprisoned. In Autumn, Metal is Prosperous, Water is Prime, Wood is Dead, Earth is Resting, Fire is Imprisoned. In Winter, Water is Prosperous, Wood is Prime, Fire is Dead, Metal is Resting, Earth is Imprisoned.

Dream interpreters must thoroughly investigate the internal dynamics of Stem-Branch generating and controlling relationships, clearly understand the true states of Five Elements' prosperity and decline, and only then can they follow the energy patterns to interpret dreams in detail.

### 核心要点

- 辨二气之乘是占梦第二核心原则
- 干支五种关系：制（干克支）、伐（支克干）、荫（干生支）、义（支生干）、专（干支比和）
- 五行五种状态：旺（当令）、相（次旺）、死（被克）、休（生出后疲）、囚（受困最弱）
- 春木旺火相土死水休金囚
- 夏火旺土相金死木休水囚
- 秋金旺水相木死土休火囚
- 冬水旺木相火死金休土囚
- 必须究干支生克之情，辨五行胜败之实

### 详细解说

此条建立了占梦的「五行生克」分析框架，将干支关系与五行旺衰两个维度结合起来。干支五种关系（制伐荫义专）反映了八字命理中天干地支的动态交互；五行五种状态（旺相死休囚）则反映了季节对五行强弱的影响。

占梦者需要将梦象中的五行属性与梦发生时的季节旺衰对应，判断梦象所代表的能量处于何种状态。例如梦见火相关意象，若在夏季则火旺，梦应更显著；若在冬季则火死，梦应受克制。

此原则与前一条「观天地之会」相辅相成：前者确定时间节点，此条则分析该时间节点上各种能量的强弱态势。

### 叙事素材（narrative_snippets）

- `[ns_mlxj_006]` `[trigger: 干支生克判断]` `[factor_trigger: dream_ganzhi_shengke AND dream_wuxing_wang AND dream_ganzhi_renlun AND element_strength AND solar_term]` `[role: 主干]` 占梦者，必究干支生克之情，五行胜败之实，而后可迎其气以详之。 → 《梦林玄解·卷之首》#辨二气之乘
- `[ns_mlxj_007]` `[trigger: 春季五行]` `[factor_trigger: dream_wuxing_seasonal]` `[role: 条件分支]` 春则木王，火相土死，水休金囚。 → 《梦林玄解·卷之首》#辨二气之乘
- `[ns_mlxj_008]` `[trigger: 夏季五行]` `[factor_trigger: dream_wuxing_seasonal]` `[role: 条件分支]` 夏则火王，土相金死，木休水囚。 → 《梦林玄解·卷之首》#辨二气之乘
- `[ns_mlxj_009]` `[trigger: 秋季五行]` `[factor_trigger: dream_wuxing_seasonal]` `[role: 条件分支]` 秋则金王，水相木死，土休火囚。 → 《梦林玄解·卷之首》#辨二气之乘
- `[ns_mlxj_010]` `[trigger: 冬季五行]` `[factor_trigger: dream_wuxing_seasonal]` `[role: 条件分支]` 冬则水王，木相火死，金休土囚。 → 《梦林玄解·卷之首》#辨二气之乘"""
    normalized_text_zh: str = """"""
    subject: str = "条目二：辨二气之乘"
    factor_refs: list = ['dream_ganzhi_shengke', 'ganzhi_zhi', 'ganzhi_fa', 'ganzhi_yin', 'ganzhi_yi', 'ganzhi_zhuan', 'wuxing_five_states']
    
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
        l1_anchor="mlxj_v1.0.0_条目二_辨二气之乘_001_L1",
    )
    version: str = "1.0.0"
