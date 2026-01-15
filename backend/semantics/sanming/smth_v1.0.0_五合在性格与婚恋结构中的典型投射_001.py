"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.264394
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
    semantic_id="smth_v1.0.0_五合在性格与婚恋结构中的典型投射_001",
    book_id="sanming",
    engine_id="bazi"
)
class 五合在性格与婚恋结构中的典型投射(SemanticEntry):
    """
    - **原文（source_text）**：  
  甲与己何名为中正之合？甲，阳木也，其性仁，位处十干之首，己阴土也，镇静淳笃，有生物之德，故甲己为中正之合。带此合，主人尊崇重大，宽厚平直。如带煞而...
    """
    
    original_text: str = """- **原文（source_text）**：  
  甲与己何名为中正之合？甲，阳木也，其性仁，位处十干之首，己阴土也，镇静淳笃，有生物之德，故甲己为中正之合。带此合，主人尊崇重大，宽厚平直。如带煞而五行无气，则多嗔好怒，性梗不可屈。乙与庚何名为仁义之合？乙，阴木也，其性仁而太柔；庚，阳金也，坚强不屈，则刚柔相济，仁义兼资，故主人果敢有守，不惑柔佞。周旋惟仁，进退惟义。五行生旺，则骨秀形清。若死绝带煞，则使气好勇，体貌不扬，自是非人。甲己乙庚之合，妇人不忌。丙与辛何名为威制之合？丙，阳火也，𪸩赫自盛；辛，阴金也，克刃喜煞，故丙辛为威制之合，主人仪表威肃，人多畏惧酷毒，好贿喜淫。若带煞或五行死绝，则寡恩少义，无情之人，妇人得之，与天中大耗咸池相并者，貌美声卑，三合夭冶而淫。丁与壬何名为淫慝之合？壬者纯阴之水，三光不照；丁者藏阴之火，自昧不明，故丁壬为淫慝之合，主人眼明神娇，多情易动，不事高洁，习下无志，躭欢姻色，于我则吝，于彼则贪。若五行死绝，或带煞，见咸池大耗，天中自败，有淫污家风之丑。亲厚小人，侮慢君子，贪婪妄作，必胜而后已。妇人淫邪奸慝，易挑易诱，多招玷辱。戊与癸何名为无情之合？戌阳土也，是老丑之夫；癸，阴水也，是婆娑之妇。老阳而少阴，虽合而无情，主人或好或丑。如戊得癸，则娇媚有神，姿美得所，子娶少妇，妇人嫁美夫。若癸得戊，则形容古朴，老相俗尘，男子娶老妻，妇人嫁老夫。

- **规范化释义（primary_lang_explained）**：  
  本段集中描述五组干合在性格、人际与婚恋层面的典型倾向。甲己为“中正之合”：甲木仁而在首，象勇于担当与发端；己土阴而厚重，有承载生养之德，二者相配，多主人格端正、宽厚平直、受人尊崇。但若命局本身无气又兼煞重，则中正易变为固执与暴躁。乙庚为“仁义之合”：乙木性仁而太柔，庚金刚健不屈，两者相济，形成“以仁行事、以义立身”的格局，身旺有气时，多见骨相清秀、性格果决；若落死绝又带煞，则可能演化为好勇使气。甲己、乙庚一类，在古书中特别说明“妇人不忌”，意在强调其对女命并不构成特殊不利。丙辛为“威制之合”：丙火炽盛、辛金锐利，合则成权威与控制之象，主人仪表严肃，能以威势制物；若再逢煞重或五行死绝，则易变为寡恩少义，甚至酷烈好淫。丁壬为“淫慝之合”：丁火幽暗、壬水阴柔，组合倾向情欲易动、志趣不高，若又与咸池、大耗等桃花、耗散之煞同宫，则尤见沉溺声色、家风不洁。戊癸为“无情之合”：戊土如老夫、癸水如少妇，象征年龄或身份悬殊的人际与婚姻结构，形式上虽成合，而情感难以平衡；然而若“戊得癸”，也可能表现为“老来得伴、少配美偶”等特殊配置。

- **完整对等诠释（secondary_lang_full）**：  
  This long paragraph profiles the five canonical stem combinations in terms of character, relationships and especially marriage patterns. Jia‑Ji is described as the "upright and balanced" union: Jia, a Yang Wood at the head of the stems, embodies benevolent initiative, while Ji, a Yin Earth, is steady and nurturing. Their combination points to dignity, fairness and reliability, though in charts lacking qi and laden with malefic stars this balance can sour into stubborn anger. Yi‑Geng is called the "benevolence and righteousness" union: Yi is kind but overly soft, Geng is firm and unyielding; together they weave compassion with moral backbone, yielding people who act kindly yet hold firm principles—unless the stems lie in dead or afflicted positions, in which case courage turns into rashness. These two unions are explicitly said not to be taboo in women's charts. Bing‑Xin is the "awe‑inspiring control" union: blazing Bing Fire and sharp Xin Metal create an image of authority and severity, producing people who command respect but may incline toward harshness, greed or sensuality, especially when accompanied by heavy killing stars. Ding‑Ren is the "licentious" union: dim Ding Fire and shadowy Ren Water incline toward emotional entanglement, heightened sensuality and a lack of lofty aspiration; when reinforced by Peach Blossom (Xianchi) and loss‑type stars, it can manifest as scandal and moral compromise. Wu‑Gui is the "heartless" union: coarse, aging Wu Earth paired with delicate Gui Water symbolizes mismatched couples and relationships in which affection is weak despite formal ties, often involving large age or status gaps; yet depending on which side "obtains" the other, it may also describe unions where physical attraction and social benefit coincide. The passage is strongly moralized in Confucian language but can be read structurally as mapping how these stem pairings colour temperament and intimacy.

- **核心要点**：
  - 甲己、乙庚、丙辛、丁壬、戊癸五合在性格、权力感、情欲与婚恋结构上各有典型画像。
  - 同一合象在“生旺有气”与“死绝带煞”时，可呈现从高尚、中正到失衡、放纵的一整条谱系。
  - 女命对丁壬、戊癸一类合象尤为敏感，常牵涉婚恋结构、年龄差与声誉风险。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_10_113]` `[trigger: 中正之合]` `[factor_trigger: zhongzheng_zhihe AND jiaji_kuanhou]` `[role: 主干]` 甲与己何名为中正之合？甲，阳木也，其性仁，位处十干之首，己阴土也，镇静淳笃。 → 《三命通会》卷十#五合在性格与婚恋结构中的典型投射
  - `[ns_smth_10_114]` `[trigger: 仁义之合]` `[factor_trigger: renyi_zhihe AND yigeng_gangrou]` `[role: 主干依赖]` 乙与庚何名为仁义之合？乙，阴木也，其性仁而太柔；庚，阳金也，坚强不屈，则刚柔相济。 → 《三命通会》卷十#五合在性格与婚恋结构中的典型投射
  - `[ns_smth_10_115]` `[trigger: 淫慝之合]` `[factor_trigger: yinni_zhihe AND dingren_duoqing]` `[role: 条件分支]` 丁与壬何名为淫慝之合？壬者纯阴之水，三光不照；丁者藏阴之火，自昧不明。 → 《三命通会》卷十#五合在性格与婚恋结构中的典型投射
  - `[ns_smth_10_116]` `[trigger: 无情之合]` `[factor_trigger: wuqing_zhihe AND wugui_laoshao]` `[role: 总结]` 戊与癸何名为无情之合？戊阳土也，是老丑之夫；癸，阴水也，是婆娑之妇。 → 《三命通会》卷十#五合在性格与婚恋结构中的典型投射

- **详细解说**：  
  若抛开古文中强烈的道德批判，这段其实是在提供一套“人格与关系模式的组合模板”：甲己偏向稳重中正的领导与承载；乙庚偏向温厚中有刚骨的“仁义之士”；丙辛偏向带压迫感的权力与控制；丁壬偏向情绪与欲望容易被触发的敏感体质；戊癸则偏向“形式搭配成功、情感难以对等”的关系结构。工程化使用时，可将“五合”拆成两层因子：一层是中性的性格与关系特征（中正、仁义、威制、情欲强度、年龄/权力差等），另一层则是当五行处于死绝、并与咸池、大耗等煞同宫时的风险权重（例如沉溺声色、婚恋失衡、名誉危机等），避免把“淫慝”“无情”之类词语原样照搬到现代判词中。

- **校勘与字词辨析（双语）**：
  - **中文**：“淫慝”“无情”在原文中带有浓重的父权道德色彩，本精校在释义部分尽量拆解为“情欲过强”“情感失衡”等结构性描述，在详细解说中再补充现代语境下的理解方式。
  - **English**: Terms like "lewd" or "heartless" reflect historical moral judgement. In contemporary practice, they can be reframed as pointers to heightened desire, asymmetry in reciprocity, or challenging relational dynamics rather than fixed moral verdicts."""
    normalized_text_zh: str = """"""
    subject: str = "五合在性格与婚恋结构中的典型投射"
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
        l1_anchor="smth_v1.0.0_五合在性格与婚恋结构中的典型投射_001_L1",
    )
    version: str = "1.0.0"
