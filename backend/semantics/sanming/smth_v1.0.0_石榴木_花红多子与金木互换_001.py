"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228846
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
    semantic_id="smth_v1.0.0_石榴木_花红多子与金木互换_001",
    book_id="sanming",
    engine_id="bazi"
)
class 石榴木花红多子与金木互换(SemanticEntry):
    """
    - **原文（source_text）**：
  庚申辛酉，石榴木石榴木者，性辛如姜，花红似火，数颗枝头累累多子，房内莹莹。干支纯金，而纳音属木，乃木之变者也，可以移盆内而妆做山，故喜成器之土，以为根...
    """
    
    original_text: str = """- **原文（source_text）**：
  庚申辛酉，石榴木石榴木者，性辛如姜，花红似火，数颗枝头累累多子，房内莹莹。干支纯金，而纳音属木，乃木之变者也，可以移盆内而妆做山，故喜成器之土，以为根基。城头为上，屋上次之。然必阴阳交见，则丙辛、丁庚互官，戊辛巳寅互印，主吉。路壁、驿砂四土，有山助之，亦吉。若无何用，见金砂中最吉。泊金干支水木而纳音金，榴木干支金而纳音木，皆脱去本性，而互换归旺。以木旺寅卯，金旺申酉，各得其位，谓之功侔造化格，主大贵。海中乙丑为山，更逄水助则吉。或壁土城头，亦得剑锋就位相克，最凶。若先有砂金，能制其毒，亦不为害。水见天河，雨露相滋，井泉溪涧，清水浇灌大海，太泛滥，非贫则夭。有艮土，稍得太阳、霹雳二火，虽喜不宜并见。炉中寅卯旺位本吉，再加别火，则凶。若此木。生于五月日时，止带一火，谓之石榴喷火，主贵。桑柘、大林、杨柳三木皆喜见之。见桑柘，癸丑为山，见大林，戊辰脱体，见杨柳，花红柳绿，皆主功名。见松柏则强，见平地则大，若无别物夹杂，则缘绕红园，亦主富贵。如得城土为基，水运为助，享福优游，最为长久。

- **规范化释义（primary_lang_explained）**：
  庚申、辛酉为石榴木。石榴木性辛如姜、花红似火，枝头累累多子，象征多子多福与装饰性之美；其干支属金而纳音属木，是"木之变者"，兼具金、木两重性质，可移植盆中妆作假山，因此最喜"成器之土"为根基：城头土最佳，屋上土次之；路旁土、壁上土、大驿土等若有山相助亦可。局中阴阳干支若能互见，例如丙辛、丁庚互为官星、戊辛配巳寅互为印星，则主吉贵。若无其他依靠而仅见金，以砂中金为最吉。泊金干支属水木而纳音属金，石榴木干支属金而纳音属木，二者皆脱本性而互换归旺：木旺寅卯、金旺申酉，各得其位，名为"功侔造化格"，主大贵。海中乙丑可为山，再得清水相助亦吉。若城头土、壁上土遇剑锋金就位生克，则为重克，最凶；先有砂金可制其毒，则凶意减弱。水以天河为上，雨露相滋；井泉、溪涧清水可灌溉石榴，若水势过大如大海水，则多主贫夭。有艮土而稍见太阳火、霹雳火尚可，然不宜二火并见；炉中火在寅卯旺位本吉，再叠加他火则凶。若此木生于五月日时，仅带一火，名"石榴喷火"，主贵。桑柘、大林、杨柳三木皆喜见石榴：桑柘癸丑为山，大林戊辰为脱体，杨柳配之成花红柳绿之象，皆主功名。见松柏则格局更强，见平地则格局更大，若无杂物夹杂，乃"缘绕红园"之象，主富贵；更得城头土为基、水运为助，则享福优游而长久。

- **完整对等诠释（secondary_lang_full）**：
  Gengshen and Xinyou form the Pomegranate Wood pattern. It is pictured as a small but vivid tree whose flowers blaze red like fire and whose branches are weighted with many shining fruits, an image of beauty, display and fertility. Its stems and branches are pure Metal while its Nayin is Wood, so it behaves like a "transformed Wood" that carries both metallic sharpness and vegetal life. Rather than growing on raw ground it is often imagined as being planted in courtyards or pots and arranged as miniature hills, so it favours finished, architectural Earth as its base: City‑Top Earth is best, Roof‑Top Earth second, and other structural Earths such as Roadside, Wall‑Top and Grand‑Post can also help when supported by mountain configurations. When yin and yang stems meet properly—Bing with Xin and Ding with Geng forming official stars, Wu with Xin and Si with Yin forming seals—the pattern inclines toward rank and distinction. Among Metals, clean Sand‑Center Metal is most welcome. Foil‑Metal has Water‑Wood stems with Metal Nayin, while Pomegranate Wood has Metal stems with Wood Nayin; when each stands in its own prosperous place (Wood in Yin‑Mao, Metal in Shen‑You), they seem to exchange strength, forming the so‑called pattern "rivaling Creation itself", which points to very high status. Too much Sword‑Edge Metal cutting down from city walls or ramparts, by contrast, acts like demolition and is ominous unless earlier Sand‑Metal has already blunted the blade. As for Water, gentle Heavenly‑River rain and well or stream water moisten and polish the tree, whereas an excess of Ocean Water, though clear, tends to wash away roots and is linked with poverty or short life. Moderate Gen‑Earth together with a touch of Sunlight or Thunder‑Bolt Fire can bring out colour and brilliance, but piling many Fires on top of Furnace Fire in Yin‑Mao scorches rather than refines. When born around the fifth lunar month with only one well‑placed Fire, the image becomes that of a pomegranate tree suddenly bursting into flame‑coloured blossom, an emblem of distinguished talent. When Mulberry, Great‑Forest or Willow Woods appear around it, the picture is that of orchards and gardens framing the tree. Meeting Pine‑Cypress or Flat‑Earth Woods without extra clutter, it is like an estate encircled by red gardens—signalling wealth, honour and long‑enjoyed leisure, especially if City‑Top Earth forms the base and favourable water periods arrive to assist.

- **核心要点**：
  - 石榴木干支属金而纳音属木，为"木之变"，兼具金木双性
  - 喜城头、屋上等成器之土与砂金、泊金等清金为伴
  - 与泊金互换归旺，成"功侔造化格"主大贵
  - 忌剑锋金就位重克，须有砂金先制其毒；水以天河、井泉为佳，忌大海泛滥

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_112]` `[trigger: 石榴木]` `[factor_trigger: gengshen_xinyou AND shiliu_mu]` `[role: 主干]` 石榴木者，性辛如姜，花红似火，数颗枝头累累多子，房内莹莹。干支纯金，而纳音属木，乃木之变者也，可以移盆内而妆做山，故喜成器之土，以为根基。 → 《三命通会》卷一#石榴木

- **详细解说**：
  石榴木在纳音中极具特征：一方面，其花果累累象征多子多福与装饰性之美；另一方面，金干木纳音形成"变性"格局，与泊金构成干支与纳音互换的对照对。它不依原野之土，而依城头、屋上等"已成建筑之土"为基，故象偏向庭院、园林、宫苑中的观赏树。砂金与泊金则扮演"镶嵌、装饰、打磨"角色，使原本艳丽的石榴更具贵气；功侔造化格则强调，当金木各居旺地又相互成就时，其格局之高几乎可比天地造化本身。相对地，剑锋金在城头、壁上之上过度切削，则如拆城毁墙，对石榴本体造成过伤；只有砂金先在局中，方能中和其锋利。水火部分，则以天河与霹雳、太阳等组合，描绘雨露与雷光映照石榴花果的画面，但水火过度皆会把观赏格局推向凶险。

- **校勘与字词辨析（双语）**：
  - **中文**："功侔造化"意为功业与天地造化相匹，此处用以形容金木互换归旺之大贵格；"性辛如姜"强调石榴之辛辣刚烈特性。
  - **English**: "Equal-to-Creation" (Gong-Mou Zao-Hua) means achievements comparable to cosmic creation, used here for a highly noble configuration; "pungent like ginger" captures the sharp, intense character of Pomegranate Wood."""
    normalized_text_zh: str = """"""
    subject: str = "石榴木：花红多子与金木互换"
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
        l1_anchor="smth_v1.0.0_石榴木_花红多子与金木互换_001_L1",
    )
    version: str = "1.0.0"
