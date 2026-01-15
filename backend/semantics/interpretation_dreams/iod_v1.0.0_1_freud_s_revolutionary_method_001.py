"""
Auto-generated semantic module for interpretation_dreams
Generated at: 2025-12-05T13:30:20.460871
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
    semantic_id="iod_v1.0.0_1_freud_s_revolutionary_method_001",
    book_id="interpretation_dreams",
    engine_id="dream"
)
class 1FreudSRevolutionaryMethod(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Free Association | Uncensored reporting | Core technique |
| Fragmentation | Break dream into parts | Not interpret as whole |
| No Dismissal | Include trivial/absurd | Everything meaningful |
| Overdetermination | Multiple meanings | Condensed in each element |

**Source Text**:

The first step in the application of my method consists in my turning my attention not to the dream as a whole but to the separate portions of its content. If a patient says to me: "I have dreamed," I demand from him: "Tell me where the dream begins to dissolve into parts; tell me the most unimportant and absurd details—everything, even what seems to you insignificant." And then I ask him to tell me what occurs to him in connection with each fragment, what "associations" present themselves if he focuses his attention on each portion taken singly instead of on the dream as a whole.

**English Paraphrase**:

Freud's method radically breaks from previous approaches. Instead of interpreting the dream as a unified symbol, he asks the dreamer to break the dream into fragments—even the most trivial, absurd details. Then, for each fragment, the dreamer reports whatever comes to mind: thoughts, memories, feelings that "associate" with that element. This technique, **free association**, bypasses conscious interpretation and reveals unconscious connections.

**Complete Chinese Interpretation (Secondary Language)**:

在方法论层面，弗洛伊德以**自由联想**彻底颠覆了传统“解梦书”模式。过去的做法，把梦视为一个整体符号，试图用固定对照关系去翻译——例如“水=情感，山=障碍，上楼=性行为”等。弗洛伊德则要求把梦**拆解成最细小的片段**：人物、动作、物件、颜色，甚至看似荒谬、无关紧要的细节，都要单独拿出来处理。

对每一个片段，分析者并不马上给出解释，而是要求梦者**毫无筛选地说出一切浮现的念头**：与之相关的记忆、联想、情绪、念头——无论看上去多么琐碎、离题或难堪，都必须被“如实报告”。这种程序看似简单，却要求梦者暂时放下平时对思维的审查与整理习惯，允许意识流直接流向语言。

自由联想之所以有效，正是因为梦的工作本来就是沿着**联想链**来变形潜梦思想：重要观念被移置到邻近联想对象上，多重记忆被凝缩进一个形象里。通过顺着显梦片段去联想，我们就有机会**逆向追踪这些联结路径**，把被压缩、伪装的意义重新展开。因此，在弗洛伊德那里，释梦不再依赖外部权威的“标准答案”，而是依赖梦者内在联想网络所呈现出的结构。

**Core Points**:
- Revolutionary departure from previous symbol-dictionary approaches
- Fragment the dream into separate elements
- Include trivial and absurd details (nothing dismissed)
- Free association to each fragment individually
- Report whatever comes to mind without censorship
- Bypasses conscious interpretation to access unconscious
- Reveals hidden connections and latent meanings

**Detailed Explanation**:

This marks Freud's break with all previous dream interpretation. Traditional approaches treated dreams as unified symbols requiring decoding via fixed meanings (water = birth, climbing = sex, etc.). Freud rejects this entirely.

**The Free Association Technique**:

1. **Fragmentation**: Break dream into smallest elements, not interpret as whole
2. **No Dismissal**: Include absurd, trivial, embarrassing details
3. **Suspended Judgment**: Don't evaluate what arises; just report it
4. **Following Chains**: Each association leads to another, following unconscious logic
5. **Patience**: May take time to reach meaningful material

**Why This Works**: Dreams are **overdetermined**—each element condenses multiple meanings. By fragmenting and freely associating, we unpack compressed material, following associative chains back to latent thoughts.

**Example Process**:
- Dream element: "A yellow lion"
- Association 1: "My yellow coat"
- Association 2: "My father called me cowardly (yellow)"
- Association 3: "Lion = Leo = my father's astrological sign"
- **Latent meaning emerges**: Dream expresses conflict with father

The method assumes dreams are **meaningful psychological products**, not random neural noise. Every element, however absurd, connects to significant mental material.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Free Association: Revolutionary break from symbol-dictionaries. Fragment dream, associate to each part. Bypasses conscious censorship. Follows associative chains to latent thoughts. Assumes dreams are meaningful.
- **中文**: 自由联想:革命性突破符号词典模式。分解梦,对每部分联想。绕过意识审查。沿联想链追溯潜梦思想。假定梦有意义。

**Narrative Snippets**:
- `[ns_freud_ch2_001]` `[trigger: free_association]` `[factor_trigger: freud_technique]` `[role: 主干]` Free association: revolutionary break from symbol-dictionaries; fragment dream, associate to each part. → Core
- `[ns_freud_ch2_002]` `[trigger: fragmentation_method]` `[factor_trigger: freud_technique AND process]` `[role: 条件分支]` Include trivial/absurd details; no dismissal; suspended judgment; follow associative chains. → Method
- `[ns_freud_ch2_003]` `[trigger: overdetermination_principle]` `[factor_trigger: freud_technique AND interpretation]` `[role: 条件分支]` Dreams overdetermined—each element condenses multiple meanings; unpack via association. → Theory"""
    normalized_text_zh: str = """"""
    subject: str = "1 Freud's Revolutionary Method: Free Association"
    factor_refs: list = []
    
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
        book_id="interpretation_dreams",
        chapter="",
        l1_anchor="iod_v1.0.0_1_freud_s_revolutionary_method_001_L1",
    )
    version: str = "1.0.0"
