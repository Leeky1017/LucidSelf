"""
Output - YAML输出和报告生成
"""

import json
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List

import yaml

from .models import ExtractionResult


class YAMLOutput:
    """YAML输出器"""
    
    def __init__(self, output_dir: Path):
        self.output_dir = output_dir
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # 创建子目录
        (self.output_dir / "factors").mkdir(exist_ok=True)
        (self.output_dir / "snippets").mkdir(exist_ok=True)
        (self.output_dir / "terms").mkdir(exist_ok=True)
        (self.output_dir / "relations").mkdir(exist_ok=True)
        (self.output_dir / "evidence").mkdir(exist_ok=True)
        (self.output_dir / "cross_system").mkdir(exist_ok=True)
    
    def _serialize(self, obj: Any) -> Any:
        """序列化对象为YAML兼容格式"""
        from enum import Enum
        
        if hasattr(obj, 'model_dump'):
            data = obj.model_dump()
            # 递归处理所有值
            return {k: self._serialize(v) for k, v in data.items()}
        elif isinstance(obj, Enum):
            return obj.value
        elif isinstance(obj, datetime):
            return obj.isoformat()
        elif isinstance(obj, list):
            return [self._serialize(item) for item in obj]
        elif isinstance(obj, dict):
            return {k: self._serialize(v) for k, v in obj.items()}
        return obj
    
    def write_result(self, result: ExtractionResult) -> Dict[str, Path]:
        """写入单个提取结果"""
        book_id = result.book_id
        written_files: Dict[str, Path] = {}
        
        # 写入因子
        if result.factors:
            factors_path = self.output_dir / "factors" / f"{book_id}_factors.yaml"
            factors_data = {
                "book_id": book_id,
                "source_file": result.source_file,
                "extracted_at": datetime.now().isoformat(),
                "factors": [self._serialize(f) for f in result.factors]
            }
            with open(factors_path, 'w', encoding='utf-8') as f:
                yaml.dump(factors_data, f, allow_unicode=True, default_flow_style=False, sort_keys=False)
            written_files["factors"] = factors_path
        
        # 写入叙事素材
        if result.snippets:
            snippets_path = self.output_dir / "snippets" / f"{book_id}_snippets.yaml"
            snippets_data = {
                "book_id": book_id,
                "source_file": result.source_file,
                "extracted_at": datetime.now().isoformat(),
                "snippets": [self._serialize(s) for s in result.snippets]
            }
            with open(snippets_path, 'w', encoding='utf-8') as f:
                yaml.dump(snippets_data, f, allow_unicode=True, default_flow_style=False, sort_keys=False)
            written_files["snippets"] = snippets_path
        
        # 写入术语
        if result.terms:
            terms_path = self.output_dir / "terms" / f"{book_id}_terms.yaml"
            terms_data = {
                "book_id": book_id,
                "source_file": result.source_file,
                "extracted_at": datetime.now().isoformat(),
                "terms": [self._serialize(t) for t in result.terms]
            }
            with open(terms_path, 'w', encoding='utf-8') as f:
                yaml.dump(terms_data, f, allow_unicode=True, default_flow_style=False, sort_keys=False)
            written_files["terms"] = terms_path
        
        # 写入关系
        if result.relations:
            relations_path = self.output_dir / "relations" / f"{book_id}_relations.yaml"
            relations_data = {
                "book_id": book_id,
                "source_file": result.source_file,
                "extracted_at": datetime.now().isoformat(),
                "relations": [self._serialize(r) for r in result.relations]
            }
            with open(relations_path, 'w', encoding='utf-8') as f:
                yaml.dump(relations_data, f, allow_unicode=True, default_flow_style=False, sort_keys=False)
            written_files["relations"] = relations_path
        
        # 写入证据链
        if result.evidence_chains:
            evidence_path = self.output_dir / "evidence" / f"{book_id}_evidence.yaml"
            evidence_data = {
                "book_id": book_id,
                "source_file": result.source_file,
                "extracted_at": datetime.now().isoformat(),
                "evidence_chains": [self._serialize(e) for e in result.evidence_chains]
            }
            with open(evidence_path, 'w', encoding='utf-8') as f:
                yaml.dump(evidence_data, f, allow_unicode=True, default_flow_style=False, sort_keys=False)
            written_files["evidence"] = evidence_path
        
        # 写入跨体系映射
        if result.cross_mappings:
            cross_path = self.output_dir / "cross_system" / f"{book_id}_cross_mappings.yaml"
            cross_data = {
                "book_id": book_id,
                "source_file": result.source_file,
                "extracted_at": datetime.now().isoformat(),
                "cross_mappings": [self._serialize(c) for c in result.cross_mappings]
            }
            with open(cross_path, 'w', encoding='utf-8') as f:
                yaml.dump(cross_data, f, allow_unicode=True, default_flow_style=False, sort_keys=False)
            written_files["cross_system"] = cross_path
        
        return written_files


class ReportGenerator:
    """提取报告生成器"""
    
    def __init__(self, output_dir: Path):
        self.output_dir = output_dir
        self.output_dir.mkdir(parents=True, exist_ok=True)
    
    def generate_summary(self, results: Dict[str, List[ExtractionResult]]) -> str:
        """生成提取摘要"""
        lines = [
            "# Schema提取报告",
            f"",
            f"**生成时间**: {datetime.now().isoformat()}",
            "",
            "## 提取统计",
            "",
            "| 典籍 | 文件数 | 因子 | 叙事素材 | 术语 | 关系 | 证据链 | 跨体系映射 | 错误 |",
            "|------|--------|------|----------|------|------|--------|------------|------|",
        ]
        
        total_factors = 0
        total_snippets = 0
        total_terms = 0
        total_relations = 0
        total_evidence = 0
        total_cross = 0
        total_errors = 0
        
        for book_id, book_results in sorted(results.items()):
            factors = sum(len(r.factors) for r in book_results)
            snippets = sum(len(r.snippets) for r in book_results)
            terms = sum(len(r.terms) for r in book_results)
            relations = sum(len(r.relations) for r in book_results)
            evidence = sum(len(r.evidence_chains) for r in book_results)
            cross = sum(len(r.cross_mappings) for r in book_results)
            errors = sum(len(r.errors) for r in book_results)
            
            total_factors += factors
            total_snippets += snippets
            total_terms += terms
            total_relations += relations
            total_evidence += evidence
            total_cross += cross
            total_errors += errors
            
            lines.append(
                f"| {book_id} | {len(book_results)} | {factors} | {snippets} | {terms} | {relations} | {evidence} | {cross} | {errors} |"
            )
        
        lines.append(
            f"| **总计** | - | **{total_factors}** | **{total_snippets}** | **{total_terms}** | **{total_relations}** | **{total_evidence}** | **{total_cross}** | **{total_errors}** |"
        )
        
        # 添加错误详情
        all_errors = []
        for book_id, book_results in results.items():
            for result in book_results:
                for error in result.errors:
                    all_errors.append(f"- [{book_id}] {error}")
        
        if all_errors:
            lines.extend([
                "",
                "## 错误详情",
                "",
            ])
            lines.extend(all_errors[:50])  # 最多显示50条
            if len(all_errors) > 50:
                lines.append(f"... 还有 {len(all_errors) - 50} 条错误")
        
        # 添加警告
        all_warnings = []
        for book_id, book_results in results.items():
            for result in book_results:
                for warning in result.warnings:
                    all_warnings.append(f"- [{book_id}] {warning}")
        
        if all_warnings:
            lines.extend([
                "",
                "## 警告",
                "",
            ])
            lines.extend(all_warnings[:30])
            if len(all_warnings) > 30:
                lines.append(f"... 还有 {len(all_warnings) - 30} 条警告")
        
        return "\n".join(lines)
    
    def write_report(self, results: Dict[str, List[ExtractionResult]], filename: str = "extraction_report.md"):
        """写入报告文件"""
        report = self.generate_summary(results)
        report_path = self.output_dir / filename
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(report)
        return report_path
