"""
Auto-generated semantic module for yuanhaiziping
Generated at: 2025-12-05T13:30:19.559193
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
    semantic_id="yhzp_v1.0.0_阴命赋_001",
    book_id="yuanhaiziping",
    engine_id="bazi"
)
class 阴命赋(SemanticEntry):
    """
    - **原文（source_text）**：  
  凡观阴命，先观夫主之盛衰；次论身荣，要见子息之强弱。夫荣子旺，定知富贵荣华。子死夫衰，只是穷孤下贱。有夫有子而贫寒者，盖因身在衰乡。无夫无子而昌盛...
    """
    
    original_text: str = """- **原文（source_text）**：  
  凡观阴命，先观夫主之盛衰；次论身荣，要见子息之强弱。夫荣子旺，定知富贵荣华。子死夫衰，只是穷孤下贱。有夫有子而贫寒者，盖因身在衰乡。无夫无子而昌盛者，亦是身居旺地。若贵人少者，不富亦昌。合贵神非妓即尼，论淫贱者。四柱伤官，暗招财损。招婿者，夫显于门户之中。偏夫者，夫旺于日时之上。夫衰身旺，主为廉洁之人。鬼旺身衰，必作孤寒之妇。凡观阴命之五行，要精详于明辨矣！

- **分字分词释义**：
  - **阴命**：指女命，因女性属阴故名，与男命（阳命）判断法则有根本差异。
  - **夫主之盛衰**：以官星（正官、七杀）代表丈夫，观其在命局中的旺衰得失。
  - **子息之强弱**：以食神、伤官代表子女，观其在命局中的生旺休囚。
  - **夫荣子旺**：官杀旺且食伤旺，夫星子星双全，主女命富贵荣华。
  - **子死夫衰**：食伤无力且官杀衰弱，夫子两失，主穷孤下贱。
  - **身在衰乡**：日主处于休囚死绝之地，虽有夫子亦难享其福。
  - **身居旺地**：日主处于临官帝旺之地，虽无夫子亦能自立昌盛。
  - **贵人少者**：天乙贵人等吉神数量不多，但格局纯净。
  - **合贵神**：日主与贵人形成天干五合或地支六合，女命反主淫贱。
  - **非妓即尼**：合贵神过多，女命不为妓女便为尼姑，皆非正途。
  - **四柱伤官**：四柱中伤官过多过旺，暗中招致财物损耗与夫运不顺。
  - **招婿**：入赘女家的丈夫，夫星显于年月（门户）之位。
  - **偏夫**：非正式婚配的男性，夫星（偏官）旺于日时之上。
  - **夫衰身旺**：官杀衰弱而日主旺盛，女命反主廉洁守节。
  - **鬼旺身衰**：七杀旺盛而日主衰弱，女命主孤寒贫苦。
  - **精详明辨**：对女命五行配置须细致分辨，不可混同男命之法。

- **规范化释义（primary_lang_explained）**：  
  《阴命赋》系统阐述女命判断的核心法则——以夫星子星为主，身旺身衰为辅。**夫星子星为主**：观女命先看夫主（官杀）盛衰，次看子息（食伤）强弱；夫荣子旺主富贵荣华，子死夫衰主穷孤下贱。**身旺身衰调节**：有夫有子而贫寒者因身在衰乡，无夫无子而昌盛者因身居旺地；夫衰身旺主廉洁，鬼旺身衰主孤寒。**格局吉凶**：若贵人（天乙）少者不富亦昌，合贵神者非妓即尼论淫贱；四柱伤官暗招财损；招婿者夫显门户，偏夫者夫旺日时。**总结**：观阴命之五行要精详明辨，不可混同男命之法。

- **完整对等诠释（secondary_lang_full）**：  
  **Yin Fate Rhapsody**: This section systematically expounds core principles for judging women's fate, centered on Husband Star and Children Stars, supplemented by Body Vigor and Weakness analysis. **Husband-Children Stars Primary**: When observing women's fate, first examine the Husband Master (Officer-Killing) prosperity and decline, next examine children (Food-Injury) strength and weakness; if Husband prospers and Children flourish, it indicates wealth, nobility, and glory; if Children die and Husband declines, it indicates poverty, solitude, and baseness. **Body Vigor-Weakness Adjustment**: Having husband and children but poverty is due to the Body being in a declining location; lacking husband and children but prosperity is due to the Body residing in a vigorous position. Husband declines while Body is vigorous indicates chastity; Ghost (Killing) prospers while Body is weak indicates solitude and coldness. **Pattern Auspice-Inauspice**: If Noble Person (Tianyi) is few, one is not wealthy but still prosperous; combining with Noble Spirit makes one either a prostitute or nun, indicating promiscuity; Four Pillars with Injury Officer secretly bring wealth damage. Recruiting a son-in-law means Husband is manifest at the doorway; Indirect Husband means Husband is vigorous in Day-Hour positions. **Summary**: When observing Yin fate's Five Elements, precision and detail in clear discrimination are required; one cannot mix this with male fate methods.

- **核心要点**：  
  - 女命以夫星（官杀）子星（食伤）为主，不同于男命以财官印为主  
  - 夫荣子旺主富贵，子死夫衰主贫贱；身旺身衰为调节因素  
  - 夫衰身旺主廉洁，鬼旺身衰主孤寒；贵人少不富亦昌，合贵神主淫贱  
  - 强调"观阴命之五行要精详明辨"，不可套用男命判断法

- **详细解说**：  《阴命赋》以"阴命"二字点题，开篇即建立女命判断的独立体系。其核心逻辑是"夫子为纲、身旺衰为辅"：首先看夫星（官杀）的盛衰来判断婚姻与丈夫运势，其次看子星（食伤）的强弱来判断子息有无与贤愚。"夫荣子旺"是女命最佳配置，主"富贵荣华"；反之"子死夫衰"则为最差配置，主"穷孤下贱"。在夫子之外，日主的旺衰起到调节作用：有夫有子却贫寒，是因为"身在衰乡"，自身承载不起福分；无夫无子却昌盛，是因为"身居旺地"，自身强健可以独立。特别值得注意的是两组对立判断：其一，"夫衰身旺"反而主"廉洁"——丈夫无力约束，女命自守其身；其二，"鬼旺身衰"则主"孤寒"——七杀过强压制弱身，女命备受煎熬。此外，"合贵神非妓即尼"提醒：女命与贵人合化过多，不主尊贵反主淫贱，因合多则情缘纷杂，失其贞节。全篇以"凡观阴命之五行，要精详于明辨矣"收尾，强调女命判断必须自成体系，不可套用男命之法。

- **叙事素材（narrative_snippets）**：
  - `[ns_yhzp_227]` `[trigger: 阴命判断纲领]` `[factor_trigger: yinming AND fuxing_shengshui AND zixing_qiangruo AND caiyin AND caiyin_qing_guansha_zu AND changyin]` `[role: 主干]` 凡观阴命，先观夫主之盛衰；次论身荣，要见子息之强弱。 → 《渊海子平·阴命赋》
  - `[ns_yhzp_228]` `[trigger: 夫荣子旺富贵]` `[factor_trigger: yinming AND furong_ziwang AND fugui AND anchong_qugui AND angui AND caiyin AND caiyin_qing_guansha_zu AND changyin]` `[role: 条件分支]` 夫荣子旺，定知富贵荣华；官杀旺且食伤旺，女命最佳配置。 → 《渊海子平·阴命赋》
  - `[ns_yhzp_229]` `[trigger: 子死夫衰贫贱]` `[factor_trigger: yinming AND zisi_fushuai AND pinqiong AND caiyin AND caiyin_qing_guansha_zu AND changyin AND husband_children_decline]` `[role: 条件分支]` 子死夫衰，只是穷孤下贱；夫子两失为女命最差配置。 → 《渊海子平·阴命赋》
  - `[ns_yhzp_230]` `[trigger: 身在衰乡]` `[factor_trigger: yinming AND shen_shuaixiang AND youfu_pinhan AND caiyin AND caiyin_qing_guansha_zu AND changyin]` `[role: 条件分支]` 有夫有子而贫寒者，盖因身在衰乡；日主衰弱难以承载福分。 → 《渊海子平·阴命赋》
  - `[ns_yhzp_231]` `[trigger: 身居旺地]` `[factor_trigger: yinming AND shen_wangdi AND wufu_changsheng AND caiyin AND caiyin_qing_guansha_zu AND changyin]` `[role: 条件分支]` 无夫无子而昌盛者，亦是身居旺地；日主旺盛可以自立。 → 《渊海子平·阴命赋》
  - `[ns_yhzp_232]` `[trigger: 合贵神淫贱]` `[factor_trigger: yinming AND he_guishen AND yinjian AND anchong_qugui AND angui AND caiyin AND caiyin_qing_guansha_zu AND changyin]` `[role: 例外处理]` 合贵神非妓即尼，论淫贱者；女命合多则情缘纷杂失节。 → 《渊海子平·阴命赋》
  - `[ns_yhzp_233]` `[trigger: 夫衰身旺廉洁]` `[factor_trigger: yinming AND fushuai_shenwang AND lianjie AND caiyin AND caiyin_qing_guansha_zu AND changyin AND husband_weak_body_strong_chaste]` `[role: 条件分支]` 夫衰身旺，主为廉洁之人；丈夫无力约束，女命自守其身。 → 《渊海子平·阴命赋》
  - `[ns_yhzp_234]` `[trigger: 鬼旺身衰孤寒]` `[factor_trigger: yinming AND guiwang_shenshuai AND guhan AND anchong_qugui AND angui AND caiyin AND caiyin_qing_guansha_zu AND changyin AND guhan_guakun]` `[role: 条件分支]` 鬼旺身衰，必作孤寒之妇；七杀过强压制弱身。 → 《渊海子平·阴命赋》
  - `[ns_yhzp_235]` `[trigger: 阴命精详明辨]` `[factor_trigger: yinming AND jingxiang_mingbian AND caiyin AND caiyin_qing_guansha_zu AND changyin]` `[role: 总结]` 凡观阴命之五行，要精详于明辨矣！女命判断自成体系，不可套用男命之法。 → 《渊海子平·阴命赋》"""
    normalized_text_zh: str = """"""
    subject: str = "阴命赋"
    factor_refs: list = ['yin_fate', 'husband_children_prosperity_decline', 'husband_weak_body_strong_chaste', 'ghost_strong_body_weak_solitary', 'combine_noble_promiscuity']
    
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
        l1_anchor="yhzp_v1.0.0_阴命赋_001_L1",
    )
    version: str = "1.0.0"
