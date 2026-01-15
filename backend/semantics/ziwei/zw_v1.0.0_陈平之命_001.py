"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699167
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
    semantic_id="zw_v1.0.0_陈平之命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 陈平之命(SemanticEntry):
    """
    - 分字分词释义：

  - **权禄生逢天府**：生年化权化禄与天府同宫，主入相之命。
  - **武曲守命垣**：武曲星坐守命宫，主财权。
  - **左右昌曲加会**：左辅右彼文昌文曲同会命宫，...
    """
    
    original_text: str = """- 分字分词释义：

  - **权禄生逢天府**：生年化权化禄与天府同宫，主入相之命。
  - **武曲守命垣**：武曲星坐守命宫，主财权。
  - **左右昌曲加会**：左辅右彼文昌文曲同会命宫，主辅佐文才。
  - **身临绝地**：身宫行至十二长生绝位，主气绝。
  - **天空天使夹地**：天空天使二星夹守地网，主多重困境。
  - **戌生忌陀罗**：戌年生人逢陀罗有特定禁忌。
  - **阳男木三局**：陈平命盘的五行局数，木三局主生发谋略。

- **原文（source_text）**：  
  陈平之命。阳男木三局。权禄生逢天府，武曲守命垣，左右昌曲加会，忻然入相之命。大限七十三入申，身临绝地，小限到天空，天使夹地，又陀罗为戍人所忌，是为不吉，故终寿。

- **规范化释义（primary_lang_explained）**：  
  陈平命属阳男木三局，权禄生逢天府、武曲守命，左右昌曲加会，主入相之命。大限七十三入申、身临绝地，小限到天空、天使夹地，陀罗为戌生人所忌，诸凶叠加而寿终。

- **完整对等诠释（secondary_lang_full）**：  
  Chen Ping's Yang male Wood Third chart has Authority‑Salary meeting Tianfu, Wuqu guards Life, Left‑Right Chang‑Qu converge—a prime minister's destiny. At 73 major enters Shen, body at Extinction; minor meets Void, Envoy flanks. Tuo Luo taboo for Xu natives. Malefics cause death.

- **核心要点**：  
  1. 权禄天府武曲守命，主入相之命。  
  2. 大限身临绝地，小限天空天使夹地。  
  3. 戌生人忌陀罗，为寿终应期。

- **叙事素材（narrative_snippets）**：
  - **入相格局**："权禄生逢天府，武曲守命垣，左右昌曲加会"，陈平命主入相之贵、筹谋在握。
  - **绝地晚限**："大限七十三入申，身临绝地，小限到天空，天使夹地"，身宫行至绝地又被天空天使夹守，为晚年气衰之象。
  - **陀罗为忌**："又陀罗为戍人所忌，是为不吉"，戌年生人逢陀罗加会，多主晚节多忧。
  - **现代应用**：高位谋臣在晚年遇到绝地+天空天使+陀罗叠加之年，宜主动退居二线、减轻负荷，以免功成身退反成险关。"""
    normalized_text_zh: str = """"""
    subject: str = "陈平之命"
    factor_refs: list = ['pos_shenlingjuedi', 'pattern_tianshijiadi', 'taboo_xushengtuoluo', 'source_ref', 'rel_chenping_001', 'pattern_quanlutianfu', 'rel_chenping_002', 'pos_shenlingjuedi', 'rel_chenping_003', 'taboo_xushengtuoluo', 'evi_chenping_001', 'taboo_xushengtuoluo', 'rule_xusheng_tuoluo', 'concept_extinction', 'concept_envoy_flank']
    
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
        l1_anchor="zw_v1.0.0_陈平之命_001_L1",
    )
    version: str = "1.0.0"
