"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228917
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
    semantic_id="smth_v1.0.0_大溪水_惊涛薄岸与归养之势_001",
    book_id="sanming",
    engine_id="bazi"
)
class 大溪水惊涛薄岸与归养之势(SemanticEntry):
    """
    - **原文（source_text）**：
  甲寅、乙卯大溪水。大溪水者，惊涛薄岸，骇浪浮天，光涵万里之宽，碧倒千山之影，最喜有归有养，遇坎则为有归，得金则为有养。所𭒡者，日月时中，有申酉冲动，或...
    """
    
    original_text: str = """- **原文（source_text）**：
  甲寅、乙卯大溪水。大溪水者，惊涛薄岸，骇浪浮天，光涵万里之宽，碧倒千山之影，最喜有归有养，遇坎则为有归，得金则为有养。所𭒡者，日月时中，有申酉冲动，或辰巳风吹，主飘流井泉水净而止。涧下有丑为艮，天河沾润，大海朝□，此四水皆吉。长流有风，独不宜见。此水以清金为助养，惟钗砂最宜，镴金亦清，若有钗金对冲，则不宜。海中虽无造化，甲子属坎，乙丑为艮，乃归源之地，亦吉。泊金最微，不能相生，岂有超显之理。剑金虽化于大溪，却忌卯雷巽风，主性不定。五行有土，皆为无益。屋上城头壅阻，此水路傍稍可，亦不为奇。壁上独辛丑为山，大驿，惟己酉有合，戊申则冲，庚子则刑，皆不为吉。

- **规范化释义（primary_lang_explained）**：
  甲寅、乙卯为大溪水。大溪水取象为山间大川，惊涛拍岸、浪花冲天，水面广阔如镜可映万里光辉、倒映千山之影，气象宏大而流速急。此水最喜"有归、有养"：遇坎位则为有归，象征水势有归宿；得清金则为有养，象征水源有养护。命局中日月时有申酉冲动，或辰巳之风吹拂，往往主水势漂流难定；若再得井泉、涧下、天河、大海四水与之相会，则能由急流汇入更大体系而成吉象。唯独长流水再加风动，多为漂泊不宁，不宜多见。大溪水最需要清金助养：钗钏金与砂中金最宜，镴金亦属清金；若钗金成对冲，则反成不稳。海中金本身在大溪中并无造化，但甲子属坎、乙丑为艮，为水之归源之地，仍可言吉。泊金太微，难以真正资生；剑锋金虽可化入大溪，但最忌卯位雷风（巽风）过动，主性情反复不定。土五行对大溪水大多无益：屋上土、城头土多成壅阻之象，路傍土略可承载水道却不见奇特；壁上土中独辛丑可作山论，而大驿土中惟己酉有合，戊申则冲、庚子则刑，皆为不吉。

- **完整对等诠释（secondary_lang_full）**：
  Jiayin and Yimao belong to Great-Stream Water. Great-Stream Water is like torrents crashing against banks, waves startling the sky. Its surface is broad enough to contain the light of ten thousand miles and to reflect the green of countless mountains—majestic, swift, and expansive. This Water most enjoys "having a return and having nourishment": encountering the Kan position means having a place to return to; receiving clear Metal means having nurturance. When the day, month, or hour pillars contain Shen-You movements or Chen-Si winds, the stream tends toward drifting and restlessness. Meeting Well, Stream-Below, Heavenly-River, or Ocean Waters allows this urgency to be gathered into larger systems and become auspicious. Yet when Long-Flowing Water combines with strong winds, instability increases and is best avoided. Great-Stream Water requires refined Metal for support: Hairpin-Gold and Sand-Center Metal are most suitable, and Pewter-like Metal is also acceptable; but if Hairpin-Gold forms direct opposition, turbulence results. Sea-Center Metal on its own has little transforming effect here, though Jiazi at Kan and Yichou at Gen as return-to-source positions remain auspicious. Foil-Metal is too faint to nourish; Sword-Edge Metal can be transformed within Great-Stream Water, yet dreads Mao-thunder and Xun-wind, which indicate a volatile, unsettled temperament. Earth of all types generally harms this Water: Roof-Top and City-Top Earths dam and obstruct it; Roadside Earth can barely host its course but yields nothing extraordinary. Among Wall-Top Earths, only Xinchou acts as a mountain; within Grand-Post Earths, only Jiyou truly combines well, while Wushen clashes and Gengzi punishes, both inauspicious.

- **核心要点**：
  - 大溪水为大川急流之象，气势宏大而性急
  - 喜"有归有养"：遇坎为归、得清金为养
  - 可与井泉、涧下、天河、大海等水会合成吉，不喜长流水加风
  - 畏杂土壅阻与卯雷巽风过动，易致性情与人生轨迹飘荡不定

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_121]` `[trigger: 大溪水]` `[factor_trigger: jiayin_yimao AND daxi_shui]` `[role: 主干]` 大溪水者，惊涛薄岸，骇浪浮天，光涵万里之宽，碧倒千山之影，最喜有归有养，遇坎则为有归，得金则为有养。 → 《三命通会》卷一#大溪水

- **详细解说**：
  大溪水与涧下水、长流水的差异更多在于"尺度"与"归宿"：涧下水精细而隐、大溪水则张扬而显。急流若无归宿，便是单纯的冲刷与漂泊；因此原文强调"遇坎则为有归"、"得金则为有养"，意在指出：若命局中有稳定的地势（坎位）和清金（山石、器物、制度）承托，则大溪之势可被导入有序渠道，成为推动社会与个人发展的巨大动力。若反之，多土壅阻、多风多雷，便是"有势无统"，人易表现为性急、好动、不定、甚至多起多落。实务解读中，大溪水命若得清金、多水而少浊土，可看作"拥有大动能又有归处"；若清金不足而土多火杂，则偏向冲刷一切、本人与环境皆不安定之象。

- **校勘与字词辨析（双语）**：
  - **中文**："惊涛薄岸"形容水势冲击岸边；"有归有养"点出大溪水对归宿与养护的双重需求。
  - **English**: "Waves dashing against the banks" conveys the water’s force against shores; "having a return and having nourishment" emphasizes Great-Stream Water’s need for both destination and support."""
    normalized_text_zh: str = """"""
    subject: str = "大溪水：惊涛薄岸与归养之势"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate']
    
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
        l1_anchor="smth_v1.0.0_大溪水_惊涛薄岸与归养之势_001_L1",
    )
    version: str = "1.0.0"
