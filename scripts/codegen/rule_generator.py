"""
RuleCodeGenerator - 规则代码生成器

将 ConfigRuleDefinition JSON 编译为 Python 规则函数。
对照架构 §2.2 和数据契约 §2.1
"""

from __future__ import annotations

import logging
import re
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

from pydantic import ValidationError as PydanticValidationError

from backend.core.contracts import (
    ConfigRuleDefinition,
    LogicalExpression,
    RuleCondition,
    VERSION_PATTERN,
)
from scripts.codegen.base import BaseCodeGenerator
from scripts.codegen.exceptions import CompilationError, ValidationError
from scripts.codegen.manifest import CodegenManifest

logger = logging.getLogger(__name__)

import json
import hashlib
from typing import Tuple

# 条件运算符映射表（对齐架构 §2.2 + design.md 11种运算符）
OPERATOR_MAP = {
    "EQ": "==",
    "==": "==",
    "NE": "!=",
    "!=": "!=",
    "GT": ">",
    ">": ">",
    "GE": ">=",
    ">=": ">=",
    "LT": "<",
    "<": "<",
    "LE": "<=",
    "<=": "<=",
    "IN": "in",
    "in": "in",
    "NOT_IN": "not in",
    "not_in": "not in",
    "CONTAINS": "in",  # 反向: value in factor
    "exists": "is not None",
    "not_exists": "is None",
    "between": "between",  # 特殊处理
}

# 运算符规范化映射（EQ→==, IN→in 等）
OPERATOR_NORMALIZE = {
    "EQ": "==",
    "NE": "!=",
    "GT": ">",
    "GE": ">=",
    "LT": "<",
    "LE": "<=",
    "IN": "in",
    "NOT_IN": "not_in",
}


class RuleCodeGenerator(BaseCodeGenerator):
    """
    规则代码生成器
    
    输入: ConfigRuleDefinition JSON
    输出: Python 规则函数模块，返回 RuntimeRuleResult
    """
    
    def __init__(self, output_dir: Optional[Path] = None):
        if output_dir is None:
            output_dir = Path("backend/generated/rules")
        super().__init__(output_dir)
    
    def _normalize_operators(self, source: Dict[str, Any]) -> Dict[str, Any]:
        """
        规范化运算符（在 Pydantic 校验前执行）
        
        将 EQ→==, NE→!=, GT→> 等大写运算符转换为 Schema 要求的格式。
        支持测试使用简写格式，同时保持 Schema 严格性。
        """
        import copy
        result = copy.deepcopy(source)
        
        def normalize_condition(cond: Any) -> Any:
            if not isinstance(cond, dict):
                return cond
            
            op = cond.get("operator")
            if op in OPERATOR_NORMALIZE:
                cond["operator"] = OPERATOR_NORMALIZE[op]
            
            # 递归处理嵌套条件
            if "conditions" in cond:
                cond["conditions"] = [normalize_condition(c) for c in cond["conditions"]]
            if "condition" in cond:
                cond["condition"] = normalize_condition(cond["condition"])
            
            return cond
        
        if "condition" in result:
            result["condition"] = normalize_condition(result["condition"])
        
        return result
    
    def validate(self, source: Dict[str, Any]) -> List[str]:
        """校验规则 JSON"""
        errors = []
        
        # 预处理：规范化运算符
        normalized = self._normalize_operators(source)
        
        # 必填字段检查
        for field in ["rule_id", "version", "status", "engine_id"]:
            if field not in normalized:
                errors.append(f"Missing required field: {field}")
        
        # version 格式检查
        if "version" in normalized:
            if not re.match(VERSION_PATTERN, normalized["version"]):
                errors.append(f"Invalid version format: {normalized['version']}")
        
        # status 枚举检查
        if "status" in normalized:
            if normalized["status"] not in ["active", "experimental", "deprecated"]:
                errors.append(f"Invalid status: {normalized['status']}")
        
        # 复杂规则必须有 python_handler_ref
        if normalized.get("is_complex_logic") and not normalized.get("python_handler_ref"):
            errors.append("python_handler_ref required when is_complex_logic=True")
        
        # Pydantic 完整校验
        if not errors:
            try:
                ConfigRuleDefinition(**normalized)
            except PydanticValidationError as e:
                for err in e.errors():
                    loc = ".".join(str(x) for x in err["loc"])
                    errors.append(f"{loc}: {err['msg']}")
        
        return errors
    
    def compile(self, source: Dict[str, Any]) -> str:
        """编译规则 JSON 为 Python 代码"""
        # 预处理：规范化运算符
        normalized = self._normalize_operators(source)
        rule = ConfigRuleDefinition(**normalized)
        
        if rule.is_complex_logic:
            return self._generate_complex_stub(rule)
        else:
            return self._generate_simple_rule(rule)
    
    def _compile_lenient(self, source: Dict[str, Any]) -> str:
        """宽松编译模式 - 直接从JSON生成代码，不经过严格Pydantic验证"""
        normalized = self._normalize_operators(source)
        
        # 提取必要字段（带默认值）
        rule_id = normalized.get("rule_id", "unknown_rule")
        category = normalized.get("category", "default")
        engine_id = normalized.get("engine_id", "unknown")
        human_label = self._escape_string(normalized.get("human_label", ""))
        exclusive_group = normalized.get("exclusive_group", "")
        priority = normalized.get("priority", 500)
        
        # Result字段
        result = normalized.get("result", {})
        dimension = result.get("dimension", "default")
        level = result.get("level", "中等")
        description = self._escape_string(result.get("conclusion_template_zh", ""))
        confidence = result.get("confidence", 0.7)
        weight = result.get("weight", 1.0)
        tags = result.get("tags", [])
        evidence_factors = result.get("evidence_factors", [])
        
        # Metadata字段
        metadata = normalized.get("metadata", {})
        book_id = metadata.get("book_id", "")
        chapter = metadata.get("chapter", "")
        l1_anchor = metadata.get("l1_anchor", "")
        
        # 编译条件
        condition = normalized.get("condition", {})
        condition_expr = self._compile_condition(condition)
        
        # 提取所有factor_id
        required_factors = normalized.get("required_factors", [])
        if not required_factors:
            required_factors = self._extract_factor_ids(condition)
        
        factors_list = ", ".join(f'"{self._sanitize_factor_id(f)}"' for f in required_factors)
        tags_list = ", ".join(f'"{t}"' for t in tags)
        evidence_list = ", ".join(f'"{self._sanitize_factor_id(e)}"' for e in evidence_factors)
        
        imports = self._get_imports()
        header = self.generate_header(f"Rule: {rule_id}", version="1.0.0")
        
        code = f'''{header}{imports}

@register_rule(
    rule_id="{rule_id}",
    category="{category}",
    exclusive_group="{exclusive_group}",
    priority={priority},
    engine_id="{engine_id}"
)
def {rule_id}_evaluate(context: RuleContext) -> RuntimeRuleResult:
    """
    {human_label}
    源文件: {book_id}:{chapter}
    L1锚点: {l1_anchor}
    """
    import time
    _start = time.perf_counter()
    
    factors = context.get_factors([{factors_list}])
    condition_met = {condition_expr}
    
    _elapsed = (time.perf_counter() - _start) * 1000
    
    if condition_met:
        return RuntimeRuleResult(
            rule_id="{rule_id}",
            matched=True,
            dimension="{dimension}",
            level="{level}",
            description="{description}",
            confidence={confidence},
            weight={weight},
            tags=[{tags_list}],
            evidence_factors=[{evidence_list}],
            source_book="{book_id}",
            l1_anchor="{l1_anchor}",
            execution_time_ms=_elapsed
        )
    
    return RuntimeRuleResult.not_matched("{rule_id}", _elapsed)
'''
        return code
    
    def _extract_factor_ids(self, condition: Dict) -> list:
        """从条件中提取所有factor_id"""
        factor_ids = []
        
        def extract(c):
            if isinstance(c, dict):
                if "factor_id" in c:
                    factor_ids.append(c["factor_id"])
                if "conditions" in c:
                    for sub in c["conditions"]:
                        extract(sub)
        
        extract(condition)
        return list(set(factor_ids))
    
    def _escape_string(self, s: str) -> str:
        """转义字符串中的特殊字符用于Python代码生成"""
        if not s:
            return ""
        # 转义反斜杠、换行、引号
        s = s.replace("\\", "\\\\")
        s = s.replace("\n", "\\n")
        s = s.replace("\r", "\\r")
        s = s.replace('"', '\\"')
        # 转义中文引号为普通引号再转义
        s = s.replace('"', '\\"')
        s = s.replace('"', '\\"')
        s = s.replace(''', "\\'")
        s = s.replace(''', "\\'")
        return s
    
    def _generate_simple_rule(self, rule: ConfigRuleDefinition) -> str:
        """生成简单规则代码"""
        imports = self._get_imports()
        header = self.generate_header(
            f"Rule: {rule.rule_id}",
            version=rule.version
        )
        
        condition_expr = self._compile_condition(rule.condition)
        factors_list = ", ".join(f'"{f}"' for f in rule.required_factors)
        tags_list = ", ".join(f'"{t}"' for t in rule.result.tags)
        evidence_list = ", ".join(f'"{e}"' for e in rule.result.evidence_factors)
        
        # 转义description中的特殊字符
        description = self._escape_string(rule.result.conclusion_template_zh)
        human_label = self._escape_string(rule.human_label)
        
        code = f'''{header}{imports}

@register_rule(
    rule_id="{rule.rule_id}",
    category="{rule.category}",
    exclusive_group="{rule.exclusive_group or ''}",
    priority={rule.priority},
    engine_id="{rule.engine_id}"
)
def {rule.rule_id}_evaluate(context: RuleContext) -> RuntimeRuleResult:
    """
    {human_label}
    源文件: {rule.metadata.book_id}:{rule.metadata.chapter or ''}
    L1锚点: {rule.metadata.l1_anchor}
    """
    import time
    _start = time.perf_counter()
    
    factors = context.get_factors([{factors_list}])
    condition_met = {condition_expr}
    
    _elapsed = (time.perf_counter() - _start) * 1000
    
    if condition_met:
        return RuntimeRuleResult(
            rule_id="{rule.rule_id}",
            matched=True,
            dimension="{rule.result.dimension}",
            level="{rule.result.level}",
            description="{description}",
            confidence={rule.result.confidence},
            weight={rule.result.weight},
            tags=[{tags_list}],
            evidence_factors=[{evidence_list}],
            source_book="{rule.metadata.book_id}",
            l1_anchor="{rule.metadata.l1_anchor}",
            execution_time_ms=_elapsed
        )
    
    return RuntimeRuleResult.not_matched("{rule.rule_id}", _elapsed)
'''
        return code
    
    def _generate_complex_stub(self, rule: ConfigRuleDefinition) -> str:
        """生成复杂规则 stub"""
        imports = self._get_imports(complex_rule=True)
        header = self.generate_header(
            f"Complex Rule Stub: {rule.rule_id}",
            version=rule.version
        )
        
        code = f'''{header}{imports}

@register_rule(
    rule_id="{rule.rule_id}",
    category="{rule.category}",
    exclusive_group="{rule.exclusive_group or ''}",
    priority={rule.priority},
    engine_id="{rule.engine_id}"
)
def {rule.rule_id}_evaluate(factor_matrix: FactorMatrix) -> RuntimeRuleResult:
    """
    {rule.human_label}
    
    复杂规则 - 需要人工实现
    Handler: {rule.python_handler_ref}
    源文件: {rule.metadata.book_id}
    """
    import time
    _start = time.perf_counter()
    
    # TODO: 调用 {rule.python_handler_ref} 实现复杂逻辑
    # from backend.rules.handlers import {rule.python_handler_ref}
    # result = {rule.python_handler_ref}(factor_matrix)
    
    _elapsed = (time.perf_counter() - _start) * 1000
    
    raise NotImplementedError(
        f"Complex rule {rule.rule_id} requires manual implementation. "
        f"Please implement {rule.python_handler_ref}."
    )
'''
        return code
    
    def _sanitize_factor_id(self, factor_id: str) -> str:
        """清理factor_id，移除无效字符"""
        if not factor_id:
            return "unknown_factor"
        import re
        # 移除括号、空格、箭头等特殊字符
        cleaned = re.sub(r'[^a-zA-Z0-9_]', '_', factor_id)
        # 确保不以数字开头
        if cleaned and cleaned[0].isdigit():
            cleaned = '_' + cleaned
        # 移除连续下划线
        cleaned = re.sub(r'_+', '_', cleaned)
        # 移除首尾下划线
        cleaned = cleaned.strip('_')
        return cleaned or "unknown_factor"
    
    def _compile_condition(self, condition: Union[RuleCondition, LogicalExpression, Dict]) -> str:
        """编译条件表达式"""
        if isinstance(condition, dict):
            op = condition.get("operator")
            
            if op in ("AND", "OR"):
                sub_conds = [self._compile_condition(c) for c in condition["conditions"]]
                joiner = " and " if op == "AND" else " or "
                return f"({joiner.join(sub_conds)})"
            
            elif op == "NOT":
                # NOT 表达式使用 conditions 数组，取第一个条件否定
                sub_conditions = condition.get("conditions", [])
                if sub_conditions:
                    sub = self._compile_condition(sub_conditions[0])
                    return f"(not {sub})"
                return "True"
            
            else:
                # 比较操作
                factor_id = self._sanitize_factor_id(condition.get("factor_id", ""))
                raw_value = condition.get("value")
                value = repr(raw_value)
                py_op = OPERATOR_MAP.get(op, "==")
                
                if op == "CONTAINS":
                    return f'({value} in (factors.get("{factor_id}") or []))'
                elif op == "exists":
                    return f'(factors.get("{factor_id}") is not None)'
                elif op == "not_exists":
                    return f'(factors.get("{factor_id}") is None)'
                elif op == "between":
                    # between 需要 [lower, upper] 值
                    if isinstance(raw_value, (list, tuple)) and len(raw_value) >= 2:
                        lower, upper = raw_value[0], raw_value[1]
                        return f'({lower} <= (factors.get("{factor_id}") or float("-inf")) <= {upper})'
                    return "False"
                elif op in ("not_in", "NOT_IN"):
                    return f'(factors.get("{factor_id}") not in {value})'
                elif op in ("in", "IN"):
                    return f'(factors.get("{factor_id}") in {value})'
                elif op in (">=", ">", "<=", "<"):
                    # 数值比较需要空值保护
                    if isinstance(raw_value, bool):
                        default = "False"
                    elif isinstance(raw_value, (int, float)):
                        default = "0"
                    else:
                        default = "''"
                    return f'((factors.get("{factor_id}") or {default}) {py_op} {value})'
                else:
                    # == 和 != 可以直接比较 None
                    return f'(factors.get("{factor_id}") {py_op} {value})'
        
        elif isinstance(condition, LogicalExpression):
            return self._compile_condition(condition.model_dump())
        
        elif isinstance(condition, RuleCondition):
            return self._compile_condition(condition.model_dump())
        
        return "True"
    
    def _get_imports(self, complex_rule: bool = False) -> str:
        """生成 import 语句"""
        imports = [
            "from typing import Any, Dict, List, Optional",
            "from backend.core.contracts import RuntimeRuleResult",
            "from backend.core.decorators import register_rule",
        ]
        
        if complex_rule:
            imports.append("from backend.core.contracts import FactorMatrix")
        else:
            imports.append("from backend.rules.core import RuleContext")
        
        return self.generate_imports(imports)
    
    # =========================================================================
    # 批量编译方法 (Task 3: Rule Codegen Pipeline)
    # =========================================================================
    
    def compile_jsonl(
        self,
        jsonl_path: Path,
        output_dir: Optional[Path] = None,
        manifest: Optional[CodegenManifest] = None,
    ) -> Dict[str, Any]:
        """
        编译 JSONL 规则文件
        
        Args:
            jsonl_path: JSONL 文件路径
            output_dir: 输出目录（默认使用 self.output_dir）
            manifest: 代码生成清单（用于增量编译）
        
        Returns:
            编译报告 {
                "source_file": str,
                "rules_compiled": int,
                "rules_skipped": int,
                "errors": List[Dict],
                "output_files": List[str]
            }
        """
        jsonl_path = Path(jsonl_path)
        if output_dir:
            self.output_dir = Path(output_dir)
        
        report = {
            "source_file": str(jsonl_path),
            "rules_compiled": 0,
            "rules_skipped": 0,
            "errors": [],
            "output_files": [],
        }
        
        if not jsonl_path.exists():
            report["errors"].append({
                "rule_id": None,
                "error": f"File not found: {jsonl_path}",
            })
            return report
        
        # 计算源文件哈希
        source_content = jsonl_path.read_text(encoding="utf-8")
        source_hash = hashlib.sha256(source_content.encode()).hexdigest()[:16]
        
        # 检查是否需要重新编译
        if manifest:
            entry = manifest.get_entry(str(jsonl_path))
            if entry and entry.source_hash == source_hash:
                report["rules_skipped"] = sum(1 for _ in source_content.strip().split("\n") if _)
                return report
        
        # 解析并编译每一行
        rules_code = []
        for line_num, line in enumerate(source_content.strip().split("\n"), 1):
            if not line.strip():
                continue
            
            try:
                rule_json = json.loads(line)
                rule_id = rule_json.get("rule_id", f"unknown_{line_num}")
                
                # 检查最低必要字段
                if not rule_json.get("condition") or not rule_json.get("result"):
                    report["errors"].append({
                        "rule_id": rule_id,
                        "line": line_num,
                        "errors": ["Missing required fields: condition or result"],
                    })
                    continue
                
                # 尝试直接编译（宽松模式）
                try:
                    code = self._compile_lenient(rule_json)
                    rules_code.append(code)
                    report["rules_compiled"] += 1
                except Exception as compile_err:
                    # 如果宽松编译失败，尝试严格模式
                    errors = self.validate(rule_json)
                    if errors:
                        report["errors"].append({
                            "rule_id": rule_id,
                            "line": line_num,
                            "errors": errors,
                        })
                    else:
                        report["errors"].append({
                            "rule_id": rule_id,
                            "line": line_num,
                            "errors": [str(compile_err)],
                        })
                
            except json.JSONDecodeError as e:
                report["errors"].append({
                    "rule_id": None,
                    "line": line_num,
                    "error": f"JSON parse error: {e}",
                })
            except Exception as e:
                report["errors"].append({
                    "rule_id": rule_json.get("rule_id") if 'rule_json' in dir() else None,
                    "line": line_num,
                    "error": str(e),
                })
        
        # 合并并保存输出
        if rules_code:
            # 生成输出文件名：包含父目录以避免同名文件覆盖
            # data/rules/bazi/career.jsonl -> bazi_career.py
            # data/rules/generated/bazi/career.jsonl -> generated_bazi_career.py
            parent_parts = []
            for parent in jsonl_path.parents:
                if parent.name in ('rules', 'data', ''):
                    break
                parent_parts.insert(0, parent.name)
            if parent_parts:
                output_filename = "_".join(parent_parts) + "_" + jsonl_path.stem + ".py"
            else:
                output_filename = jsonl_path.stem + ".py"
            
            # 合并所有规则代码
            combined_code = self._merge_rules_code(rules_code, jsonl_path)
            
            # 格式化
            try:
                combined_code = self.format_code(combined_code)
            except Exception as e:
                logger.warning(f"Formatting failed, saving unformatted: {e}")
            
            # 语法检查
            try:
                self.verify_syntax(combined_code)
            except Exception as e:
                report["errors"].append({
                    "rule_id": None,
                    "error": f"Syntax error in combined code: {e}",
                })
                return report
            
            # 保存
            output_path = self.save(combined_code, output_filename)
            report["output_files"].append(str(output_path))
            
            # 更新 manifest
            if manifest:
                output_hash = hashlib.sha256(combined_code.encode()).hexdigest()[:16]
                # 提取 engine_id（从第一个规则）
                first_rule = json.loads(source_content.strip().split("\n")[0])
                manifest.add_entry(
                    source_file=str(jsonl_path),
                    output_file=str(output_path),
                    source_hash=source_hash,
                    output_hash=output_hash,
                    generator_type="rule",
                    engine_id=first_rule.get("engine_id", "unknown"),
                    version=first_rule.get("version", "0.0.0"),
                )
        
        return report
    
    def _merge_rules_code(self, rules_code: List[str], source_path: Path) -> str:
        """
        合并多个规则代码为单一模块
        
        Args:
            rules_code: 各规则的代码列表
            source_path: 源文件路径
        
        Returns:
            合并后的模块代码
        """
        # 提取公共 import 和 header
        header = self.generate_header(
            f"Rules Module: {source_path.stem}",
            source_file=str(source_path),
        )
        
        imports = self._get_imports()
        
        # 移除各规则代码中的重复 import 和 header
        cleaned_rules = []
        for code in rules_code:
            # 找到 @register_rule 开始的位置
            idx = code.find("@register_rule")
            if idx != -1:
                cleaned_rules.append(code[idx:])
            else:
                cleaned_rules.append(code)
        
        # 组装
        combined = f"{header}{imports}\n\n" + "\n\n".join(cleaned_rules)
        return combined
    
    def compile_batch(
        self,
        rule_files: List[Path],
        output_base_dir: Optional[Path] = None,
        manifest: Optional[CodegenManifest] = None,
    ) -> Dict[str, Any]:
        """
        批量编译多个规则文件
        
        Args:
            rule_files: 规则 JSONL 文件列表
            output_base_dir: 输出基础目录
            manifest: 代码生成清单
        
        Returns:
            批量编译报告
        """
        import time
        start_time = time.time()
        
        batch_report = {
            "timestamp": time.time(),
            "files_processed": 0,
            "total_rules_compiled": 0,
            "total_rules_skipped": 0,
            "total_errors": 0,
            "file_reports": [],
        }
        
        for rule_file in rule_files:
            # 确定输出目录（保持源目录结构）
            if output_base_dir:
                # data/rules/bazi/career.jsonl -> backend/rules/bazi/
                rel_path = rule_file.parent.name
                output_dir = Path(output_base_dir) / rel_path
            else:
                output_dir = self.output_dir
            
            # 编译
            report = self.compile_jsonl(
                rule_file,
                output_dir=output_dir,
                manifest=manifest,
            )
            
            batch_report["files_processed"] += 1
            batch_report["total_rules_compiled"] += report["rules_compiled"]
            batch_report["total_rules_skipped"] += report["rules_skipped"]
            batch_report["total_errors"] += len(report["errors"])
            batch_report["file_reports"].append(report)
        
        batch_report["duration_seconds"] = time.time() - start_time
        
        return batch_report
    
    def needs_recompile(self, jsonl_path: Path, manifest: CodegenManifest) -> bool:
        """
        检查 JSONL 文件是否需要重新编译
        
        Args:
            jsonl_path: JSONL 文件路径
            manifest: 代码生成清单
        
        Returns:
            是否需要重新编译
        """
        jsonl_path = Path(jsonl_path)
        if not jsonl_path.exists():
            return False
        
        source_content = jsonl_path.read_text(encoding="utf-8")
        source_hash = hashlib.sha256(source_content.encode()).hexdigest()[:16]
        
        return manifest.needs_recompile(str(jsonl_path), source_hash)
