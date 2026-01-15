"""
Auto-generated semantic module for christian_astrology
Generated at: 2025-12-05T13:30:20.147443
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
    semantic_id="ca_v1.0.0_health_and_illness_questions_001",
    book_id="christian_astrology",
    engine_id="astro"
)
class HealthAndIllnessQuestions(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Latin/English | Definition | Significance |
|------|---------------...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Latin/English | Definition | Significance |
|------|---------------|------------|---------------|
| 6th house | Domus VI | Disease, illness | Signifies the malady itself |
| L1 vs L6 | Patient vs Disease | Relative strength comparison | Determines recovery prognosis |
| 7th house | Domus VII | Physician, doctor | The healer consulted |
| 10th house | Domus X | Medicine, treatment | The cure applied |

**Source Text** (Synthesized from Lilly Book II):
> In questions of sickness, the Ascendant and its Lord signify the sick person; the 6th House and its Lord, the disease itself; the 7th House, the physician; the 10th, the medicine. If the Lord of the Ascendant be stronger than the Lord of the 6th, the native shall overcome the disease.

**English Paraphrase (Primary Language)**:

**Health/Illness questions** use multiple houses:

| House | Significator | Meaning |
|-------|--------------|---------|
| 1st | L1 | The sick person (querent) |
| 6th | L6 | The disease/illness itself |
| 7th | L7 | The physician/doctor |
| 10th | L10 | The medicine/treatment |
| 8th | L8 | Death (if prognosis asked) |

**Judgment patterns**:

| Configuration | Prognosis |
|--------------|-----------|
| L1 stronger than L6 | Recovery likely |
| L6 stronger than L1 | Disease prevails |
| L1 separating from L6 | Already recovering |
| L1 applying to L6 | Getting worse |
| L1 in 6th house | Querent weakened by illness |
| Benefics aspecting L1 | Help and recovery |
| Malefics aspecting L1 | Complications |

**Complete Chinese Interpretation (Secondary Language)**:

**健康/疾病问题**使用多个宫位：

| 宫位 | 象征星 | 含义 |
|------|--------|------|
| 第1宫 | L1 | 病人（问卜者） |
| 第6宫 | L6 | 疾病本身 |
| 第7宫 | L7 | 医生 |
| 第10宫 | L10 | 药物/治疗 |
| 第8宫 | L8 | 死亡（若问预后） |

**判断模式**：

| 配置 | 预后 |
|------|------|
| L1 比 L6 强 | 可能康复 |
| L6 比 L1 强 | 疾病占上风 |
| L1 离开 L6 | 已在康复 |
| L1 趋近 L6 | 正在恶化 |
| L1 在第6宫 | 问卜者被疾病削弱 |
| 吉星相位 L1 | 有帮助和康复 |
| 凶星相位 L1 | 有并发症 |

**Core Points**:
- 1st house = patient, 6th house = disease
- L1 vs L6 strength determines outcome
- Application/separation shows disease trajectory
- 7th = doctor, 10th = medicine

#### Narrative Snippets

- `[ns_lilly_033]` `[trigger: horary_health]` `[factor_trigger: horary_6th_house]` `[role: 主干]` In sickness questions: 1st house and its lord = the patient; 6th house and its lord = the disease. Compare their dignities to judge who prevails. → Christian Astrology Health
- `[ns_lilly_034]` `[trigger: health_prognosis]` `[factor_trigger: L1_L6_strength AND astro_prognosis]` `[role: 主干依赖]` If L1 stronger than L6, patient overcomes disease. If L6 stronger, disease prevails. L1 separating from L6 = recovering; applying = worsening. → Christian Astrology Health
- `[ns_lilly_035]` `[trigger: medical_help]` `[factor_trigger: horary_7th_doctor AND astro_physician_help]` `[role: 总结]` 7th house = physician consulted; 10th house = medicine/treatment. Benefic aspects to L1 indicate help and recovery. → Christian Astrology Health

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Medical horary was crucial in Lilly's era before modern diagnostics. The 6th house for disease derives from its position opposite the 12th (hidden enemies within). The 7th for physician reflects the "other person consulted." Lilly's method assesses relative strength (patient vs disease) rather than diagnosing specific conditions.
- **中文**: 医疗占星在Lilly时代现代诊断之前至关重要。第6宫用于疾病源于其与第12宫（内在隐敵）的对宫位置。第7宫用于医生反映"被咨询的他人"。Lilly的方法评估相对强度（病人 vs 疾病）而非诊断具体病情。"""
    normalized_text_zh: str = """"""
    subject: str = "Health and Illness Questions"
    factor_refs: list = ['house_6_disease', 'new_candidate', 'disease_trajectory', 'benefic_assistance', 'house_7_doctor', 'house_10_medicine']
    
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
        book_id="christian_astrology",
        chapter="",
        l1_anchor="ca_v1.0.0_health_and_illness_questions_001_L1",
    )
    version: str = "1.0.0"
