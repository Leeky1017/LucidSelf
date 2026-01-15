"""
Auto-generated semantic module for zipingzhenquan
Generated at: 2025-12-05T13:30:19.523469
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
    semantic_id="zpzq_v1.0.0_有是五行_何以又有十干十二支乎_001",
    book_id="zipingzhenquan",
    engine_id="bazi"
)
class 有是五行何以又有十干十二支乎(SemanticEntry):
    """
    - **原文（source_text）**：
  有是五行，何以又有十干十二支乎？盖有阴阳，因生五行，而五行之中，各有阴阳。即以木论，甲乙者，木之阴阳也。甲者，乙之气；乙者，甲之质。在天为生气，而流行...
    """
    
    original_text: str = """- **原文（source_text）**：
  有是五行，何以又有十干十二支乎？盖有阴阳，因生五行，而五行之中，各有阴阳。即以木论，甲乙者，木之阴阳也。甲者，乙之气；乙者，甲之质。在天为生气，而流行于万物者，甲也；在地为万物，而承兹生气者，乙也。又细分之，生气之散布者，甲之甲，而生气之凝成者，甲之乙；万木之所以有枝叶者，乙之甲，而万木之枝枝叶叶者，乙之乙也。方其为甲，而乙之气已备；及其为乙，而甲之质乃坚。有是甲乙，而木之阴阳具矣。

- 原注（原文注解）：
  　　此段由“五行”进而解释“十干”的必要性，以甲乙为例，示干之阴阳与气质、流行与承载之别，原书无单列夹注。

- 分字分词释义：
  - 十干十二支：十天干与十二地支，是在五行基础上进一步细分阴阳与时空的位置系统。
  - 因生五行：有阴阳，因之而生五行，先有“二”再有“五”。
  - 五行之中各有阴阳：每一行之内再分阴干与阳干，如木有甲乙。

- **规范化释义（primary_lang_explained）**：
  既然有五行，为何还要十干十二支？因为有阴阳，才生出五行；而五行之中，各自又有阴阳之分。以木为例，甲乙就是木的阴阳两面。甲是乙的气，乙是甲的质。在天为生气、流行于万物的是甲；在地为万物、承载这生气的是乙。更细分之，生气散布者是"甲之甲"，生气凝成者是"甲之乙"；万木之所以有枝叶是"乙之甲"，枝枝叶叶本身是"乙之乙"。当其为甲时，乙之气已蕴其中；及其为乙时，甲之质方显坚实。有了甲乙，木之阴阳便完备了。

- **完整对等诠释（secondary_lang_full）**：
  Given that there are Five Elements, why do we also need Ten Heavenly Stems and Twelve Earthly Branches? It is because Yin-Yang gives birth to the Five Elements, and within each Element there exists its own Yin-Yang polarity. Taking Wood as an example: Jia and Yi represent the Yang and Yin aspects of Wood. Jia is the Qi (vital energy) of Yi; Yi is the substance (Zhi) of Jia. In heaven, as the generative force flowing through all things, it is Jia; on earth, as the myriad forms that receive this vitality, it is Yi. Further subdivision shows: the dispersing aspect of Jia is "Jia within Jia," while the condensing aspect is "Yi within Jia"; the reason trees have branches and leaves is "Jia within Yi," while the branches and leaves themselves are "Yi within Yi." When it manifests as Jia, the Qi of Yi is already prepared within; when it becomes Yi, the substance of Jia has solidified. With Jia and Yi complete, the Yin-Yang of Wood is fully established.

- **详细解说**：
  本段以甲乙二木为例，揭示十干存在的必要性：五行只是粗分，十干才是精分。每一行内部再分阴阳，阳干主"气"、阴干主"质"，前者偏于流行发散，后者偏于承载凝聚。甲木为阳，代表生气在天、条达上行；乙木为阴，代表形质在地、枝叶承载。更进一步，甲中有甲乙（散布与凝成），乙中亦有甲乙（枝干与叶末），层层嵌套，说明阴阳之理无处不在。由此推及丙丁、戊己、庚辛、壬癸，皆可类比：阳干主象、阴干主形；阳干主发、阴干主收。这是全书论十神、论格局的基础逻辑之一。

- 应用推演：
  1) 判行：先定日主属哪一行（木火土金水）。
  2) 判阴阳：再看是阳干还是阴干（如甲/乙、丙/丁等）。
  3) 判气质倾向：结合时令、格局与用神，判断此干更侧重“气”的流行，还是“质”的形成与承担。
  4) 推及他行：由甲乙之例，触类旁通到丙丁、戊己、庚辛、壬癸的不同侧面。

- 反例与边界：
  - 只说“甲乙皆木”，不顾阴阳与气质之差，容易把许多干支组合看成“同一类”，失去辨证能力。
  - 把“气”与“质”理解成抽象形容，而不落实到“在天为象、在地为形”的实际判断上，会失去本段的精华。

- 小例（示意）：
  - 同为木旺之局，甲木偏重“气势”与上达，适合作“纲纪、方向”之象；乙木偏重“具体枝叶”，适合作“执行、细节、关系”之象。

- 校勘与字词辨析（双语）：
  - **中文**：本段文字在各本之间差异不大，“甲之甲、甲之乙、乙之甲、乙之乙”等句式虽不常见，但结构清楚，今仍从今本，不作改动，仅在注中加以解释。
  - **English**: This paragraph shows little variation across editions. The fourfold expressions "Jia within Jia", "Yi within Jia", "Jia within Yi" and "Yi within Yi" are unusual but structurally clear, so this edition keeps the received wording and explains the meaning in the commentary rather than emending the text.

- **叙事素材（narrative_snippets）**：
 - **叙事素材（narrative_snippets）**：
  - `[ns_zpzy_072]` `[trigger: 十干必要性]` `[factor_trigger: wuxing_nei_fen_yinyang AND tiangan_count=10]` `[role: 主干]` 五行之中各有阴阳，故有十干。 → 《子平真诠·论十干十二支》#十干由来
  - `[ns_zpzy_073]` `[trigger: 甲木特性]` `[factor_trigger: stem=jia AND role=yi_zhi_qi AND location=zaitian AND function=shengqi_liuxing]` `[role: 主干依赖]` 甲者乙之气，在天为生气，流行于万物。 → 《子平真诠·论十干十二支》#甲木
  - `[ns_zpzy_074]` `[trigger: 乙木特性]` `[factor_trigger: stem=yi AND role=jia_zhi_zhi AND location=zaidi AND function=cheng_shengqi]` `[role: 主干依赖]` 乙者甲之质，在地为万物，承兹生气。 → 《子平真诠·论十干十二支》#乙木
  - `[ns_zpzy_075]` `[trigger: 气质分辨]` `[factor_trigger: (stem=jia AND yi_qi_yibei) OR (stem=yi AND jia_zhi_naijian)]` `[role: 总结]` 方其为甲而乙之气已备，及其为乙而甲之质乃坚。 → 《子平真诠·论十干十二支》#气质互含
  - `[ns_zpzy_076]` `[trigger: 干支阴阳]` `[factor_trigger: lunming_rigan AND check_wuxing AND check_yinyang AND check_qizhi]` `[role: 主干依赖]` 论日干不仅看属何行，还要看属阴属阳、偏气偏质。 → 《子平真诠·论十干十二支》#方法论
  - `[ns_zpzy_077]` `[trigger: 天干地支]` `[factor_trigger: tiangan_dizhi AND yinyang_xiang]` `[role: 主干依赖]` 天干地支，阴阳之象也。 → 《子平真诠》#论十干十二支
  - `[ns_zpzy_078]` `[trigger: 干支配合]` `[factor_trigger: ganzhi_peihe AND shengke_zhihua_li]` `[role: 主干依赖]` 干支配合，生克制化之理。 → 《子平真诠》#论十干十二支
  - `[ns_zpzy_079]` `[trigger: 甲乙属木]` `[factor_trigger: (jiayi=mu) AND (bingding=huo) AND (wuji=tu) AND (gengxin=jin) AND (rengui=shui)]` `[role: 主干依赖]` 甲乙属木，丙丁属火，戊己属土，庚辛属金，壬癸属水。 → 《子平真诠》#论十干十二支
  - `[ns_zpzy_080]` `[trigger: 冬水用事]` `[factor_trigger: season=dong AND shui_yongshi AND shui_wang_mu_xiang]` `[role: 条件分支]` 冬水用事，水旺木相。 → 《子平真诠》#上卷
  - `[ns_zpzy_081]` `[trigger: 四季土旺]` `[factor_trigger: season=siji AND tu_wang AND tu_wang_jin_xiang]` `[role: 条件分支]` 四季土旺，土旺金相。 → 《子平真诠》#上卷
  - `[ns_zpzy_082]` `[trigger: 假神无力]` `[factor_trigger: jiashen_exists AND strength=wuli AND geju=hunza]` `[role: 条件分支]` 假神无力，格局混杂。 → 《子平真诠》#上卷
  - `[ns_zpzy_083]` `[trigger: 清气为上]` `[factor_trigger: qingqi_weishang AND zhuoqi_weixia]` `[role: 总结]` 清气为上，浊气为下。 → 《子平真诠》#上卷
  - `[ns_zpzy_084]` `[trigger: 纯粹可贵]` `[factor_trigger: chuncui_kegui AND zaluan_bukan]` `[role: 总结]` 纯粹可贵，杂乱不堪。 → 《子平真诠》#上卷
  - `[ns_zpzy_085]` `[trigger: 寒暖燥湿]` `[factor_trigger: condition IN (han, nuan, zao, shi) AND tiaohou_weixian]` `[role: 主干依赖]` 寒暖燥湿，调候为先。 → 《子平真诠》#上卷
  - `[ns_zpzy_086]` `[trigger: 喜神来助]` `[factor_trigger: xishen_laizhu AND result=shishi_shunsui]` `[role: 条件分支]` 喜神来助，事事顺遂。 → 《子平真诠》#上卷
  - `[ns_zpzy_087]` `[trigger: 天干主动]` `[factor_trigger: tiangan_zhudong AND ying_su_er_xian]` `[role: 条件分支]` 天干主动，应速而显。 → 《子平真诠》#上卷"""
    normalized_text_zh: str = """"""
    subject: str = "有是五行，何以又有十干十二支乎？"
    factor_refs: list = ['tiangan', 'qi_energy', 'zhi_substance', 'zai_tian', 'zai_di', 'jia_wood', 'yi_wood']
    
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
        book_id="zipingzhenquan",
        chapter="",
        l1_anchor="zpzq_v1.0.0_有是五行_何以又有十干十二支乎_001_L1",
    )
    version: str = "1.0.0"
