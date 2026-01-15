"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.264231
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
    semantic_id="smth_v1.0.0_生旺死绝与神煞吉凶_001",
    book_id="sanming",
    engine_id="bazi"
)
class 生旺死绝与神煞吉凶(SemanticEntry):
    """
    - 原文（source_text）：
  凡命带上死绝、生旺、库墓等，不可就以所带言之，须看月令以辨清浊。清者，有制伏之谓，如水病，见土则浊，却非土隄防，则不能止息。既止息，则清之有渐也。浊者，无制伏...
    """
    
    original_text: str = """- 原文（source_text）：
  凡命带上死绝、生旺、库墓等，不可就以所带言之，须看月令以辨清浊。清者，有制伏之谓，如水病，见土则浊，却非土隄防，则不能止息。既止息，则清之有渐也。浊者，无制伏之谓。
  凡命最怕鬼克，而窠鬼最毒。如丙子水见庚子土，丁丑水见辛丑土之类，窠中就位相克，所以最毒。
  有墓中鬼，如壬辰水见丙辰土。有隔壁鬼，如庚子土见癸丑木。有空亡鬼，如甲戌见甲申、乙酉之类。
  若木命人得火月、金日时之类，有火克金，金不得伤木，是御鬼也，鬼不为害。

- 分字分词释义：
  - **清浊**：有制伏为清，无制伏为浊。
  - **窠鬼**：纳音相克，且干支同位（如丙子水克庚子土？原文“丙子水见庚子土”，纳音丙子水，庚子土，土克水。同柱或同支？此处指年柱丙子见月/日/时庚子，地支相同，纳音相克，如在窠穴中受克）。
  - **御鬼**：有食伤制煞，或印绶化煞。

- **规范化释义（primary_lang_explained）**：
  看命时，不能只看表面的生旺死绝，必须结合月令看气势清浊。有制伏、配合得宜为清；无制伏、混乱无序为浊。
  最怕纳音鬼克身。其中“窠鬼”最毒，即地支相同（如同在子宫），纳音相克。墓中鬼（同在墓库）、隔壁鬼（相邻）、空亡鬼（落空亡）也有害，但轻于窠鬼。
  若命中有鬼（煞），但有物制伏（如火克金鬼），叫“御鬼”，此时鬼不为害，反能成就在艰难中立身。

- 核心要点：
  - **纳音鬼**：纳音相克，尤忌窠鬼。
  - **制鬼**：御鬼（制煞）为贵。
  - **清浊**：看月令与制化。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_10_049]` `[trigger: 清浊辨析]` `[factor_trigger: qingzhuo_bianxi AND youzhifu_wuzhifu]` `[role: 主干]` 凡命带上死绝、生旺、库墓等，不可就以所带言之，须看月令以辨清浊。清者，有制伏之谓。 → 《三命通会》卷十#生旺死绝与神煞吉凶
  - `[ns_smth_10_050]` `[trigger: 窠鬼最毒]` `[factor_trigger: kegui_zuidu AND tongzhi_nayin_ke]` `[role: 主干依赖]` 凡命最怕鬼克，而窠鬼最毒。如丙子水见庚子土，窠中就位相克。 → 《三命通会》卷十#生旺死绝与神煞吉凶
  - `[ns_smth_10_051]` `[trigger: 墓中鬼]` `[factor_trigger: muzhong_gui AND renchen_bingchen]` `[role: 条件分支]` 有墓中鬼，如壬辰水见丙辰土。有隔壁鬼，如庚子土见癸丑木。 → 《三命通会》卷十#生旺死绝与神煞吉凶
  - `[ns_smth_10_052]` `[trigger: 御鬼不害]` `[factor_trigger: yugui_buhai AND huoke_jinxie]` `[role: 总结]` 若木命人得火月、金日时之类，有火克金，金不得伤木，是御鬼也，鬼不为害。 → 《三命通会》卷十#生旺死绝与神煞吉凶"""
    normalized_text_zh: str = """"""
    subject: str = "生旺死绝与神煞吉凶"
    factor_refs: list = ['new_candidate', 'new_candidate', 'engine_id', 'bazi_state_factor_232', 'bazi_semantic', 'bazi_state_factor_233', 'bazi_semantic', 'bazi_condition_factor_100', 'bazi_semantic', 'bazi_state_factor_234', 'bazi_semantic', 'bazi_condition_factor_101', 'bazi_semantic', 'source_ref', 'rel_smth_10_037', 'shengwang_sijue', 'rel_smth_10_038', 'kegui_zuidu', 'rel_smth_10_039', 'yugui', 'evi_smth_10_037', 'qingzhuo_bianxi', 'rule_qingzhuo_bianxi1', 'evi_smth_10_038', 'mozghong_gui', 'rule_kegui_zuidu1', 'evi_smth_10_039', 'yugui', 'rule_yugui1', 'map_smth_10_025', 'map_smth_10_026']
    
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
        l1_anchor="smth_v1.0.0_生旺死绝与神煞吉凶_001_L1",
    )
    version: str = "1.0.0"
