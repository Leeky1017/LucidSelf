"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228660
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
    semantic_id="smth_v1.0.0_庚戌辛亥钗钏金_坚成之金不可见火_001",
    book_id="sanming",
    engine_id="bazi"
)
class 庚戌辛亥钗钏金坚成之金不可见火(SemanticEntry):
    """
    - **原文（source_text）**：
  庚戌、辛亥坚成之金，不可见火，恐有所伤，若得水土相之为贵。阎东叟云：庚戌火墓之金，有刚烈自恃之暴，秋冬庶几沉厚，春夏动生悔吝，君子执兵刑之权，小人恣犷...
    """
    
    original_text: str = """- **原文（source_text）**：
  庚戌、辛亥坚成之金，不可见火，恐有所伤，若得水土相之为贵。阎东叟云：庚戌火墓之金，有刚烈自恃之暴，秋冬庶几沉厚，春夏动生悔吝，君子执兵刑之权，小人恣犷悍之性。辛亥金，禀乾健纯明中正之气，春秋冬三时吉，夏七吉三凶。贵格乘之，体仁守义，若带刑煞，肆暴贪功。

- **分字分词释义**：
  - **坚成之金**：坚硬已成的金。
  - **恐有所伤**：恐怕有所伤害。
  - **水土相之**：水土相辅相成。
  - **火墓之金**：火墓中的金。
  - **刚烈自恃**：刚烈自负。
  - **庶几沉厚**：差不多沉稳深厚。
  - **动生悔吝**：动辄产生悔恨吝啬。
  - **执兵刑之权**：掌握兵刑大权。
  - **恣犷悍之性**：放纵粗犷强悍的性格。
  - **禀乾健纯明中正**：禀受乾卦刚健纯正光明中正的气质。
  - **体仁守义**：体现仁爱坚守道义。
  - **肆暴贪功**：放纵暴虐贪图功劳。

- **规范化释义（primary_lang_explained）**：
  庚戌、辛亥是坚硬已成的金，不可见火，恐怕有所伤害，如果得到水土相辅则为贵。阎东叟说：庚戌是火墓中的金，有刚烈自负的暴烈性格，秋冬差不多沉稳深厚，春夏动辄产生悔恨，君子掌握兵刑大权，小人放纵粗犷强悍的性格。辛亥金，禀受乾卦刚健纯正光明中正的气质，春秋冬三季吉利，夏天七成吉利三成凶险。如果贵格乘之，体现仁爱坚守道义，如果带刑煞，则放纵暴虐贪图功劳。

- **完整对等诠释（secondary_lang_full）**：
  Gengxu, Xinhai are firm-formed metal, cannot see Fire, fearing injury. If seeing Metal-Water abundantly assisting, then wealth-nobility honored-glory pattern. Yan Dongsou says: Gengxu is fire-tomb metal, has fierce-violent self-reliant violent-nature, autumn-winter nearly steady-thick, spring-summer moving generates regret-stinginess. Gentleman wields military-punishment authority, petty-man indulges rough-fierce nature. Xinhai Metal receives Qian-vigorous pure-bright centered-upright energy, spring-autumn-winter three-seasons auspicious, summer seven-auspicious three-inauspicious. Noble pattern riding it, embodies benevolence guards righteousness. If carrying punishment-sha, indulges violent-tyrannical greedy-meritorious.

- **核心要点**：
  - 庚戌辛亥为钗钏金，坚成之金
  - 不可见火恐伤、水土相助为贵
  - 庚戌火墓金、刚烈自恃
  - 秋冬沉厚、春夏悔吝
  - 君子兵刑权、小人犷悍性
  - 辛亥禀乾健、春秋冬吉夏七吉三凶
  - 贵格体仁守义、带煞肆暴贪功

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_240]` `[trigger: 庚戌辛亥金性质]` `[factor_trigger: gengxu_xinhai_firm_formed_metal AND fierce_self_reliant_qian_vigorous_upright AND noble_benevolent_righteous_sha_violent_tyrannical]` `[role: 主干]` 庚戌、辛亥坚成之金，不可见火，恐有所伤，若得水土相之为贵。阎东叟云：庚戌火墓之金，有刚烈自恃之暴，秋冬庶几沉厚，春夏动生悔吝，君子执兵刑之权，小人恣犷悍之性。辛亥金，禀乾健纯明中正之气，春秋冬三时吉，夏七吉三凶。贵格乘之，体仁守义，若带刑煞，肆暴贪功。 → 《三命通会》卷一#庚戌辛亥金性质

- **详细解说**：
  此条详论庚戌、辛亥（钗钏金）的性质与格局。二者为坚成之金，不可见火（火克金），需水土相助为贵（水润金、土生金）。阎东叟分析：庚戌火墓金刚烈自恃，秋冬沉厚、春夏悔吝，君子执兵刑权、小人犷悍性；辛亥禀乾健纯明中正，春秋冬吉夏七吉三凶，贵格体仁守义、带煞肆暴贪功。这是论述成器金的性格两极与季节影响。

- **校勘与字词辨析（双语）**：
  - **中文**："坚成"指金已成器坚硬。"火墓"指戌为火墓。"乾健"指乾卦刚健之德。"体仁守义"指实践仁义。
  - **English**: "Firm-formed" means metal already formed into vessel and hard. "Fire-tomb" means Xu is fire's tomb. "Qian-vigorous" means vigorous virtue of Qian trigram. "Embodies benevolence guards righteousness" means practicing benevolence and righteousness."""
    normalized_text_zh: str = """"""
    subject: str = "庚戌辛亥钗钏金：坚成之金不可见火"
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
        l1_anchor="smth_v1.0.0_庚戌辛亥钗钏金_坚成之金不可见火_001_L1",
    )
    version: str = "1.0.0"
