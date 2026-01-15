"""
Auto-generated semantic module for zipingzhenquan
Generated at: 2025-12-05T13:30:19.523961
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
    semantic_id="zpzq_v1.0.0_何谓救应_八字妙用_全在成败救应_001",
    book_id="zipingzhenquan",
    engine_id="bazi"
)
class 何谓救应八字妙用全在成败救应(SemanticEntry):
    """
    - **原文（source_text）**：
  何谓救应？如官逢伤而透印以解之，杂煞而合煞以清之，刑冲而会合以解之；财逢劫而透食以化之，生官以制之，逢煞而食神制煞以生财，或存财而合煞；印逢财而劫财以...
    """
    
    original_text: str = """- **原文（source_text）**：
  何谓救应？如官逢伤而透印以解之，杂煞而合煞以清之，刑冲而会合以解之；财逢劫而透食以化之，生官以制之，逢煞而食神制煞以生财，或存财而合煞；印逢财而劫财以解之，或合财而存印；食逢枭而就煞以成格，或生财以护食；煞逢食制，印来护煞，而逢财以去印存食；伤官生财透煞而煞逢合；阳刃用官煞带伤食，而重印以护之；建禄月劫用官，遇伤而伤被合，用财带煞而煞被合，是谓之救应也。八字妙用，全在成败救应，其中权轻权重，甚是活泼。学者从此留心，能于万变中融以一理，则于命之一道，其庶几乎。

- 原注（原文注解）：
  　　本段总结“救应”的多种形式：
  - 官逢伤，透印解伤；
  - 杂煞合煞以清；
  - 刑冲以会合解之；
  - 财逢劫，以食化财，以官制之；
  - 印逢财，以劫解财，或用合存印；
  - 食逢枭，就煞成格，或以财护食；
  - 煞逢食制，印护煞，再用财去印存食；
  - 伤官生财透煞，煞逢合则煞清；
  - 阳刃用官煞兼带伤食，重印护之；
  - 建禄月劫用官，逢伤则伤被合，财带煞而煞被合。

- 分字分词释义：
  - 救应：在成/败结构中，负责挽救与调节的那一环。
  - 合煞以清之：通过合化清理杂煞，使煞不杂。
  - 会合以解刑冲：用会局或合局来解除刑冲。
  - 就煞以成格：主动承认煞为用，使煞成为格局主神，而不再视为纯忌。

- **规范化释义（primary_lang_explained）**：
  作者在此总提“救应”的各种工具：
  - 当官星遇伤官时，透出印星来“解伤”，或使伤官佩印；
  - 杂煞太多时，通过合煞、会煞的方式，使煞归一、清纯；
  - 刑冲过重时，借三会六合来解刑冲；
  - 财星被劫时，用食神来化财，再用官星来制裁劫财；
  - 印星被财泄时，用劫财来制财，或用合去财以存印；
  - 食神被枭神克制时，要么索性“就煞成格”，转为煞印格，要么以财来护食，使食神不被夺；
  - 煞星既被食制又有印护，再逢财来去印存食，是“煞有制而不暴，食有用而不偏”；
  - 伤官生财格中若又透出煞星，遇合则煞清、格局反而提升；
  - 阳刃格用官煞制刃、兼带伤食，重印护之，使刃有用而不乱；
  - 建禄月劫用官时，若遇伤官，最好伤被合；用财带煞，煞被合，如此方不破格.

  最后一句“八字妙用，全在成败救应，其中权轻权重，甚是活泼”，点出全书命理的核心：不在死记格名，而在活用成/败/救应三者之间的权衡.能在万变中融会为一个原则，便算真正抓住命理之道.

- **完整对等诠释（secondary_lang_full）**：  
  This paragraph sets out what “remedy and response” (jiu-ying) means in actual chart work. When a properly placed Officer star is harmed by Hurting Officer, the appearance of Resource can absorb that attacking energy and redirect it into learning, culture and inner discipline, so that upright authority is no longer directly undermined. When many different Killings are mixed together and turbid, suitable combinations can bind part of them away so that a single, clean Killing remains to act as command. When the branches are locked in punishments and clashes, three-meeting and six-combination structures can rearrange the support lines so that the original impact no longer falls with its full weight on the key position.
  For Wealth, rescue may come when Food-God appears and transforms Wealth that would otherwise be stolen by Rob Wealth, and when Officer stands out to restrain Rob Wealth itself. For Resource, rescue may come from Rob Wealth cutting back excessive Wealth so that the seal is preserved, or from combinations that take Wealth away and “leave the seal behind”. For Food-God, one path is to “follow Killing and make it the pattern”, turning the configuration into a Killing-and-Resource structure instead of fighting the Owl; another path is to use Wealth to protect Food so that its expressive function is not devoured. For Killing, Food controls it, Resource protects it, and later Wealth can remove surplus Resource so that Food remains as the visible pivot. In Hurting-Officer and Wealth structures, a timely combination that removes exposed Killings can clarify the pattern again. In Yang-Blade and Jianlu–Yuejie structures, strong Officer and Killing, together with Food and heavy seals, can restrain Blade or Rob Wealth while still allowing them to do useful work. All of these are instances of “remedy and response” in action.
  On this basis the author concludes that the subtle art of a chart lies entirely in how completion, failure and remedy interweave. The relative weight of each factor is highly flexible; if one can see a single coherent principle behind this play of support and restraint, one has already come close to grasping the way of destiny reading.

- 详细解说：
  - 命局的高下，不在“有没有问题”，而在“有没有救应".
  - 救应之道，是在既有生克结构上找到“转圜点”，让原本可能成为凶象的地方，转而为成格之助.
  - 成败救应三者合看，才是“活泼”的命理，而非僵化的格局分类.

- 核心要点：
  - 核心要领：
    - 看“成”：用神得位、组合得宜；
    - 看“败”：带忌与破局路线；
    - 看“救”：解伤、解煞、解刑冲、解财印矛盾等。
  - 真正的高明在于，在成败之间寻找救应，使人生走向“趋吉避凶”。

- 应用推演：
  1) 先判断本局属何格，其成格条件是否具备；
  2) 再检查是否“带忌”，有哪些潜在破局点；
  3) 接着寻找“救应”线路：印、合、会、制、化等；
  4) 最后综合成败救应三者之权衡，给出整体评价与实际建议。

- 反例与边界：
  - 只会判“格局好坏”，不会看“救应”，容易给出过于极端的结论。

- 小例（示意）：
  - 一命官格成而带伤，若局中印星透出又不受破，便可视为“有伤有救”，富贵中带坎坷而不至断绝。

  - 校勘与字词辨析：
    - “学者从此留心，能于万变中融以一理，则于命之一道，其庶几乎”：本精校将此句视为本篇总纲，“一理”即为成败救应三者之统一。"""
    normalized_text_zh: str = """"""
    subject: str = "何谓救应？八字妙用，全在成败救应"
    factor_refs: list = ['jiuying', 'hesha_yiqing', 'huihe_jiexingchong', 'jiusha_chengge', 'touyin_jieshang', 'engine_id', 'jiuying_type', 'bazi_rule_engine', 'jiuying_daowei', 'bazi_rule_engine', 'jiuying_guanxi', 'bazi_rule_engine', 'chengbai_jiuying_zonghe', 'bazi_rule_engine', 'source_ref', 'rel_zpzq_100', 'jiuying_type', 'rel_zpzq_101', 'jiuying_daowei', 'rel_zpzq_102', 'chengbai_jiuying_zonghe', 'evi_zpzq_096', 'touyin_jieshang', 'rule_guanfengshang_touyin', 'evi_zpzq_097', 'chengbai_jiuying_zonghe', 'rule_chengbai_jiuying_core', 'concept_remedy', 'concept_dynamic_balance', 'concept_core_principle']
    
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
        book_id="zipingzhenquan",
        chapter="",
        l1_anchor="zpzq_v1.0.0_何谓救应_八字妙用_全在成败救应_001_L1",
    )
    version: str = "1.0.0"
