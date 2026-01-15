"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.101604
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
    semantic_id="smth_v1.0.0_论返本与阴阳煞_001",
    book_id="sanming",
    engine_id="bazi"
)
class 论返本与阴阳煞(SemanticEntry):
    """
    - **原文（source_text）**：
  返本煞。五行无贵气，下克上为返。歌曰："五行死绝并来时，有格如闲福不随；更忌日时克年主，定无官贵切须知。"如甲子金命得戊午日，又胎月日时多带寅巳，犯者...
    """
    
    original_text: str = """- **原文（source_text）**：
  返本煞。五行无贵气，下克上为返。歌曰："五行死绝并来时，有格如闲福不随；更忌日时克年主，定无官贵切须知。"如甲子金命得戊午日，又胎月日时多带寅巳，犯者定主孤立，或富或贵，一旺便克，伤父母尊长。
  阴阳煞。女属阴而喜阳，命得戊午旺火为正阳。男属阳而喜阴，命得丙子旺水为正阴。是阴阳和畅，故男得丙子，平生多得美妇人；女得戊午，平生多逢美男子。日上遇之，男得美妻，女得美夫。大忌元辰、咸池同宫，不论男女，皆淫。如男得戊午，多妇人相爱；女得丙子，多男子挑诱。更看有无贵贱消息。

- **分字分词释义**：
  - **返本煞**：五行无贵气且下克上（如日时克年命），主孤立伤亲。
  - **阴阳煞**：男得丙子、女得戊午为阴阳和畅，主得美配偶；忌元辰咸池则淫。

- **规范化释义（primary_lang_explained）**：
  返本煞指命局五行无贵气，且出现"下克上"（日时克年命）的逆向克制结构，如甲子金命见戊午日。犯者主孤立无援，即使富贵也难维系，易伤父母尊长。阴阳煞则基于"男喜阴、女喜阳"原则：男命得丙子旺水、女命得戊午旺火为"阴阳和畅"，主异性缘佳、配偶美丽。但若同时见元辰、咸池，则转为淫欲之象。

- **次语种完整诠释（secondary_lang_full）**：
  Returning Root Sha (Fan Ben) occurs when Five Elements lack nobility and "lower restrains upper" (Day/Hour restrains Year), as in Jia-Zi Metal Life meeting Wu-Wu Day. Afflicted individuals face isolation and injury to parents/elders, even if wealthy. Yin-Yang Sha is based on "male favors Yin, female favors Yang": male with Bing-Zi (Water) or female with Wu-Wu (Fire) achieve harmony, indicating good romantic fortune and beautiful spouses. However, if meeting Yuan Chen or Peach Blossom, it turns into promiscuity.

- **核心要点**：
  - 返本：下克上 + 无贵气 -> 孤立伤亲
  - 阴阳：性别配五行 -> 美配偶 / 忌咸池则淫

- **详细解说**：
  返本煞体现了儒家“孝道”与五行结构的结合，认为“下克上”违反伦理秩序，即使富贵也难以孝养父母。阴阳煞则是性别与五行阴阳匹配理论，认为男性（阳）需要阴水滋润、女性（阴）需要阳火温暖，方能吸引优质配偶。现代理解可视为“代际冲突风险”与“异性吸引力”标记。"""
    normalized_text_zh: str = """"""
    subject: str = "论返本与阴阳煞"
    factor_refs: list = ['new_candidate', 'new_candidate']
    
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
        l1_anchor="smth_v1.0.0_论返本与阴阳煞_001_L1",
    )
    version: str = "1.0.0"
