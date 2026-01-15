"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.789212
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
    semantic_id="mlxj_v1.0.0_3_五神所属物类_001",
    book_id="mlxj",
    engine_id="dream"
)
class 3五神所属物类(SemanticEntry):
    """
    #### 原文摘要

**肝属之物**（东方青色）：风雷、桥林、木小儿、书籍、纸笔、头眼、目肝、胆手、须发、谷食、蔬菜、冠巾、帽笄、布帛、绢纩、絮衾、帷楼、阁仓、廒亭、台窗、户栋、梁车、舟楫、弓矢、卤...
    """
    
    original_text: str = """#### 原文摘要

**肝属之物**（东方青色）：风雷、桥林、木小儿、书籍、纸笔、头眼、目肝、胆手、须发、谷食、蔬菜、冠巾、帽笄、布帛、绢纩、絮衾、帷楼、阁仓、廒亭、台窗、户栋、梁车、舟楫、弓矢、卤簿、笾豆、桌鼓、木鱼板、箎犁、机梭、筐篚、梳栉、规矩、网罗、衡钓、纶牿、杏李、梅桃、芦蓬、麻榆、梓杉、桧檀、孔雀、莺鸾、鹧鸪、戴胜、麟象、獬豸、狼豻、蛟鱼鳌、蚕蝶、蛾子、虫蛆。

**心属之物**（南方赤色）：日月、星斗、云霞、闪电、霹雳、烟雾、火光、帝王、神圣、舌心、酒肉、食冕、旒龙、衮黼、黻绯、袍凤、冠塔、殿阁、灶廐、寺观、轮辐、琴瑟、风车、绳索、珊瑚、琥珀、朱砂、牡丹、榴葵、莲松、枫枣、栗凤、鹔鹴、鹏鹄、猴雉、鸡马、蛇鼠、狮虎、彪熊、豕龟、蜂蚁、萤蜈蚣。

**脾属之物**（中央黄色）：星地、土山、城塞、野岸、堰路、田苑、囿圃、坟墓、身鼻、腹脾、胃肠、脐臀、粪佩、绅带、笏宫、阙库、藏础、石坑、厕樯、桅墨、床榻、椅石、磬瓯、缶埙、鞍辔、玉宝、石贝、玛瑙、石萱、草蔬、黍禾、稷榖、麦菽、乌鹅、貉獐、驼蜣、螂蝠、蝎虱。

**肺属之物**（西方白色）：天石、耳骨、咽喉、肺镮、镯剑、厅堂、井钮、砚戟、矛斧、锤爵、银杯、瓦巵、钟磬、笙竽、箫筦、镈铚、锹水、车钗、钿口、庭斤、锯锣、铙铃、银铜、锡铁、钱桂、花薇、菊花、竹柏、槐桑、瓜鹤、鸿雁、鹡鸰、龙牛、犬羊、蟹䲡、鳝蛩、蜗牛、蛙锥、刀化、首耜、权黄、金铅、梧桐、蝉兰、鹦鹉、萍藻、骡驴。

**肾属之物**（北方黑色）：月云、虹霓、霜雪、露冰、雹水、海江、河女、子老、人夷、人背、乳肾、阴户、膝溺、血茶、汤水、果靴、鞋舄、窖窨、雨栊、伞雨、琉璃、水晶、霰芭、蕉鸾、沟池、鸱枭、鸡漱、齿兕、牛犀、牛肾、茎兔、狐足、蜃螺、浆鼋、鳖牢、蜘蛛、蝌斗、珠杨、柳猩、猩凫、鸥鹯、鹰獭、蛤蚌、芙蕖、猫蚯、蚓乌、㺄鸭、鼍蝇。"""
    normalized_text_zh: str = """"""
    subject: str = "3 五神所属物类"
    factor_refs: list = ['source_ref']
    
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
        book_id="mlxj",
        chapter="",
        l1_anchor="mlxj_v1.0.0_3_五神所属物类_001_L1",
    )
    version: str = "1.0.0"
