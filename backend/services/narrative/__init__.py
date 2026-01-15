"""
Narrative Generator Module

叙事生成模块:
- PromptBuilder: 构建 LLM prompt
- NarrativeGenerator: 生成叙事
- HallucinationDetector: 幻觉检测

对照 design.md, tasks.md 5-3
"""

from backend.services.narrative.prompt_builder import PromptBuilder
from backend.services.narrative.generator import (
    NarrativeGenerator,
    NarrativeOutput,
)

__all__ = [
    "PromptBuilder",
    "NarrativeGenerator",
    "NarrativeOutput",
]
