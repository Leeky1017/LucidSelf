"""
Auto-generated semantic module for yuanhaiziping
Generated at: 2025-12-05T13:30:19.558644
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
    semantic_id="yhzp_v1.0.0_又地支藏遁歌_001",
    book_id="yuanhaiziping",
    engine_id="bazi"
)
class 又地支藏遁歌(SemanticEntry):
    """
    - **原文（source_text）**：  
  子宫癸水在其中，丑癸辛金己土同；寅宫甲木兼丙戊，卯宫乙木独相逢。辰藏乙戊三分癸，巳中庚金丙戊丛；午宫丁火并己土，未宫乙己丁共宗。申位庚金壬水戊，酉...
    """
    
    original_text: str = """- **原文（source_text）**：  
  子宫癸水在其中，丑癸辛金己土同；寅宫甲木兼丙戊，卯宫乙木独相逢。辰藏乙戊三分癸，巳中庚金丙戊丛；午宫丁火并己土，未宫乙己丁共宗。申位庚金壬水戊，酉宫辛金独丰隆；戌宫辛金及丁戊，亥藏壬甲是真踪。

- **分字分词释义**：
  - **地支藏遁**："藏"指隐藏，"遁"通"遯"，指隐藏、潜伏。地支藏遁即地支中所藏天干的配置系统。
  - **子宫癸水**：子支中只藏癸水一气，为纯水之地。
  - **丑癸辛金己土同**：丑支中藏癸水、辛金、己土三者，为杂气之库。
  - **寅宫甲木兼丙戊**：寅支中藏甲木（本气）、丙火（中气）、戊土（余气）。
  - **卯宫乙木独相逢**：卯支中只藏乙木一气，为纯木之地。
  - **辰藏乙戊三分癸**：辰支中藏乙木、戊土、癸水三者，戊土为主气，为杂气之库。
  - **巳中庚金丙戊丛**：巳支中藏庚金、丙火、戊土三者，丙火为主气。
  - **午宫丁火并己土**：午支中藏丁火（本气）、己土（余气）。
  - **未宫乙己丁共宗**：未支中藏乙木、己土、丁火三者，己土为主气，为杂气之库。
  - **申位庚金壬水戊**：申支中藏庚金（本气）、壬水（中气）、戊土（余气）。
  - **酉宫辛金独丰隆**：酉支中只藏辛金一气，为纯金之地。
  - **戌宫辛金及丁戊**：戌支中藏辛金、丁火、戊土三者，戊土为主气，为杂气之库。
  - **亥藏壬甲是真踪**：亥支中藏壬水（本气）、甲木（余气）。

- **规范化释义（primary_lang_explained）**：  
  这条歌诀列举十二地支各自所藏的天干配置。子支中只藏癸水，为纯水之地；丑支藏癸水、辛金、己土三者，属杂气墓库。寅支藏甲木为主，兼有丙火、戊土；卯支只藏乙木一气。辰支藏乙木、戊土、癸水，戊土为主气，属杂气库。巳支藏庚金、丙火、戊土，丙火为主气。午支藏丁火与己土；未支藏乙木、己土、丁火，己土为主气，属杂气库。申支藏庚金、壬水、戊土，庚金为主气。酉支只藏辛金一气，为纯金之地。戌支藏辛金、丁火、戊土，戊土为主气，属杂气库。亥支藏壬水与甲木。这个系统是判断天干"有根无根"的空间基础：天干透出于四柱，若在地支中有对应的藏干，则称"有根"，力量强大；若无对应藏干，则称"无根"或"虚浮"，力量微弱。子、卯、酉三支为纯气，力量专一；辰、戌、丑、未四库为杂气，内含多气，判断时需辨别主气、中气、余气的力量差异。

- **完整对等诠释（secondary_lang_full）**：  
  This formula enumerates the Heavenly Stems hidden within each of the twelve Earthly Branches. Zi Branch contains only Gui Water, representing pure Water element. Chou Branch hides Gui Water, Xin Metal, and Ji Earth—a mixed-qi tomb-storage. Yin Branch stores Jia Wood as primary qi, accompanied by Bing Fire and Wu Earth. Mao Branch contains only Yi Wood in pure form. Chen Branch hides Yi Wood, Wu Earth, and Gui Water, with Wu Earth as dominant qi, forming a mixed-qi storage. Si Branch contains Geng Metal, Bing Fire, and Wu Earth, with Bing Fire as primary force. Wu Branch stores Ding Fire and Ji Earth. Wei Branch hides Yi Wood, Ji Earth, and Ding Fire, with Ji Earth dominant—another mixed-qi storage. Shen Branch contains Geng Metal, Ren Water, and Wu Earth, with Geng Metal primary. You Branch holds only Xin Metal in pure concentration. Xu Branch stores Xin Metal, Ding Fire, and Wu Earth, with Wu Earth dominant—the fourth mixed-qi storage. Hai Branch contains Ren Water and Jia Wood. This system provides the spatial foundation for judging whether Heavenly Stems have "roots": when a Stem appears transparently in the Four Pillars and finds its corresponding hidden counterpart in an Earthly Branch below, it is said to "have roots" and possesses strong power; without such correspondence, it is "rootless" or "floating empty," manifesting weak force. Zi, Mao, and You represent pure qi with concentrated power; Chen, Xu, Chou, and Wei form the four storages of mixed qi, containing multiple elements—requiring practitioners to distinguish primary, middle, and residual qi strengths during analysis.

- **核心要点**：
  - 建立十二地支藏干配置表，每支藏1-3个天干不等
  - 子、卯、酉为纯气（单一天干），辰、戌、丑、未为杂气库（多天干混藏）
  - 地支藏干是判断天干"有根无根"的空间依据，有根则力强，无根则力弱
  - 藏干分主气、中气、余气，力量权重依次递减

- **详细解说**：  
  地支藏干系统是子平命理的核心空间结构。与第1条"节气司令"形成时空双轴：节气司令解决"时间上谁当令"的问题，地支藏干解决"空间上谁有根"的问题。二者结合，才能准确判断某个天干在命局中的真实力量。例如甲木日主，若生于寅月（甲木得令），且地支中有寅、亥等藏甲木之支（甲木有根），则身强力旺；若生于申月（甲木失令），且地支无寅亥（甲木无根），则身弱无依。地支藏干的力量判断，有"主气、中气、余气"之分：寅支藏甲丙戊，甲为主气（力量最强），丙为中气（次之），戊为余气（最弱）。这种力量差异在实际断命时非常关键。四库（辰戌丑未）被称为"杂气"，是因为它们各藏三个天干，且五行混杂，不像子卯酉那样纯粹。杂气库的特点是"能藏善变"：遇到三合局或天干透出时，库中相应的藏干会"透出发力"；遇到冲刑时，库门打开，内藏之物显现。这使得四库在命局和大运中具有特殊的变化性。纯气支（子卯酉）的特点是"专一而强"：子水纯粹，卯木专一，酉金凝聚，各自代表该五行的纯粹力量。在判断格局时，纯气支往往比杂气支更易成局、更有力。

- **校勘与字词辨析**：
  - **藏遁**：部分版本作"藏遯"，"遁""遯"二字通用，皆指隐藏之意。本次据底本作"藏遁"。
  - **辰藏乙戊三分癸**："三分"有版本作"三支"，文义略有差异。"三分"可理解为乙戊癸三者分占辰支，"三支"则易生歧义。本次据底本作"三分"。
  - **巳中庚金丙戊丛**：传统命理中，巳火藏干有"丙戊庚"与"丙戊戊"两种说法。本书采用"丙戊庚"系统，即巳中有庚金（长生于巳），此为《渊海子平》一脉的特色，与《三命通会》等书略有不同。

- **叙事素材（narrative_snippets）**：
  - `[ns_yhzp_009]` `[trigger: 地支藏干]` `[factor_trigger: earthly_branch_hidden_stems]` `[role: 主干]` 十二地支各自所藏的天干配置，形成命局的深层结构。 → 《渊海子平·又地支藏遁歌》
  - `[ns_yhzp_010]` `[trigger: 纯气支]` `[factor_trigger: dizhi_zi OR dizhi_mao OR dizhi_you AND dizhi_pure_qi]` `[role: 条件分支]` 子卯酉为纯气，各藏单一天干，力量专一而强。 → 《渊海子平·又地支藏遁歌》
  - `[ns_yhzp_011]` `[trigger: 杂气库]` `[factor_trigger: dizhi_chen OR dizhi_xu OR dizhi_chou OR dizhi_wei AND dizhi_mixed_qi]` `[role: 条件分支]` 辰戌丑未为杂气库，各藏多个天干，需辨别主次。 → 《渊海子平·又地支藏遁歌》
  - `[ns_yhzp_012]` `[trigger: 天干有根]` `[factor_trigger: stem_rooted AND earthly_branch_hidden_stems AND canggan_tougan]` `[role: 主干依赖]` 天干在地支中有对应藏干则有根，力量强大；藏干透出更显力量。 → 《渊海子平·又地支藏遁歌》
  - `[ns_yhzp_013]` `[trigger: 天干无根]` `[factor_trigger: stem_rooted]` `[role: 主干依赖]` 天干在地支中无对应藏干则无根，力量微弱。 → 《渊海子平·又地支藏遁歌》
  - `[ns_yhzp_014]` `[trigger: 主气中气余气]` `[factor_trigger: canggan_hierarchy AND kumen_state]` `[role: 条件分支]` 支中藏干分主气、中气、余气，力量权重依次递减。 → 《渊海子平·又地支藏遁歌》
  - `[ns_yhzp_015]` `[trigger: 时空双轴]` `[factor_trigger: solar_term AND earthly_branch_hidden_stems]` `[role: 总结]` 节气司令与地支藏干形成时空双轴，共同决定天干真实力量。 → 《渊海子平·又地支藏遁歌》
  - `[ns_yhzp_325]` `[trigger: 从格]` `[factor_trigger: embracing_pattern]` `[role: 条件分支]` 从格者日主无根，从势而行。 → 《渊海子平·又地支藏遁歌》
  - `[ns_yhzp_326]` `[trigger: 太过]` `[factor_trigger: excess]` `[role: 条件分支]` 太过者宜泄，不宜再生。 → 《渊海子平·又地支藏遁歌》
  - `[ns_yhzp_327]` `[trigger: 过不及]` `[factor_trigger: excess_deficiency]` `[role: 主干]` 过与不及皆非吉，中和为贵。 → 《渊海子平·又地支藏遁歌》
  - `[ns_yhzp_328]` `[trigger: 杀露官藏]` `[factor_trigger: exposed_killing_hidden_officer]` `[role: 条件分支]` 杀露官藏，主权势。 → 《渊海子平·又地支藏遁歌》
  - `[ns_yhzp_329]` `[trigger: 官露杀藏]` `[factor_trigger: exposed_officer_hidden_killing]` `[role: 条件分支]` 官露杀藏，主清贵。 → 《渊海子平·又地支藏遁歌》
  - `[ns_yhzp_330]` `[trigger: 绝]` `[factor_trigger: extinction]` `[role: 条件分支]` 绝处逢生方为吉，绝而无救则凶。 → 《渊海子平·又地支藏遁歌》
  - `[ns_yhzp_331]` `[trigger: 父]` `[factor_trigger: father]` `[role: 主干]` 偏财为父星，年柱为父宫。 → 《渊海子平·又地支藏遁歌》
  - `[ns_yhzp_332]` `[trigger: 填实]` `[factor_trigger: filling]` `[role: 条件分支]` 空亡逢填实方能发用。 → 《渊海子平·又地支藏遁歌》
  - `[ns_yhzp_333]` `[trigger: 火]` `[factor_trigger: fire AND bing_ding_fire]` `[role: 主干]` 火为南方之气，主礼主心。 → 《渊海子平·又地支藏遁歌》
  - `[ns_yhzp_334]` `[trigger: 顺从格]` `[factor_trigger: follow_pattern]` `[role: 条件分支]` 顺从格者弃日主而从强势。 → 《渊海子平·又地支藏遁歌》
  - `[ns_yhzp_335]` `[trigger: 从象]` `[factor_trigger: following_image]` `[role: 条件分支]` 从象者随势而变，不守本位。 → 《渊海子平·又地支藏遁歌》
  - `[ns_yhzp_336]` `[trigger: 运]` `[factor_trigger: fortune]` `[role: 主干]` 大运流年为后天之命，配合原局论吉凶。 → 《渊海子平·又地支藏遁歌》
  - `[ns_yhzp_337]` `[trigger: 门户]` `[factor_trigger: gate]` `[role: 条件分支]` 门户者年柱也，为祖宗根基。 → 《渊海子平·又地支藏遁歌》
  - `[ns_yhzp_338]` `[trigger: 将星]` `[factor_trigger: general_star]` `[role: 条件分支]` 将星临日主，主权威。 → 《渊海子平·又地支藏遁歌》
  - `[ns_yhzp_339]` `[trigger: 生克]` `[factor_trigger: generation_restraint]` `[role: 主干]` 五行生克为命理根本，生者助，克者制。 → 《渊海子平·又地支藏遁歌》
  - `[ns_yhzp_340]` `[trigger: 真官]` `[factor_trigger: genuine_official]` `[role: 条件分支]` 真官不见杀，主清贵。 → 《渊海子平·又地支藏遁歌》
  - `[ns_yhzp_341]` `[trigger: 神煞]` `[factor_trigger: god_sha]` `[role: 主干]` 神煞为格局辅助，不可独断。 → 《渊海子平·又地支藏遁歌》
  - `[ns_yhzp_342]` `[trigger: 合禄]` `[factor_trigger: he_lu]` `[role: 条件分支]` 合禄者六合逢禄，主贵显。 → 《渊海子平·又地支藏遁歌》
  - `[ns_yhzp_343]` `[trigger: 合贵]` `[factor_trigger: he_noble AND combine_noble_promiscuity]` `[role: 条件分支]` 合贵者六合逢贵人，主遇贵。 → 《渊海子平·又地支藏遁歌》
  - `[ns_yhzp_344]` `[trigger: 天干]` `[factor_trigger: heavenly_stem]` `[role: 主干]` 天干为十，主时间与透出。 → 《渊海子平·又地支藏遁歌》
  - `[ns_yhzp_345]` `[trigger: 印绶]` `[factor_trigger: indirect_resource]` `[role: 条件分支]` 印绶为生我之神，主学问、权柄。 → 《渊海子平·又地支藏遁歌》
  - `[ns_yhzp_346]` `[trigger: 伤官]` `[factor_trigger: injuring_officer]` `[role: 条件分支]` 伤官克官，主聪明、叛逆。 → 《渊海子平·又地支藏遁歌》
  - `[ns_yhzp_347]` `[trigger: 刑]` `[factor_trigger: injury]` `[role: 条件分支]` 刑者伤也，三刑主灾厄。 → 《渊海子平·又地支藏遁歌》
  - `[ns_yhzp_348]` `[trigger: 吉凶]` `[factor_trigger: luck_misfortune]` `[role: 主干]` 吉凶由格局定，喜用为吉，忌仇为凶。 → 《渊海子平·又地支藏遁歌》"""
    normalized_text_zh: str = """"""
    subject: str = "又地支藏遁歌"
    factor_refs: list = ['earthly_branch_hidden_stems', 'stem_rooted', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate']
    
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
        l1_anchor="yhzp_v1.0.0_又地支藏遁歌_001_L1",
    )
    version: str = "1.0.0"
