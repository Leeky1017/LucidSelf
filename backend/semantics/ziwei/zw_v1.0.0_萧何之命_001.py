"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699157
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
    semantic_id="zw_v1.0.0_萧何之命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 萧何之命(SemanticEntry):
    """
    - 分字分词释义：

  - **府相朝垣格**：天府天相拱照命宫的极贵格局。
  - **紫府左右权禄昌曲**：多重吉星会合命宫，主入相之命。
  - **坐贵向贵**：命宫坐贵又向贵人，主富贵双全...
    """
    
    original_text: str = """- 分字分词释义：

  - **府相朝垣格**：天府天相拱照命宫的极贵格局。
  - **紫府左右权禄昌曲**：多重吉星会合命宫，主入相之命。
  - **坐贵向贵**：命宫坐贵又向贵人，主富贵双全。
  - **限到擎羊**：大限行至擎羊星宫位，为凶险之限。
  - **酉生人忌**：酉年生人逢擎羊限有特定禁忌。
  - **流羊冲命**：流年擎羊与命宫相冲，主寿终应期。
  - **入相之命**：主宰相之位的命格。

- **原文（source_text）**：  
  萧何之命。阴男水二局。府相朝垣格紫府左右，权禄嘉会，又兼昌曲禄合，乃坐贵向贵，富贵双全。入相之命，限到擎羊，酉人忌之，小限流羊与命垣相冲，故六十难过。

- **规范化释义（primary_lang_explained）**：  
  萧何命属阴男水二局，府相朝垣格，紫府左右、权禄嘉会、昌曲禄合，坐贵向贵，主富贵双全、入相之命。然限到擎羊，酉生人有忌，小限流羊与命垣相冲，故六十难过而亡。

- **完整对等诠释（secondary_lang_full）**：  
  Xiao He's Yin male Water Second chart forms Fu Xiang Facing Court with Ziwei‑Tianfu Left‑Right, Authority‑Salary auspiciously converge, Chang‑Qu and Salary combine—sitting noble facing noble, dual wealth and honour, a prime minister's destiny. Period reaches Yang Blade, You natives face taboos. Minor transiting Blade clashes Life court. Could not survive past 60.

- **核心要点**：  
  1. 府相朝垣、紫府左右权禄昌曲会合，主入相之命。  
  2. 酉生人忌擎羊限。  
  3. 小限流羊与命垣相冲，为六十寿终应期。

- **叙事素材（narrative_snippets）**：
  - **入相之命**："府相朝垣格紫府左右，权禄嘉会，又兼昌曲禄合，乃坐贵向贵，富贵双全"，萧何命主入相之贵、富贵双全。
  - **擎羊为忌**："限到擎羊，酉人忌之"，点出酉年生人逢擎羊限的关键禁忌。
  - **流羊冲命**："小限流羊与命垣相冲，故六十难过"，流羊冲命垣为六十岁寿终的具体触发点。
  - **现代应用**：位极人臣者在遇到擎羊限与流羊冲命的叠加年份，应主动减压、分权与养生，以避免因过劳与决策压力触发极端事件。"""
    normalized_text_zh: str = """"""
    subject: str = "萧何之命"
    factor_refs: list = ['pattern_zuoguixianggui', 'result_ruxiang', 'pattern_liuyangchong', 'source_ref', 'rel_xiaohe_001', 'pattern_fuxiangchaoyuan', 'rel_xiaohe_002', 'star_qingyang', 'rel_xiaohe_003', 'pattern_liuyangchong', 'evi_xiaohe_001', 'pattern_liuyangchong', 'rule_yousheng_qingyang', 'concept_prime_minister', 'concept_transiting_blade']
    
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
        book_id="ziwei",
        chapter="",
        l1_anchor="zw_v1.0.0_萧何之命_001_L1",
    )
    version: str = "1.0.0"
