"""
Schema Validator

验证生成的规则是否符合 ConfigRuleDefinition Schema。

Feature: rule-converter
Requirement Refs: Req 9.4
"""

import logging
import re
from dataclasses import dataclass
from typing import Any, Dict, List, Optional

logger = logging.getLogger(__name__)


# 正则模式（来自 backend/core/contracts/base.py）
RULE_ID_PATTERN = re.compile(r"^[a-z][a-z0-9_]*$")
VERSION_PATTERN = re.compile(r"^\d+\.\d+\.\d+$")

# 有效的操作符
VALID_OPERATORS = {
    "==", "!=", ">", "<", ">=", "<=",
    "in", "not_in", "exists", "not_exists", "between"
}

# 有效的逻辑操作符
VALID_LOGICAL_OPERATORS = {"AND", "OR", "NOT"}

# 有效的状态
VALID_STATUSES = {"active", "experimental", "deprecated"}

# 有效的维度
VALID_DIMENSIONS = {
    "career", "wealth", "marriage", "health",
    "personality", "guidance", "fortune"
}

# 有效的等级
VALID_LEVELS = {"大吉", "吉", "中等", "凶", "大凶"}


@dataclass
class ValidationError:
    """验证错误"""
    field: str
    message: str
    value: Any = None


@dataclass
class ValidationResult:
    """验证结果"""
    is_valid: bool
    errors: List[ValidationError]
    
    def to_dict(self) -> Dict:
        return {
            "is_valid": self.is_valid,
            "errors": [
                {"field": e.field, "message": e.message, "value": e.value}
                for e in self.errors
            ],
        }


class SchemaValidator:
    """
    规则 Schema 验证器
    
    验证生成的规则是否符合 ConfigRuleDefinition Schema。
    
    验证内容：
    1. 必填字段存在性
    2. 字段类型正确性
    3. 字段值合法性（如 rule_id 格式、status 枚举值等）
    4. 条件表达式结构正确性
    
    Requirement Refs: Req 9.4
    """
    
    # 必填字段
    REQUIRED_FIELDS = [
        "rule_id",
        "human_label",
        "category",
        "condition",
        "required_factors",
        "result",
    ]
    
    # 结果必填字段
    RESULT_REQUIRED_FIELDS = [
        "dimension",
        "level",
        "conclusion_template_zh",
    ]
    
    def validate(self, rule: Dict[str, Any]) -> ValidationResult:
        """
        验证规则
        
        Args:
            rule: 规则字典
            
        Returns:
            ValidationResult
        """
        errors = []
        
        # 1. 验证必填字段
        for field in self.REQUIRED_FIELDS:
            if field not in rule or rule[field] is None:
                errors.append(ValidationError(
                    field=field,
                    message=f"必填字段缺失: {field}",
                ))
        
        # 如果必填字段缺失太多，直接返回
        if len(errors) > 3:
            return ValidationResult(is_valid=False, errors=errors)
        
        # 2. 验证 rule_id 格式
        if "rule_id" in rule and rule["rule_id"]:
            if not RULE_ID_PATTERN.match(rule["rule_id"]):
                errors.append(ValidationError(
                    field="rule_id",
                    message="rule_id 格式无效，必须以小写字母开头，只允许小写字母、数字、下划线",
                    value=rule["rule_id"],
                ))
        
        # 3. 验证 version 格式
        if "version" in rule and rule["version"]:
            if not VERSION_PATTERN.match(rule["version"]):
                errors.append(ValidationError(
                    field="version",
                    message="version 格式无效，必须为 x.y.z 格式",
                    value=rule["version"],
                ))
        
        # 4. 验证 status
        if "status" in rule and rule["status"]:
            if rule["status"] not in VALID_STATUSES:
                errors.append(ValidationError(
                    field="status",
                    message=f"status 值无效，必须为 {VALID_STATUSES} 之一",
                    value=rule["status"],
                ))
        
        # 5. 验证 condition
        if "condition" in rule and rule["condition"]:
            cond_errors = self._validate_condition(rule["condition"])
            errors.extend(cond_errors)
        
        # 6. 验证 required_factors
        if "required_factors" in rule:
            if not isinstance(rule["required_factors"], list):
                errors.append(ValidationError(
                    field="required_factors",
                    message="required_factors 必须是列表",
                    value=type(rule["required_factors"]).__name__,
                ))
        
        # 7. 验证 result
        if "result" in rule and rule["result"]:
            result_errors = self._validate_result(rule["result"])
            errors.extend(result_errors)
        
        # 8. 验证 metadata
        if "metadata" in rule and rule["metadata"]:
            meta_errors = self._validate_metadata(rule["metadata"])
            errors.extend(meta_errors)
        
        return ValidationResult(
            is_valid=len(errors) == 0,
            errors=errors,
        )
    
    def _validate_condition(self, condition: Dict) -> List[ValidationError]:
        """验证条件表达式"""
        errors = []
        
        if not isinstance(condition, dict):
            errors.append(ValidationError(
                field="condition",
                message="condition 必须是字典",
            ))
            return errors
        
        # 检查是否是逻辑表达式
        if "operator" in condition:
            op = condition["operator"]
            
            if op in VALID_LOGICAL_OPERATORS:
                # 逻辑表达式
                if "conditions" not in condition:
                    errors.append(ValidationError(
                        field="condition.conditions",
                        message="逻辑表达式缺少 conditions 字段",
                    ))
                elif isinstance(condition["conditions"], list):
                    for i, sub_cond in enumerate(condition["conditions"]):
                        sub_errors = self._validate_condition(sub_cond)
                        for e in sub_errors:
                            e.field = f"condition.conditions[{i}].{e.field}"
                        errors.extend(sub_errors)
            elif op in VALID_OPERATORS:
                # 简单条件
                if "factor_id" not in condition:
                    errors.append(ValidationError(
                        field="condition.factor_id",
                        message="条件缺少 factor_id 字段",
                    ))
            else:
                errors.append(ValidationError(
                    field="condition.operator",
                    message=f"无效的操作符: {op}",
                    value=op,
                ))
        else:
            # 可能是简单条件
            if "factor_id" not in condition:
                errors.append(ValidationError(
                    field="condition",
                    message="条件缺少 operator 或 factor_id 字段",
                ))
        
        return errors
    
    def _validate_result(self, result: Dict) -> List[ValidationError]:
        """验证结果"""
        errors = []
        
        if not isinstance(result, dict):
            errors.append(ValidationError(
                field="result",
                message="result 必须是字典",
            ))
            return errors
        
        # 检查必填字段
        for field in self.RESULT_REQUIRED_FIELDS:
            if field not in result or result[field] is None:
                errors.append(ValidationError(
                    field=f"result.{field}",
                    message=f"result 缺少必填字段: {field}",
                ))
        
        # 验证 dimension
        if "dimension" in result and result["dimension"]:
            if result["dimension"] not in VALID_DIMENSIONS:
                # 允许自定义 dimension，但记录警告
                logger.debug(f"非标准 dimension: {result['dimension']}")
        
        # 验证 level
        if "level" in result and result["level"]:
            if result["level"] not in VALID_LEVELS:
                errors.append(ValidationError(
                    field="result.level",
                    message=f"level 值无效，必须为 {VALID_LEVELS} 之一",
                    value=result["level"],
                ))
        
        # 验证 weight
        if "weight" in result:
            if not isinstance(result["weight"], (int, float)):
                errors.append(ValidationError(
                    field="result.weight",
                    message="weight 必须是数值",
                    value=type(result["weight"]).__name__,
                ))
        
        # 验证 confidence
        if "confidence" in result:
            if not isinstance(result["confidence"], (int, float)):
                errors.append(ValidationError(
                    field="result.confidence",
                    message="confidence 必须是数值",
                ))
            elif not 0 <= result["confidence"] <= 1:
                errors.append(ValidationError(
                    field="result.confidence",
                    message="confidence 必须在 0-1 范围内",
                    value=result["confidence"],
                ))
        
        return errors
    
    def _validate_metadata(self, metadata: Dict) -> List[ValidationError]:
        """验证元数据"""
        errors = []
        
        if not isinstance(metadata, dict):
            errors.append(ValidationError(
                field="metadata",
                message="metadata 必须是字典",
            ))
            return errors
        
        # 推荐有 book_id
        if "book_id" not in metadata:
            logger.debug("metadata 缺少 book_id")
        
        return errors
    
    def validate_batch(self, rules: List[Dict]) -> Dict[str, Any]:
        """
        批量验证规则
        
        Returns:
            {
                "total": int,
                "valid": int,
                "invalid": int,
                "errors": List[Dict]
            }
        """
        total = len(rules)
        valid = 0
        invalid = 0
        all_errors = []
        
        for i, rule in enumerate(rules):
            result = self.validate(rule)
            if result.is_valid:
                valid += 1
            else:
                invalid += 1
                all_errors.append({
                    "index": i,
                    "rule_id": rule.get("rule_id", "unknown"),
                    "errors": result.to_dict()["errors"],
                })
        
        return {
            "total": total,
            "valid": valid,
            "invalid": invalid,
            "errors": all_errors,
        }
