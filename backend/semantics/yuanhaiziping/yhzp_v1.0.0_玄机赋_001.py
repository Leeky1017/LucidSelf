"""
Auto-generated semantic module for yuanhaiziping
Generated at: 2025-12-05T13:30:19.559428
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
    semantic_id="yhzp_v1.0.0_玄机赋_001",
    book_id="yuanhaiziping",
    engine_id="bazi"
)
class 玄机赋(SemanticEntry):
    """
    - **原文（source_text）**：
  太极判为天地，一气分有阴阳。
  日干为主，专论财官。月支取格，乃分贵贱。
  有格不正者，败。无格有用者，成。
  有官，莫寻格局。有格局，喜官星。...
    """
    
    original_text: str = """- **原文（source_text）**：
  太极判为天地，一气分有阴阳。
  日干为主，专论财官。月支取格，乃分贵贱。
  有格不正者，败。无格有用者，成。
  有官，莫寻格局。有格局，喜官星。
  官印财食无破，清高。杀伤枭刃，用之为吉。
  善恶相交，喜去杀而从善。吉凶混杂，忌害吉以化凶。
  有官有杀，宜身旺，制杀为奇。有官有印，畏财兴，助财为祸。
  身强杀浅，杀运无妨。杀重身轻，制乡为福。
  身旺印多，喜行财地。财多身弱，畏入财乡。
  男逢比劫伤官，克妻害子。女犯伤官偏印，丧子刑夫。
  幼失双亲，财星太重。为人孤克，身旺无依。
  年冲月令，离祖成家。日破提冲，弦断再续。时日对冲，伤妻克子。
  日通月令，得祖安身。
  木遇春长，遇庚辛反假为权。火归夏生，见壬癸能为福厚。
  土逢辰戌丑未，木重成名。金坐申酉之中，火乡发福。水居亥子，戊己难侵。
  身坐休囚，平生未济。身旺喜逢禄马。身弱忌见财官。
  得时俱为旺论。失令便作衰看。
  四柱无根，得时为旺。日干无气，遇劫为强。
  身弱喜印。主旺宜官。
  财官印绶，破则无功。杀伤枭劫，去之为福。
  甲乙秋生金透露，水木火运荣昌。丙丁冬降水汪洋，火土木方贵显。
  戊己春生，西南方有救。庚辛夏长，水土运无伤。壬癸逢于土旺，金木宜荣。
  身弱有印，杀旺无伤；忌行财地。
  伤官伤尽，行官运以无妨。伤官用印宜去财。伤官用财宜去印。
  是或，伤官财印俱彰，将何发福；身旺者用财，身弱者用印。用财去印，用印去财，方发弥福；正所谓喜者存之，憎者去之。
  财多身弱，身旺以为荣。身旺财衰，财旺乡而发福。
  重犯官星，只宜制伏。食神叠见，须忌官乡。
  顽金无火，大用不成。强木无金，清名难著。
  水多得土，财多蓄。火焰逢波（水星），禄位高。
  有官有印，无破无荣。无印无官，有格取贵。
  阳刃格喜偏官。金神最宜制伏。杂气财官，刑冲则发。
  官贵太盛，旺处必倾。身太旺，喜见财官。主太柔，不宜禄马。
  旺官旺印与旺财，入墓有祸。伤官食神并身旺，遇库兴灾。
  运贵在于支取。岁重向乎干求。
  印多者，行财而发。财旺者，遇比何妨。
  格清局正，富贵荣华。印旺官旺，声名特达。
  合官，非为贵取。合杀，莫作凶推。
  桃花带杀，喜淫奔。华盖逢空，多刻剥。
  平生不发，八字休囚。一世无权，身衰遇鬼。
  身旺者，则宜泄、宜伤。身衰者，则喜扶、喜助。
  禀中和，莫令太过不及。
  若遵此法推详，祸福验如影响。

- **分字分词释义**：
  - **日干为主专论财官**：日干是自身，首重财官配置。
  - **月支取格乃分贵贱**：月令定格局，分辨贵贱高低。
  - **有格不正者败无格有用者成**：格局不纯则败，无格但有用神亦成。
  - **有官莫寻格局**：正官透出即为贵格，不必另寻。
  - **身强杀浅杀运无妨**：身旺杀弱，行杀运反吉。
  - **杀重身轻制乡为福**：杀旺身弱，行制杀运为福。
  - **伤官伤尽行官运以无妨**：伤官见尽无官，可行官运。
  - **顽金无火大用不成**：金无火炼，难成大器。
  - **禀中和莫令太过不及**：保持中和，避免太过或不及。
  - **祸福验如影响**：验证祸福如影随形。

- **规范化释义（primary_lang_explained）**：
  本篇名为《玄机赋》，是渊海子平中最核心的综合性论命总纲，涵盖格局判定、身财官平衡、用神取舍、运程吉凶等所有命理核心法则：
  - **总纲**：日干为主（自身），月令取格（贵贱之分）。有格不正则败，无格有用则成。
  - **格局法则**：
    - **有官莫寻格局**：正官透干为正统贵格，不必强取其他特殊格局。
    - **有格局喜官星**：其他格局（如食神、印格）若见官星，反增贵气。
  - **善恶辨别**：
    - **清高四神**：官印财食无破损，主清高。
    - **凶神转吉**：杀伤枭刃若有制化得宜，反主大贵（如七杀有制）。
  - **身杀平衡**：
    - **身强杀浅**：喜行杀运增威。
    - **杀重身轻**：喜行制杀运（食伤）或身旺运（比劫印）。
    - **身旺印多**：印生身太过，喜行财地破印。
    - **财多身弱**：财为负担，畏入财乡，喜身旺运。
  - **六亲克应**：
    - **男命**：比劫伤官克妻害子。
    - **女命**：伤官偏印丧子刑夫。
  - **季节调候**：
    - **木春金秋**：木生春月遇金克反为栋梁之材（假杀为权）。
    - **火夏水冬**：火生夏月见水反为既济之功。
  - **伤官三用**：
    - **伤官伤尽**：四柱无官星，可行官运。
    - **伤官用印**：去财护印。
    - **伤官用财**：去印护财。
  - **中和为贵**：太过不及皆凶，身旺者宜泄伤，身衰者宜扶助，禀中和气最吉。

- **完整对等诠释（secondary_lang_full）**：
  **Ode on Mysterious Principles (Xuan Ji Fu)**:
  - **Foundation**: Day Stem is Master; Month Command determines pattern (noble/base distinction). Correct pattern succeeds; incorrect pattern fails. Patternless with Use-God also succeeds.
  - **Pattern Rules**:
    - **Have Officer, Don't Seek Patterns**: Direct Officer exposed = Orthodox nobility. No need for special patterns.
    - **Have Pattern, Love Officer**: Other patterns (Food, Seal) benefit from Officer Star.
  - **Good/Evil Distinction**:
    - **Four Pure**: Officer, Seal, Wealth, Food undamaged = High integrity.
    - **Fierce Transformed**: Killing, Injury, Owl, Blade with proper control = Great nobility (e.g., Controlled Killing).
  - **Self-Killing Balance**:
    - **Strong Self, Weak Killing**: Benefit from Killing Luck.
    - **Heavy Killing, Light Self**: Need Control Luck (Food/Injury) or Self-Strengthening (Parallel/Seal).
    - **Strong Self, Many Seals**: Seals over-nourish; need Wealth to break Seals.
    - **Much Wealth, Weak Self**: Wealth as burden; fear Wealth Luck, need Self-Strengthening.
  - **Relations**:
    - **Men**: Parallels/Injury harm wife/children.
    - **Women**: Injury/Owl harm children/husband.
  - **Seasonal Climate**:
    - **Wood/Spring, Metal/Autumn**: Wood in Spring meeting Metal = Carved into beams (Borrowed Killing).
    - **Fire/Summer, Water/Winter**: Fire in Summer meeting Water = Balance/Success (Ji Ji).
  - **Injury Three Uses**:
    - **Injury Injures Fully**: No Officer in pillars, can enter Officer Luck.
    - **Injury Uses Seal**: Remove Wealth to protect Seal.
    - **Injury Uses Wealth**: Remove Seal to protect Wealth.
  - **Moderation Paramount**: Excess/deficiency both inauspicious. Strong Self = needs output/injury. Weak Self = needs support. Central Harmony (Zhong He) is best.

- **核心要点**：
  - **格局正误**：有格不正则败，无格有用则成
  - **身杀平衡**：强杀喜制，弱身喜扶，相停为贵
  - **伤官三用**：伤尽（行官）、用印（去财）、用财（去印）
  - **中和至上**：太过不及皆凶，禀中和气最吉
  - **季节调候**：木春遇金、火夏遇水皆为妙用

- **详细解说**：  《玄机赋》是渊海子平中最核心的综合性论命总纲，开篇"太极判为天地，一气分有阴阳"溯源太极，"日干为主，专论财官；月支取格，乃分贵贱"确立核心法则。**格局法则**——"有格不正者败，无格有用者成"揭示格局成败关键；"有官莫寻格局"强调正官透干即为正统贵格。**身杀平衡**——"身强杀浅，杀运无妨"，"杀重身轻，制乡为福"，揭示身杀配合的核心原理。**伤官三用**——"伤官伤尽，行官运以无妨"；"伤官用印宜去财"；"伤官用财宜去印"，系统阐述伤官格的三种取用方法。**调候成器**——"顽金无火，大用不成"；"强木无金，清名难著"，揭示五行制化成器的道理。**中和至上**——"身旺者则宜泄宜伤，身衰者则喜扶喜助；禀中和，莫令太过不及"，强调中和为贵的核心思想。末句"若遵此法推详，祸福验如影响"点明此赋为论命圭臬。

- **叙事素材（narrative_snippets）**：
  - `[ns_yhzp_719]` `[trigger: 日干月令核心]` `[factor_trigger: rigan_weizhu AND yuezhi_quege AND lunming_faze]` `[role: 主干]` 日干为主专论财官；月支取格乃分贵贱；论命核心法则。 → 《渊海子平·玄机赋》
  - `[ns_yhzp_720]` `[trigger: 格局成败]` `[factor_trigger: geju_buzheng_bai AND wuge_youyong_cheng AND cheng AND improper_pattern AND pattern_less_useful]` `[role: 主干依赖]` 有格不正者败，无格有用者成；格局成败关键。 → 《渊海子平·玄机赋》
  - `[ns_yhzp_721]` `[trigger: 有官莫寻格局]` `[factor_trigger: youguan_moxun_geju AND zhengguan_tougan_gui AND anchong_qugui AND angui]` `[role: 条件分支]` 有官莫寻格局，有格局喜官星；正官透干为贵。 → 《渊海子平·玄机赋》
  - `[ns_yhzp_722]` `[trigger: 身杀平衡]` `[factor_trigger: shenqiang_shaqian AND shazhong_shenqing AND zhi_weifu AND killing_heavy_self_light]` `[role: 条件分支]` 身强杀浅杀运无妨；杀重身轻制乡为福；身杀配合法则。 → 《渊海子平·玄机赋》
  - `[ns_yhzp_723]` `[trigger: 伤官三用]` `[factor_trigger: shangguan_shangjin AND yongyin_qucai AND yongcai_quyin AND caiyin AND caiyin_qing_guansha_zu AND changyin AND shangguan_yun]` `[role: 条件分支]` 伤官伤尽行官运无妨；伤官用印宜去财；伤官用财宜去印。 → 《渊海子平·玄机赋》
  - `[ns_yhzp_724]` `[trigger: 调候成器]` `[factor_trigger: wanjin_wuhuo_bucheng AND qiangmu_wujin_nanzhuo AND hard_metal]` `[role: 条件分支]` 顽金无火大用不成；强木无金清名难著；五行制化成器。 → 《渊海子平·玄机赋》
  - `[ns_yhzp_725]` `[trigger: 中和至上]` `[factor_trigger: shenwang_xie_shang AND shenshuai_fu_zhu AND zhonghe]` `[role: 条件分支]` 身旺者宜泄宜伤，身衰者喜扶喜助；禀中和莫令太过不及。 → 《渊海子平·玄机赋》
  - `[ns_yhzp_726]` `[trigger: 玄机赋纲领]` `[factor_trigger: xuanji_fu AND rigan_yueling AND geju_shensha_tiaohao_zhonghe]` `[role: 总结]` 玄机赋以日干月令为核心，论格局身杀伤官调候中和，为论命圭臬。 → 《渊海子平·玄机赋》"""
    normalized_text_zh: str = """"""
    subject: str = "玄机赋"
    factor_refs: list = ['mysterious_principles_ode', 'improper_pattern', 'borrowed_killing_authority', 'injury_fully', 'central_harmony']
    
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
        l1_anchor="yhzp_v1.0.0_玄机赋_001_L1",
    )
    version: str = "1.0.0"
