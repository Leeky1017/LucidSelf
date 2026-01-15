"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.739842
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
    semantic_id="zw_v1.0.0_批贵命_贪狼遇火申垣格_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 批贵命贪狼遇火申垣格(SemanticEntry):
    """
    - 分字分词释义：

  - **火贪格**：贪狼于申宫遇火星形成的武贵格局，恶杀逢火化吉。
  - **贪狼遇火**：贪狼星与火星同宫或会照，化贪狼之欲为进取之力。
  - **戌巳生人合格**：戌...
    """
    
    original_text: str = """- 分字分词释义：

  - **火贪格**：贪狼于申宫遇火星形成的武贵格局，恶杀逢火化吉。
  - **贪狼遇火**：贪狼星与火星同宫或会照，化贪狼之欲为进取之力。
  - **戌巳生人合格**：戌年或巳年出生者遇此格局尤为合格。
  - **祖生鞭**：典出祖逖闻鸡起舞，效法先贤的决心与进取心。
  - **魁钺三合**：天魁天钺在三合位置拱照身命，主贵人提携。
  - **鹿鸣宴**：科举及第后的庆功宴席，典出《诗经·鹿鸣》。
  - **二十余年重擢职**：仕途稳健进升，二十多年来不断晋升。

- **原文（source_text）**：  
  贪狼遇火局申垣，戍巳生人合格妍。破军七杀相扶照，何妨恶杀在水缠。据此斗数之理论，青年拟着祖生鞭。魁钺三合身命内，科禄夹命主希贤。前后星曜有循序，何忧富贵不双全。椿树萱花臻福祉，阶前棠棣乐翩翩。佳人贤淑同谐老，继后双成朵朵鲜。且论如今在某限，犹如花柳竞春妍。放心收却归腔子，须坐韩毡与郑毡。越岁相看符吉梦，笑贺重开汤饼筵。某星到某限，文星光射斗牛边。芹宫水暖鱼龙化，名挂儒林翰墨鲜。脱某看到某年近，乘风休驾子陵船。某年喜会某星美，食廪科场妙莫言。花如罗绮春光艳，又喜重重产俊贤。四八东西左与右，喜有尤，慎有忧。愆某年流禄科星集，鹿鸣宴上许争先。金勤马嘶芳草地，玉楼人醉杏花天。拜官百里声名振，子继书香孙又贤。二十余年重擢职，伫看金带系腰缠。寿元某岁里，谈笑入桃源。

- **规范化释义（primary_lang_explained）**：  
  此为批断「贪狼遇火·申垣格」的标准套语，即著名的「火贪格」。贪狼于申宫遇火星，戌巳年生人尤为合格。破军七杀相扶照，即使恶杀在水缠亦无妨——这是杀破狼逢火化吉的典型格局。套语从青年「拟着祖生鞭」（效法先贤）、科举登第到二十余年重擢职，展现火贪格的武贵兼文贵路径。

- **完整对等诠释（secondary_lang_full）**：  
  This template interprets the "Tan Lang Meeting Fire in Shen Palace" pattern—the famous "Fire‑Tan Lang" configuration. Tan Lang in Shen encounters Fire Star; those born in Xu or Si years especially fit this pattern. Po Jun and Qi Sha support; even malefics in Water positions pose no harm—a classic transformation of Sha‑Po‑Lang through Fire. The template traces from youth emulation to twenty‑plus years of career advancement.

- **核心要点**：  
  1. 适用格局：贪狼申宫遇火星（火贪格），戌巳生人合格。  
  2. 杀破狼特征：破军七杀相扶照，恶杀逢火化吉。  
  3. 仕途特征：二十余年重擢职，金带系腰缠。"""
    normalized_text_zh: str = """"""
    subject: str = "批贵命·贪狼遇火申垣格"
    factor_refs: list = ['pattern_huotan_shenyuan', 'star_tanlang_yuohuo', 'time_xusi_shengren', 'symbol_zushengbian', 'pattern_kuiyue_sanhe', 'symbol_lumingyan', 'source_ref', 'rel_vol7_06_001', 'star_tanlang_yuohuo', 'rel_vol7_06_002', 'time_xusi_shengren', 'rel_vol7_06_003', 'star_tanlang_yuohuo', 'rel_vol7_06_004', 'pattern_kuiyue_sanhe', 'evi_vol7_06_001', 'rule_huotan_shenyuan_chengge', 'evi_vol7_06_002', 'symbol_zushengbian', 'rule_zushengbian_jinqu', 'evi_vol7_06_003', 'symbol_lumingyan', 'rule_luming_zhongzhi', 'concept_fire_tan_transformation', 'concept_emulate_ancestors', 'concept_martial_literary']
    
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
        l1_anchor="zw_v1.0.0_批贵命_贪狼遇火申垣格_001_L1",
    )
    version: str = "1.0.0"
