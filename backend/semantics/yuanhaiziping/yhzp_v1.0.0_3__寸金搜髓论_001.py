"""
Auto-generated semantic module for yuanhaiziping
Generated at: 2025-12-05T13:30:19.559375
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
    semantic_id="yhzp_v1.0.0_3__寸金搜髓论_001",
    book_id="yuanhaiziping",
    engine_id="bazi"
)
class 3寸金搜髓论(SemanticEntry):
    """
    - **原文（source_text）**：
  造化先须看日主，后把提纲看次第。四柱专论其财官，身旺财官多富贵。若还身旺财官损，只是朝求暮讨儿。财官旺时日主强，紫袍金带有何疑。财官旺而日主弱，运行身...
    """
    
    original_text: str = """- **原文（source_text）**：
  造化先须看日主，后把提纲看次第。四柱专论其财官，身旺财官多富贵。若还身旺财官损，只是朝求暮讨儿。财官旺时日主强，紫袍金带有何疑。财官旺而日主弱，运行身旺最为奇。日主旺而财官弱，运入财官名利驰。
  日主坐下有财官，月令相逢贵不难。身旺无依更迁祖，不迁居死在外地。身旺印旺，破财不聚。
  官喜露，露则清高。财要藏，藏则丰厚。杀藏官露，恶隐善扬。
  官杀太重身更强，一逢制伏作贤良。杀官拱印贵非轻。
  身居九夏火土多，相逢水济贵中和。生居三冬，水冷金寒；得火相扶，莫作等闲。
  南火利北水，北水利南火，东木宜西金，西金宜东木（指运程）。
  三丘五行（辰戌丑未）重见，骨肉刑悲。身旺比肩坐驿马，兄弟飘蓬。八字四马交驰，身荣劳碌。
  财星入库主聚财，妻悭吝。财星坐四马，妻贤欣欣。
  官杀重重不带财，妻能内助不和谐。官星生旺，子息聪明著绯衣。
  比劫伤官旺，伤妻更损儿。日主七杀带枭神，妻虚胎小产。
  印绶旺身身更旺，刑克孤贫。女命伤官旺，坐下伤官会骂夫。
  日支乙巳、戊辰、庚午、辛未，权贵之妻。
  甲子丙寅等日（日坐空亡/沐浴/绝地），虚名虚利。
  好将四柱分强弱，莫犯阴阳执一言；此是五行真妙诀，不逢智者莫虚传。

- **分字分词释义**：
  - **造化先须看日主**：论命首先确立日主（日干）为核心。
  - **后把提纲看次第**：其次看月令提纲定格局。
  - **身旺财官多富贵**：日主旺且财官也旺，主富贵。
  - **运行身旺最为奇**：身弱财官旺时，喜行身旺之运。
  - **官喜露露则清高**：官星透出天干显贵气。
  - **财要藏藏则丰厚**：财星宜藏于地支免被劫。
  - **杀藏官露恶隐善扬**：七杀隐藏正官透出，主凶性隐藏显示贵气。
  - **水冷金寒得火相扶**：冬月水金需火调候。
  - **财星入库主聚财**：财星入墓库主积财但吝啬。
  - **伤官旺坐下伤官会骂夫**：女命伤官旺主骂夫克夫。

- **规范化释义（primary_lang_explained）**：
  本篇歌诀全面总结了子平论命的精髓：
  1. **身财官平衡**：身旺财官旺为富贵；身旺财官损为贫穷；身弱财官旺喜行身旺运；身旺财官弱喜行财官运。
  2. **露藏喜忌**：官喜露（显荣），财喜藏（不被劫）。杀藏官露为"恶隐善扬"之贵。
  3. **调候中和**：夏火喜水济，冬金喜火扶。东南西北运程宜反向互补（木宜金运等）。
  4. **六亲断法**：
     - **兄弟**：比肩坐马主兄弟飘蓬。
     - **妻财**：财入库主聚财妻吝，财坐马主妻贤。
     - **子息**：官星生旺子显贵，伤官劫财旺损子。
  5. **女命**：伤官旺骂夫克夫，印旺身强孤贫。

- **完整对等诠释（secondary_lang_full）**：
  **Inch Gold Searching Marrow Treatise**:
  - **Balance**: Strong Self + Strong Wealth/Officer = Riches/Nobility. Strong Self + Damaged Wealth/Officer = Beggar. Weak Self + Strong Wealth/Officer = Needs Self-Strengthening Luck. Strong Self + Weak Wealth/Officer = Needs Wealth/Officer Luck.
  - **Exposure/Hiding**: Officer likes Exposure (Status); Wealth likes Hiding (Accumulation). "Hidden Killing, Exposed Officer" = Hidden evil, exposed good (Noble).
  - **Climate**: Summer Fire needs Water; Winter Metal needs Fire.
  - **Relations**:
    - **Siblings**: Parallels on Post Horse = Wandering siblings.
    - **Wife/Wealth**: Wealth in Tomb = Accumulation but stingy wife. Wealth on Horse = Virtuous happy wife.
    - **Children**: Prosperous Officer = Noble children. Prosperous Injury/Rob = Harmed children.
  - **Women**: Prosperous Injury cursing husband; Prosperous Seal/Self implying loneliness.

- **核心要点**：
  - **身旺运**：身弱财官旺宜行
  - **财官运**：身旺财官弱宜行
  - **调候**：金寒水冷要火，火炎土燥要水
  - **妻财子禄**：财库妻吝，官旺子贵

- **详细解说**：  《寸金搜髓论》是子平法论命精髓的歌诀总结，开篇即定调"造化先须看日主，后把提纲看次第"，确立日主与月令的核心地位。**身财官平衡**是本篇核心："身旺财官多富贵"为上格；"身旺财官损"则"朝求暮讨"为贫穷；身弱财官旺喜"运行身旺"；身旺财官弱喜"运入财官"。**露藏之法**——"官喜露，露则清高；财要藏，藏则丰厚"，官透主显贵，财藏主积富；"杀藏官露"则"恶隐善扬"主贵。**调候中和**——"生居三冬，水冷金寒；得火相扶，莫作等闲"，强调冬金夏火需水火调候。**六亲断法**——兄弟看比肩（坐马主飘蓬），妻财看财星（入库主吝，坐马主贤），子息看官星（生旺主贵）。**女命特论**——伤官旺"会骂夫"，印旺身强主"刑克孤贫"。末句"好将四柱分强弱，莫犯阴阳执一言"点明论命需灵活。

- **叙事素材（narrative_snippets）**：
  - `[ns_yhzp_665]` `[trigger: 日主提纲]` `[factor_trigger: rizhu_weizhu AND tigang_cidi]` `[role: 主干]` 造化先须看日主，后把提纲看次第；日主月令为论命核心。 → 《渊海子平·寸金搜髓论》
  - `[ns_yhzp_666]` `[trigger: 身财官平衡]` `[factor_trigger: shenwang_caiguanduo AND fugui AND anchong_qugui AND angui]` `[role: 条件分支]` 身旺财官多富贵；身旺财官损只是朝求暮讨儿。 → 《渊海子平·寸金搜髓论》
  - `[ns_yhzp_667]` `[trigger: 运程补弱]` `[factor_trigger: caiguanwang_rizhuruo AND yunxing_shenwang]` `[role: 条件分支]` 财官旺而日主弱运行身旺最为奇；日主旺而财官弱运入财官名利驰。 → 《渊海子平·寸金搜髓论》
  - `[ns_yhzp_668]` `[trigger: 官露财藏]` `[factor_trigger: guanlu_qinggao AND caicang_fenghou AND fenghou AND officer_exposed]` `[role: 条件分支]` 官喜露露则清高；财要藏藏则丰厚；杀藏官露恶隐善扬。 → 《渊海子平·寸金搜髓论》
  - `[ns_yhzp_669]` `[trigger: 调候冬夏]` `[factor_trigger: sandong_shuileng_jinhan AND dehuo_xiangfu AND climate_adjustment]` `[role: 条件分支]` 生居三冬水冷金寒得火相扶莫作等闲；调候中和之法。 → 《渊海子平·寸金搜髓论》
  - `[ns_yhzp_670]` `[trigger: 财入库妻吝]` `[factor_trigger: caixing_ruku AND qiqianlin AND jucai]` `[role: 条件分支]` 财星入库主聚财妻悭吝；财星坐四马妻贤欣欣。 → 《渊海子平·寸金搜髓论》
  - `[ns_yhzp_671]` `[trigger: 寸金搜髓纲领]` `[factor_trigger: cunjin_sousui AND shencaiguan_pingheng AND tiaohao_zhonghe]` `[role: 总结]` 寸金搜髓论以身财官平衡、官露财藏、调候中和为论命精髓。 → 《渊海子平·寸金搜髓论》"""
    normalized_text_zh: str = """"""
    subject: str = "3. 寸金搜髓论"
    factor_refs: list = ['officer_exposed', 'wealth', 'climate_adjustment', 'high_rank_symbol']
    
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
        l1_anchor="yhzp_v1.0.0_3__寸金搜髓论_001_L1",
    )
    version: str = "1.0.0"
