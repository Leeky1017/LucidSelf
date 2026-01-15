"""
Migration Validator

迁移验证器 - 确保数据质量，对齐 design.md Components and Interfaces §2

验证内容:
- ID 格式验证 (semantic_id, factor_id, snippet_id, relation_id, evidence_id, concept_id)
- 因子本体验证 (factor_refs 存在性)
- L2.5 完整性验证 (related_semantics, evidence_refs, cross_domain_refs)
- 叙事素材格式验证 (snippet_id, trigger_human, trigger_condition, role, snippet_text)
"""

from __future__ import annotations

import logging
import re
from pathlib import Path
from typing import Any, Dict, List, Optional, Set

from scripts.codegen.engine_mapping import FACTOR_ID_PREFIXES, infer_engine_id

logger = logging.getLogger(__name__)


# -----------------------------------------------------------------------------
# ID 格式正则常量 (对齐数据契约 §9.2, tasks.md 1.2)
# -----------------------------------------------------------------------------

SEMANTIC_ID_PATTERN = r"^[a-z]+_v\d+_[a-z0-9_]+_\d{3}$"
FACTOR_ID_PATTERN = r"^[a-z][a-z0-9_]*$"
SNIPPET_ID_PATTERN = r"^[a-z][a-z0-9_]*_\d{3}$"
RELATION_ID_PATTERN = r"^rel_[a-z0-9_]+_\d{3}$"
EVIDENCE_ID_PATTERN = r"^evi_[a-z0-9_]+_\d{3}$"
CONCEPT_ID_PATTERN = r"^concept_[a-z0-9_]+$"

# 编译正则
_SEMANTIC_ID_RE = re.compile(SEMANTIC_ID_PATTERN)
_FACTOR_ID_RE = re.compile(FACTOR_ID_PATTERN)
_SNIPPET_ID_RE = re.compile(SNIPPET_ID_PATTERN)
_RELATION_ID_RE = re.compile(RELATION_ID_PATTERN)
_EVIDENCE_ID_RE = re.compile(EVIDENCE_ID_PATTERN)
_CONCEPT_ID_RE = re.compile(CONCEPT_ID_PATTERN)


# -----------------------------------------------------------------------------
# 验证错误类型
# -----------------------------------------------------------------------------

class ValidationErrorType:
    """验证错误类型常量"""
    INVALID_SEMANTIC_ID = "INVALID_SEMANTIC_ID"
    INVALID_FACTOR_ID = "INVALID_FACTOR_ID"
    INVALID_SNIPPET_ID = "INVALID_SNIPPET_ID"
    INVALID_RELATION_ID = "INVALID_RELATION_ID"
    INVALID_EVIDENCE_ID = "INVALID_EVIDENCE_ID"
    INVALID_CONCEPT_ID = "INVALID_CONCEPT_ID"
    UNKNOWN_FACTOR = "UNKNOWN_FACTOR"
    INVALID_FACTOR_PREFIX = "INVALID_FACTOR_PREFIX"
    MISSING_L1_FIELD = "MISSING_L1_FIELD"
    MISSING_L2_FIELD = "MISSING_L2_FIELD"
    MISSING_L25_FIELD = "MISSING_L25_FIELD"
    INVALID_SNIPPET_FORMAT = "INVALID_SNIPPET_FORMAT"
    EMPTY_FACTOR_REFS = "EMPTY_FACTOR_REFS"


# -----------------------------------------------------------------------------
# 验证错误数据类
# -----------------------------------------------------------------------------

class ValidationError:
    """
    验证错误
    
    对齐 design.md Data Models §1, tasks.md 1.2
    """
    
    def __init__(
        self,
        file: str,
        line: int,
        column: int,
        error_type: str,
        message: str,
        suggestion: Optional[str] = None,
        severity: str = "ERROR",  # ERROR, WARNING
    ):
        self.file = file
        self.line = line
        self.column = column
        self.error_type = error_type
        self.message = message
        self.suggestion = suggestion
        self.severity = severity
    
    def __str__(self) -> str:
        """格式: {file}:{line}:{column}: {error_type}: {message}"""
        return f"{self.file}:{self.line}:{self.column}: {self.error_type}: {self.message}"
    
    def __repr__(self) -> str:
        return f"ValidationError({self.error_type}, {self.message!r})"
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "file": self.file,
            "line": self.line,
            "column": self.column,
            "error_type": self.error_type,
            "message": self.message,
            "suggestion": self.suggestion,
            "severity": self.severity,
        }


# -----------------------------------------------------------------------------
# 迁移验证器
# -----------------------------------------------------------------------------

class MigrationValidator:
    """
    迁移验证器 - 确保数据质量
    
    对齐 design.md Components and Interfaces §2, tasks.md 1.2
    """
    
    def __init__(self):
        self._factor_ontology: Optional[Set[str]] = None
    
    # -------------------------------------------------------------------------
    # 因子本体加载
    # -------------------------------------------------------------------------
    
    def _load_factor_ontology(self) -> Set[str]:
        """
        从 data/factor_ontology/certified/ 加载所有已认证因子 ID
        
        支持两种格式:
        1. by_category 格式: {by_category: {category: [{id: ...}, ...]}}
        2. factors 列表格式: {factors: [{id: ...}, ...]}
        """
        if self._factor_ontology is not None:
            return self._factor_ontology
        
        self._factor_ontology = set()
        certified_path = Path("data/factor_ontology/certified")
        
        if certified_path.exists():
            for yaml_file in certified_path.glob("**/*.yaml"):
                try:
                    import yaml
                    with open(yaml_file, encoding="utf-8") as f:
                        data = yaml.safe_load(f)
                    
                    if not isinstance(data, dict):
                        continue
                    
                    # 格式 1: by_category 结构 (certified 文件格式)
                    if "by_category" in data:
                        for category, factors in data["by_category"].items():
                            if isinstance(factors, list):
                                for factor in factors:
                                    if isinstance(factor, dict) and "id" in factor:
                                        self._factor_ontology.add(factor["id"])
                    
                    # 格式 2: factors 列表
                    elif "factors" in data:
                        for factor in data["factors"]:
                            if isinstance(factor, dict) and "id" in factor:
                                self._factor_ontology.add(factor["id"])
                            elif isinstance(factor, str):
                                self._factor_ontology.add(factor)
                                
                except Exception as e:
                    logger.warning(f"Failed to load factor ontology from {yaml_file}: {e}")
        
        # 备用: 从旧格式因子本体文件加载
        if not self._factor_ontology:
            ontology_file = Path("典籍/因子本体_总览_v1.md")
            if ontology_file.exists():
                try:
                    content = ontology_file.read_text(encoding="utf-8")
                    factor_pattern = re.compile(r'\|\s*([a-z][a-z0-9_]*)\s*\|')
                    self._factor_ontology = set(factor_pattern.findall(content))
                except Exception as e:
                    logger.warning(f"Failed to load factor ontology from {ontology_file}: {e}")
        
        logger.info(f"Loaded {len(self._factor_ontology)} factors from ontology")
        return self._factor_ontology
    
    # -------------------------------------------------------------------------
    # 验证入口
    # -------------------------------------------------------------------------
    
    def validate_entry(self, entry_data: Dict[str, Any], file_path: str = "") -> List[ValidationError]:
        """
        验证单个条目
        
        调用以下验证方法并汇总错误:
        - _validate_ids
        - _validate_factor_refs
        - _validate_l25_completeness
        - _validate_narrative_snippets
        
        Args:
            entry_data: 条目数据字典
            file_path: 源文件路径
        
        Returns:
            验证错误列表
        """
        errors: List[ValidationError] = []
        errors.extend(self._validate_ids(entry_data, file_path))
        errors.extend(self._validate_factor_refs(entry_data, file_path))
        errors.extend(self._validate_l1_completeness(entry_data, file_path))
        errors.extend(self._validate_l2_completeness(entry_data, file_path))
        errors.extend(self._validate_l25_completeness(entry_data, file_path))
        errors.extend(self._validate_narrative_snippets(entry_data, file_path))
        return errors
    
    # -------------------------------------------------------------------------
    # ID 格式验证
    # -------------------------------------------------------------------------
    
    def _validate_ids(self, entry_data: Dict[str, Any], file_path: str) -> List[ValidationError]:
        """
        验证所有 ID 格式
        
        验证: semantic_id, snippet_id, relation_id, evidence_id, concept_id
        """
        errors: List[ValidationError] = []
        
        # semantic_id
        semantic_id = entry_data.get("semantic_id", "")
        if semantic_id and not _SEMANTIC_ID_RE.match(semantic_id):
            errors.append(ValidationError(
                file=file_path,
                line=1,
                column=1,
                error_type=ValidationErrorType.INVALID_SEMANTIC_ID,
                message=f"Invalid semantic_id format: {semantic_id}",
                suggestion=f"Must match pattern: {SEMANTIC_ID_PATTERN}",
            ))
        
        # snippet_ids in narrative_snippets
        for snippet in entry_data.get("narrative_snippets", []):
            snippet_id = snippet.get("snippet_id", "")
            if snippet_id and not _SNIPPET_ID_RE.match(snippet_id):
                errors.append(ValidationError(
                    file=file_path,
                    line=1,
                    column=1,
                    error_type=ValidationErrorType.INVALID_SNIPPET_ID,
                    message=f"Invalid snippet_id format: {snippet_id}",
                    suggestion=f"Must match pattern: {SNIPPET_ID_PATTERN}",
                ))
        
        # relation_ids in related_semantics
        for rel in entry_data.get("related_semantics", []):
            relation_id = rel.get("relation_id", "")
            if relation_id and not _RELATION_ID_RE.match(relation_id):
                errors.append(ValidationError(
                    file=file_path,
                    line=1,
                    column=1,
                    error_type=ValidationErrorType.INVALID_RELATION_ID,
                    message=f"Invalid relation_id format: {relation_id}",
                    suggestion=f"Must match pattern: {RELATION_ID_PATTERN}",
                ))
        
        # evidence_ids in evidence_refs
        for evi in entry_data.get("evidence_refs", []):
            evidence_id = evi.get("evidence_id", "")
            if evidence_id and not _EVIDENCE_ID_RE.match(evidence_id):
                errors.append(ValidationError(
                    file=file_path,
                    line=1,
                    column=1,
                    error_type=ValidationErrorType.INVALID_EVIDENCE_ID,
                    message=f"Invalid evidence_id format: {evidence_id}",
                    suggestion=f"Must match pattern: {EVIDENCE_ID_PATTERN}",
                ))
        
        # concept_ids in cross_domain_refs
        for cross in entry_data.get("cross_domain_refs", []):
            concept_id = cross.get("concept_id", "")
            if concept_id and not _CONCEPT_ID_RE.match(concept_id):
                errors.append(ValidationError(
                    file=file_path,
                    line=1,
                    column=1,
                    error_type=ValidationErrorType.INVALID_CONCEPT_ID,
                    message=f"Invalid concept_id format: {concept_id}",
                    suggestion=f"Must match pattern: {CONCEPT_ID_PATTERN}",
                ))
        
        return errors
    
    # -------------------------------------------------------------------------
    # 因子引用验证
    # -------------------------------------------------------------------------
    
    def _validate_factor_refs(self, entry_data: Dict[str, Any], file_path: str) -> List[ValidationError]:
        """
        验证因子引用
        
        - 验证 factor_refs 列表中每个 factor_id 格式
        - 检查是否在因子本体中存在（不存在则记录 WARNING 级别）
        - 验证因子前缀与 engine_id 匹配
        """
        errors: List[ValidationError] = []
        factor_refs = entry_data.get("factor_refs", [])
        engine_id = entry_data.get("engine_id", "")
        book_id = entry_data.get("book_id", "")
        
        # 如果没有 engine_id，从 book_id 推断
        if not engine_id and book_id:
            engine_id = infer_engine_id(book_id)
        
        # 加载因子本体
        ontology = self._load_factor_ontology()
        
        for factor_id in factor_refs:
            # 格式验证
            if not _FACTOR_ID_RE.match(factor_id):
                errors.append(ValidationError(
                    file=file_path,
                    line=1,
                    column=1,
                    error_type=ValidationErrorType.INVALID_FACTOR_ID,
                    message=f"Invalid factor_id format: {factor_id}",
                    suggestion=f"Must match pattern: {FACTOR_ID_PATTERN}",
                ))
                continue
            
            # 因子本体存在性检查 (WARNING 级别)
            if ontology and factor_id not in ontology:
                errors.append(ValidationError(
                    file=file_path,
                    line=1,
                    column=1,
                    error_type=ValidationErrorType.UNKNOWN_FACTOR,
                    message=f"factor_id '{factor_id}' not in ontology (new_candidate)",
                    suggestion="请检查因子本体或添加为 new_candidate",
                    severity="WARNING",
                ))
            
            # 因子前缀验证
            if engine_id:
                prefixes = FACTOR_ID_PREFIXES.get(engine_id, [])
                if prefixes and not any(factor_id.startswith(p) for p in prefixes):
                    errors.append(ValidationError(
                        file=file_path,
                        line=1,
                        column=1,
                        error_type=ValidationErrorType.INVALID_FACTOR_PREFIX,
                        message=f"factor_id '{factor_id}' does not match engine '{engine_id}' prefixes",
                        suggestion=f"Valid prefixes: {', '.join(prefixes)}",
                        severity="WARNING",
                    ))
        
        return errors
    
    # -------------------------------------------------------------------------
    # L1 完整性验证
    # -------------------------------------------------------------------------
    
    def _validate_l1_completeness(self, entry_data: Dict[str, Any], file_path: str) -> List[ValidationError]:
        """验证 L1 字段存在性"""
        errors: List[ValidationError] = []
        
        l1_data = entry_data.get("l1", {})
        original_text = l1_data.get("original_text", "") or entry_data.get("original_text", "")
        
        if not original_text or not original_text.strip():
            errors.append(ValidationError(
                file=file_path,
                line=1,
                column=1,
                error_type=ValidationErrorType.MISSING_L1_FIELD,
                message="Missing or empty original_text (L1)",
                suggestion="请确保 L1 原文区块存在且非空",
            ))
        
        return errors
    
    # -------------------------------------------------------------------------
    # L2 完整性验证
    # -------------------------------------------------------------------------
    
    def _validate_l2_completeness(self, entry_data: Dict[str, Any], file_path: str) -> List[ValidationError]:
        """验证 L2 字段存在性"""
        errors: List[ValidationError] = []
        
        l2_data = entry_data.get("l2", {})
        subject = entry_data.get("subject", "") or l2_data.get("subject", "")
        factor_refs = entry_data.get("factor_refs", []) or l2_data.get("factors", [])
        
        if not subject or not subject.strip():
            errors.append(ValidationError(
                file=file_path,
                line=1,
                column=1,
                error_type=ValidationErrorType.MISSING_L2_FIELD,
                message="Missing or empty subject (L2)",
                suggestion="请确保 L2 语义区块包含 subject 字段",
                severity="WARNING",
            ))
        
        if not factor_refs:
            errors.append(ValidationError(
                file=file_path,
                line=1,
                column=1,
                error_type=ValidationErrorType.EMPTY_FACTOR_REFS,
                message="Empty factor_refs list (L2)",
                suggestion="请确保 L2 语义区块包含至少一个因子引用",
                severity="WARNING",
            ))
        
        return errors
    
    # -------------------------------------------------------------------------
    # L2.5 完整性验证
    # -------------------------------------------------------------------------
    
    def _validate_l25_completeness(self, entry_data: Dict[str, Any], file_path: str) -> List[ValidationError]:
        """
        验证 L2.5 桥接层完整性
        
        验证 related_semantics, evidence_refs, cross_domain_refs 存在性
        """
        errors: List[ValidationError] = []
        
        l25_data = entry_data.get("l25", {})
        
        # related_semantics
        related = entry_data.get("related_semantics", []) or l25_data.get("relations", [])
        if not related:
            errors.append(ValidationError(
                file=file_path,
                line=1,
                column=1,
                error_type=ValidationErrorType.MISSING_L25_FIELD,
                message="Empty related_semantics (L2.5)",
                suggestion="请补充 L2.5 因子关系表",
                severity="WARNING",
            ))
        
        # evidence_refs
        evidence = entry_data.get("evidence_refs", []) or l25_data.get("evidence", [])
        if not evidence:
            errors.append(ValidationError(
                file=file_path,
                line=1,
                column=1,
                error_type=ValidationErrorType.MISSING_L25_FIELD,
                message="Empty evidence_refs (L2.5)",
                suggestion="请补充 L2.5 证据链表",
                severity="WARNING",
            ))
        
        # cross_domain_refs (可选，仅对 psych 体系必需)
        cross = entry_data.get("cross_domain_refs", []) or l25_data.get("cross_system", [])
        engine_id = entry_data.get("engine_id", "")
        if engine_id == "psych" and not cross:
            errors.append(ValidationError(
                file=file_path,
                line=1,
                column=1,
                error_type=ValidationErrorType.MISSING_L25_FIELD,
                message="Empty cross_domain_refs for psych engine (L2.5)",
                suggestion="心理学体系应包含跨体系映射",
                severity="WARNING",
            ))
        
        return errors
    
    # -------------------------------------------------------------------------
    # 叙事素材格式验证
    # -------------------------------------------------------------------------
    
    def _validate_narrative_snippets(self, entry_data: Dict[str, Any], file_path: str) -> List[ValidationError]:
        """
        验证叙事素材格式
        
        验证每个 snippet 的: snippet_id, trigger_human, trigger_condition, role, snippet_text
        """
        errors: List[ValidationError] = []
        snippets = entry_data.get("narrative_snippets", [])
        
        valid_roles = {"描述", "解释", "建议", "警示", "比喻", "引用"}
        
        for i, snippet in enumerate(snippets):
            if not isinstance(snippet, dict):
                errors.append(ValidationError(
                    file=file_path,
                    line=1,
                    column=1,
                    error_type=ValidationErrorType.INVALID_SNIPPET_FORMAT,
                    message=f"Snippet {i} is not a dict",
                    suggestion="叙事素材必须是字典格式",
                ))
                continue
            
            # snippet_id 必需
            snippet_id = snippet.get("snippet_id", "")
            if not snippet_id:
                errors.append(ValidationError(
                    file=file_path,
                    line=1,
                    column=1,
                    error_type=ValidationErrorType.INVALID_SNIPPET_FORMAT,
                    message=f"Snippet {i} missing snippet_id",
                    suggestion="叙事素材必须包含 snippet_id",
                ))
            
            # role 必需
            role = snippet.get("role", "")
            role_str = role.value if hasattr(role, "value") else str(role)
            if not role_str:
                errors.append(ValidationError(
                    file=file_path,
                    line=1,
                    column=1,
                    error_type=ValidationErrorType.INVALID_SNIPPET_FORMAT,
                    message=f"Snippet {snippet_id or i} missing role",
                    suggestion=f"有效角色: {', '.join(valid_roles)}",
                ))
            
            # snippet_text 必需
            snippet_text = snippet.get("snippet_text", "")
            if not snippet_text or not snippet_text.strip():
                errors.append(ValidationError(
                    file=file_path,
                    line=1,
                    column=1,
                    error_type=ValidationErrorType.INVALID_SNIPPET_FORMAT,
                    message=f"Snippet {snippet_id or i} missing or empty snippet_text",
                    suggestion="叙事素材必须包含非空文本",
                ))
            
            # trigger_human 和 trigger_condition 映射验证
            trigger_human = snippet.get("trigger_human", "")
            trigger_condition = snippet.get("trigger_condition", "")
            factor_trigger = snippet.get("factor_trigger", "")
            
            # 如果有 factor_trigger，trigger_condition 应该等于它
            if factor_trigger and trigger_condition != factor_trigger:
                errors.append(ValidationError(
                    file=file_path,
                    line=1,
                    column=1,
                    error_type=ValidationErrorType.INVALID_SNIPPET_FORMAT,
                    message=f"Snippet {snippet_id or i}: trigger_condition != factor_trigger",
                    suggestion="factor_trigger 非空时 trigger_condition 应等于 factor_trigger",
                    severity="WARNING",
                ))
        
        return errors
    
    # -------------------------------------------------------------------------
    # 批量验证
    # -------------------------------------------------------------------------
    
    def validate_batch(
        self, entries: List[Dict[str, Any]], file_path: str = ""
    ) -> Dict[str, List[ValidationError]]:
        """
        批量验证多个条目
        
        Returns:
            {entry_id: [errors]} 映射
        """
        results: Dict[str, List[ValidationError]] = {}
        for i, entry in enumerate(entries):
            entry_id = entry.get("semantic_id", f"entry_{i}")
            results[entry_id] = self.validate_entry(entry, file_path)
        return results
