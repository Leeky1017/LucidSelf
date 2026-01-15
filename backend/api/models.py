"""
API Models

API 请求/响应模型。

对照 design.md 2.5:
- AnalyzeRequest/Response
- InterpretRequest/Response
"""

from datetime import datetime
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


# ==================== 请求模型 ====================

class BirthData(BaseModel):
    """出生数据"""
    year: int = Field(..., ge=1900, le=2100, description="出生年份")
    month: int = Field(..., ge=1, le=12, description="出生月份")
    day: int = Field(..., ge=1, le=31, description="出生日期")
    hour: int = Field(..., ge=0, le=23, description="出生时辰")
    minute: int = Field(default=0, ge=0, le=59, description="出生分钟")
    timezone: str = Field(default="Asia/Shanghai", description="时区")
    gender: str = Field(default="male", description="性别 (male/female)")
    location: Optional[str] = Field(default=None, description="出生地点")
    latitude: Optional[float] = Field(default=None, ge=-90, le=90, description="纬度")
    longitude: Optional[float] = Field(default=None, ge=-180, le=180, description="经度")


class TarotSpread(BaseModel):
    """塔罗牌阵"""
    cards: List[str] = Field(..., min_length=1, max_length=10, description="抽到的牌")
    positions: Optional[List[str]] = Field(default=None, description="牌位")
    spread_type: str = Field(default="single", description="牌阵类型")


class AnalyzeRequest(BaseModel):
    """分析请求"""
    user_id: str = Field(..., min_length=1, description="用户 ID")
    birth_data: Optional[BirthData] = Field(default=None, description="出生数据")
    dream_text: Optional[str] = Field(default=None, max_length=5000, description="梦境文本")
    tarot_spread: Optional[TarotSpread] = Field(default=None, description="塔罗牌阵")
    question: Optional[str] = Field(default=None, max_length=500, description="用户问题")
    engines: Optional[List[str]] = Field(default=None, description="指定使用的引擎")
    include_narrative: bool = Field(default=True, description="是否生成叙事")
    language: str = Field(default="zh", description="语言 (zh/en)")


class InterpretRequest(BaseModel):
    """解读请求"""
    user_id: str = Field(..., min_length=1, description="用户 ID")
    fusion_id: Optional[str] = Field(default=None, description="融合结果 ID")
    request_id: Optional[str] = Field(default=None, description="分析请求 ID")
    question: Optional[str] = Field(default=None, max_length=500, description="追问")
    language: str = Field(default="zh", description="语言")


# ==================== 响应模型 ====================

class AnalyzeResponse(BaseModel):
    """分析响应"""
    request_id: str = Field(..., description="请求 ID")
    fusion_id: str = Field(..., description="融合结果 ID")
    primary_themes: List[str] = Field(..., description="主要主题")
    cross_validation_score: float = Field(..., description="交叉验证分数")
    contributing_engines: List[str] = Field(..., description="参与引擎")
    narrative: Optional[str] = Field(default=None, description="叙事解读")
    processing_time_ms: float = Field(..., description="处理时间 (毫秒)")
    disclaimer: Optional[str] = Field(default=None, description="免责声明")


class InterpretResponse(BaseModel):
    """解读响应"""
    request_id: str = Field(..., description="请求 ID")
    fusion_id: str = Field(..., description="融合结果 ID")
    narrative: str = Field(..., description="叙事解读")
    processing_time_ms: float = Field(..., description="处理时间")
    disclaimer: Optional[str] = Field(default=None, description="免责声明")


class HealthResponse(BaseModel):
    """健康检查响应"""
    status: str = Field(..., description="服务状态")
    timestamp: datetime = Field(default_factory=datetime.utcnow, description="时间戳")
    version: str = Field(..., description="版本号")
    version_id: Optional[str] = Field(default=None, description="不可变版本标识 (ver_*)")
    corpus_release_id: Optional[str] = Field(default=None, description="语料发布版本标识 (cr_*)")


class VersionResponse(BaseModel):
    """版本信息响应"""
    version: str = Field(..., description="版本号")
    build: Optional[str] = Field(default=None, description="构建号")
    api_version: str = Field(default="v1", description="API 版本")
    version_id: Optional[str] = Field(default=None, description="不可变版本标识 (ver_*)")
    corpus_release_id: Optional[str] = Field(default=None, description="语料发布版本标识 (cr_*)")


class ErrorResponse(BaseModel):
    """错误响应"""
    error: str = Field(..., description="错误类型")
    message: str = Field(..., description="错误消息")
    request_id: Optional[str] = Field(default=None, description="请求 ID")
    details: Optional[Dict[str, Any]] = Field(default=None, description="详细信息")
