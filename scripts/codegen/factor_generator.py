"""
FactorCodeGenerator - 因子代码生成器

将 ConfigFactor JSONL 编译为 Python 因子定义模块。
对照数据契约 §1.1
"""

from __future__ import annotations

import json
import logging
import re
from pathlib import Path
from typing import Any, Dict, List, Optional

from pydantic import ValidationError as PydanticValidationError

from backend.core.contracts import (
    ConfigFactor,
    FactorCategory,
    VERSION_PATTERN,
)
from scripts.codegen.base import BaseCodeGenerator
from scripts.codegen.exceptions import CompilationError, ValidationError

logger = logging.getLogger(__name__)


class FactorCodeGenerator(BaseCodeGenerator):
    """
    因子代码生成器
    
    输入: ConfigFactor JSONL
    输出: Python 因子定义模块（Enum + 校验函数 + 元数据）
    运行时产出: FactorValue → 组装为 FactorMatrix
    """
    
    def __init__(self, output_dir: Optional[Path] = None):
        if output_dir is None:
            output_dir = Path("backend/generated/factors")
        super().__init__(output_dir)
    
    def validate(self, source: Dict[str, Any]) -> List[str]:
        """校验因子 JSON"""
        errors = []
        
        # 必填字段检查（数据契约 §1.1）
        for field in ["factor_id", "version", "status", "engine_id"]:
            if field not in source:
                errors.append(f"Missing required field: {field}")
        
        # version 格式检查
        if "version" in source:
            if not re.match(VERSION_PATTERN, source["version"]):
                errors.append(f"Invalid version format: {source['version']}")
        
        # status 枚举检查
        if "status" in source:
            if source["status"] not in ["active", "experimental", "deprecated"]:
                errors.append(f"Invalid status: {source['status']}")
        
        # Pydantic 完整校验
        if not errors:
            try:
                ConfigFactor(**source)
            except PydanticValidationError as e:
                for err in e.errors():
                    loc = ".".join(str(x) for x in err["loc"])
                    errors.append(f"{loc}: {err['msg']}")
        
        return errors
    
    def compile(self, source: Dict[str, Any]) -> str:
        """编译单个因子为 Python 代码片段"""
        factor = ConfigFactor(**source)
        return self._generate_factor_entry(factor)
    
    def compile_batch(
        self,
        factors: List[Dict[str, Any]],
        engine_id: str,
        version: str,
    ) -> str:
        """批量编译因子为完整模块"""
        # 校验所有因子
        all_errors = []
        validated_factors = []
        
        for i, factor_data in enumerate(factors):
            errors = self.validate(factor_data)
            if errors:
                all_errors.extend([f"[{i}] {e}" for e in errors])
            else:
                validated_factors.append(ConfigFactor(**factor_data))
        
        if all_errors:
            raise ValidationError(
                f"Batch validation failed for {len(all_errors)} factors",
                errors=all_errors
            )
        
        return self._generate_module(validated_factors, engine_id, version)
    
    def _generate_factor_entry(self, factor: ConfigFactor) -> str:
        """生成单个因子的元数据字典"""
        return f'''    "{factor.factor_id}": {{
        "factor_id": "{factor.factor_id}",
        "label_zh": "{factor.label_zh}",
        "label_en": {repr(factor.label_en)},
        "category": FactorCategory.{factor.category.name},
        "value_type": "{factor.value_type}",
        "enum_values": {factor.enum_values!r},
        "status": "{factor.status.value}",
        "description_zh": "{factor.description_zh}",
        "knowledge_ref": {factor.knowledge_ref!r},
        "version": "{factor.version}",
        "engine_id": "{factor.engine_id}",
    }},'''
    
    def _generate_module(
        self,
        factors: List[ConfigFactor],
        engine_id: str,
        version: str,
    ) -> str:
        """生成完整的因子模块"""
        header = self.generate_header(
            f"Factors: {engine_id}",
            version=version
        )
        
        imports = self._get_imports()
        
        # 生成因子 Enum
        enum_entries = []
        for factor in factors:
            enum_entries.append(
                f'    {factor.factor_id.upper()} = "{factor.factor_id}"'
            )
        enum_block = "\n".join(enum_entries)
        
        # 生成因子元数据字典
        metadata_entries = []
        for factor in factors:
            metadata_entries.append(self._generate_factor_entry(factor))
        metadata_block = "\n".join(metadata_entries)
        
        # 按类别分组
        categories = set(f.category.value for f in factors)
        category_groups = {}
        for cat in categories:
            cat_factors = [f.factor_id for f in factors if f.category.value == cat]
            category_groups[cat] = cat_factors
        
        category_dict = ",\n    ".join(
            f'"{cat}": {fids!r}' for cat, fids in category_groups.items()
        )
        
        code = f'''{header}{imports}


class {engine_id.title().replace("_", "")}Factors(str, Enum):
    """
    {engine_id} 因子枚举
    
    共 {len(factors)} 个因子
    """
{enum_block}


# 因子元数据字典
FACTOR_METADATA: Dict[str, Dict[str, Any]] = {{
{metadata_block}
}}


# 按类别分组
FACTORS_BY_CATEGORY: Dict[str, List[str]] = {{
    {category_dict}
}}


def get_factor_metadata(factor_id: str) -> Optional[Dict[str, Any]]:
    """获取因子元数据"""
    return FACTOR_METADATA.get(factor_id)


def validate_factor_value(factor_id: str, value: Any) -> bool:
    """
    校验因子值
    
    Args:
        factor_id: 因子ID
        value: 因子值
    
    Returns:
        True 表示值有效
    """
    meta = FACTOR_METADATA.get(factor_id)
    if not meta:
        return False
    
    value_type = meta["value_type"]
    
    if value_type == "boolean":
        return isinstance(value, bool)
    elif value_type == "float":
        return isinstance(value, (int, float))
    elif value_type == "string":
        return isinstance(value, str)
    elif value_type == "enum":
        return value in (meta.get("enum_values") or [])
    
    return True


def create_factor_value(
    factor_id: str,
    value: Any,
    confidence: float = 1.0,
    source: str = "calculator"
) -> FactorValue:
    """
    创建 FactorValue 实例
    
    Args:
        factor_id: 因子ID
        value: 因子值
        confidence: 置信度
        source: 来源
    
    Returns:
        FactorValue 实例
    """
    return FactorValue(
        factor_id=factor_id,
        value=value,
        confidence=confidence,
        source=source
    )
'''
        return code
    
    def _get_imports(self) -> str:
        """生成 import 语句"""
        imports = [
            "from enum import Enum",
            "from typing import Any, Dict, List, Optional",
            "from backend.core.contracts import FactorCategory, FactorValue",
        ]
        return self.generate_imports(imports)
    
    def compile_jsonl_file(
        self,
        jsonl_path: Path,
        engine_id: str,
        version: str,
    ) -> str:
        """
        从 JSONL 文件编译因子模块
        
        Args:
            jsonl_path: JSONL 文件路径
            engine_id: 引擎ID
            version: 版本号
        
        Returns:
            生成的 Python 代码
        """
        factors = []
        
        with open(jsonl_path, "r", encoding="utf-8") as f:
            for line_num, line in enumerate(f, 1):
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                
                try:
                    factor_data = json.loads(line)
                    factors.append(factor_data)
                except json.JSONDecodeError as e:
                    raise CompilationError(
                        f"Invalid JSON at line {line_num}: {e}",
                        source_file=str(jsonl_path)
                    )
        
        return self.compile_batch(factors, engine_id, version)
