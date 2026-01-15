"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699485
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
    semantic_id="zw_v1.0.0_王莽之命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 王莽之命(SemanticEntry):
    """
    - 分字分词释义：

  - **科权禄拱**：科星、权星、禄星同会命宫，主名誉、权力与俸禄齐至。
  - **紫破辰戌**：紫微与破军同在辰戌轴上，主结构不稳、臣道不忠。
  - **篡汉之佐**：...
    """
    
    original_text: str = """- 分字分词释义：

  - **科权禄拱**：科星、权星、禄星同会命宫，主名誉、权力与俸禄齐至。
  - **紫破辰戌**：紫微与破军同在辰戌轴上，主结构不稳、臣道不忠。
  - **篡汉之佐**：超越臣子边界、有僭越篡逆之心。
  - **申人忌见久铃**：申宫安命之人忌见铃星成久铃格局，主一生多波折灾厄。
  - **大铃地网重并**：铃星与天罗地网在大限重叠成局，主大祸难逃。
  - **天伤刑伤**：天伤星与刑伤诸星同会，主身体伤损或司法刑罚。
  - **阳男木三局**：王莽命盘的五行局数，木三局主生发权谋。

- **原文（source_text）**：  
  王莽之命。阳男木三局。科权禄拱，名誉声扬，紫破辰戌，为臣不忠，篡汉之佐是也。且申人忌见久铃，五十三大限入戍，遇大铃地网重并，小限天伤𮞸刑伤而亡。

- **规范化释义（primary_lang_explained）**：  
  王莽为阳男木三局，命宫得科、权、禄三吉同拱，名誉与权力齐来，是典型「科权禄拱，名誉声扬」之格，足以成就一代权臣。然命局亦见紫微、破军居辰戌之地，原文以「紫破辰戌，为臣不忠」点出其性格与行事偏离臣道正轨，终成篡汉之佐。  
  对申人而言，「久铃」一类铃星格局尤为忌见。五十三岁时，大限入戌，与大铃、地网重叠，小限又逢天伤及刑伤诸星，会成「铃星 + 地网 + 刑伤」的多重凶局。此时既有权势结构本身的偏斜，又有岁运上的重压，极易在政变、兵祸或司法清算中暴亡。此命例展示「极盛之权臣，在篡逆与大凶岁运叠加下身死名裂」的格局。

- **完整对等诠释（secondary_lang_full）**：  
  Wang Mang’s chart belongs to a Yang Wood native of the Third Configuration. With Ke, Quan and Lu encircling the Life palace, his pattern promises strong reputation and substantial authority—"honours and stipends flanking together." Yet Zi Wei together with Po Jun in the Chen‑Xu axis carries a warning: "with Zi‑Po in Chen and Xu, a minister cannot remain loyal." This points to a courtier whose ambition exceeds the bounds of proper service, eventually becoming an accomplice in the usurpation of the Han.  
  For natives of the Shen branch, lingering configurations involving the bell star Ling are particularly ominous. Around the age of fifty‑three, the major period moves into Xu while the "great bell" and the Net of Heaven and Earth double up; the minor period at the same time encounters Tian Shang and other punitive stars. This stack of Ling, the Net and wounding indicators describes a moment when structural disloyalty and hostile timing converge, making death by rebellion, military disaster or judicial purge highly likely. The case exemplifies a power‑hungry minister whose rise and fall both crystallise around acts of usurpation.

- **核心要点**：  
  1. 科权禄拱使王莽具备极高权势与声誉，是标准「权臣格局」。  
  2. 紫破辰戌暗示臣道不忠，结构上即埋下篡逆与颠覆的可能。  
  3. 五十三岁大限入戌，与大铃、地网及天伤刑伤同会，构成暴烈身亡的高危岁运。

- **叙事素材（narrative_snippets）**：
  - **权臣格局**："科权禄拱，名誉声扬"，王莽命主以科名与权势齐备，堪称一代权臣。
  - **紫破不忠**："紫破辰戌，为臣不忠，篡汉之佐是也"，紫破辰戌结构，将其推向僭越与篡逆之路。
  - **铃星地网**："且申人忌见久铃，五十三大限入戍，遇大铃地网重并，小限天伤𮞸刑伤而亡"，铃星加地网与天伤刑伤叠加，为暴烈身亡的节点。
  - **现代应用**：对职场与权力边界模糊、喜欢「玩规则」的人而言，一旦命局又带铃星地网重凶组合，在关键年份极易因越界操作而遭遇法律与舆论的双重反噬。"""
    normalized_text_zh: str = """"""
    subject: str = "王莽之命"
    factor_refs: list = ['pattern_kequanlu_gong', 'pattern_zipo_chenxu', 'result_weichen_buzhong', 'condition_shenren_jiuling', 'malefic_daling_diwang', 'malefic_tianshang_xingshang']
    
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
        l1_anchor="zw_v1.0.0_王莽之命_001_L1",
    )
    version: str = "1.0.0"
