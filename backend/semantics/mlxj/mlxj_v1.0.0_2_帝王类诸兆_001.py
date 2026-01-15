"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.842895
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
    semantic_id="mlxj_v1.0.0_2_帝王类诸兆_001",
    book_id="mlxj",
    engine_id="dream"
)
class 2帝王类诸兆(SemanticEntry):
    """
    #### 分类汇总

**大吉类**：
- 封王吉：不论贵贱贫富，主宠荣显位
- 立太子吉：帝王主祖宗之灵，常人主神明获利生子
- 传位（得人传我）：事无不佳
- 梦见伏羲：文才另辟，孕育奇男
- 梦...
    """
    
    original_text: str = """#### 分类汇总

**大吉类**：
- 封王吉：不论贵贱贫富，主宠荣显位
- 立太子吉：帝王主祖宗之灵，常人主神明获利生子
- 传位（得人传我）：事无不佳
- 梦见伏羲：文才另辟，孕育奇男
- 梦见女娲：补天奇绩，非凡之兆
- 梦见神农：疾愈家丰，禾稻大熟
- 梦见黄帝：弃儒习医，业精国手
- 梦见尧舜：圣君继统，孝子贵儿
- 梦见大禹：通达利济，耀祖荣亲

**凶类**：
- 梦见夏桀：先乐后忧，败家亡身之种
- 梦见纣王：残虐荒淫之兆
- 梦见隋炀帝：穷奢丧国，乐极悲生

**贞吉否凶类**：
- 传位（传与人）：身居其位者不祥
- 争位：详其胜负而定吉凶
- 梦见晋文公：骨肉之变，险阻艰难后成业
- 梦见越王句践：利患难不利安乐

#### 历代帝王梦象速查

| 帝王 | 吉凶 | 核心主应 |
|------|------|---------|
| 伏羲 | 吉 | 文才另辟，孕育奇男 |
| 女娲 | 大吉 | 补天奇绩，非凡之兆 |
| 神农 | 吉 | 疾愈家丰 |
| 黄帝 | 吉 | 弃儒习医 |
| 尧 | 吉 | 招佳婿 |
| 舜 | 吉 | 晚年亨达，得孝子 |
| 大禹 | 吉 | 通达利济 |
| 成汤 | 吉 | 开创之功 |
| 文王 | 吉 | 晚年贵显 |
| 武王 | 吉 | 征战创业 |
| 秦始皇 | 吉 | 兵权在手，一统天下 |
| 汉高祖 | 吉 | 发迹草野 |
| 汉武帝 | 吉 | 富贵尊荣 |
| 光武帝 | 吉 | 中兴复业 |
| 唐太宗 | 贞吉否凶 | 骨肉情乖，君臣得合 |
| 宋太祖 | 吉 | 胜祖之兆 |
| 宋仁宗 | 吉 | 太平天子 |"""
    normalized_text_zh: str = """"""
    subject: str = "2 帝王类诸兆"
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
        l1_anchor="mlxj_v1.0.0_2_帝王类诸兆_001_L1",
    )
    version: str = "1.0.0"
