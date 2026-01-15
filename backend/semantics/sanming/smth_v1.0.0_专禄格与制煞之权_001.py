"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.458364
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
    semantic_id="smth_v1.0.0_专禄格与制煞之权_001",
    book_id="sanming",
    engine_id="bazi"
)
class 专禄格与制煞之权(SemanticEntry):
    """
    - **原文（source_text）**：
  此格：六庚日见巳时，庚金长生之地，内有丙戊二禄。戊生庚，丙为庚煞；柱要壬癸制丙，当为武帅持权。若逢煞运，不吉。
  
  诗曰：专禄庚来就巳位，也须制...
    """
    
    original_text: str = """- **原文（source_text）**：
  此格：六庚日见巳时，庚金长生之地，内有丙戊二禄。戊生庚，丙为庚煞；柱要壬癸制丙，当为武帅持权。若逢煞运，不吉。
  
  诗曰：专禄庚来就巳位，也须制伏始为奇。武职当权为帅座，忽逢七煞祸来时。

- 分字分词释义：
  - **专禄**：指日主一身专享禄位之地，如庚日见巳时，巳为庚之长生，禄气集中于一处。
  - **六庚日见巳时**：十天干中庚日（六庚）坐巳时，巳火为金之长生，内藏丙戊，为庚金的食神与偏财（或禄神）。
  - **丙戊二禄**：巳中丙火、戊土对庚金而言，皆有禄、用之象：戊能生庚为财源，丙又为庚之煞与权柄。
  - **壬癸制丙**：壬癸水透出，以水克火制丙，使煞不致失控而伤身。
  - **武帅持权**：指武职高权，如统兵之将帅，握有实权。

- **规范化释义（primary_lang_explained）**：
  专禄格是指禄气集中于一处、日主一身专受禄位之象。以庚日见巳时为例：巳为庚金长生之地，巳中又藏丙火、戊土两种禄用之物——戊土能生庚金为财源，丙火则为庚之七煞、权柄所在。因此，此格若能再得壬癸水透出制伏丙火，则煞可为用，形成"专禄而有制"的局面，多主武职当权，为将帅之命。
  
  然而，一旦行运再遇煞地，而制煞之水不足或受损，则七煞之力难以约束，原本的权煞之力易转为祸患，故诗云："专禄庚来就巳位，也须制伏始为奇；武职当权为帅座，忽逢七煞祸来时"。

- **完整对等诠释（secondary_lang_full）**：
  The 'exclusive salary' pattern is illustrated by the six Geng days that see Si hour. There, Geng metal stands in its place of growth, and within Si are hidden Bing fire and Wu earth, both acting as forms of salary: Wu earth generates Geng as a source of wealth, while Bing fire is its Seven Killing and the symbol of martial power. If Ren or Gui water also appears on the stems to restrain Bing, the Killing is held in check and becomes usable, so that the native can hold real military authority as a commander. If, however, later fortunes move into further Killing lands without adequate water to restrain Bing, the same concentrated salary and power turn into danger, just as the verse warns that when the exclusive salary Geng comes to Si it must be controlled to be marvellous, and that a marshal in full command can suddenly meet disaster when Seven Killing surges unchecked.


- 核心要点：
  - 专禄格的关键在于**禄气集中且有煞可制**：禄专而不散，煞有制而不猛。
  - 庚日巳时为典型例子：巳为长生之地，藏丙戊二禄，若再得壬癸制丙，则易成武权之贵。
  - 若运中再逢煞地而制煞之力不足，则原有贵气易反转为灾祸。

- 详细解说：
  在传统格局中，"禄"代表俸禄、职位与现实资源，"专禄"则意味着这类资源高度集中：日主在某一宫位（如时柱）获得极强的支持。这样的结构若配合得当，可使命主在某一个领域（多为武职或带权职位）高度成功；但一旦制衡失当，也容易走向偏激。
  
  庚日巳时的例子中，巳为火地，庚金居其间，一方面象征金投火炼而成器，另一方面也使庚金在此得禄；巳中戊土生庚，为财之源；丙火为煞，为权力与危险并存之象。若命局中再有壬癸水透出，则水火相制，煞气得以约束，日主可凭借专禄与煞权，成为掌兵、掌刑之人。反之，若行运再加重火煞、削弱壬癸，则煞气难制，易有兵祸、官灾等事。

 - 校勘与字词辨析：
  - "六庚日见巳时"之说，沿用古命书称呼十干中庚日为"六庚"，本稿不改其传统称呼，仅在释义中解释。
  - 诗句"专禄庚来就巳位"等语保留原文格式，仅在标点上作现代化处理，以利阅读。
  - **English**：
    - Modern punctuation applied for readability.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_05_068]` `[trigger: 专禄结构]` `[factor_trigger: zhuanlu_presence AND luqi_jizhong_config]` `[role: 主干]` 六庚日见巳时，庚金长生之地，内有丙戊二禄。 → 《三命通会》卷五#专禄格
  - `[ns_smth_05_069]` `[trigger: 武帅持权]` `[factor_trigger: zhisha_dedang_condition AND wuquan_weishi_score]` `[role: 主干依赖]` 柱要壬癸制丙，当为武帅持权。 → 《三命通会》卷五#专禄格
  - `[ns_smth_05_070]` `[trigger: 运逢煞地]` `[factor_trigger: yunfeng_shadi_risk]` `[role: 条件分支]` 若逢煞运，不吉。 → 《三命通会》卷五#专禄格
  - `[ns_smth_05_071]` `[trigger: 制伏始奇]` `[factor_trigger: zhuanlu_presence AND zhi_fu_wei_qi]` `[role: 总结]` 专禄庚来就巳位，也须制伏始为奇。 → 《三命通会》卷五#专禄格"""
    normalized_text_zh: str = """"""
    subject: str = "专禄格与制煞之权"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'zhuanlu_presence', 'bazi_semantic', 'luqi_jizhong_config', 'bazi_semantic', 'shaquan_pingheng_score', 'bazi_semantic', 'wuquan_weishi_score', 'bazi_semantic', 'zhisha_dedang_condition', 'bazi_semantic', 'yunfeng_shadi_risk', 'bazi_semantic', 'source_ref', 'rel_smth_05_052', 'zhuanlu_presence', 'rel_smth_05_053', 'wuquan_weishi_score', 'rel_smth_05_054', 'yunfeng_shadi_risk', 'evi_smth_05_052', 'zhisha_dedang_condition', 'rule_wuquan', 'evi_smth_05_053', 'luqi_jizhong_config', 'rule_luqi', 'evi_smth_05_054', 'yunfeng_shadi_risk', 'rule_shayun', 'map_smth_05_035', 'map_smth_05_036']
    
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
        l1_anchor="smth_v1.0.0_专禄格与制煞之权_001_L1",
    )
    version: str = "1.0.0"
