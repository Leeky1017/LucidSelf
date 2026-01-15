import pytest

from backend.core.engines.governance import (
    EngineIdGovernanceError,
    validate_engine_id_or_raise,
)
from backend.integration import FusionEngine
from backend.core.contracts import RuntimeRuleResult, FusionResult
from backend.pipeline.orchestrator import Pipeline, PipelineInput


def test_validate_engine_id_missing_is_deterministic():
    with pytest.raises(EngineIdGovernanceError) as exc:
        validate_engine_id_or_raise(None)
    assert exc.value.code == "MISSING_ENGINE_ID"


def test_validate_engine_id_invalid_format_is_deterministic():
    with pytest.raises(EngineIdGovernanceError) as exc:
        validate_engine_id_or_raise("Bad Engine")
    assert exc.value.code == "INVALID_ENGINE_ID"


def test_validate_engine_id_unregistered_is_deterministic():
    with pytest.raises(EngineIdGovernanceError) as exc:
        validate_engine_id_or_raise("unknown-engine")
    assert exc.value.code == "ENGINE_ID_NOT_FOUND"


@pytest.mark.asyncio
async def test_pipeline_rejects_unregistered_engine_id_in_filter():
    pipeline = Pipeline()
    pipeline._initialized = True

    with pytest.raises(EngineIdGovernanceError) as exc:
        await pipeline.execute(PipelineInput(user_id="test_user", engines=["unknown-engine"]))

    assert exc.value.code == "ENGINE_ID_NOT_FOUND"


def test_fusion_rejects_unregistered_engine_id_key():
    engine = FusionEngine()
    results = {
        "unknown-engine": [
            RuntimeRuleResult(
                rule_id="rule_001",
                matched=True,
                confidence=0.8,
                weight=1.0,
                tags=[],
                evidence_factors=[],
                execution_time_ms=1.0,
            )
        ]
    }

    with pytest.raises(EngineIdGovernanceError) as exc:
        engine.fuse_results(results)

    assert exc.value.code == "ENGINE_ID_NOT_FOUND"

