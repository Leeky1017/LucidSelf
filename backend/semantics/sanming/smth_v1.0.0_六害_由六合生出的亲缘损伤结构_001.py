"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.264466
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
    semantic_id="smth_v1.0.0_六害_由六合生出的亲缘损伤结构_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六害由六合生出的亲缘损伤结构(SemanticEntry):
    """
    - **原文（source_text）**：  
  论六害，因昼夜阴阳之气感而六合，因六合而生六害，因六害而忌昼夜阴阳之气。六害者，十二支凌战之辰也。子未相害者，谓未旺土害子旺水，名势家相害，故子见...
    """
    
    original_text: str = """- **原文（source_text）**：  
  论六害，因昼夜阴阳之气感而六合，因六合而生六害，因六害而忌昼夜阴阳之气。六害者，十二支凌战之辰也。子未相害者，谓未旺土害子旺水，名势家相害，故子见未则为害。丑午相害者，谓午以旺火凌丑死金，名官鬼相害，故丑见午，而午更带丑干之真鬼，则为害尤甚。寅巳相害者，谓各恃临官擅能而进相害，若干神往来有鬼者尤甚。况刑在其中，尤不可不加减灾福言之。卯辰相害者，谓卯以旺木凌辰死土，此以少凌长相害，故辰见卯，而卯更带辰干真鬼，则其害尤甚。申亥相害者，谓各恃临官竞嫉才能，争进相害，故申见亥，亥见申，均为害。更纳音相克者重。酉戌相害者，谓戌以死火害酉旺金，此嫉妒相害，故酉人见戌则凶，戌人见酉无灾。若乙酉人得戊戌，乙为真金，戊为真火，为害尤甚。又云：六亲害，损也。犯之，主六亲上有损克，故谓六害……凡六害入命，大率主妨害孤独，骨肉参商，财帛澹泊，女命尤忌。

- **规范化释义（primary_lang_explained）**：  
  六害被定义为“因六合而生”的一组地支相害：子未、丑午、寅巳、卯辰、申亥、酉戌。它们本源于昼夜阴阳之气感应形成的六合结构，但因力量失衡或角色冲突，反而从和生害。作者分别以“势家相害”（未土压迫子水），“官鬼相害”（午火凌丑金），“恃能相害”（寅巳、申亥），“少凌长相害”（卯辰），“嫉妒相害”（酉戌）等标签，指出其中的社会与心理意涵：有的是资源过度集中一方，有的是权力与责任错配，有的是互相妒忌、争进不让。若再叠加纳音相克与真鬼（官杀）同临，六害的破坏力大增，多应在六亲关系破损、骨肉参商、财帛不聚与晚年孤独等领域。女命带六害，古书尤为忌讳，常以婚姻、子息与家庭支持系统为主要受害点。

- **完整对等诠释（secondary_lang_full）**：  
  This section frames the Six Harms as the shadow side of the Six Harmonies: configurations that arise from the same Yin‑Yang resonance but turn sour due to imbalance. Each harming pair is given a thematic label: Zi‑Wei embodies "status‑based harm" in which powerful Earth overwhelms vulnerable Water; Chou‑Wu is "official‑ghost harm," where blazing Fire oppresses dead Metal; Yin‑Si and Shen‑Hai are cases of "talent‑driven rivalry," where both parties cling to their own authority; Mao‑Chen represents "the young attacking the elder"; You‑Xu stands for "jealous harm." In practice, the text warns that when these pairs appear prominently in a chart—especially together with hostile na‑yin, active killing stars or being involved with the spouses' or parents' palaces—they often correspond to damaged family ties, conflict among siblings, marital strain and financial leakage. Importantly, the harms are not uniform: sometimes the harm is unilateral (as with You harmed by Xu but not vice versa), reflecting asymmetric vulnerability. Interpreted structurally, Liu Hai marks relationship patterns where complementarity has collapsed into competition, and where the very ties that should support one another instead erode trust and resources.

  - 六害为六合的反面，是在阴阳感应基础上“由和转害”的六组支对。
  - 每一组都有特定的社会—心理主题：势压、官鬼、妒忌、少凌长等。
  - 命带六害通常指向六亲关系损伤、资源流失与心理上难以信赖他人。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_10_149]` `[trigger: 六合生六害]` `[factor_trigger: liuhe_sheng_liuhai AND yinyang_ganying]` `[role: 主干]` 因昼夜阴阳之气感而六合，因六合而生六害，因六害而忌昼夜阴阳之气。 → 《三命通会》卷十#六害
  - `[ns_smth_10_150]` `[trigger: 势家相害]` `[factor_trigger: shijia_xianghai AND weitu_haizi]` `[role: 主干依赖]` 子未相害者，谓未旺土害子旺水，名势家相害。 → 《三命通会》卷十#六害
  - `[ns_smth_10_151]` `[trigger: 嫉妒相害]` `[factor_trigger: jidu_xianghai AND youxu_danfang]` `[role: 条件分支]` 酉戌相害者，谓戌以死火害酉旺金，此嫉妒相害，故酉人见戌则凶，戌人见酉无灾。 → 《三命通会》卷十#六害
  - `[ns_smth_10_152]` `[trigger: 六亲损克]` `[factor_trigger: liuqin_sunke AND gurou_canshang]` `[role: 总结]` 六亲害，损也。犯之，主六亲上有损克，故谓六害。 → 《三命通会》卷十#六害

- **详细解说**：  
  在建模时，可以将六合与六害视作一组"正负因子"”：六合强调协同与互补，六害则标记协同失败与角色错位。对于具体支对，可引入方向性：如酉遇戌为“受害方”，戌遇酉则几乎无事；子遇未被土压，未遇子则多为“顾虑或压力源”而非被害者本身。这样既尊重古文中“谁见谁为害”的差异，又便于在算法上细分影响路径。在解读时，不宜简单断“六害必凶”，而应看其是否落在命宫、夫妻、父母、子女等关键宫位，以及是否得到官印、贵人等调和；否则容易把天然的紧张关系放大成宿命式诅咒。

- **校勘与字词辨析（双语）**：
  - **中文**：“六亲害，损也”一句，将六害与六亲损伤直接相连，本精校在释义中强调其为“风险倾向，而非必然结果”。
  - **English**: The term "harm" here covers a spectrum from tension and distance to outright breakage; it should not be read as guaranteeing tragedy but as highlighting relational stress points."""
    normalized_text_zh: str = """"""
    subject: str = "六害：由六合生出的亲缘损伤结构"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate']
    
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
        l1_anchor="smth_v1.0.0_六害_由六合生出的亲缘损伤结构_001_L1",
    )
    version: str = "1.0.0"
