"""
V2 Data Models - V2版本专用数据模型

定义V2升级所需的新数据模型。
"""

from datetime import datetime
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class DataQualityIssue(BaseModel):
    """数据质量问题"""
    type: str = Field(..., description="问题类型: incomplete_extraction, orphan_relations, coarse_source_ref")
    description: str = Field(..., description="问题描述")
    remediation: str = Field(default="", description="建议的修复措施")


class ValidationReport(BaseModel):
    """源数据校验报告"""
    book_id: str = Field(..., description="书籍ID")
    is_complete: bool = Field(default=True, description="数据是否完整")
    snippet_count: int = Field(default=0, description="snippet数量")
    relation_count: int = Field(default=0, description="relation数量")
    missing_chapters: List[str] = Field(default_factory=list, description="缺失的章节")
    orphan_relations: List[str] = Field(default_factory=list, description="孤儿关系列表")
    issues: List[DataQualityIssue] = Field(default_factory=list, description="质量问题列表")


class QualityReportV2(BaseModel):
    """升级版质量报告 - 包含6个质量维度"""
    connectivity: float = Field(default=0.0, description="连通性 (0-1)")
    orphan_ratio: float = Field(default=0.0, description="孤立节点比例 (越低越好)")
    reasoning_coherence: float = Field(default=0.0, description="推理连贯性 (0-1)")
    condition_coverage: float = Field(default=0.0, description="条件覆盖度 (0-1)")
    argument_completeness: float = Field(default=0.0, description="论证完整性 (0-1)")
    node_homogeneity: float = Field(default=0.0, description="节点同质性 (0-1)")


class ThresholdFailure(BaseModel):
    """阈值失败记录"""
    book_id: str = Field(..., description="书籍ID")
    metric: str = Field(..., description="失败的指标名称")
    actual_value: float = Field(..., description="实际值")
    threshold: float = Field(..., description="阈值")
    remediation: str = Field(default="", description="建议的修复措施")


class BookStatsV2(BaseModel):
    """单本书籍统计 V2版"""
    book_id: str = Field(..., description="书籍ID")
    snippet_count: int = Field(default=0, description="snippet数量")
    node_count: int = Field(default=0, description="节点数")
    edge_count: int = Field(default=0, description="边数")
    coverage: float = Field(default=0.0, description="snippet覆盖率")
    quality_report: Optional[QualityReportV2] = Field(None, description="质量报告")
    edge_inference_breakdown: Dict[str, int] = Field(default_factory=dict, description="边推断方法分布")
    cluster_level_breakdown: Dict[str, int] = Field(default_factory=dict, description="聚类层级分布")
    status: str = Field(default="success", description="处理状态: success, failed, skipped")
    error_message: Optional[str] = Field(None, description="错误消息")
    threshold_failures: List[str] = Field(default_factory=list, description="阈值失败列表")


class BuildReportV2(BaseModel):
    """升级版构建报告"""
    generated_at: datetime = Field(default_factory=datetime.now, description="生成时间")
    total_books: int = Field(default=0, description="总书籍数")
    successful_books: int = Field(default=0, description="成功处理的书籍数")
    failed_books: int = Field(default=0, description="失败的书籍数")
    book_stats: List[BookStatsV2] = Field(default_factory=list, description="各书籍统计")
    edge_inference_breakdown: Dict[str, int] = Field(default_factory=dict, description="边推断方法总分布")
    cluster_level_breakdown: Dict[str, int] = Field(default_factory=dict, description="聚类层级总分布")
    threshold_failures: List[ThresholdFailure] = Field(default_factory=list, description="阈值失败汇总")
    average_quality: Optional[QualityReportV2] = Field(None, description="平均质量指标")


class BookBuildResult(BaseModel):
    """单本书籍构建结果"""
    book_id: str = Field(..., description="书籍ID")
    success: bool = Field(default=True, description="是否成功")
    chain: Optional[Any] = Field(None, description="构建的逻辑链")
    quality_report: Optional[QualityReportV2] = Field(None, description="质量报告")
    validation_report: Optional[ValidationReport] = Field(None, description="校验报告")
    error_message: Optional[str] = Field(None, description="错误消息")
