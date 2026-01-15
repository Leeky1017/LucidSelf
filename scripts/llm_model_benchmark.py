"""
LLM Model Benchmark Test

测试灵芽中转站上的所有模型：
- gpt-4.1-nano
- gemini-2.5-flash
- gemini-2.5-flash-lite
- doubao-seed-1.6-thinking
- grok-4-1-fast-reasoning

测试内容:
1. 基本连通性
2. 解析能力 (A层适用性)
3. 生成能力 (B层适用性)
4. 双语表现
5. 延迟和成本效益
"""

import asyncio
import time
import os
from pathlib import Path
from dataclasses import dataclass
from typing import List, Dict, Optional
import json

import sys
REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

if not os.getenv("OPENAI_API_KEY", "").strip():
    raise RuntimeError(
        "Missing OPENAI_API_KEY. Export it in your shell before running this benchmark."
    )

os.environ.setdefault("OPENAI_BASE_URL", "https://api.lingyaai.cn/v1")

from backend.core.llm.providers.openai import OpenAIProvider
from backend.core.llm.models import LLMRequest


@dataclass
class TestResult:
    """测试结果"""
    model: str
    test_name: str
    success: bool
    latency_ms: float
    input_tokens: int
    output_tokens: int
    response_preview: str
    quality_notes: str = ""
    error: Optional[str] = None


# 测试用的模型列表
MODELS = [
    "gpt-4.1-nano",
    "gemini-2.5-flash",
    "gemini-2.5-flash-lite",
    "doubao-seed-1.6-thinking",
    "grok-4-1-fast-reasoning",
]


# 测试用例
TEST_CASES = {
    # A层测试：解析能力
    "parse_intent_zh": {
        "prompt": """请解析以下用户输入的意图，输出JSON格式：
用户输入："我昨晚梦见自己在一片森林里奔跑，后面有蛇在追我"
输出格式：{"intent": "dream_analysis", "entities": [...], "complexity": "low/medium/high"}""",
        "expected_format": "json",
        "purpose": "A层解析-中文意图识别",
    },
    
    "parse_intent_en": {
        "prompt": """Parse the user's intent from the following input, output in JSON format:
User input: "I had a dream last night where I was running through a forest with a snake chasing me"
Output format: {"intent": "dream_analysis", "entities": [...], "complexity": "low/medium/high"}""",
        "expected_format": "json",
        "purpose": "A层解析-英文意图识别",
    },
    
    "parse_bazi_input": {
        "prompt": """从以下对话中提取八字排盘所需信息，输出JSON：
用户："我是1990年5月15日下午2点半在北京出生的，男性"
输出：{"birth_date": "...", "birth_time": "...", "location": "...", "gender": "..."}""",
        "expected_format": "json",
        "purpose": "A层解析-结构化信息提取",
    },
    
    # B层测试：生成能力-中文
    "generate_bazi_zh": {
        "prompt": """基于以下八字信息，生成一段100字左右的事业运势解读：
- 日主：甲木
- 格局：正官格
- 当前大运：财旺
- 流年：2024甲辰年

要求：语言流畅、有洞察力、积极正面""",
        "expected_format": "narrative",
        "purpose": "B层生成-中文命理解读",
    },
    
    "generate_dream_zh": {
        "prompt": """基于以下梦境符号，生成一段150字左右的心理学解读：
- 主要符号：森林(未知领域)、奔跑(逃避/追求)、蛇(转变/威胁)
- 情绪：恐惧、紧张
- 荣格原型：阴影

要求：结合荣格心理学，语言温和有启发性""",
        "expected_format": "narrative",
        "purpose": "B层生成-中文梦境解读",
    },
    
    # B层测试：生成能力-英文
    "generate_astro_en": {
        "prompt": """Based on the following astrological factors, generate a ~100 word career reading:
- Sun: Taurus in 10th house
- Moon: Cancer in 4th house  
- Saturn: transiting 10th house
- Current aspect: Sun trine Saturn

Requirements: Insightful, practical, encouraging tone""",
        "expected_format": "narrative",
        "purpose": "B层生成-英文占星解读",
    },
    
    "generate_tarot_en": {
        "prompt": """Based on the following tarot spread, generate a ~100 word reading:
- Past: The Tower (reversed) - upheaval ending
- Present: The Star - hope and healing
- Future: The World - completion

Requirements: Symbolic interpretation, hopeful tone""",
        "expected_format": "narrative",
        "purpose": "B层生成-英文塔罗解读",
    },
    
    # 复杂推理测试
    "complex_cross_cultural": {
        "prompt": """请结合中西方视角分析以下情况：
用户八字显示"正官格，财星旺"，西洋占星显示"太阳金牛座10宫，土星过境"。
两者是否有共通之处？请用100字给出跨文化的综合解读。""",
        "expected_format": "narrative",
        "purpose": "复杂推理-跨文化分析",
    },
}


async def test_model(provider: OpenAIProvider, model: str, test_name: str, test_case: dict) -> TestResult:
    """测试单个模型的单个用例"""
    request = LLMRequest(
        prompt=test_case["prompt"],
        model=model,
        max_tokens=300,
        temperature=0.5,
        timeout=60.0,
    )
    
    try:
        start_time = time.perf_counter()
        response = await provider.complete(request)
        latency_ms = (time.perf_counter() - start_time) * 1000
        
        # 质量评估
        quality_notes = ""
        response_text = response.content.strip()
        
        if test_case["expected_format"] == "json":
            # 检查是否能解析为 JSON
            try:
                # 尝试提取 JSON
                if "```json" in response_text:
                    json_str = response_text.split("```json")[1].split("```")[0]
                elif "{" in response_text:
                    start = response_text.index("{")
                    end = response_text.rindex("}") + 1
                    json_str = response_text[start:end]
                else:
                    json_str = response_text
                json.loads(json_str)
                quality_notes = "✓ Valid JSON"
            except:
                quality_notes = "✗ Invalid JSON format"
        else:
            # 叙事质量简单评估
            if len(response_text) < 50:
                quality_notes = "✗ Too short"
            elif len(response_text) > 500:
                quality_notes = "△ Verbose"
            else:
                quality_notes = "✓ Good length"
        
        return TestResult(
            model=model,
            test_name=test_name,
            success=True,
            latency_ms=latency_ms,
            input_tokens=response.usage.prompt_tokens,
            output_tokens=response.usage.completion_tokens,
            response_preview=response_text[:150] + "..." if len(response_text) > 150 else response_text,
            quality_notes=quality_notes,
        )
        
    except Exception as e:
        return TestResult(
            model=model,
            test_name=test_name,
            success=False,
            latency_ms=0,
            input_tokens=0,
            output_tokens=0,
            response_preview="",
            error=str(e),
        )


async def run_all_tests():
    """运行所有测试"""
    provider = OpenAIProvider(
        api_key=os.environ["OPENAI_API_KEY"],
        base_url=os.environ["OPENAI_BASE_URL"],
    )
    
    results: List[TestResult] = []
    
    print("=" * 80)
    print("LLM Model Benchmark Test")
    print("=" * 80)
    print(f"Base URL: {os.environ['OPENAI_BASE_URL']}")
    print(f"Models: {', '.join(MODELS)}")
    print(f"Test Cases: {len(TEST_CASES)}")
    print("=" * 80)
    
    for model in MODELS:
        print(f"\n{'='*40}")
        print(f"Testing: {model}")
        print(f"{'='*40}")
        
        for test_name, test_case in TEST_CASES.items():
            print(f"  {test_case['purpose']}...", end=" ", flush=True)
            result = await test_model(provider, model, test_name, test_case)
            results.append(result)
            
            if result.success:
                print(f"✓ {result.latency_ms:.0f}ms | {result.input_tokens}+{result.output_tokens} tokens | {result.quality_notes}")
            else:
                print(f"✗ ERROR: {result.error}")
        
        # 简短延迟避免限流
        await asyncio.sleep(1)
    
    # 生成汇总报告
    print("\n" + "=" * 80)
    print("SUMMARY REPORT")
    print("=" * 80)
    
    # 按模型汇总
    model_stats = {}
    for r in results:
        if r.model not in model_stats:
            model_stats[r.model] = {"success": 0, "fail": 0, "total_latency": 0, "total_tokens": 0}
        
        if r.success:
            model_stats[r.model]["success"] += 1
            model_stats[r.model]["total_latency"] += r.latency_ms
            model_stats[r.model]["total_tokens"] += r.input_tokens + r.output_tokens
        else:
            model_stats[r.model]["fail"] += 1
    
    print(f"\n{'Model':<30} {'Success':<10} {'Fail':<10} {'Avg Latency':<15} {'Total Tokens'}")
    print("-" * 80)
    for model, stats in model_stats.items():
        total = stats["success"] + stats["fail"]
        avg_latency = stats["total_latency"] / stats["success"] if stats["success"] > 0 else 0
        print(f"{model:<30} {stats['success']}/{total:<8} {stats['fail']:<10} {avg_latency:,.0f}ms        {stats['total_tokens']}")
    
    # 按用途分类评估
    print("\n" + "-" * 80)
    print("A层适用性评估 (解析能力):")
    a_layer_tests = [r for r in results if "parse" in r.test_name]
    for model in MODELS:
        model_results = [r for r in a_layer_tests if r.model == model]
        success = sum(1 for r in model_results if r.success and "Valid JSON" in r.quality_notes)
        total = len(model_results)
        avg_latency = sum(r.latency_ms for r in model_results if r.success) / max(1, sum(1 for r in model_results if r.success))
        print(f"  {model}: {success}/{total} valid JSON, avg {avg_latency:.0f}ms")
    
    print("\nB层适用性评估 (生成能力):")
    b_layer_tests = [r for r in results if "generate" in r.test_name]
    for model in MODELS:
        model_results = [r for r in b_layer_tests if r.model == model]
        success = sum(1 for r in model_results if r.success and "Good" in r.quality_notes)
        total = len(model_results)
        avg_latency = sum(r.latency_ms for r in model_results if r.success) / max(1, sum(1 for r in model_results if r.success))
        print(f"  {model}: {success}/{total} good quality, avg {avg_latency:.0f}ms")
    
    print("\n双语能力评估:")
    for model in MODELS:
        zh_results = [r for r in results if r.model == model and "_zh" in r.test_name]
        en_results = [r for r in results if r.model == model and "_en" in r.test_name]
        zh_success = sum(1 for r in zh_results if r.success)
        en_success = sum(1 for r in en_results if r.success)
        print(f"  {model}: 中文 {zh_success}/{len(zh_results)}, English {en_success}/{len(en_results)}")
    
    return results


if __name__ == "__main__":
    asyncio.run(run_all_tests())
