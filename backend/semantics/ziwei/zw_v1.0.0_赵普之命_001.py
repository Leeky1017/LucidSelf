"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699645
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
    semantic_id="zw_v1.0.0_赵普之命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 赵普之命(SemanticEntry):
    """
    - 分字分词释义：

  - **左右夹贵**：左辅、右彼夹拱贵星，主有辅佐之臣与贵人围绕。
  - **禄合加会**：禄星与财星、官星相合加会，主财官双美。
  - **天使之地**：与官职、制度与...
    """
    
    original_text: str = """- 分字分词释义：

  - **左右夹贵**：左辅、右彼夹拱贵星，主有辅佐之臣与贵人围绕。
  - **禄合加会**：禄星与财星、官星相合加会，主财官双美。
  - **天使之地**：与官职、制度与责任相关的宫位，主职位压力与规训。
  - **太岁到酉**：太岁行至酉位，特定生人此位有凶。
  - **文曲化忌**：文曲由吉化忌，主名誉、文书或学术方面的纠纷与损害。
  - **流羊来命**：流年羊刃冲击命宫，主意外冲击与血光之灾。
  - **阳男水二局**：赵普命盘的五行局数，水二局主智慧权谋。

- **原文（source_text）**：  
  赵普之命。阳男水二局。左右夹贵，禄合加会，富贵双全，有到终。七十八岁，太岁到酉，大限在于天使之地，小限到卯，流年文曲化忌流羊来命，是以凶也。

- **规范化释义（primary_lang_explained）**：  
  赵普命为阳男水二局，「左右夹贵」指左右辅弼夹拱贵星，「禄合加会」则禄星与财星、官星相合，构成富贵双全的格局，原文言「有到终」，显示其寿数本可接近自然全程，一生多能安享权位与财富。  
  然而在七十八岁，太岁行至酉位，大限行「天使之地」，象征在权势结构与制度位阶中承受特殊压力；小限到卯，与命局形成冲动，流年文曲又化忌并同流羊来冲命，是「太岁酉位 + 天使地 + 文曲化忌 + 流羊冲命」的多重凶象。最终在此年，由于文化声望、权力结构与凶曜齐集，对身心与处境形成致命压力而凶亡。

- **完整对等诠释（secondary_lang_full）**：  
  Zhao Pu’s chart is that of a Yang Water native in the Second Configuration. With Left and Right Assistants flanking noble stars and Lu joining other benefics, the pattern "Zuo‑You flanking nobles, Lu combining" promises both rank and material abundance. The phrase "he almost reaches the end" suggests a near‑full natural lifespan spent in relative security and honour.  
  At seventy‑eight, however, the Annual Tai Sui moves into You, the major period occupies a "Heavenly Office" sector, and the minor period arrives at Mao, setting up冲s within the chart. In that year Wen Qu turns into a Ji‑type malefic and flowing Yang star also comes to the Life, forming a combination of "You Tai Sui + Heavenly Office stress + Wen Qu turning Ji + Yang attacking the chart." This convergence symbolises pressures from office, reputation and sharp transits collectively overwhelming the native, leading to a fatal outcome. The case illustrates a statesman‑type chart that enjoys long‑term fortune yet still meets a sharply defined terminal year.

- **核心要点**：  
  1. 左右夹贵、禄合加会，是富贵双全且寿数本可接近终寿的权臣格局。  
  2. 七十八岁太岁到酉、大限天使之地、小限到卯，流年文曲化忌并同流羊冲命，形成终结性压力。  
  3. 命例展现「长寿权臣在特定年份被名位与凶曜合击而亡」的情形。

- **叙事素材（narrative_snippets）**：
  - **左右夹贵**："左右夹贵，禄合加会，富贵双全，有到终"，赵普命主以左右夹贵与禄合之格，享权位与财富并重且几乎终寿。
  - **酉太岁与天使**："七十八岁，太岁到酉，大限在于天使之地"，太岁酉位配天使地，象征制度责任与名誉审视在高龄仍然很重。
  - **文曲化忌流羊**："小限到卯，流年文曲化忌流羊来命，是以凶也"，文曲化忌与羊刃冲命，为「声名与刀光」一起压向命宫的终局年份。
  - **现代应用**：对长期处在政策、法律或舆论核心位置的老牌权臣或专家而言，在高龄又出现「文曲化忌 + 羊刃冲命」时，应刻意淡出公众一线，做好声誉与健康的双重防护，以免被晚年的一场风波意外收尾。"""
    normalized_text_zh: str = """"""
    subject: str = "赵普之命"
    factor_refs: list = ['pattern_zuoyou_jiagui', 'pattern_luhe_jiahui', 'timing_tianshi_di', 'timing_taisui_you', 'transform_wenqu_huaji', 'timing_liuyang_laiming']
    
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
        l1_anchor="zw_v1.0.0_赵普之命_001_L1",
    )
    version: str = "1.0.0"
