"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.793457
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
    semantic_id="mlxj_v1.0.0_1_日月同宫_日类首条_完整精校_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1日月同宫日类首条完整精校(SemanticEntry):
    """
    #### 原文（source_text）

日月同宫大吉，主爵禄荣耀。易卦为离，大明当天，继照四方之象。梦此者，父母俱泰，夫妇齐眉，子孙孕育，凡事向明之兆也。日者，阳精之宗，人君之象。月者，阴精之宗，...
    """
    
    original_text: str = """#### 原文（source_text）

日月同宫大吉，主爵禄荣耀。易卦为离，大明当天，继照四方之象。梦此者，父母俱泰，夫妇齐眉，子孙孕育，凡事向明之兆也。日者，阳精之宗，人君之象。月者，阴精之宗，母后之象。

#### 分字分词释义

- **日**：太阳 / 阳精之宗 / 人君、父亲、夫君之象
- **月**：太阴 / 阴精之宗 / 母后、妻子之象
- **同宫**：并处一处 / 日月合照 / 阴阳并明
- **爵禄**：官爵与禄位 / 功名地位 / 主官运
- **离卦**：易经第三十卦，火上火下 / 光明、附丽 / 主文明显达
- **大明当天**：日月并照 / 光辉灿烂 / 至尊之象
- **齐眉**：夫妇和谐 / 白头偕老 / 主婚姻
- **孕育**：子孙繁衍 / 后代昌盛 / 主子嗣

#### 规范化释义（primary_lang_explained）

梦见日月同在一宫，大吉，主爵禄荣耀。对应《易经》离卦，大明当天、继照四方之象。做此梦者，父母俱安泰，夫妇齐眉，子孙孕育，凡事向明向好。

日是阳精之宗主，象征人君（及父亲、夫君）；月是阴精之宗主，象征母后（及妻子）。日月同宫，意味着阴阳并明、君后和谐、父母双全。

#### 完整对等诠释（secondary_lang_full）

Dreaming of the Sun and Moon together in one palace is greatly auspicious, indicating noble rank and glorious position. It corresponds to the Li (Clinging Fire) hexagram in the I Ching, symbolizing great brilliance illuminating all directions. The dreamer will enjoy both parents in good health, a harmonious marriage, and flourishing descendants—all affairs tend toward brightness and success.

The Sun represents the essence of Yang and symbolizes the sovereign (as well as the father and husband). The Moon represents the essence of Yin and symbolizes the empress (as well as the mother and wife). When Sun and Moon appear together, it signifies the harmonious union of Yin and Yang, the accord between ruler and consort, and the blessing of both parents being present.

#### 核心要点

- 日月同宫为日类梦象最高吉兆
- 对应离卦，火上火下，光明重明
- 日=阳精/人君/父/夫
- 月=阴精/母后/母/妻
- 日月并照=阴阳和合=大吉
- 主爵禄荣耀——功名显达
- 主夫妇齐眉——婚姻和谐
- 主子孙孕育——后代繁盛

#### 详细解说

本条是日类梦象的开篇，以「日月同宫」这一最高吉兆统领全节。

日月在中国古代天文与命理体系中地位极高。日为阳精之宗，主显、主尊、主男性权力；月为阴精之宗，主隐、主柔、主女性滋养。日月同宫，意味着阴阳两极同时呈现、并行不悖，是宇宙和谐的极致表现。

对应离卦，离为火，火上火下，光明重明。离卦象征附丽、依附，在人事上主文明、显达、离丽。日月同宫配离卦，则取其「大明当天」的光辉意象。

在人事应验上，日月同宫分层映射为：
- **政治层**：君后和谐、朝廷安定
- **家庭层**：父母双全、夫妇齐眉
- **个人层**：功名显达、子孙繁盛

#### 叙事素材（narrative_snippets）

- `[ns_mlxj_v1_006]` `[trigger: 梦日月同宫]` `[factor_trigger: dream_riyue_tonggong AND yijing_li AND dream_tianxiang AND dream_riyue AND dream_xingdou]` `[role: 主干]` 日月同宫大吉，主爵禄荣耀。易卦为离，大明当天。 → 《梦林玄解·卷一》#日月同宫
- `[ns_mlxj_v1_007]` `[trigger: 梦日月同宫]` `[factor_trigger: dream_riyue_tonggong]` `[role: 主干依赖]` 父母俱泰，夫妇齐眉，子孙孕育，凡事向明之兆。 → 《梦林玄解·卷一》#日月同宫
- `[ns_mlxj_v1_008]` `[trigger: 日象]` `[factor_trigger: dream_symbol_ri AND dream_tian AND dream_rishi]` `[role: 理论基础]` 日者，阳精之宗，人君之象。 → 《梦林玄解·卷一》#日月同宫
- `[ns_mlxj_v1_009]` `[trigger: 月象]` `[factor_trigger: dream_symbol_yue AND dream_yueshi AND dream_leiyu AND dream_fenglei]` `[role: 理论基础]` 月者，阴精之宗，母后之象。 → 《梦林玄解·卷一》#日月同宫"""
    normalized_text_zh: str = """"""
    subject: str = "1 日月同宫（日类首条·完整精校）"
    factor_refs: list = ['dream_riyue_tonggong', 'yijing_li', 'yang_jing', 'yin_jing']
    
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
        l1_anchor="mlxj_v1.0.0_1_日月同宫_日类首条_完整精校_001_L1",
    )
    version: str = "1.0.0"
