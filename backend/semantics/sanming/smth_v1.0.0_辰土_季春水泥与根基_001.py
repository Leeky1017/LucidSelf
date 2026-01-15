"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.042465
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
    semantic_id="smth_v1.0.0_辰土_季春水泥与根基_001",
    book_id="sanming",
    engine_id="bazi"
)
class 辰土季春水泥与根基(SemanticEntry):
    """
    - **原文（source_text）**：
  辰建季春，为水泥之湿，而万物之根皆赖此培养。甲至此虽衰，而有乙之余气；壬至此虽墓，而有癸之还魂。见戌为钥，能开库中之物，若三戍重冲破门，非吉。日时多见...
    """
    
    original_text: str = """- **原文（source_text）**：
  辰建季春，为水泥之湿，而万物之根皆赖此培养。甲至此虽衰，而有乙之余气；壬至此虽墓，而有癸之还魂。见戌为钥，能开库中之物，若三戍重冲破门，非吉。日时多见水木，其运更向西北，则辰土不能存矣。

- **分字分词释义**：
  - **水泥之湿**：水与土相杂，如泥田之象，用以培根。
  - **甲衰乙余、壬墓癸还魂**：指木水主气虽衰，却有余气与复苏之机。
  - **戌为钥**：戌如钥匙，可开辰库；重冲则如破门。

- **规范化释义（primary_lang_explained）**：
  辰为季春之土，湿润如水泥，万物之根须凭此土来培养。甲木至此虽不如春初之旺，却有乙木余气可接续；壬水至此虽入墓，但癸水之气犹在，如「还魂」。见戌如钥匙开库，可取用库中之物；若戌多而重冲，则等于把库门打破，为凶象。若日时水木太多，又行西北金水之运，则辰土之身恐难久存。

- **完整对等诠释（secondary_lang_full）**：
  Chen belongs to late spring and is pictured as wet mud in which all roots are embedded. By this time Jia Wood has passed its peak yet is continued by the residual qi of Yi; Ren Water has entered the tomb here, but Gui still hovers like a returning spirit, so that both Wood and Water can be stored and buffered. As a vault earth, Chen interacts with Xu like a key: moderate Xu can open the storehouse and release what has accumulated, whereas repeated Xu attacks smash the door and undermine the very foundation. When day and hour contain abundant Water and Wood and the life further moves toward north‑west Metal‑Water regions, this soft earth is easily washed away entirely. In chart reading, Chen points to the quality of underlying foundations and reserves: is there enough but not too much moisture to nourish roots, and are the vault’s openings controlled, or are resources and stability being eroded by constant clashes and excessive flow?"""
    normalized_text_zh: str = """"""
    subject: str = "辰土：季春水泥与根基"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'dizhi_chen_presence', 'bazi_calculator', 'chen_xu_chong', 'bazi_calculator', 'shen_zi_chen_combo', 'bazi_calculator', 'seasonal_phase', 'bazi_calculator', 'earth_water_wood_balance', 'bazi_calculator', 'wu_ji_transition_window', 'bazi_calculator', 'dizhi_layer_loss_flag', 'bazi_calculator', 'source_ref', 'rel_smth_02_057', 'dizhi_chen_presence', 'rel_smth_02_058', 'chen_xu_chong', 'rel_smth_02_059', 'earth_water_wood_balance', 'evi_smth_02_053', 'chen_xu_chong', 'rule_chen_xu_key', 'evi_smth_02_054', 'chen_xu_chong', 'rule_chen_xu_break', 'evi_smth_02_055', 'earth_water_wood_balance', 'rule_chen_nurture_root', 'map_smth_02_039', 'map_smth_02_040']
    
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
        l1_anchor="smth_v1.0.0_辰土_季春水泥与根基_001_L1",
    )
    version: str = "1.0.0"
