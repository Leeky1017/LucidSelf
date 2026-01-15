"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.739824
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
    semantic_id="zw_v1.0.0_批贵命_天相未垣辅弼加会格_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 批贵命天相未垣辅弼加会格(SemanticEntry):
    """
    - 分字分词释义：

  - **天相未垣**：天相星守命于未宫，为本套语核心格局。
  - **辅彼加会**：左辅右彼加会命身宫，增强辅佐与贵人力量。
  - **台辅到命不逢空**：台辅星到命宫且...
    """
    
    original_text: str = """- 分字分词释义：

  - **天相未垣**：天相星守命于未宫，为本套语核心格局。
  - **辅彼加会**：左辅右彼加会命身宫，增强辅佐与贵人力量。
  - **台辅到命不逢空**：台辅星到命宫且不逢空亡，主贵人提携。
  - **焚膏继晕**：勤学苦读不辍，形容科举备考的刻苦精神。
  - **百步穿扬**：科举高中的比喻，喃一举成功，出自养由基射柳叶典故。
  - **银带换金带**：仕途升迁的比喻，由低阶晋升高阶官职。
  - **盛世英才**：天相未垣得辅彼加会所成之格，主科举登第、仕途通达。

- **原文（source_text）**：  
  天相未垣真可羡，对宫某宿喜朝垣。身星辅弼来加会，三方会吉无刑战。台辅到命不逢空。盛世英才从此见，焚膏继晷何芸窗。笃志稳期登月殿，趋庭闻礼与闻诗。少年怀抱温公见，机关百出迈群见，智识谋深应不浮。双亲百岁沐恩荣，棠棣田直可共伦。佳人金石同偕老，丹桂传芳朵朵馨。某限某星喜入庙，青灯夜雨要番心。气盾陶镕人俊雅，二八游芹压世英。某限之中廿五年，文昌科禄吉神临，百步穿扬应一箭，春闱秋榜占先魁。承恩出仕花封县，重擢重堕乐陶陶。银带换却金带旋，六六前后六七傍，恶星作祸忧当见。某宫某星喜又来，滚滚红尘拂人面，官居宪副却归来。稀寿悭悭猿鹤怨。

- **规范化释义（primary_lang_explained）**：  
  此为批断「天相未垣·辅弼加会」格的标准套语。天相守命于未宫，对宫吉宿朝拱，身星得辅弼加会，三方吉星汇聚无刑冲，台辅到命不逢空亡，是盛世英才之格。套语勾勒勤学苦读（焚膏继晷）、科举登第（百步穿扬一箭）、仕途升迁（银带换金带）的完整仕途历程。

- **完整对等诠释（secondary_lang_full）**：  
  This template interprets the "Tian Xiang in Wei Palace, Fu Bi Converging" pattern. Tian Xiang guards Life in Wei, opposite palace has auspicious stars aspecting, Body star receives Zuo Fu You Bi, triad gathers auspicious stars without clash, Tai Fu arrives without encountering Void—a pattern of prosperous‑era talent. The template outlines diligent study, examination triumph, and career advancement.

- **核心要点**：  
  1. 适用格局：天相未垣，辅弼加会，三方吉星汇聚。  
  2. 勤学特征：焚膏继晷、趋庭闻礼闻诗。  
  3. 仕途特征：百步穿扬一箭、银带换金带。"""
    normalized_text_zh: str = """"""
    subject: str = "批贵命·天相未垣辅弼加会格"
    factor_refs: list = ['star_tianxiang_weiyuan', 'pattern_fubi_jiahui', 'pattern_taifu_daoming', 'symbol_fengao_jigui', 'symbol_baibu_chuanyang', 'symbol_yindai_huanjindai', 'source_ref', 'rel_vol7_05_001', 'star_tianxiang_weiyuan', 'rel_vol7_05_002', 'pattern_taifu_daoming', 'rel_vol7_05_003', 'symbol_fengao_jigui', 'rel_vol7_05_004', 'symbol_baibu_chuanyang', 'evi_vol7_05_001', 'rule_tianxiang_wei_gui', 'evi_vol7_05_002', 'rule_fengao_baibu_keju', 'evi_vol7_05_003', 'symbol_yindai_huanjindai', 'rule_yindai_jindai_shengqian', 'concept_diligent_scholar', 'concept_exam_success', 'concept_career_promotion']
    
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
        l1_anchor="zw_v1.0.0_批贵命_天相未垣辅弼加会格_001_L1",
    )
    version: str = "1.0.0"
