"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.789132
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
    semantic_id="mlxj_v1.0.0_1_五神传梦基本原理_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1五神传梦基本原理(SemanticEntry):
    """
    #### 原文（source_text）

身有五脏，脏有五神，神有五运。夫人梦则魂交，神为之也。发于五脏，窍于泥丸，万事万物，各属本脏，乃传本神。正气旺，是相生，相生者为吉为休；客邪胜，是相克，相克...
    """
    
    original_text: str = """#### 原文（source_text）

身有五脏，脏有五神，神有五运。夫人梦则魂交，神为之也。发于五脏，窍于泥丸，万事万物，各属本脏，乃传本神。正气旺，是相生，相生者为吉为休；客邪胜，是相克，相克者为凶为悔。正邪相乘，生克迭变。

#### 规范化释义（primary_lang_explained）

人身有五脏（肝心脾肺肾），五脏各有其神（魂魄意志精），五神各有其运行规律。人做梦时是魂在交游，由神所主导。梦发于五脏，通窍于泥丸宫（脑），万事万物各归属于本脏，传于本神。

正气旺盛时，是相生关系，相生者主吉、主休（安）；客邪得胜时，是相克关系，相克者主凶、主悔。正气与邪气相互作用，生克不断变化。

#### 完整对等诠释（secondary_lang_full）

The human body has five viscera (liver, heart, spleen, lungs, kidneys), each viscus has its spirit (Hun, Po, Yi, Zhi, Jing), and each spirit has its operational pattern. When dreaming, the Hun (ethereal soul) engages in communion, directed by the spirits. Dreams originate from the five viscera and connect through the Niwan Palace (brain). All things in dreams belong to their respective viscera and transmit through their corresponding spirits.

When vital Qi is flourishing, relationships are generative—generative patterns indicate fortune and peace. When pathogenic influences prevail, relationships are restrictive—restrictive patterns indicate misfortune and regret. Vital and pathogenic forces interact continuously, with generative and restrictive patterns alternating.

#### 核心要点

- **五脏**：肝、心、脾、肺、肾
- **五神**：魂（肝）、神（心）、意（脾）、魄（肺）、志（肾）
- **梦发机制**：发于五脏，窍于泥丸
- **吉凶判断**：相生为吉为休，相克为凶为悔
- **动态原理**：正邪相乘，生克迭变

#### 叙事素材（narrative_snippets）

- `[ns_mlxj_v24_001]` `[trigger: 五神传梦]` `[factor_trigger: wushen_system AND wushen AND wuzang AND dream_wushen_zhengchuan AND dream_wushen_nichuan AND niwan AND meng]` `[role: 理论基础]` 身有五脏，脏有五神，神有五运。夫人梦则魂交，神为之也。梦发于泥丸。 → 《梦林玄解·卷二十四》#五神传梦
- `[ns_mlxj_v24_002]` `[trigger: 生克判断]` `[factor_trigger: shengke_pattern AND shengke AND jixi AND dream_jizhao AND dream_xiongzhao AND shengke_zhuanhua]` `[role: 判断规则]` 正气旺是相生，相生者为吉为休；客邪胜是相克，相克者为凶为悔。 → 《梦林玄解·卷二十四》#五神传梦
- `[ns_mlxj_v24_003]` `[trigger: 五神传序]` `[factor_trigger: wushen_pi AND wushen_fei AND wushen_shen AND wushen_shengxu AND wushen_kexu AND wushen_shunhuan AND wushen_nihuan]` `[role: 传序规则]` 脾→肺→肾→肝→心为正传占吉，脾→肾→心→肺→肝为逆传占凶。 → 《梦林玄解·卷二十四》#五神传梦
- `[ns_mlxj_v24_004]` `[trigger: 阴阳气态]` `[factor_trigger: yangqi AND yinqi AND yinyang_state AND yangyin]` `[role: 诊断依据]` 阳气盛阴气衰，或阴气盛阳气衰，皆影响梦象吉凶。 → 《梦林玄解·卷二十四》#五神诊法
- `[ns_mlxj_v24_005]` `[trigger: 八卦配属]` `[factor_trigger: bagua AND shixu_pinghe AND shiwu_lei AND wulei AND dream_core AND dream_exception]` `[role: 配属体系]` 五神配八卦，实虚平和诊断，事物分类。 → 《梦林玄解·卷二十四》#五神配八卦
- `[ns_mlxj_v24_006]` `[trigger: 元素梦象]` `[factor_trigger: dream_fire AND dream_water AND baoyuan AND dream_type AND tiaoyang AND gan_shen]` `[role: 元素对应]` 火水等元素梦象，调阳保元，肝神等脏神对应。 → 《梦林玄解·卷二十四》#五神事物"""
    normalized_text_zh: str = """"""
    subject: str = "1 五神传梦基本原理"
    factor_refs: list = ['wushen', 'niwan', 'zhengxie_xiangcheng']
    
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
        l1_anchor="mlxj_v1.0.0_1_五神传梦基本原理_001_L1",
    )
    version: str = "1.0.0"
