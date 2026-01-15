"""
Auto-generated semantic module for yuanhaiziping
Generated at: 2025-12-05T13:30:19.559529
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
    semantic_id="yhzp_v1.0.0_子平百章论科甲歌_001",
    book_id="yuanhaiziping",
    engine_id="bazi"
)
class 子平百章论科甲歌(SemanticEntry):
    """
    - **原文（source_text）**：  
  子平百章论科甲歌。  
  魁罡岁驾五经名，甲旺提纲榜眼清；火明木秀从魁印，金白水清甲第新。重叠玉堂登紫阁，调和木火贯黄金；木生春令逢伤食，甲宿文...
    """
    
    original_text: str = """- **原文（source_text）**：  
  子平百章论科甲歌。  
  魁罡岁驾五经名，甲旺提纲榜眼清；火明木秀从魁印，金白水清甲第新。重叠玉堂登紫阁，调和木火贯黄金；木生春令逢伤食，甲宿文场义理深。财印两轻官杀足，甲第连科一举成；根苗天乙俱榜眼，为魁木火定解英。相涵金水亲黄榜，递互丙丁侍紫宸；金水秋气炎方取，魁星官杀贵分明。杀重身轻休道弱，如逢印绶作魁星；谁知识此分高下，熟记犹如徐子平。

- **分字分词释义**：
  - **魁罡岁驾五经名**：魁罡配岁驾，主五经学问。
  - **甲旺提纲榜眼清**：甲木旺于月令，主榜眼清贵。
  - **火明木秀从魁印**：火明木秀配从魁印绶。
  - **金白水清甲第新**：金白水清格，主新科及第。
  - **财印两轻官杀足甲第连科一举成**：财印轻官杀足，一举连科。
  - **根苗天乙俱榜眼**：根苗天乙俱全，主榜眼。
  - **金水秋气炎方取**：金水秋生取炎方运。
  - **杀重身轻休道弱如逢印绶作魁星**：杀重身轻遇印绶可成魁星。
  - **谁知识此分高下熟记犹如徐子平**：识此高下需熟记如徐子平。
  - **木火通明调和贯黄金**：木火调和通明，主科甲贯金。
- **规范化释义（primary_lang_explained）**：  
  《子平百章论科甲歌》专论科举功名之命格与配置要点，以歌诀形式总结何种八字可中进士、榜眼、状元等科甲。**魁罡与岁驾**：魁罡岁驾配五经学问，甲木旺于提纲（月令）主榜眼清贵；火明木秀得从魁印绶，金白水清主甲第新科。**玉堂紫阁与调和**：重叠玉堂登紫阁要调和木火贯黄金，木生春令逢伤食主甲宿文场义理深厚。**财印官杀与榜眼**：财印两轻而官杀足者甲第连科一举成，根苗天乙俱全主榜眼，木火为魁者定解英才。**金水与魁星**：金水相涵亲黄榜，丙丁递互侍紫宸；金水秋气取炎方运，魁星配官杀贵分明。**印绶化杀成魁**：杀重身轻不为弱，如逢印绶可作魁星；识此高下分法，需熟记如徐子平。

- **完整对等诠释（secondary_lang_full）**：  
  **Song on Examination Honors in Hundred Chapters**: This section specifically treats fate configurations for imperial examination success (Jinshi, Bangyan, Zhuangyuan degrees) in verse form. **Kuigang and Year Post**: Kuigang combined with Year Post indicates mastery of Five Classics; Jia Wood strong at Month Command indicates Bangyan honor; bright Fire and elegant Wood with Congkui Seal; white Metal and clear Water bring new degree honors. **Jade Hall and Purple Pavilion**: Multiple Jade Halls ascending to Purple Pavilion requires harmonizing Wood and Fire penetrating Gold; Wood born in spring meeting Injury-Food indicates deep literary reasoning. **Wealth-Seal-Officer-Killing**: Light Wealth and Seal but sufficient Officer and Killing achieves consecutive degrees in one attempt; Root and Sprout both with Tianyi (Noble) indicates Bangyan; Wood and Fire as Kui Star determines distinguished talent. **Metal-Water and Kui Star**: Metal and Water mutually containing approaches the Yellow List; Bing and Ding alternating serves the Purple Palace; Metal and Water with autumn Qi taking Fire direction fortune; Kui Star with Officer and Killing shows clear nobility. **Seal transforms Killing into Kui**: Heavy Killing with light Body is not weak if meeting Seal, which can become Kui Star; understanding these distinctions requires mastery like Xu Ziping.

- **核心要点**：  
  - 以歌诀形式总结科举功名的八字配置（魁罡岁驾、官杀印绶、木火金水等）  
  - 强调特殊格局：魁罡格、从魁印格、金白水清格、木火通明格等  
  - 官杀配印绶可化煞为权成魁星，财印两轻而官杀足主连科及第  
  - 需识别季节与五行配合：春木秋金、金水炎方、木火调和等

- **详细解说**：  《子平百章论科甲歌》以歌诀形式专论科举功名之命格。**魁罡岁驾**——"魁罡岁驾五经名，甲旺提纲榜眼清"揭示魁罡与岁驾配合主科名。**五行清格**——"火明木秀从魁印，金白水清甲第新"揭示金白水清、木火通明等清格主科甲。**财印官杀**——"财印两轻官杀足，甲第连科一举成"；"根苗天乙俱榜眼，为魁木火定解英"阐述财印官杀与榜眼的配置。**金水魁星**——"相涵金水亲黄榜，递互丙丁侍紫宸"；"金水秋气炎方取，魁星官杀贵分明"揭示金水配魁星的科名之法。**印绶化杀**——"杀重身轻休道弱，如逢印绶作魁星"揭示杀重身轻遇印可成魁星。末句"谁知识此分高下，熟记犹如徐子平"点明需熟记子平之法。

- **叙事素材（narrative_snippets）**：
  - `[ns_yhzp_470]` `[trigger: 魁罡岁驾]` `[factor_trigger: kuigang_suijia_wujing AND jiawang_tigang_bangyan]` `[role: 主干]` 魁罡岁驾五经名；甲旺提纲榜眼清；魁罡配岁驾主科名。 → 《渊海子平·子平百章论科甲歌》
  - `[ns_yhzp_471]` `[trigger: 金白水清]` `[factor_trigger: huoming_muxiu_kuiyin AND jinbai_shuiqing_jiadi AND caiyin AND caiyin_qing_guansha_zu AND changyin AND jiadi]` `[role: 条件分支]` 火明木秀从魁印；金白水清甲第新；五行清格主科甲。 → 《渊海子平·子平百章论科甲歌》
  - `[ns_yhzp_472]` `[trigger: 财印官杀]` `[factor_trigger: caiyin_liangqing_guansha_zu AND jiadi_lianke AND tianyi_bangyan AND caiyin_qing_guansha_zu AND changyin AND genmiao_tianyi AND lianke]` `[role: 条件分支]` 财印两轻官杀足甲第连科一举成；根苗天乙俱榜眼。 → 《渊海子平·子平百章论科甲歌》
  - `[ns_yhzp_473]` `[trigger: 金水魁星]` `[factor_trigger: xianghan_jinshui_huangbang AND kuixing_guansha_guifen AND anchong_qugui AND angui]` `[role: 条件分支]` 相涵金水亲黄榜；金水秋气炎方取魁星官杀贵分明。 → 《渊海子平·子平百章论科甲歌》
  - `[ns_yhzp_474]` `[trigger: 杀化为魁]` `[factor_trigger: shazhong_shenqing AND feng_yinshou_zuokuixing AND caiyin AND caiyin_qing_guansha_zu AND changyin]` `[role: 条件分支]` 杀重身轻休道弱如逢印绶作魁星；印绶化杀成魁。 → 《渊海子平·子平百章论科甲歌》
  - `[ns_yhzp_475]` `[trigger: 木火调和]` `[factor_trigger: yutang_deng_zige AND muho_tiaohe_huangjin AND muhuo_tongming]` `[role: 条件分支]` 重叠玉堂登紫阁调和木火贯黄金；木火通明主科名。 → 《渊海子平·子平百章论科甲歌》
  - `[ns_yhzp_476]` `[trigger: 熟记子平]` `[factor_trigger: shuji_xu_ziping AND kejia_panduan_ziping_fa]` `[role: 总结]` 谁知识此分高下熟记犹如徐子平；科甲判断需熟记子平法。 → 《渊海子平·子平百章论科甲歌》"""
    normalized_text_zh: str = """"""
    subject: str = "子平百章论科甲歌"
    factor_refs: list = ['examination_honors', 'kuigang_year_post', 'congkui_seal', 'wood_fire_illumination', 'killing_seal_kui']
    
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
        book_id="yuanhaiziping",
        chapter="",
        l1_anchor="yhzp_v1.0.0_子平百章论科甲歌_001_L1",
    )
    version: str = "1.0.0"
