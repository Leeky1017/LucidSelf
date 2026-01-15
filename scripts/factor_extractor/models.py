"""Factor Extractor Models - 因子提取数据模型"""

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import Dict, List, Optional


class FactorStatus(str, Enum):
    """因子状态枚举"""
    EXISTING = "existing"
    NEW_CANDIDATE = "new_candidate"


class DivinationSystem(str, Enum):
    """术数体系枚举"""
    BAZI = "bazi"
    ZIWEI = "ziwei"
    ASTRO = "astro"
    DREAM = "dream"
    YIJING = "yijing"
    TAROT = "tarot"
    PSYCH = "psych"
    UNKNOWN = "unknown"


@dataclass
class FactorCandidate:
    """因子候选项"""
    # 必填字段
    factor_type: str          # 因子类型
    factor_label: str         # 因子标签（人话）
    factor_source: str        # 因子来源: existing/new_candidate
    
    # 可选字段
    factor_id: Optional[str] = None      # 因子ID（如已存在）
    role_position: Optional[str] = None  # 角色/位置
    value_constraints: Optional[str] = None  # 取值/约束
    engine_id: Optional[str] = None      # engine_id
    notes: Optional[str] = None          # 备注
    
    # 元数据
    source_file: Optional[str] = None    # 来源文件
    line_number: Optional[int] = None    # 行号
    block_index: Optional[int] = None    # 第几个因子块
    
    @property
    def status(self) -> FactorStatus:
        """获取因子状态"""
        source_lower = self.factor_source.lower().strip()
        if source_lower == "existing":
            return FactorStatus.EXISTING
        return FactorStatus.NEW_CANDIDATE
    
    @property
    def is_existing(self) -> bool:
        """是否已入库"""
        return self.status == FactorStatus.EXISTING
    
    @property
    def is_new_candidate(self) -> bool:
        """是否为新候选"""
        return self.status == FactorStatus.NEW_CANDIDATE
    
    def infer_system(self) -> DivinationSystem:
        """推断所属术数体系"""
        # 从engine_id推断
        if self.engine_id:
            eid = self.engine_id.lower()
            if "bazi" in eid:
                return DivinationSystem.BAZI
            if "ziwei" in eid:
                return DivinationSystem.ZIWEI
            if "astro" in eid:
                return DivinationSystem.ASTRO
            if "dream" in eid:
                return DivinationSystem.DREAM
            if "yijing" in eid or "iching" in eid:
                return DivinationSystem.YIJING
            if "tarot" in eid:
                return DivinationSystem.TAROT
            if "psych" in eid or "jung" in eid:
                return DivinationSystem.PSYCH
        
        # 从factor_id推断
        if self.factor_id:
            fid = self.factor_id.lower()
            if fid.startswith("bazi_") or "dizhi" in fid or "tiangan" in fid:
                return DivinationSystem.BAZI
            if fid.startswith("ziwei_"):
                return DivinationSystem.ZIWEI
            if fid.startswith("astro_") or "planet" in fid or "sign" in fid:
                return DivinationSystem.ASTRO
            if fid.startswith("dream_"):
                return DivinationSystem.DREAM
            if fid.startswith("yijing_") or "trigram" in fid or "hexagram" in fid:
                return DivinationSystem.YIJING
            if fid.startswith("tarot_"):
                return DivinationSystem.TAROT
        
        # 从源文件路径推断
        if self.source_file:
            path_lower = self.source_file.lower()
            if "中文典籍" in path_lower:
                # 根据子目录进一步推断
                if "三命通会" in path_lower or "滴天髓" in path_lower or \
                   "渊海子平" in path_lower or "子平真诠" in path_lower or \
                   "穷通宝鉴" in path_lower:
                    return DivinationSystem.BAZI
                if "紫微" in path_lower:
                    return DivinationSystem.ZIWEI
                if "周易" in path_lower:
                    return DivinationSystem.YIJING
                if "解梦" in path_lower or "梦林" in path_lower:
                    return DivinationSystem.DREAM
            elif "texts" in path_lower:
                if "astro" in path_lower or "inner sky" in path_lower or \
                   "tetrabiblos" in path_lower or "planets in transit" in path_lower or \
                   "christian astrology" in path_lower or "astrological" in path_lower:
                    return DivinationSystem.ASTRO
                if "tarot" in path_lower or "thoth" in path_lower or \
                   "78 degrees" in path_lower or "waite" in path_lower:
                    return DivinationSystem.TAROT
                if "dream" in path_lower or "freud" in path_lower or \
                   "jung" in path_lower or "archetype" in path_lower:
                    return DivinationSystem.DREAM
        
        return DivinationSystem.UNKNOWN
    
    def to_dict(self) -> Dict:
        """转换为字典"""
        return {
            "factor_type": self.factor_type,
            "factor_label": self.factor_label,
            "factor_id": self.factor_id,
            "factor_source": self.factor_source,
            "role_position": self.role_position,
            "value_constraints": self.value_constraints,
            "engine_id": self.engine_id,
            "notes": self.notes,
            "source_file": self.source_file,
            "line_number": self.line_number,
            "block_index": self.block_index,
            "inferred_system": self.infer_system().value,
        }


@dataclass
class ExtractionResult:
    """单个文件的提取结果"""
    file_path: str
    factors: List[FactorCandidate] = field(default_factory=list)
    block_count: int = 0
    existing_count: int = 0
    new_candidate_count: int = 0
    parse_errors: List[str] = field(default_factory=list)
    
    def add_factor(self, factor: FactorCandidate):
        """添加因子"""
        self.factors.append(factor)
        if factor.is_existing:
            self.existing_count += 1
        else:
            self.new_candidate_count += 1
    
    @property
    def total_count(self) -> int:
        """总因子数"""
        return len(self.factors)
    
    @property
    def success(self) -> bool:
        """是否成功"""
        return len(self.parse_errors) == 0


@dataclass
class FactorExtractionReport:
    """因子提取报告"""
    # 统计数据
    total_files: int = 0
    processed_files: int = 0
    failed_files: int = 0
    total_blocks: int = 0
    total_factors: int = 0
    existing_factors: int = 0
    new_candidate_factors: int = 0
    
    # 按体系分类
    factors_by_system: Dict[str, int] = field(default_factory=dict)
    
    # 高频new_candidate类型
    new_candidate_by_type: Dict[str, int] = field(default_factory=dict)
    
    # 结果详情
    results: List[ExtractionResult] = field(default_factory=list)
    errors: List[str] = field(default_factory=list)
    
    # 元信息
    extraction_time: Optional[str] = None
    root_directory: Optional[str] = None
    
    def add_result(self, result: ExtractionResult):
        """添加提取结果"""
        self.results.append(result)
        self.processed_files += 1
        self.total_blocks += result.block_count
        self.total_factors += result.total_count
        self.existing_factors += result.existing_count
        self.new_candidate_factors += result.new_candidate_count
        
        if not result.success:
            self.failed_files += 1
            self.errors.extend(result.parse_errors)
        
        # 按体系统计
        for factor in result.factors:
            system = factor.infer_system().value
            self.factors_by_system[system] = self.factors_by_system.get(system, 0) + 1
            
            # 统计new_candidate类型
            if factor.is_new_candidate:
                ftype = factor.factor_type or "unknown"
                self.new_candidate_by_type[ftype] = self.new_candidate_by_type.get(ftype, 0) + 1
    
    def to_dict(self) -> Dict:
        """转换为字典"""
        return {
            "extraction_time": self.extraction_time or datetime.now().isoformat(),
            "root_directory": self.root_directory,
            "summary": {
                "total_files": self.total_files,
                "processed_files": self.processed_files,
                "failed_files": self.failed_files,
                "total_blocks": self.total_blocks,
                "total_factors": self.total_factors,
                "existing_factors": self.existing_factors,
                "new_candidate_factors": self.new_candidate_factors,
            },
            "by_system": self.factors_by_system,
            "new_candidate_by_type": dict(sorted(
                self.new_candidate_by_type.items(),
                key=lambda x: x[1],
                reverse=True
            )),
            "errors": self.errors[:50],  # 只保留前50个错误
        }
