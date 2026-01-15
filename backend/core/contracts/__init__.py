"""
LucidSelf Core Contracts

数据契约层 - 所有 Pydantic 模型定义。
对照文档: docs/数据契约_Schema定义规范_v1.md

模块结构:
- base: 基础类型（FactorCategory, SourceMetadata）
- config_models: 配置态模型（ConfigFactor, ConfigRuleDefinition）
- runtime_models: 运行态模型（FactorValue, FactorMatrix, RuntimeRuleResult）
- narrative_models: 叙事与融合模型（NarrativeConfig, FusionResult）
- memory_models: 记忆层模型（Event, Insight, UserProfile）
- toon_models: TOON 协议模型（ToonPayload）
- engine_models: 引擎注册表模型（EngineDescriptor）
- test_schema_models: 三层测试体系模型（RuleTestCase, GoldenCase, NarrativeGolden）
- l25_models: L2.5 桥接层模型（ConfigRelation, EvidenceChainEntry, CrossSystemMapping）
- narrative_snippet_models: 叙事素材模型（NarrativeSnippet, LogicChain, AssemblyProtocol）
- cross_domain_models: 跨域轴模型（CrossDomainAxes）

v0.9.0 更新：
- 新增 L2.5 桥接层 Schema（数据契约 v1.1 §1.5）
- 新增叙事素材 Schema（数据契约 v1.1 §3.4-3.6）
- 新增 CrossDomainAxes（schema-core spec v0.4.0）
- RuntimeRuleResult 新增 cross_domain_axes 字段
"""

from backend.core.contracts.base import (
    FACTOR_ID_PATTERN,
    RULE_ID_PATTERN,
    VERSION_PATTERN,
    FUSION_ID_PATTERN,
    EVENT_ID_PATTERN,
    INSIGHT_ID_PATTERN,
    LOCALE_PATTERN,
    FactorCategory,
    StatusEnum,
    SourceMetadata,
)

from backend.core.contracts.config_models import (
    ConfigFactor,
    RuleCondition,
    LogicalExpression,
    ConfigRuleResult,
    ConfigRuleDefinition,
)

from backend.core.contracts.runtime_models import (
    FactorValue,
    FactorMatrix,
    RuntimeRuleResult,
)

from backend.core.contracts.narrative_models import (
    NarrativeConfig,
    ConflictWarning,
    FusionResult,
)

from backend.core.contracts.memory_models import (
    PrivacyLevel,
    MemoryBase,
    SENSITIVE_FIELDS,
    Event,
    Insight,
    UserProfile,
)

from backend.core.contracts.toon_models import (
    TOON_SYNTAX,
    ABBREVIATIONS,
    ABBREVIATIONS_REVERSE,
    TOON_CONSTRAINTS,
    ToonPayload,
)

from backend.core.contracts.engine_models import (
    EngineDescriptor,
    ENGINE_REGISTRY_CONSTRAINTS,
    ENGINE_KINDS,
    SUPPORTED_SYSTEMS,
)

from backend.core.contracts.test_schema_models import (
    RuleTestCase,
    GoldenCase,
    NarrativeGolden,
    TEST_PYRAMID_STANDARDS,
    RELEASE_CHECKLIST,
)

# L2.5 桥接层模型 (v1.1 §1.5)
from backend.core.contracts.l25_models import (
    RELATION_ID_PATTERN,
    EVIDENCE_ID_PATTERN,
    CONCEPT_ID_PATTERN,
    RelationType,
    EffectDirection,
    ConfidenceLevel,
    ConfigRelation,
    EvidenceChainEntry,
    CrossSystemMapping,
)

# 叙事素材模型 (v1.1 §3.4-3.6)
from backend.core.contracts.narrative_snippet_models import (
    SNIPPET_ID_PATTERN,
    CHAIN_ID_PATTERN,
    PROTOCOL_ID_PATTERN,
    SnippetRole,
    ConflictResolutionStrategy,
    NarrativeOrderStrategy,
    NarrativeSnippet,
    LogicNode,
    LogicEdge,
    LogicChain,
    AssemblyProtocol,
)

# 跨域轴模型 (schema-core spec v0.4.0)
from backend.core.contracts.cross_domain_models import (
    CrossDomainAxes,
)

# Action 层模型 (Phase 5.5 Action Compiler Layer)
from backend.core.contracts.action_models import (
    ACTION_PROJECT_ID_PATTERN,
    ACTION_ITEM_ID_PATTERN,
    ActionSourceKind,
    ActionTimeScope,
    ActionContext,
    ActionStatus,
    EffortEstimate,
    InsightCompileStatus,
    ActionBase,
    ActionSourceRef,
    ActionProject,
    ActionItem,
    InsightCompileRecord,
    AvoidanceInsight,
)

# 验证工具 (calculator-integration spec §10)
from backend.core.contracts.validation import (
    VALID_SYSTEM_PREFIXES,
    VALID_SOURCES,
    ValidationError,
    ValidationResult,
    validate_factor_id_format,
    validate_factor_value,
    validate_factor_matrix,
    get_system_from_factor_id,
    is_valid_factor_id,
)

# 认证模型 (api_contracts.md §2.1)
from backend.core.contracts.auth_models import (
    AUTH_ID_PATTERN,
    SESSION_ID_PATTERN,
    AuthProvider,
    AuthCredential,
    TokenPair,
    JWTPayload,
    AppleSignInRequest,
    GoogleSignInRequest,
    EmailSignupRequest,
    EmailLoginRequest,
    EmailVerifyRequest,
    RefreshTokenRequest,
    UserInfo,
)

# 订阅模型 (api_contracts.md §2.2)
from backend.core.contracts.subscription_models import (
    SUBSCRIPTION_ID_PATTERN,
    MembershipTier,
    SubscriptionProvider,
    SubscriptionStatus,
    Subscription,
    TierLimits,
    TIER_LIMITS,
    SubscriptionStatusResponse,
    AppleReceiptRequest,
    GooglePurchaseRequest,
    VerifyResponse,
    PlanInfo,
)

# TODO 模型 (api_contracts.md §2.3)
from backend.core.contracts.todo_models import (
    TODO_ID_PATTERN,
    TODO_CONTENT_MAX_LENGTH,
    TODO_DAILY_LIMIT,
    TodoType,
    TodoStatus,
    TodoEntry,
    TodoDailySummary,
    TodoCreateRequest,
    TodoUpdateRequest,
    TodoListResponse,
    TodoListParams,
)

__all__ = [
    # Base types & patterns
    "FACTOR_ID_PATTERN",
    "RULE_ID_PATTERN",
    "VERSION_PATTERN",
    "FUSION_ID_PATTERN",
    "EVENT_ID_PATTERN",
    "INSIGHT_ID_PATTERN",
    "LOCALE_PATTERN",
    "FactorCategory",
    "StatusEnum",
    "SourceMetadata",
    # Config models
    "ConfigFactor",
    "RuleCondition",
    "LogicalExpression",
    "ConfigRuleResult",
    "ConfigRuleDefinition",
    # Runtime models
    "FactorValue",
    "FactorMatrix",
    "RuntimeRuleResult",
    # Narrative models
    "NarrativeConfig",
    "ConflictWarning",
    "FusionResult",
    # Memory models
    "PrivacyLevel",
    "MemoryBase",
    "SENSITIVE_FIELDS",
    "Event",
    "Insight",
    "UserProfile",
    # TOON models
    "TOON_SYNTAX",
    "ABBREVIATIONS",
    "ABBREVIATIONS_REVERSE",
    "TOON_CONSTRAINTS",
    "ToonPayload",
    # Engine models
    "EngineDescriptor",
    "ENGINE_REGISTRY_CONSTRAINTS",
    "ENGINE_KINDS",
    "SUPPORTED_SYSTEMS",
    # Test schema models
    "RuleTestCase",
    "GoldenCase",
    "NarrativeGolden",
    "TEST_PYRAMID_STANDARDS",
    "RELEASE_CHECKLIST",
    # L2.5 models (v1.1 §1.5)
    "RELATION_ID_PATTERN",
    "EVIDENCE_ID_PATTERN",
    "CONCEPT_ID_PATTERN",
    "RelationType",
    "EffectDirection",
    "ConfidenceLevel",
    "ConfigRelation",
    "EvidenceChainEntry",
    "CrossSystemMapping",
    # Narrative snippet models (v1.1 §3.4-3.6)
    "SNIPPET_ID_PATTERN",
    "CHAIN_ID_PATTERN",
    "PROTOCOL_ID_PATTERN",
    "SnippetRole",
    "ConflictResolutionStrategy",
    "NarrativeOrderStrategy",
    "NarrativeSnippet",
    "LogicNode",
    "LogicEdge",
    "LogicChain",
    "AssemblyProtocol",
    # Cross domain models (schema-core spec v0.4.0)
    "CrossDomainAxes",
    # Action layer models (Phase 5.5)
    "ACTION_PROJECT_ID_PATTERN",
    "ACTION_ITEM_ID_PATTERN",
    "ActionSourceKind",
    "ActionTimeScope",
    "ActionContext",
    "ActionStatus",
    "EffortEstimate",
    "InsightCompileStatus",
    "ActionBase",
    "ActionSourceRef",
    "ActionProject",
    "ActionItem",
    "InsightCompileRecord",
    "AvoidanceInsight",
    # Validation tools (calculator-integration spec §10)
    "VALID_SYSTEM_PREFIXES",
    "VALID_SOURCES",
    "ValidationError",
    "ValidationResult",
    "validate_factor_id_format",
    "validate_factor_value",
    "validate_factor_matrix",
    "get_system_from_factor_id",
    "is_valid_factor_id",
    # Auth models (api_contracts.md §2.1)
    "AUTH_ID_PATTERN",
    "SESSION_ID_PATTERN",
    "AuthProvider",
    "AuthCredential",
    "TokenPair",
    "JWTPayload",
    "AppleSignInRequest",
    "GoogleSignInRequest",
    "EmailSignupRequest",
    "EmailLoginRequest",
    "EmailVerifyRequest",
    "RefreshTokenRequest",
    "UserInfo",
    # Subscription models (api_contracts.md §2.2)
    "SUBSCRIPTION_ID_PATTERN",
    "MembershipTier",
    "SubscriptionProvider",
    "SubscriptionStatus",
    "Subscription",
    "TierLimits",
    "TIER_LIMITS",
    "SubscriptionStatusResponse",
    "AppleReceiptRequest",
    "GooglePurchaseRequest",
    "VerifyResponse",
    "PlanInfo",
    # TODO models (api_contracts.md §2.3)
    "TODO_ID_PATTERN",
    "TODO_CONTENT_MAX_LENGTH",
    "TODO_DAILY_LIMIT",
    "TodoType",
    "TodoStatus",
    "TodoEntry",
    "TodoDailySummary",
    "TodoCreateRequest",
    "TodoUpdateRequest",
    "TodoListResponse",
    "TodoListParams",
]
