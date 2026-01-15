"""
Auto-generated semantic module for yuanhaiziping
Generated at: 2025-12-05T13:30:19.559224
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
    semantic_id="yhzp_v1.0.0_滚浪桃花_001",
    book_id="yuanhaiziping",
    engine_id="bazi"
)
class 滚浪桃花(SemanticEntry):
    """
    - **原文（source_text）**：  
  女命用官为夫、或杀；只喜一位，多者克夫。如命满盘官星为忌；满柱杀星，为福反吉。伤官不为贵，伤官运复行克夫。伤官有制身绝。女命伤官，刑子、克夫为决。...
    """
    
    original_text: str = """- **原文（source_text）**：  
  女命用官为夫、或杀；只喜一位，多者克夫。如命满盘官星为忌；满柱杀星，为福反吉。伤官不为贵，伤官运复行克夫。伤官有制身绝。女命伤官，刑子、克夫为决。女命官星多者，伤夫主贱。伤官桃花，为妓女命，或主克子息。若见贵人一位，或带荣神、或犯绝地，多富贵贞洁。禄马相随，桃花带贵，咸池遇马，多淫、妨夫破家。有辰无戌命孤，晚景寂寞。戌多无辰，初年劳碌，中年好；不妨夫、不克子，风流而淫。辰戌全则淫乱破家、伤夫克子、夭寿残疾。

- **分字分词释义**：
  - **女命用官为夫**：女命以正官为丈夫代表，官星即夫星。
  - **只喜一位**：官星或七杀以单一纯正为佳，忌多位混杂。
  - **满盘官星为忌**：官星过多反成凶象，夫多则乱。
  - **满柱杀星反吉**：七杀满柱反主从杀格，可能因此反吉。
  - **伤官不为贵**：伤官克制官星（夫星），女命不以伤官为贵。
  - **伤官有制身绝**：伤官若有制化，则日主反受其害。
  - **刑子克夫**：伤官既克官星（夫），又泄日主气（影响子星），故刑子克夫。
  - **伤官桃花**：伤官与桃花同见，女命主妓女之命或克子息。
  - **贵人一位**：天乙贵人单一纯正，主富贵贞洁。
  - **荣神**：主荣耀的吉神，与贵人类似。
  - **犯绝地**：日主入绝地，反而主贞洁（因无桃花之力）。
  - **禄马相随**：禄神与驿马同柱，女命主奔波劳碌。
  - **咸池遇马**：咸池（桃花煞）遇驿马，主多淫妨夫破家。
  - **有辰无戌命孤**：只见辰不见戌，主命孤晚景寂寞。
  - **戌多无辰**：只见戌不见辰，初年劳碌中年转好，风流而淫。
  - **辰戌全**：辰戌二支皆现，为女命最凶配置，主淫乱破家伤夫克子夭寿残疾。

- **规范化释义（primary_lang_explained）**：  
  《滚浪桃花》专论女命桃花咸池与淫乱克夫的判断法则。**官杀为夫**：女命用官为夫或杀只喜一位多者克夫；满盘官星为忌满柱杀星反吉。**伤官克夫**：伤官不为贵伤官运复行克夫；伤官有制身绝；女命伤官刑子克夫为决；女命官星多者伤夫主贱。**桃花淫乱**：伤官桃花为妓女命或主克子息；若见贵人一位或带荣神或犯绝地多富贵贞洁。**禄马咸池**：禄马相随桃花带贵咸池遇马多淫妨夫破家。**辰戌吉凶**：有辰无戌命孤晚景寂寞；戌多无辰初年劳碌中年好不妨夫不克子风流而淫；辰戌全则淫乱破家伤夫克子夭寿残疾。

- **完整对等诠释（secondary_lang_full）**：  
  **Rolling-Wave Peach Flower**: This section specifically treats women's fate regarding Peach Blossom, Salty Pond (Hamchi), and the principles for judging promiscuity and harming husbands. **Officer-Killing as Husband**: Women's fate uses Officer as husband, or Killing; it only delights in having one position—if many, it harms the husband. If the fate has a full chart of Officer Stars, it is taboo; but if full pillars of Killing Stars, it paradoxically becomes auspicious fortune. **Harm Officer Harms Husband**: Harm Officer is not noble; if Harm Officer fortune runs repeatedly, it harms the husband. If Harm Officer has control, the body (Self) becomes extinct. For women's fate, Harm Officer punishing children and harming husband is a definitive conclusion. Women's fate with many Officer Stars indicates harming husband and baseness. **Peach Blossom Promiscuity**: Harm Officer with Peach Blossom indicates a prostitute's fate, or mainly harming children. If seeing Noble Person in one position, or carrying Glory Spirit, or encountering Extinction land, it mostly indicates wealth, nobility, and chastity. **Salary-Horse-Salty Pond**: Salary and Horse following each other, Peach Blossom carrying Noble, or Salty Pond meeting Horse—all indicate much promiscuity, obstructing the husband, and breaking the family. **Chen-Xu Auspice-Inauspice**: Having Chen without Xu makes fate solitary with lonely late years; having many Xu without Chen means early years laborious, middle years good, not obstructing husband or harming children, but romantic and promiscuous. If Chen and Xu are both complete, it indicates promiscuous chaos, broken family, harming husband, harming children, early death, and disability.

- **核心要点**：  
  - 专论女命桃花咸池与淫乱克夫的判断法则  
  - 官杀为夫喜一位忌多位；满盘官星为忌满柱杀星反吉  
  - 伤官为女命大忌：刑子克夫为决；伤官桃花为妓女命  
  - 辰戌全主淫乱破家伤夫克子夭寿残疾为女命最凶配置

- **详细解说**：  《滚浪桃花》是女命判断中专论"淫贱克夫"的重要篇章。"滚浪"二字形象描绘桃花过旺、情缘纷杂的状态。全篇围绕三大主题展开：**官杀与克夫**——女命以官或杀为夫，"只喜一位，多者克夫"是核心法则；但有一特例："满柱杀星，为福反吉"，即七杀极多反成从杀格。**伤官与桃花**——"伤官不为贵"是女命铁律，伤官克夫且"刑子克夫为决"；"伤官桃花，为妓女命"更是女命最凶配置之一。**辰戌与淫乱**——辰戌的配置决定女命淫贱程度："有辰无戌命孤"，"戌多无辰初年劳碌中年好"，但"辰戌全则淫乱破家、伤夫克子、夭寿残疾"是女命最凶。特别值得注意的是几组对立判断：贵人一位主贞洁，贵人多反主淫；犯绝地反主贞洁（因桃花无力）；禄马相随、咸池遇马则"多淫、妨夫破家"。这些对立判断提醒命师，女命判断不可一概而论，需细辨配置组合。

- **叙事素材（narrative_snippets）**：
  - `[ns_yhzp_258]` `[trigger: 官杀喜一位]` `[factor_trigger: nvming AND guansha_yiwei AND kefu]` `[role: 主干]` 女命用官为夫、或杀；只喜一位，多者克夫。 → 《渊海子平·滚浪桃花》
  - `[ns_yhzp_259]` `[trigger: 满柱杀星反吉]` `[factor_trigger: nvming AND manzhu_shaxing AND fanji AND full_killings_paradox]` `[role: 例外处理]` 如命满盘官星为忌；满柱杀星，为福反吉。 → 《渊海子平·滚浪桃花》
  - `[ns_yhzp_260]` `[trigger: 伤官刑子克夫]` `[factor_trigger: nvming AND shangguan AND xingzi_kefu]` `[role: 条件分支]` 女命伤官，刑子、克夫为决；伤官为女命大忌。 → 《渊海子平·滚浪桃花》
  - `[ns_yhzp_261]` `[trigger: 伤官桃花妓女命]` `[factor_trigger: nvming AND shangguan_taohua AND jinvming AND harm_officer_peach_prostitute]` `[role: 条件分支]` 伤官桃花，为妓女命，或主克子息。 → 《渊海子平·滚浪桃花》
  - `[ns_yhzp_262]` `[trigger: 贵人一位贞洁]` `[factor_trigger: nvming AND guiren_yiwei AND zhenjie AND anchong_qugui AND angui AND noble_glory_chastity]` `[role: 条件分支]` 若见贵人一位，或带荣神、或犯绝地，多富贵贞洁。 → 《渊海子平·滚浪桃花》
  - `[ns_yhzp_263]` `[trigger: 咸池遇马多淫]` `[factor_trigger: nvming AND xianchi_yuma AND duoyin AND caiyin AND caiyin_qing_guansha_zu AND changyin AND duoyin_fangfu]` `[role: 条件分支]` 禄马相随，桃花带贵，咸池遇马，多淫、妨夫破家。 → 《渊海子平·滚浪桃花》
  - `[ns_yhzp_264]` `[trigger: 有辰无戌命孤]` `[factor_trigger: nvming AND youchen_wuxu AND minggu]` `[role: 条件分支]` 有辰无戌命孤，晚景寂寞；只见辰不见戌主孤独。 → 《渊海子平·滚浪桃花》
  - `[ns_yhzp_265]` `[trigger: 辰戌全最凶]` `[factor_trigger: nvming AND chenxu_quan AND zuixiong]` `[role: 条件分支]` 辰戌全则淫乱破家、伤夫克子、夭寿残疾；女命最凶配置。 → 《渊海子平·滚浪桃花》
  - `[ns_yhzp_266]` `[trigger: 滚浪桃花纲领]` `[factor_trigger: nvming AND gunlang_taohua AND gangling]` `[role: 总结]` 滚浪桃花专论女命桃花咸池与淫乱克夫的判断法则，辰戌配置决定淫贱程度。 → 《渊海子平·滚浪桃花》"""
    normalized_text_zh: str = """"""
    subject: str = "滚浪桃花"
    factor_refs: list = ['rolling_wave_peach', 'harm_officer_peach_prostitute', 'promiscuity', 'chen_xu_complete_chaos', 'noble_glory_chastity']
    
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
        l1_anchor="yhzp_v1.0.0_滚浪桃花_001_L1",
    )
    version: str = "1.0.0"
