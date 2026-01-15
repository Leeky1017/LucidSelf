"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.080901
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
    semantic_id="smth_v1.0.0_1_官煞刃印的贵格_001",
    book_id="sanming",
    engine_id="bazi"
)
class 1官煞刃印的贵格(SemanticEntry):
    """
    - 原文（source_text）：
  官星带刃，无克破，掌兵刑之大权。财印相资，没刑冲，登黄阁三公之贵。
  财官生旺逢印绶，拜薇垣宪府之尊；三合印财会局全，登五马诸侯之贵。
  伤官逢煞刃，兼将...
    """
    
    original_text: str = """- 原文（source_text）：
  官星带刃，无克破，掌兵刑之大权。财印相资，没刑冲，登黄阁三公之贵。
  财官生旺逢印绶，拜薇垣宪府之尊；三合印财会局全，登五马诸侯之贵。
  伤官逢煞刃，兼将相于明时；印绶若相扶，登龙门于早岁。
  伤官得食神重辅，麟阁图魏相之功；岁运忌制伏刑冲，再伤官而祸至。
  财资七煞，威权独压万人；印若相扶，断定官居极品。
  月会既同煞刃，英名俦汉室之霍光；时岁复带印财，高位埒中兴之邓禹。
  煞失时而印无气，更主旺而任常流。
  印司令而煞相扶，再见财而官翰苑。

- 分字分词释义：
  - **官星带刃**：正官格配羊刃（如甲日辛官乙刃），刚柔相济。
  - **财印相资**：财不坏印，互为喜用（如身旺印轻，财星滋煞生印？不，应是财官印顺生，或印赖煞生，财资煞）。
  - **伤官煞刃**：伤官制煞，羊刃帮身。
  - **财资七煞**：财生煞，煞生印，印生身（或身强煞浅，财生煞）。

- 规范化释义（primary_lang_explained）：  
  本节真宝赋专门讲“官、煞、刃、印、财”几大要素如何组合成真正的大贵之格。首句“官星带刃，无克破，掌兵刑之大权”，点明最典型的一种结构：以正官为名分、以羊刃为权力的锋刃，二者同宫而无刑冲破害，命主便有机会掌管军旅与刑狱等高风险职务。若再有财星与印绶相生相资，使得“财官印”气脉贯通，不但身不受损，反而能借外界资源不断放大官星的效力，于是便有“登黄阁三公之贵”“拜薇垣宪府之尊”的层级出现；若三合印局、财局完备，则更上一层楼，入诸侯、藩辅之列。  
  伤官、七煞与羊刃的组合，则是另一条出将入相之路。单纯的伤官见官，多主忤逆犯上，但在这里，伤官一方面制约七煞的凶暴，一方面又在羊刃帮身之下，将日主的主观能动性与煞刃的决断力打通——于是“伤官逢煞刃”可以“兼将相于明时”，加上印绶相扶，更容易早年登科、入翰苑。财星资助七煞（财滋煞）、煞印相生时，则形成以财富喂养权力、以压力淬炼名望的闭环：身旺而煞有用，才有“威权独压万人”“官居极品”的可能。反之，若七煞失时、印绶无气，即便日主一身旺气，也不过是“身旺无依”的常流之人；只有在印绶司令、七煞相扶、再得财星推波助澜时，这股力量才会落在具体的官职与文名上，而不是停留在锋芒毕露的潜势中。  

- 完整对等诠释（secondary_lang_full）：  
  This section of the "True Treasure" ode focuses on how Direct Officer, Seven Killings, Yang Blade, Seals and Wealth must interlock to produce truly exalted patterns. The opening formula, "Officer star accompanied by Blade, with no clashes or breaks, commands great power over arms and punishment," defines a flagship structure: Officer provides legitimacy and position, while Blade supplies courage and the willingness to act decisively. When the two occupy the same space without being damaged, the chart can carry military or judicial authority. If, on top of this, Wealth and Seals mutually nourish one another—resources feeding power, and moral capital protecting the self—then the channel linking Wealth, Officer and Seal becomes continuous. Such configurations justify phrases like "ascending to the Yellow Pavilion as one of the Three Excellencies" or joining the highest censorial courts; when full trines of Seal or Wealth are present, the person rises even further, into ducal or princely ranks.  
  Configurations built around Wounded Officer, Seven Killings and Blade provide another route to greatness. Ordinarily, a strong Wounded Officer clashing with Officer signifies insubordination and trouble, but here the text describes a case in which Wounded Officer restrains Killings, Blade strengthens the self, and Seals later come in to legitimise and refine this raw edge. In such a pattern, the same rebellious force that might have caused ruin becomes the very thing that allows someone to "command armies and serve as minister." Wealth feeding Killings and Killings feeding Seals form a loop in which material support, harsh responsibility and reputation reinforce one another; only when the Day Master is strong enough, and when these flows are coherent rather than chaotic, can the chart bear "power that suppresses ten‑thousand men" and "the highest offices." When Killings are mistimed, Seals drained of qi or the supporting cycles hostile, the pattern collapses back into that of a capable but ordinary person. Only when timing, structure and support all cooperate does the configuration crystallise into the sort of realised talent that later generations praise as a "true treasure".  

- 核心要点：
  - **官刃双全**：权柄。
  - **财印互用**：贵。
  - **伤官驾杀**：大贵。
  - **财滋煞**：身旺为贵。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_12_009]` `[trigger: 官星带刃]` `[factor_trigger: guanxing_dairen AND zhangbingxing_daquan]` `[role: 主干]` 官星带刃，无克破，掌兵刑之大权。财印相资，没刑冲，登黄阁三公之贵。 → 《三命通会》卷十二#官煞刃印的贵格
  - `[ns_smth_12_010]` `[trigger: 伤官煞刃]` `[factor_trigger: shangguan_sharen AND jiangxiang_mingshi]` `[role: 主干依赖]` 伤官逢煞刃，兼将相于明时；印绶若相扶，登龙门于早岁。 → 《三命通会》卷十二#官煞刃印的贵格
  - `[ns_smth_12_011]` `[trigger: 财资七煞]` `[factor_trigger: caizi_qisha AND weiquan_yawanren]` `[role: 条件分支]` 财资七煞，威权独压万人；印若相扶，断定官居极品。 → 《三命通会》卷十二#官煞刃印的贵格
  - `[ns_smth_12_012]` `[trigger: 煞失时印无气]` `[factor_trigger: sha_shishi AND yin_wuqi]` `[role: 总结]` 煞失时而印无气，更主旺而任常流。 → 《三命通会》卷十二#官煞刃印的贵格"""
    normalized_text_zh: str = """"""
    subject: str = "1 官煞刃印的贵格"
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
        book_id="sanming",
        chapter="",
        l1_anchor="smth_v1.0.0_1_官煞刃印的贵格_001_L1",
    )
    version: str = "1.0.0"
