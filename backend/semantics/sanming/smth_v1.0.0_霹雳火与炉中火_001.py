"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228208
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
    semantic_id="smth_v1.0.0_霹雳火与炉中火_001",
    book_id="sanming",
    engine_id="bazi"
)
class 霹雳火与炉中火(SemanticEntry):
    """
    - **原文（source_text）**：
  戊子己丑，何以取象霹雳火？盖气在一阳，形居水位，水中之火，非神龙则无，故曰霹雳火。丙寅丁卯，气渐发辉，因薪而显，阴阳为冶，天地为炉，乃曰炉中火也。

...
    """
    
    original_text: str = """- **原文（source_text）**：
  戊子己丑，何以取象霹雳火？盖气在一阳，形居水位，水中之火，非神龙则无，故曰霹雳火。丙寅丁卯，气渐发辉，因薪而显，阴阳为冶，天地为炉，乃曰炉中火也。

- **分字分词释义**：
  - **霹雳火**：闪电雷火。
  - **气在一阳**：气在一阳初生之时。
  - **形居水位**：形体处在水的位置。
  - **水中之火**：水中的火。
  - **非神龙则无**：不是神龙就没有。
  - **气渐发辉**：气逐渐发出光辉。
  - **因薪而显**：因为柴薪而显现。
  - **阴阳为冶**：阴阳作为冶炼。
  - **天地为炉**：天地作为熔炉。

- **规范化释义（primary_lang_explained）**：
  戊子己丑，为什么取象为霹雳火？因为气在一阳初生之时，形体处在水的位置，水中的火，不是神龙就没有，所以叫霹雳火。丙寅丁卯，气逐渐发出光辉，因为柴薪而显现，阴阳作为冶炼，天地作为熔炉，就叫炉中火。

- **完整对等诠释（secondary_lang_full）**：
  Wuzi-Jichou, why symbolize Thunderbolt Fire? Because qi at one-yang emerging moment, form dwelling in Water position, fire within water—without divine dragon it cannot exist, thus called Thunderbolt Fire. Bingyin-Dingmao: qi gradually radiating brilliance, manifesting through firewood, yin-yang as smelting, Heaven-Earth as furnace, thus called Furnace Fire.

- **核心要点**：
  - 戊子己丑：霹雳火（气在一阳，水中之火）
  - 丙寅丁卯：炉中火（气渐发辉，天地为炉）
  - 霹雳火为火的神异初现
  - 炉中火为火的冶炼之功

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_185]` `[trigger: 霹雳火与炉中火]` `[factor_trigger: thunderbolt_fire AND furnace_fire AND nayin_fire_initial]` `[role: 主干]` 戊子己丑，何以取象霹雳火？盖气在一阳，形居水位，水中之火，非神龙则无，故曰霹雳火。丙寅丁卯，气渐发辉，因薪而显，阴阳为冶，天地为炉，乃曰炉中火也。 → 《三命通会》卷一#霹雳火与炉中火

- **详细解说**：
  此条开始解释火纳音。戊子己丑为"霹雳火"：子丑属冬季水旺之地，火在水中极其罕见，只有神龙吐火（闪电）才会有，这是火最神异的形态。丙寅丁卯为"炉中火"：寅卯属春季木旺之地（木生火），火因柴薪而旺，阴阳冶炼，天地如炉，这是火的冶炼功用。从霹雳火（神异）到炉中火（冶炼），体现了火从罕见到实用的转变。命理上，霹雳火命格神奇多变，炉中火命格炽热有力。

- **校勘与字词辨析（双语）**：
  - **中文**："霹雳火"指闪电雷火。"气在一阳"指冬至一阳初生。"神龙"指能驾驭水火的龙。"炉中火"指冶炼用火。"阴阳为冶"指阴阳之气如冶炼。
  - **English**: "Thunderbolt Fire" refers to lightning thunder fire. "Qi at one-yang" means winter solstice one yang emerging. "Divine dragon" means dragons commanding water and fire. "Furnace Fire" refers to smelting fire. "Yin-yang as smelting" means yin-yang qi like smelting process."""
    normalized_text_zh: str = """"""
    subject: str = "霹雳火与炉中火"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate']
    
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
        l1_anchor="smth_v1.0.0_霹雳火与炉中火_001_L1",
    )
    version: str = "1.0.0"
