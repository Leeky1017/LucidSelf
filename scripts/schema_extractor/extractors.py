"""
Extractors - 从Markdown提取各类Schema的核心逻辑
"""

import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from .models import (
    ConfigFactor,
    ConfigRelation,
    CrossSystemMapping,
    EvidenceChainEntry,
    ExtractionResult,
    NarrativeSnippet,
    SnippetRole,
    TermGlossary,
)


class MarkdownExtractor:
    """Markdown内容提取器"""
    
    def __init__(self, content: str, source_file: str, book_id: str):
        self.content = content
        self.source_file = source_file
        self.book_id = book_id
        self.errors: List[str] = []
        self.warnings: List[str] = []
        
    def extract_between_tags(self, begin_tag: str, end_tag: str) -> List[str]:
        """提取标签之间的内容块"""
        pattern = rf"<!--\s*{begin_tag}\s*-->(.*?)<!--\s*{end_tag}\s*-->"
        matches = re.findall(pattern, self.content, re.DOTALL)
        return matches
    
    def parse_table(self, table_content: str) -> List[Dict[str, str]]:
        """解析Markdown表格（保留空单元格）"""
        lines = [l.strip() for l in table_content.strip().split('\n') if l.strip()]
        
        # 找到表头行（包含|的行）
        table_lines = [l for l in lines if '|' in l]
        if len(table_lines) < 3:  # 至少需要表头、分隔符、一行数据
            return []
        
        # 解析表头 - 保留空单元格
        header_line = table_lines[0]
        # 去掉首尾的|，然后按|分割
        header_parts = header_line.strip('|').split('|')
        headers = [h.strip() for h in header_parts]
        
        # 跳过分隔符行（包含---的行）
        data_lines = [l for l in table_lines[1:] if '---' not in l]
        
        results = []
        for line in data_lines:
            # 清理行首空格后再解析
            clean_line = line.strip()
            cell_parts = clean_line.strip('|').split('|')
            cells = [c.strip() for c in cell_parts]
            
            # 处理第一列为空的情况（可能是格式问题导致的偏移）
            if cells and cells[0] == '' and len(cells) > 1:
                # 检查是否第二列看起来像因子类型
                potential_type = cells[1] if len(cells) > 1 else ''
                if potential_type and any(kw in potential_type for kw in ['类', 'Type', '时间', '关系', '结构', '状态', '能量', '边界']):
                    # 向左移动一位
                    cells = cells[1:]
            
            if len(cells) == len(headers):
                row = dict(zip(headers, cells))
                results.append(row)
            elif len(cells) > 0:
                # 列数不匹配时尝试修复
                # 补齐或截断
                while len(cells) < len(headers):
                    cells.append("")
                cells = cells[:len(headers)]
                row = dict(zip(headers, cells))
                results.append(row)
        
        return results
    
    def extract_factors(self) -> List[ConfigFactor]:
        """提取因子层表格（支持多种格式）"""
        factors = []
        
        # 中英文列名映射（扩展版）
        column_map = {
            # 中文列名变体
            "因子类型": "factor_type",
            "因子标签（人话）": "factor_label",
            "因子标签": "factor_label",
            "因子ID（如已存在）": "factor_id",
            "因子ID（必填）": "factor_id",
            "因子ID": "factor_id",
            "factor_id": "factor_id",
            "因子来源": "factor_source",
            "角色/位置": "role_position",
            "取值/约束": "value_constraint",
            "engine_id": "engine_id",
            "引擎归属": "engine_id",
            "备注": "notes",
            # 英文列名变体（西方典籍）
            "Factor Type": "factor_type",
            "Factor Label": "factor_label",
            "Factor Label (Human-readable)": "factor_label",
            "Factor ID": "factor_id",
            "Factor ID (if exists)": "factor_id",
            "Factor Source": "factor_source",
            "Role/Position": "role_position",
            "Value/Constraints": "value_constraint",
            "Value Constraints": "value_constraint",
            "Notes": "notes",
        }
        
        # 策略1: 从FACTOR_BEGIN块提取
        blocks = self.extract_between_tags("FACTOR_BEGIN", "FACTOR_END")
        
        # 策略2: 从全文搜索因子表格（处理没有FACTOR标记的情况）
        # 识别因子表格的表头模式
        factor_table_patterns = [
            r'\|\s*因子类型\s*\|[^\n]+\|\n\|[-:\s|]+\|([^#]+?)(?=\n\n|\n###|\n##|\n#|$)',
            r'\|\s*Factor Type\s*\|[^\n]+\|\n\|[-:\s|]+\|([^#]+?)(?=\n\n|\n###|\n##|\n#|$)',
        ]
        
        for pattern in factor_table_patterns:
            matches = re.findall(pattern, self.content, re.DOTALL)
            for match in matches:
                # 包含表头重建完整块
                blocks.append(match)
        
        for block in blocks:
            rows = self.parse_table(block)
            for row in rows:
                # 跳过表头行（检测是否为表头）
                if self._is_header_row(row):
                    continue
                
                try:
                    # 标准化列名
                    normalized_row = {}
                    for key, value in row.items():
                        normalized_key = column_map.get(key, key)
                        normalized_row[normalized_key] = value
                    
                    # 获取factor_id
                    factor_id = normalized_row.get("factor_id", "").strip()
                    factor_label = normalized_row.get("factor_label", "").strip()
                    factor_source = normalized_row.get("factor_source", "").strip()
                    
                    # 如果factor_id为空，尝试从factor_label生成临时ID
                    if not factor_id or factor_id == "":
                        if factor_label:
                            # 从中文标签生成临时ID：取拼音首字母或简化
                            # 简单方案：使用 "temp_" + hash
                            import hashlib
                            label_hash = hashlib.md5(factor_label.encode()).hexdigest()[:8]
                            factor_id = f"temp_{label_hash}"
                        else:
                            continue  # 既没有ID也没有标签，跳过
                    
                    # 验证factor_id格式
                    factor_id = factor_id.lower().strip()
                    if not re.match(r'^[a-z][a-z0-9_]*$', factor_id):
                        # 如果是复合ID（用逗号分隔），取第一个
                        if ',' in factor_id:
                            factor_id = factor_id.split(',')[0].strip()
                        # 仍然无效则生成临时ID
                        if not re.match(r'^[a-z][a-z0-9_]*$', factor_id):
                            if factor_label:
                                import hashlib
                                label_hash = hashlib.md5(factor_label.encode()).hexdigest()[:8]
                                factor_id = f"temp_{label_hash}"
                            else:
                                self.warnings.append(f"跳过无效factor_id: {factor_id}")
                                continue
                    
                    factor = ConfigFactor(
                        factor_type=normalized_row.get("factor_type", ""),
                        factor_label=normalized_row.get("factor_label", ""),
                        factor_id=factor_id,
                        factor_source=normalized_row.get("factor_source", "new_candidate"),
                        role_position=normalized_row.get("role_position", ""),
                        value_constraint=normalized_row.get("value_constraint", ""),
                        engine_id=normalized_row.get("engine_id", ""),
                        notes=normalized_row.get("notes", ""),
                        source_book=self.book_id,
                    )
                    factors.append(factor)
                except Exception as e:
                    self.errors.append(f"因子解析错误: {row} - {str(e)}")
        
        return factors
    
    def _is_header_row(self, row: Dict[str, str]) -> bool:
        """检测是否为表头行（被误识别的）"""
        header_patterns = [
            "因子类型", "因子标签", "因子ID", "Factor Type", "Factor ID",
            "关系ID", "关系类型", "证据ID", "概念ID",
        ]
        values = list(row.values())
        if not values:
            return True
        # 如果第一个值看起来像表头
        first_val = str(values[0]).strip()
        return first_val in header_patterns
    
    def extract_snippets(self) -> List[NarrativeSnippet]:
        """提取叙事素材（支持多种格式）"""
        # 使用字典存储，key为snippet_id，value为snippet对象
        # 当遇到重复ID时，优先保留有factor_trigger的版本
        snippets_dict: Dict[str, NarrativeSnippet] = {}
        
        # 格式1: 完整格式 `[ns_xxx]` `[trigger: xxx]` `[factor_trigger: xxx]` `[role: xxx]` 内容 → 来源
        # 注意：每个标签都可能被单独的 ` ` 包裹
        pattern_full = r'\[ns_([^\]]+)\]\s*`?\s*`?\[trigger:\s*([^\]]+)\]\s*`?\s*`?\[factor_trigger:\s*([^\]]+)\]\s*`?\s*`?\[role:\s*([^\]]+)\]`?\s*(.+?)\s*→\s*(.+)'
        
        # 格式1b: 完整格式但无 factor_trigger
        pattern_full_no_ft = r'\[ns_([^\]]+)\]\s*`?\s*`?\[trigger:\s*([^\]]+)\]\s*`?\s*`?\[role:\s*([^\]]+)\]`?\s*(.+?)\s*→\s*(.+)'
        
        # 格式2: 简化格式（无role）`[ns_xxx]` `[trigger: xxx]` 内容 → 来源
        pattern_simple = r'\[ns_([^\]]+)\]\s*`?\s*`?\[trigger:\s*([^\]]+)\]`?\s+([^→\[]+?)\s*→\s*(.+)'
        
        # 格式3: 极简格式（无trigger）`[ns_xxx]` 内容 → 来源
        pattern_minimal = r'\[ns_([^\]]+)\]\s*`?\s*([^→\[\]]+?)\s*→\s*(.+)'
        
        # 格式4: 无来源格式 `[ns_xxx]` `[trigger: xxx]` `[role: xxx]` 内容（无→）
        pattern_no_source = r'\[ns_([^\]]+)\]\s*`?\s*`?\[trigger:\s*([^\]]+)\]\s*`?\s*`?\[factor_trigger:\s*([^\]]+)\]\s*`?\s*`?\[role:\s*([^\]]+)\]`?\s*(.+)'
        
        def should_replace(existing: NarrativeSnippet, new_snippet: NarrativeSnippet) -> bool:
            """判断是否应该用新snippet替换已有的"""
            # 如果新的有factor_trigger而旧的没有，则替换
            if new_snippet.factor_trigger and not existing.factor_trigger:
                return True
            return False
        
        # 映射role到枚举
        role_map = {
            "主干": SnippetRole.MAIN,
            "主干依赖": SnippetRole.MAIN_DEPENDENCY,
            "条件分支": SnippetRole.CONDITION_BRANCH,
            "例外处理": SnippetRole.EXCEPTION,
            "总结": SnippetRole.SUMMARY,
            "理论基础": SnippetRole.MAIN_DEPENDENCY,
            "吉象": SnippetRole.MAIN,
            "凶象": SnippetRole.CONDITION_BRANCH,
        }
        
        lines = self.content.split('\n')
        for line in lines:
            if '[ns_' in line:  # 只需要有ns_
                clean_line = line.replace('`', '')
                
                # 尝试完整格式
                match = re.search(pattern_full, clean_line)
                if match:
                    try:
                        snippet_id = f"ns_{match.group(1)}"
                        trigger = match.group(2).strip()
                        factor_trigger = match.group(3).strip() if match.group(3) else None
                        role_str = match.group(4).strip()
                        snippet_text = match.group(5).strip()
                        source_ref = match.group(6).strip()
                        role = role_map.get(role_str, SnippetRole.MAIN)
                        
                        snippet = NarrativeSnippet(
                            snippet_id=snippet_id,
                            trigger=trigger,
                            factor_trigger=factor_trigger,
                            role=role,
                            snippet_text=snippet_text,
                            source_ref=source_ref,
                            source_book=self.book_id,
                        )
                        # 智能去重：优先保留有factor_trigger的版本
                        if snippet_id not in snippets_dict or should_replace(snippets_dict[snippet_id], snippet):
                            snippets_dict[snippet_id] = snippet
                        continue
                    except Exception as e:
                        self.errors.append(f"叙事素材解析错误(完整格式): {line[:80]} - {str(e)}")
                
                # 尝试完整格式但无 factor_trigger
                match = re.search(pattern_full_no_ft, clean_line)
                if match:
                    try:
                        snippet_id = f"ns_{match.group(1)}"
                        trigger = match.group(2).strip()
                        role_str = match.group(3).strip()
                        snippet_text = match.group(4).strip()
                        source_ref = match.group(5).strip()
                        role = role_map.get(role_str, SnippetRole.MAIN)
                        
                        snippet = NarrativeSnippet(
                            snippet_id=snippet_id,
                            trigger=trigger,
                            factor_trigger=None,
                            role=role,
                            snippet_text=snippet_text,
                            source_ref=source_ref,
                            source_book=self.book_id,
                        )
                        if snippet_id not in snippets_dict or should_replace(snippets_dict[snippet_id], snippet):
                            snippets_dict[snippet_id] = snippet
                        continue
                    except Exception as e:
                        self.errors.append(f"叙事素材解析错误(无factor_trigger格式): {line[:80]} - {str(e)}")
                
                # 尝试简化格式（无role）
                match = re.search(pattern_simple, clean_line)
                if match:
                    try:
                        snippet_id = f"ns_{match.group(1)}"
                        trigger = match.group(2).strip()
                        snippet_text = match.group(3).strip()
                        source_ref = match.group(4).strip()
                        
                        snippet = NarrativeSnippet(
                            snippet_id=snippet_id,
                            trigger=trigger,
                            factor_trigger=None,
                            role=SnippetRole.MAIN,
                            snippet_text=snippet_text,
                            source_ref=source_ref,
                            source_book=self.book_id,
                        )
                        if snippet_id not in snippets_dict or should_replace(snippets_dict[snippet_id], snippet):
                            snippets_dict[snippet_id] = snippet
                        continue
                    except Exception as e:
                        self.errors.append(f"叙事素材解析错误(简化格式): {line[:80]} - {str(e)}")
                
                # 尝试极简格式（无trigger）
                match = re.search(pattern_minimal, clean_line)
                if match:
                    try:
                        snippet_id = f"ns_{match.group(1)}"
                        snippet_text = match.group(2).strip()
                        source_ref = match.group(3).strip()
                        
                        snippet = NarrativeSnippet(
                            snippet_id=snippet_id,
                            trigger="",
                            factor_trigger=None,
                            role=SnippetRole.MAIN,
                            snippet_text=snippet_text,
                            source_ref=source_ref,
                            source_book=self.book_id,
                        )
                        if snippet_id not in snippets_dict or should_replace(snippets_dict[snippet_id], snippet):
                            snippets_dict[snippet_id] = snippet
                        continue
                    except Exception as e:
                        self.errors.append(f"叙事素材解析错误(极简格式): {line[:80]} - {str(e)}")
                
                # 尝试无来源格式（有trigger/role但无→）
                match = re.search(pattern_no_source, clean_line)
                if match and '→' not in clean_line:
                    try:
                        snippet_id = f"ns_{match.group(1)}"
                        trigger = match.group(2).strip()
                        factor_trigger = match.group(3).strip() if match.group(3) else None
                        role_str = match.group(4).strip()
                        snippet_text = match.group(5).strip()
                        role = role_map.get(role_str, SnippetRole.MAIN)
                        
                        snippet = NarrativeSnippet(
                            snippet_id=snippet_id,
                            trigger=trigger,
                            factor_trigger=factor_trigger,
                            role=role,
                            snippet_text=snippet_text,
                            source_ref="",  # 无来源
                            source_book=self.book_id,
                        )
                        if snippet_id not in snippets_dict or should_replace(snippets_dict[snippet_id], snippet):
                            snippets_dict[snippet_id] = snippet
                    except Exception as e:
                        self.errors.append(f"叙事素材解析错误(无来源格式): {line[:80]} - {str(e)}")
        
        return list(snippets_dict.values())
    
    def extract_terms(self) -> List[TermGlossary]:
        """提取术语表"""
        terms = []
        
        # 在L2块中查找术语对齐表
        l2_blocks = self.extract_between_tags("L2_BEGIN", "L2_END")
        
        for block in l2_blocks:
            # 查找术语表格
            if "术语对齐" in block or "Term Glossary" in block:
                rows = self.parse_table(block)
                for row in rows:
                    if "中文术语" in row and row.get("中文术语"):
                        try:
                            # 解析status
                            status_str = row.get("status", "new_candidate").lower()
                            from .models import FactorStatus
                            status = FactorStatus.NEW_CANDIDATE
                            if status_str == "existing":
                                status = FactorStatus.EXISTING
                            
                            term = TermGlossary(
                                term_zh=row.get("中文术语", ""),
                                term_en=row.get("英文术语", ""),
                                definition_zh=row.get("中文定义", ""),
                                definition_en=row.get("英文定义", ""),
                                factor_id=row.get("factor_id", ""),
                                status=status,
                                source_book=self.book_id,
                            )
                            terms.append(term)
                        except Exception as e:
                            self.errors.append(f"术语解析错误: {row} - {str(e)}")
        
        return terms
    
    def extract_relations(self) -> List[ConfigRelation]:
        """提取因子关系层（全文搜索）"""
        relations = []
        seen_ids = set()
        
        # 关系表格的表头模式
        relation_patterns = [
            r'\|\s*关系ID\s*\|[^\n]+\|\n\|[-:\s|]+\|',
            r'\|\s*Relation ID\s*\|[^\n]+\|\n\|[-:\s|]+\|',
        ]
        
        # 从全文搜索包含关系表的位置
        for line in self.content.split('\n'):
            if '|' in line and ('rel_' in line.lower() or 'relation' in line.lower()):
                # 可能是关系表数据行
                pass
        
        # 查找包含关系表的段落
        sections = re.split(r'\n(?=#+\s*|\*\*)', self.content)
        for section in sections:
            if any(kw in section for kw in ["因子关系层", "Factor Relation", "关系ID", "Relation ID"]):
                rows = self.parse_table(section)
                for row in rows:
                    rel_id = row.get("关系ID", row.get("Relation ID", ""))
                    if rel_id and rel_id not in seen_ids:
                        seen_ids.add(rel_id)
                        try:
                            relation = ConfigRelation(
                                relation_id=rel_id,
                                relation_type=row.get("关系类型", row.get("Relation Type", row.get("relation_type", ""))),
                                factor_a=row.get("因子A", row.get("Factor A", row.get("factor_a", ""))),
                                factor_b=row.get("因子B", row.get("Factor B", row.get("factor_b", ""))),
                                relation_nature=row.get("关系性质", row.get("Relation Nature", row.get("relation_nature", ""))),
                                condition_constraint=row.get("条件约束", row.get("Condition Constraint", row.get("Condition", row.get("condition_constraint", "")))),
                                effect_direction=row.get("效果方向", row.get("Effect Direction", row.get("Effect", row.get("effect_direction", "")))),
                                source_ref=row.get("source_ref", row.get("Source", row.get("Source Ref", ""))),
                                source_book=self.book_id,
                            )
                            relations.append(relation)
                        except Exception as e:
                            self.errors.append(f"关系解析错误: {row} - {str(e)}")
        
        return relations
    
    def extract_evidence_chains(self) -> List[EvidenceChainEntry]:
        """提取推理溯源层"""
        evidence_chains = []
        
        # 查找推理溯源层表格
        sections = re.split(r'\n#+\s*', self.content)
        for section in sections:
            if "推理溯源层" in section or "Evidence Chain" in section:
                rows = self.parse_table(section)
                for row in rows:
                    if row.get("证据ID") and "evi_" in row.get("证据ID", ""):
                        try:
                            # 解析涉及因子列表
                            factors_str = row.get("涉及因子", "")
                            involved_factors = [f.strip() for f in factors_str.split(",") if f.strip()]
                            
                            # 解析可生成规则
                            can_generate = row.get("可生成规则", "").strip()
                            can_generate_rule = can_generate in ["✅", "是", "yes", "true", "1"]
                            
                            evidence = EvidenceChainEntry(
                                evidence_id=row.get("证据ID", ""),
                                original_anchor=row.get("原文锚点", ""),
                                involved_factors=involved_factors,
                                reasoning_steps=row.get("推理步骤", ""),
                                conclusion_direction=row.get("结论方向", ""),
                                confidence=row.get("置信度", "中"),
                                can_generate_rule=can_generate_rule,
                                target_rule_id=row.get("目标规则ID", None),
                                source_book=self.book_id,
                            )
                            evidence_chains.append(evidence)
                        except Exception as e:
                            self.errors.append(f"证据链解析错误: {row} - {str(e)}")
        
        return evidence_chains
    
    def extract_cross_mappings(self) -> List[CrossSystemMapping]:
        """提取跨体系概念映射"""
        mappings = []
        
        # 查找跨体系映射表
        sections = re.split(r'\n#+\s*', self.content)
        for section in sections:
            if "跨体系" in section or "Cross System" in section or "概念映射" in section:
                rows = self.parse_table(section)
                for row in rows:
                    if row.get("概念ID") and "concept_" in row.get("概念ID", ""):
                        try:
                            mapping = CrossSystemMapping(
                                concept_id=row.get("概念ID", ""),
                                common_semantics=row.get("共通语义", ""),
                                bazi_mapping=row.get("八字对应", ""),
                                astro_mapping=row.get("占星对应", ""),
                                dream_mapping=row.get("梦学对应", ""),
                                psychology_mapping=row.get("心理学对应", ""),
                                notes=row.get("备注", ""),
                                source_book=self.book_id,
                            )
                            mappings.append(mapping)
                        except Exception as e:
                            self.errors.append(f"跨体系映射解析错误: {row} - {str(e)}")
        
        return mappings
    
    def extract_all(self) -> ExtractionResult:
        """执行完整提取"""
        result = ExtractionResult(
            source_file=self.source_file,
            book_id=self.book_id,
        )
        
        # 提取各类数据
        result.factors = self.extract_factors()
        result.snippets = self.extract_snippets()
        result.terms = self.extract_terms()
        result.relations = self.extract_relations()
        result.evidence_chains = self.extract_evidence_chains()
        result.cross_mappings = self.extract_cross_mappings()
        
        # 收集错误和警告
        result.errors = self.errors
        result.warnings = self.warnings
        
        return result


def extract_from_file(file_path: Path, book_id: Optional[str] = None) -> ExtractionResult:
    """从文件提取Schema"""
    content = file_path.read_text(encoding='utf-8')
    
    # 推断book_id
    if book_id is None:
        # 从文件路径推断
        # 典籍/中文典籍/滴天髓/编辑/滴天髓_完整规范化_上卷.md -> ditianshui
        path_parts = file_path.parts
        if "中文典籍" in path_parts:
            idx = path_parts.index("中文典籍")
            if idx + 1 < len(path_parts):
                book_id = path_parts[idx + 1].lower().replace(" ", "_")
        elif "texts" in path_parts:
            idx = path_parts.index("texts")
            if idx + 1 < len(path_parts):
                book_id = path_parts[idx + 1].lower().replace(" ", "_")
        else:
            book_id = file_path.stem.lower()
    
    extractor = MarkdownExtractor(content, str(file_path), book_id)
    return extractor.extract_all()


def extract_from_directory(
    directory: Path, 
    exclude_books: Optional[List[str]] = None
) -> Dict[str, List[ExtractionResult]]:
    """从目录批量提取"""
    exclude_books = exclude_books or []
    results: Dict[str, List[ExtractionResult]] = {}
    
    # 遍历所有md文件
    for md_file in directory.rglob("*.md"):
        # 跳过排除的书籍
        skip = False
        for excluded in exclude_books:
            if excluded.lower() in str(md_file).lower():
                skip = True
                break
        if skip:
            continue
        
        # 跳过非精校文件
        if "编辑" not in str(md_file) and "编辑" not in md_file.parts:
            # 对于西方典籍，也检查是否在正确位置
            if "原文" in str(md_file):
                continue
        
        # 提取
        result = extract_from_file(md_file)
        
        if result.book_id not in results:
            results[result.book_id] = []
        results[result.book_id].append(result)
    
    return results
