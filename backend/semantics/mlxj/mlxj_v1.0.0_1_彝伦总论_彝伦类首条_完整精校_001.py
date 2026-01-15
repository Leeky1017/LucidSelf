"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.840285
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
    semantic_id="mlxj_v1.0.0_1_彝伦总论_彝伦类首条_完整精校_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1彝伦总论彝伦类首条完整精校(SemanticEntry):
    """
    #### 原文（source_text）

凡皇戚，如太上皇太后、后妃之类。三党如三代祖考妣、叔伯舅、甥、姨姑姊妹、妻兄弟、妻姊妹、婿侄等诸亲属，俱以类推之。此梦精神所通，形于梦寐。或地远而心赴，或形...
    """
    
    original_text: str = """#### 原文（source_text）

凡皇戚，如太上皇太后、后妃之类。三党如三代祖考妣、叔伯舅、甥、姨姑姊妹、妻兄弟、妻姊妹、婿侄等诸亲属，俱以类推之。此梦精神所通，形于梦寐。或地远而心赴，或形睽而性接，或别久而思深。如臣不得君，则形于梦君；念臣下则形于梦子；念父母则形于梦父母；思子则形于梦子；夫妻别离则形于梦夫妻；师友契阔则形于梦师友。或休征将至而神先告，或祸咎将临而兆先呈。占者宜精推玄解，不可拘方。

#### 分字分词释义

- **彝伦**：五伦 / 君臣父子夫妇兄弟朋友 / 伦常之道
- **精神所通**：心神感应 / 精神交感 / 灵魂相通
- **地远心赴**：虽然地理遥远，但心神相赴
- **形睽性接**：虽然形体分离，但性灵相接
- **休征**：吉祥之征兆 / 休，美也
- **祸咎**：灾祸过失 / 凶险之兆
- **精推玄解**：精细推断、玄妙解读

#### 规范化释义（primary_lang_explained）

凡是皇戚，如太上皇、太后、后妃之类；三党如三代祖考妣、叔伯舅甥、姨姑姊妹、妻兄弟、妻姊妹、婿侄等诸亲属，都以此类推。

这类梦是精神所通，形于梦寐。或地远而心赴，或形睽而性接，或别久而思深。如臣子思念君主不得见，就会梦见君主；思念臣下就梦见臣下；思念父母就梦见父母；思念子女就梦见子女；夫妻别离就梦见夫妻；师友阔别就梦见师友。

或吉祥之征将至而神明先行告知，或祸咎将临而兆象先行呈现。占断者应当精细推断、玄妙解读，不可拘泥一方。

#### 完整对等诠释（secondary_lang_full）

All imperial relatives such as the Retired Emperor, Empress Dowager, consorts, and the like; relatives from three sides including grandparents of three generations, uncles, nephews, maternal aunts and uncles, wife's siblings, sons-in-law and nephews—all should be interpreted by analogy.

Such dreams arise from the connection of spirits, manifesting in dreams. Perhaps though geographically distant, the heart travels there; though physically separated, the natures connect; though long parted, the longing deepens. When a minister cannot meet his lord, he dreams of the lord; when thinking of subordinates, he dreams of children; thinking of parents, he dreams of parents; missing one's spouse leads to dreams of the spouse; yearning for teachers and friends leads to dreams of them.

Perhaps auspicious signs approach and the spirit forewarns, or calamities loom and omens appear first. Interpreters should analyze subtly and explain profoundly, without rigid adherence to fixed methods.

#### 核心要点

- **精神所通**：亲属梦象的根本原理是心神感应
- **三种感应模式**：
  - 地远心赴：空间距离不阻隔心神
  - 形睽性接：形体分离不阻隔性灵
  - 别久思深：时间久别加深思念
- **五伦对应**：君臣→父子→夫妻→兄弟→朋友
- **双重功能**：休征先告（预示吉）+ 祸咎先呈（预示凶）
- **占断原则**：精推玄解，不可拘方

#### 详细解说

彝伦类是人物梦象中最贴近日常生活的部分。其核心原理是「精神所通」——人与至亲之间存在心灵感应，这种感应可以跨越时空，通过梦境呈现。

「地远心赴」「形睽性接」「别久思深」三种模式，描述了不同类型的亲属感应：空间的、形体的、时间的。无论哪种模式，本质都是心神的交感。

彝伦梦象有两种主要功能：一是预示吉祥（休征先告），二是预示灾祸（祸咎先呈）。占断时需要「精推玄解」，根据具体情况灵活判断。

#### 叙事素材（narrative_snippets）

- `[ns_mlxj_v6_001]` `[trigger: 梦亲属]` `[factor_trigger: dream_jian_qinshu AND dream_ganying AND dream_renlun AND dream_shousuan AND yijing_li AND jingshen_suotong]` `[role: 理论基础]` 此梦精神所通，形于梦寐。或地远而心赴，或形睽而性接，或别久而思深。 → 《梦林玄解·卷六》#彝伦总论
- `[ns_mlxj_v6_002]` `[trigger: 梦亲属]` `[factor_trigger: dream_jian_qinshu]` `[role: 占断原则]` 或休征将至而神先告，或祸咎将临而兆先呈。占者宜精推玄解，不可拘方。 → 《梦林玄解·卷六》#彝伦总论
- `[ns_mlxj_v6_003]` `[trigger: 亲属梦象]` `[factor_trigger: dream_yilun AND dream_laoyou AND dream_youji AND yushi_function]` `[role: 亲属类]` 彝伦、老友、游记等亲属梦象，御史职能。 → 《梦林玄解·卷六》#亲属"""
    normalized_text_zh: str = """"""
    subject: str = "1 彝伦总论（彝伦类首条·完整精校）"
    factor_refs: list = ['jingshen_suotong', 'diyuan_xinfu', 'xingkui_xingjie', 'xiuzheng', 'huojiu']
    
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
        book_id="mlxj",
        chapter="",
        l1_anchor="mlxj_v1.0.0_1_彝伦总论_彝伦类首条_完整精校_001_L1",
    )
    version: str = "1.0.0"
