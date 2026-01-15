"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.288945
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
    semantic_id="smth_v1.0.0_土_湿燥平衡与承载中枢_001",
    book_id="sanming",
    engine_id="bazi"
)
class 土湿燥平衡与承载中枢(SemanticEntry):
    """
    - **原文（source_text）**：
  论土。土值春时，土膏脉起，万物含生，木气发泄，前哲所谓病寅、死卯、墓辰者，良有以也。雨则阴凝土湿而荫甲不舒，晴则冻释阳和而生意发越，故春令之土一接阳气...
    """
    
    original_text: str = """- **原文（source_text）**：
  论土。土值春时，土膏脉起，万物含生，木气发泄，前哲所谓病寅、死卯、墓辰者，良有以也。雨则阴凝土湿而荫甲不舒，晴则冻释阳和而生意发越，故春令之土一接阳气，就能发育万物。正月之土尚有霜寒，遇雨则冻，遇水则冰，值木则病，惟得火以温之，则荣华莫比，逢金制木，亦名利两成。二月之土，正木盛土崩之时，遇木同躔，有脾胃肠风痔漏之灾，轻者疾，重者夭，徐、扬人干支有火而值昼晴者，无咎，见火同躔，位登台鼎，见水则凶，冀、雍、青、兖人土浑水浊，终有水涌土溃之危，盖水生旺木而伤土也，值此者贫寒疾夭，徐、扬、豫人干支火者反吉，见金以泄土气，难免灾凶。三月之土，渐有生意，盖土旺季月故也，有火温燠则阳气发舒而生物茂矣，见木非疾则夭，徐、扬、豫人无害，水木同度，贫薄无聊，冀、雍、兖、青人尤甚，见金制木，反凶成吉，运喜南方，西方次之。土旺长夏，火盛土生之故也，阴雨则湿养万物，故见水为吉；亢旱则田畴龟裂，故遇火为凶。孟夏之土，炎气未盛，终喜火以助之，逢木则疾夭无疑，见水为财，徐、扬人富足，见金遇木则贵，逢水则贫。五、六月之土，见火则燥，而万物焦枯，徐、扬人干支火盛者，有火焚风血之灾，轻者危，重者死，或阴雨，或夜生，虽灾不甚。冀、雍人干支有壬、癸、亥、子者，富贵非凡，见水滋养万物，主富贵文章，见木疏通其性，多聪明特达，遇金无用，盖火盛金衰不能制木，所以金无用也，气运宜行西北，最忌南方，盖夏土逢火，太燥故也。土逢秋令，金气盛旺，泄土而气薄矣，晴雨须要得宜。七月之土，火气未除，土性尚燥，喜水滋之，则万物实矣，若火太盛，亦有燥土之嫌，得水济之为妙，逢木为灾，徐、扬、荆、梁人无忌。八、九月之土，见木则不能克，此万物凋零之时，金气生旺，子复母仇，荆、梁、徐、扬人富贵而寿，见金泄气太甚，西北人不免有冷退怯弱之患，见火助之，文武名高，君子小人皆吉，见水为财，徐、扬、豫人富而无敌，冀、雍、兖、梁人水过盛者反主贫薄，戌月仅可，运喜火土之乡，水木金方有忌。土于冬也，正天地肃杀之时，寒亦至矣，虽一阳下生，土脉未温，值水雪，则冰寒土冻，见火日则寒谷回春。十月之土，惟喜火以温之，则土脉阳和而万物归根矣，见木则凶，逢金则滞，遇水则主孤寒，徐、扬人干支火多者可富。子丑之月，寒气之极，火日融和，功名成就，见木最忌，见火解之为吉，见水则阴气愈甚，水寒地冻，轻者疾，重者夭，见金亦主贫薄，岁运南方最佳，北方大忌。

 - 分字分词释义：
  - **土膏脉起**：春时土气回升、土中阳气萌动，好比土地苏醒，具备承载与滋养能力。
  - **病寅、死卯、墓辰**：以土对春木之病死墓而言，指出木旺之时土易受伤，提醒「木盛土崩」的时令背景。
  - **土崩**：木盛过度、土失其位，象征承载结构被掏空，易出脾胃与基础支撑方面的问题。
  - **湿养 / 龟裂**：水与火作用于土的两极状态：适水则滋润万物，过旱则土地龟裂，比喻资源与安全边界的不同状态。
  - **金无用**：火盛土旺之时，金力被削弱，虽有金而难以承担制木之职，提示某些理论上的「克」在实际气候中无法生效。
  - **冷退怯弱**：土在秋冬被金水泄弱而缺乏温度与支撑时，容易表现为保守、退缩与体质虚冷。

 - 白话原意：
  土在四时与不同地域中，总是担任「承载与调剂」的角色：春土一接阳气，膏脉渐起，能扶助萌芽，却又最怕木气太盛以致「木盛土崩」；长夏火旺土旺，阴雨则成滋润沃土，亢旱则为燥裂之田；秋令金气泄土，使土性转薄，既忌再受木耗，又需少火温养；冬令水旺土衰，须借火暖与节制之水，方免「土浑水溺」。因时因地调其湿燥与载荷，土方能稳居中宫，成为全局的承载中枢。

 - 核心要点：
  - 土主承载与中和，一方面托起万物生长，一方面承接水火木金的变化压力，是安全边界与根基厚薄的关键指标。
  - 春季木旺之时易「木盛土崩」；长夏火炽则有「夏土逢火太燥」之忧；秋金泄土、冬水浊土，各有不同的薄弱环节。
  - 调土之道在于水火决定湿燥、木金决定负载与约束，不能只以「土多/土少」粗略判断吉凶。
  - 不同地域（徐扬、兖青、冀雍、荆梁等）本身的寒热干湿与社会环境，会放大或缓和上述象意，论命时须连同出生地一并考量。

 - 详细解说：
  春令之土，一接阳气便可「土膏脉起」，承载萌芽、发育万物，但寅卯辰为木旺之乡，土处其中往往被木气穿透，所以说「木盛土崩」。原文以脾胃肠风、痔漏等病象喻之，意在说明：当木气过度疏泄而土失其位时，无论在身体、家业还是制度根基上，都容易出现「基础被掏空」的问题，须以火温土、以金节木，方能转危为安。

  至长夏土旺之际，火盛土生，一方面能成为众物扎根之沃壤，另一方面又极易因炎热而燥裂。阴雨与适度水分，可以使土保持「湿养」之状，利于万物成长；若亢旱无雨，则「田畴龟裂」，在命局上常见为内心干枯、脾胃火盛、环境焦躁等象。原文明言徐、扬等南方火土本旺之地，更怕夏土再逢火运；反之，冀、雍等偏寒之地，若得壬癸亥子之水滋养，则土得其润，反成富贵文章之资。

  秋令金气盛旺，本来就泄土元气，故此时之土「气薄」而不耐再耗；若仍逢木来克土，则有克伐争竞之忧，宜借少火温土，使之不至冷退怯弱。冬月水旺，水多则土浑，水尽则土坚：少水足以滋润，水太盛则反致土溺。十、十一、十二月之土，各随水火金木多寡而有不同病象与解法：或借火以温土，或用木来疏土性，或以节水护土，总不外在「不过不及」之间求中和。

 - 校勘与字词辨析：
  - 「病寅、死卯、墓辰」为古法所称土在寅卯辰三支上的病、死、墓地位，并非日常语义中的「生病/死亡/坟墓」，而是用来概括春木正盛时土势渐衰、承载困难的状态。
  - 「土膏脉起」中的「膏」指地中肥膏、「脉」指土气脉动，用以形容春天土气自下而上萌动苏醒之状，说明此时只要阳气微接，土便具备滋养与承载的潜力。
  - **English**：
    - Day-master strength analysis terms clarified; pattern formation conditions explained with structural logic."""
    normalized_text_zh: str = """"""
    subject: str = "土：湿燥平衡与承载中枢"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'earth_moist_dry_bearing_state', 'bazi_semantic', 'spring_earth_wood_collapse_risk', 'bazi_semantic', 'midsummer_earth_moist_vs_cracked', 'bazi_semantic', 'autumn_earth_metal_drains_thin', 'bazi_semantic', 'winter_earth_needs_fire_control_water', 'bazi_semantic', 'earth_region_moisture_profile', 'bazi_semantic', 'source_ref', 'rel_smth_04_061', 'spring_earth_wood_collapse_risk', 'rel_smth_04_062', 'midsummer_earth_moist_vs_cracked', 'rel_smth_04_063', 'winter_earth_needs_fire_control_water', 'evi_smth_04_061', 'spring_earth_wood_collapse_risk', 'rule_spring_earth', 'evi_smth_04_062', 'midsummer_earth_moist_vs_cracked', 'rule_summer_earth', 'evi_smth_04_063', 'winter_earth_needs_fire_control_water', 'rule_winter_earth', 'map_smth_04_041', 'map_smth_04_042']
    
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
        l1_anchor="smth_v1.0.0_土_湿燥平衡与承载中枢_001_L1",
    )
    version: str = "1.0.0"
