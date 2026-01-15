"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.157729
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
    semantic_id="smth_v1.0.0_六戊日丙辰时断_食神入库与比肩同宫_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六戊日丙辰时断食神入库与比肩同宫(SemanticEntry):
    """
    - 原文（source_text）：

  六戊日丙辰时断。

  六戊日生时丙辰，食神入库比肩同；若逢戌字冲开库，定主文章福禄隆。戊日丙辰时，食神入库，丙火食神入辰库，戊土比肩同在辰，若生戌月，辰戌...
    """
    
    original_text: str = """- 原文（source_text）：

  六戊日丙辰时断。

  六戊日生时丙辰，食神入库比肩同；若逢戌字冲开库，定主文章福禄隆。戊日丙辰时，食神入库，丙火食神入辰库，戊土比肩同在辰，若生戌月，辰戌相冲，冲开食神库，主文章秀发。辰戌丑未月，杂气食神，大贵。

  戊子日丙辰时，子辰半合，春印旺，贵。夏身旺，吉。秋财旺，富。

  戊寅日丙辰时，春印旺，贵。夏身旺，吉。戌月冲库，大贵。

  戊辰日丙辰时，两辰自刑，伤妻害子。戌月冲库，大贵。

  戊午日丙辰时，午辰暗合，春印旺，贵。夏身旺，吉。

  戊申日丙辰时，申子辰月，合财，大富。寅午戌月，身旺，大贵。

  戊戌日丙辰时，辰戌相冲，冲开食神库，大贵。辰戌丑未年月，大贵。

  戊日丙辰时上逢，食神入库比肩同；运行戌字冲开库，定主文章福禄隆。戊日丙辰时准，食神入库相逢。若还冲动发荣昌，不冲终为平常。

- 分字分词释义：

  - **食神入库**：丙火食神入辰库，食神有储藏。
  - **比肩同宫**：戊土比肩与食神同在辰位。
  - **冲开食神库**：戌冲辰，冲开食神库，食神得用。

- 规范化释义（primary_lang_explained）：

  本节讲「六戊日，丙辰时」：

  - 丙火食神入辰库，戊土比肩同在辰位；若生戌月，辰戌相冲，冲开食神库，主文章秀发；
  - 不冲则食神储而不发，平常衣禄。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Wu Days with Bing-Chen Hour":

  - Bing Fire Food God enters Chen treasury; Wu Earth Shoulder also at Chen position.
  - If born in Xu month, Chen-Xu clash opens food-god treasury—indicating literary elegance.
  - Without clash, food-god remains stored but not released—ordinary livelihood.

- 核心要点：

  - 本格以「食神入库」为核心，需冲开方能发用。
  - 比肩同宫帮身，增强日主力量。
  - 冲开则文章秀发，不冲则平常。

- 详细解说：

  1. **食神入库的特点**  
     - 辰为水库（也藏火气），丙火食神入库有储藏；  
     - 需要戌冲或行运冲开，方能发挥。

  2. **比肩同宫的优势**  
     - 戊土比肩同在辰位，帮身有力；  
     - 增强日主力量，利于用食神。

- 校勘与字词辨析：

  - 「福禄隆」形容福禄兴隆。
  - 「发荣昌」形容发达兴旺。
  - **English**：
    - Describes prospering and flourishing.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_08_209]` `[trigger: 食神入库]` `[factor_trigger: shishen_ruku AND bijian_tong]` `[role: 主干]` 六戊日生时丙辰，食神入库比肩同。 → 《三命通会》卷八#六戊日丙辰时
  - `[ns_smth_08_210]` `[trigger: 戌字冲库]` `[factor_trigger: xuzi_chongku AND wenzhang_fulu]` `[role: 主干依赖]` 若逢戌字冲开库，定主文章福禄隆。 → 《三命通会》卷八#六戊日丙辰时
  - `[ns_smth_08_211]` `[trigger: 杂气食神]` `[factor_trigger: zaqi_shishen AND da_gui]` `[role: 条件分支]` 辰戌丑未月，杂气食神，大贵。 → 《三命通会》卷八#六戊日丙辰时
  - `[ns_smth_08_212]` `[trigger: 冲动荣昌]` `[factor_trigger: chongdong_rongchang AND bu_chong_pingchang]` `[role: 总结]` 若还冲动发荣昌，不冲终为平常。 → 《三命通会》卷八#六戊日丙辰时"""
    normalized_text_zh: str = """"""
    subject: str = "六戊日丙辰时断：食神入库与比肩同宫"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'day_master_wu', 'bazi_semantic', 'bazi_state_shishen_4', 'bazi_semantic', 'bazi_relation_bijian', 'bazi_semantic', 'bazi_state_shishen_5', 'bazi_semantic', 'hour_branch_chen', 'bazi_semantic', 'bazi_condition_factor_79', 'bazi_semantic', 'source_ref', 'rel_smth_08_157', 'shishen_ruku', 'rel_smth_08_158', 'bijian_tonggong', 'rel_smth_08_159', 'youchong_youfa', 'evi_smth_08_157', 'shishen_ruku', 'rule_shishenruku', 'evi_smth_08_158', 'bijian_tonggong', 'rule_tonggong2', 'evi_smth_08_159', 'chongkai_shishenku', 'rule_chongkai6', 'map_smth_08_105', 'map_smth_08_106']
    
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
        l1_anchor="smth_v1.0.0_六戊日丙辰时断_食神入库与比肩同宫_001_L1",
    )
    version: str = "1.0.0"
