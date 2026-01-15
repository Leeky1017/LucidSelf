"""
Auto-generated semantic module for christian_astrology
Generated at: 2025-12-05T13:30:20.156378
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
    semantic_id="ca_v1.0.0_house_significations_001",
    book_id="christian_astrology",
    engine_id="astro"
)
class HouseSignifications(SemanticEntry):
    """
    #### Source Text
(Lilly Book I, pp. 47-56): "The twelve Houses of Heaven have their several signific...
    """
    
    original_text: str = """#### Source Text
(Lilly Book I, pp. 47-56): "The twelve Houses of Heaven have their several significations. The First House signifies the Life of man, the Second his Substance, the Third his Brethren..."

#### English Paraphrase (Primary Language)

**The Twelve Houses** represent life domains:

| House | Name | Significations |
|-------|------|----------------|
| 1st | Vita (Life) | Self, body, appearance, beginnings |
| 2nd | Lucrum (Gain) | Money, possessions, values |
| 3rd | Fratres (Siblings) | Siblings, communication, short journeys |
| 4th | Genitor (Parent) | Home, father, endings, property |
| 5th | Nati (Children) | Children, creativity, pleasure |
| 6th | Valetudo (Health) | Illness, servants, daily work |
| 7th | Uxor (Spouse) | Marriage, partnerships, open enemies |
| 8th | Mors (Death) | Death, inheritance, transformation |
| 9th | Pietas (Religion) | Religion, long journeys, higher learning |
| 10th | Regnum (Kingdom) | Career, honor, mother, authority |
| 11th | Benefacta (Benefits) | Friends, hopes, groups |
| 12th | Carcer (Prison) | Hidden enemies, confinement, self-undoing |

**Angular Houses** (1, 4, 7, 10): Most powerful
**Succedent Houses** (2, 5, 8, 11): Moderate strength
**Cadent Houses** (3, 6, 9, 12): Weakest placement

#### Complete Chinese Interpretation (Secondary Language)

**十二宫**代表生活领域：第1宫（生命）=自我；第2宫（财富）=金钱；第3宫（兄弟）=兄弟姐妹、沟通；第4宫（父亲）=家庭；第5宫（子女）=子女、创造；第6宫（健康）=疾病、仆人；第7宫（配偶）=婚姻、敌人；第8宫（死亡）=死亡、遗产；第9宫（宗教）=宗教、远行；第10宫（王国）=事业、荣誉；第11宫（福报）=朋友、希望；第12宫（监狱）=隐藏敌人、禁闭。**角宫**（1,4,7,10）最强；**续宫**（2,5,8,11）中等；**果宫**（3,6,9,12）最弱。

**Narrative Snippets**:
- `[ns_lilly_house_001]` `[trigger: angular_house]` `[factor_trigger: astro_house_angular]` `[role: 主干]` Angular houses (1, 4, 7, 10) are most powerful—planets here act strongly. → CA I #Houses
- `[ns_lilly_house_002]` `[trigger: house_meaning]` `[factor_trigger: astro_house_signification]` `[role: 主干依赖]` Each house governs specific life domains from life (1st) to hidden enemies (12th). → CA I #Houses"""
    normalized_text_zh: str = """"""
    subject: str = "House Significations"
    factor_refs: list = ['house_angular', 'house_succedent', 'house_cadent']
    
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
        book_id="christian_astrology",
        chapter="",
        l1_anchor="ca_v1.0.0_house_significations_001_L1",
    )
    version: str = "1.0.0"
