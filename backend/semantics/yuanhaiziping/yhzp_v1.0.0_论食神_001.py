"""
Auto-generated semantic module for yuanhaiziping
Generated at: 2025-12-05T13:30:19.558814
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
    semantic_id="yhzp_v1.0.0_论食神_001",
    book_id="yuanhaiziping",
    engine_id="bazi"
)
class 论食神(SemanticEntry):
    """
    - **原文（source_text）**：食神者，生我财神之谓也；如甲属木，丙属火，名盗气，故谓之'食神'。何也？殊不知丙能生我戊土中食丙之戊财，故以此名之也。命中带此者，主人财厚食丰、腹量宽洪、肌...
    """
    
    original_text: str = """- **原文（source_text）**：食神者，生我财神之谓也；如甲属木，丙属火，名盗气，故谓之'食神'。何也？殊不知丙能生我戊土中食丙之戊财，故以此名之也。命中带此者，主人财厚食丰、腹量宽洪、肌体肥大、优游自足、有子息、有寿考。恒不喜见官星，忌倒食，恐伤其食神；喜财神相生。独一位见之，则为福人；然终亦不清。却喜身旺，不喜印绶，亦恐伤其食神也。

- **分字分词释义**：
  - **食神**：我生之神且阴阳相异者，如甲木生丙火，丙火为甲木之食神，能生财。
  - **盗气**：食神泄日主之气，故有"盗气"之称，但泄而生财故为吉。
  - **财厚食丰**：财富丰厚、饮食丰盛，食神格的典型福报。
  - **腹量宽洪**：度量宽广，胸襟开阔，食神之人的性格特征。
  - **肌体肥大**：身体丰腴，食神主口福故体态偏胖。
  - **优游自足**：悠闲自在，知足常乐，食神之人的生活状态。
  - **倒食/枭神**：偏印克食神，名"倒食"或"枭神夺食"，为食神格大忌。
  - **独一位**：食神宜单一清纯，多则杂而不清。

- **规范化释义（primary_lang_explained）**：食神是我生之神且阴阳相异，能生财故名"食神"。命带食神主财厚食丰、腹量宽广、肌体肥大、优游自足、有子有寿。食神不喜见官星（官克食），最忌偏印（倒食，印克食）；喜见财星（食生财）。食神宜一位独见为福，多则不清。喜身旺，不喜印绶。

- **完整对等诠释（secondary_lang_full）**：Eating God is what-I-generate with opposite polarity, generating Wealth hence named "Eating God." Fate bearing Eating God indicates abundant wealth and food, broad-minded disposition, corpulent physique, leisurely contentment, having children and longevity. Eating God dislikes meeting Officer Star (Officer controls Eating God), most taboos Indirect Seal/Reversed Eating (Seal controls Eating God); favors Wealth Star (Eating God generates Wealth). Eating God ideally singular for blessings, multiple brings impurity. Prefers strong Self, dislikes Seal.

- **核心要点**：
  - 食神为我生之神且阴阳相异，能生财故名"食神"
  - 食神主财厚食丰、腹量宽洪、优游自足、有子有寿
  - 食神不喜官星，最忌偏印（倒食/枭神夺食）
  - 食神喜财星相生，喜身旺
  - 食神宜一位独见为福，多则不清

- **详细解说**：  
  本条论述食神的性质、福报与喜忌。食神为我生之神且阴阳相异（如甲木生丙火），其名来自"生财"之意——食神能生财星，如丙火能生戊土（甲木之财）。食神格之人的典型福报是"财厚食丰、腹量宽洪、肌体肥大、优游自足、有子息、有寿考"，综合体现了食神的福禄寿全之象。食神的喜忌十分明确：不喜官星（官星会泄财星之气），最忌偏印（偏印克食神，名"倒食"或"枭神夺食"，是食神格的大忌）；喜财星（食神生财为流通之美），喜身旺（身旺能任食神之泄）。特别强调"独一位见之，则为福人"——食神宜单一清纯，多则杂而不清，与伤官"伤尽"的要求相呼应，都体现了子平法对格局纯粹性的追求。

- **叙事素材（narrative_snippets）**：
  - `[ns_yhzp_048]` `[trigger: 食神定义]` `[factor_trigger: eating_god AND eating_god_single]` `[role: 主干]` 食神者，生我财神之谓也。 → 《渊海子平·论食神》
  - `[ns_yhzp_049]` `[trigger: 食神福报]` `[factor_trigger: eating_god AND fulu_shouquan]` `[role: 主干依赖]` 命中带此者，主人财厚食丰、腹量宽洪、肌体肥大、优游自足。 → 《渊海子平·论食神》
  - `[ns_yhzp_050]` `[trigger: 食神有子有寿]` `[factor_trigger: eating_god]` `[role: 主干依赖]` 有子息、有寿考。 → 《渊海子平·论食神》
  - `[ns_yhzp_051]` `[trigger: 食神忌官]` `[factor_trigger: eating_god AND direct_officer]` `[role: 条件分支]` 恒不喜见官星。 → 《渊海子平·论食神》
  - `[ns_yhzp_052]` `[trigger: 食神忌枭]` `[factor_trigger: indirect_seal AND eating_god]` `[role: 条件分支]` 忌倒食，恐伤其食神。 → 《渊海子平·论食神》
  - `[ns_yhzp_053]` `[trigger: 食神喜财]` `[factor_trigger: eating_god AND direct_wealth]` `[role: 条件分支]` 喜财神相生。 → 《渊海子平·论食神》
  - `[ns_yhzp_054]` `[trigger: 食神宜单]` `[factor_trigger: eating_god]` `[role: 条件分支]` 独一位见之，则为福人；然终亦不清。 → 《渊海子平·论食神》"""
    normalized_text_zh: str = """"""
    subject: str = "论食神"
    factor_refs: list = ['eating_god', 'pattern_reversed_eating_proposal', 'relation_eating_generates_wealth_proposal']
    
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
        book_id="yuanhaiziping",
        chapter="",
        l1_anchor="yhzp_v1.0.0_论食神_001_L1",
    )
    version: str = "1.0.0"
