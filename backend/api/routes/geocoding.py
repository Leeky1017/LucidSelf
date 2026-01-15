"""
Geocoding Route

地理编码 API 端点，提供城市搜索和经纬度解析。
"""

import logging
from typing import Optional, List

from fastapi import APIRouter, HTTPException, Query, status
from pydantic import BaseModel, Field

from backend.core.geocoding.service import GeocodingService
from backend.core.geocoding.models import ResolvePlaceInput, Place
from backend.core.geocoding.exceptions import NotFoundError, InvalidInputError

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/geocoding", tags=["Geocoding"])

# 服务单例
_geocoding_service: Optional[GeocodingService] = None


def get_geocoding_service() -> GeocodingService:
    """获取 GeocodingService 单例"""
    global _geocoding_service
    if _geocoding_service is None:
        _geocoding_service = GeocodingService()
    return _geocoding_service


# ==================== 请求/响应模型 ====================

class PlaceResponse(BaseModel):
    """地点响应"""
    place_id: str = Field(..., description="地点唯一标识")
    country_code: str = Field(..., description="ISO 3166-1 alpha-2 国家代码")
    city_name: str = Field(..., description="城市名称")
    lat: float = Field(..., description="纬度")
    lng: float = Field(..., description="经度")
    timezone: str = Field(..., description="IANA 时区标识")
    source: str = Field(..., description="数据来源")
    admin1_name: Optional[str] = Field(None, description="一级行政区名称")
    display_name: str = Field(..., description="显示用完整地址")


class SearchPlacesResponse(BaseModel):
    """搜索地点响应"""
    results: List[PlaceResponse]
    total: int


class ResolvePlaceRequest(BaseModel):
    """解析地点请求"""
    input_text: str = Field(..., min_length=1, description="地点输入文本")
    hint_country: Optional[str] = Field(None, description="国家提示")
    user_id: Optional[str] = Field(None, description="用户ID")
    hint_label: Optional[str] = Field(None, description="语义标签，如 birth_place")


# ==================== API 端点 ====================

@router.post("/resolve", response_model=PlaceResponse)
async def resolve_place(request: ResolvePlaceRequest):
    """
    解析地点文本获取详细地理信息
    
    根据输入的地点文本（支持中英文），返回经纬度、时区等信息。
    解析顺序：用户缓存 → 系统缓存 → 离线数据库 → Amap → Nominatim
    """
    service = get_geocoding_service()
    
    try:
        input_data = ResolvePlaceInput(
            input_text=request.input_text,
            hint_country=request.hint_country,
            user_id=request.user_id,
            hint_label=request.hint_label,
        )
        
        place = await service.resolve_place(input_data)
        
        # 构建显示名称
        display_parts = [place.city_name]
        if place.admin1_name:
            display_parts.insert(0, place.admin1_name)
        display_parts.insert(0, place.country_code)
        display_name = " · ".join(display_parts)
        
        return PlaceResponse(
            place_id=place.place_id,
            country_code=place.country_code,
            city_name=place.city_name,
            lat=place.lat,
            lng=place.lng,
            timezone=place.timezone,
            source=place.source,
            admin1_name=place.admin1_name,
            display_name=display_name,
        )
        
    except InvalidInputError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except NotFoundError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )
    except Exception as e:
        logger.exception(f"Geocoding error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="地理编码服务内部错误"
        )


@router.get("/search", response_model=SearchPlacesResponse)
async def search_places(
    q: str = Query(..., min_length=1, description="搜索关键词"),
    country: Optional[str] = Query(None, description="限定国家代码"),
    limit: int = Query(10, ge=1, le=50, description="返回数量限制"),
):
    """
    搜索地点
    
    根据关键词搜索匹配的城市列表。
    """
    service = get_geocoding_service()
    
    try:
        # 使用 resolve_place 进行搜索
        # 注: 当前实现返回单个最佳匹配，未来可扩展为返回多个候选
        input_data = ResolvePlaceInput(
            input_text=q,
            hint_country=country,
        )
        
        place = await service.resolve_place(input_data)
        
        # 构建显示名称
        display_parts = [place.city_name]
        if place.admin1_name:
            display_parts.insert(0, place.admin1_name)
        display_parts.insert(0, place.country_code)
        display_name = " · ".join(display_parts)
        
        result = PlaceResponse(
            place_id=place.place_id,
            country_code=place.country_code,
            city_name=place.city_name,
            lat=place.lat,
            lng=place.lng,
            timezone=place.timezone,
            source=place.source,
            admin1_name=place.admin1_name,
            display_name=display_name,
        )
        
        return SearchPlacesResponse(results=[result], total=1)
        
    except (InvalidInputError, NotFoundError):
        return SearchPlacesResponse(results=[], total=0)
    except Exception as e:
        logger.exception(f"Search error: {e}")
        return SearchPlacesResponse(results=[], total=0)


# ==================== 常用城市数据 ====================

# 中国常用城市（用于离线快速选择）
CHINA_COMMON_CITIES = [
    {"name": "北京", "province": "北京市", "lat": 39.9042, "lng": 116.4074, "timezone": "Asia/Shanghai"},
    {"name": "上海", "province": "上海市", "lat": 31.2304, "lng": 121.4737, "timezone": "Asia/Shanghai"},
    {"name": "广州", "province": "广东省", "lat": 23.1291, "lng": 113.2644, "timezone": "Asia/Shanghai"},
    {"name": "深圳", "province": "广东省", "lat": 22.5431, "lng": 114.0579, "timezone": "Asia/Shanghai"},
    {"name": "杭州", "province": "浙江省", "lat": 30.2741, "lng": 120.1551, "timezone": "Asia/Shanghai"},
    {"name": "南京", "province": "江苏省", "lat": 32.0603, "lng": 118.7969, "timezone": "Asia/Shanghai"},
    {"name": "成都", "province": "四川省", "lat": 30.5728, "lng": 104.0668, "timezone": "Asia/Shanghai"},
    {"name": "武汉", "province": "湖北省", "lat": 30.5928, "lng": 114.3055, "timezone": "Asia/Shanghai"},
    {"name": "西安", "province": "陕西省", "lat": 34.3416, "lng": 108.9398, "timezone": "Asia/Shanghai"},
    {"name": "重庆", "province": "重庆市", "lat": 29.4316, "lng": 106.9123, "timezone": "Asia/Shanghai"},
    {"name": "天津", "province": "天津市", "lat": 39.0842, "lng": 117.2009, "timezone": "Asia/Shanghai"},
    {"name": "苏州", "province": "江苏省", "lat": 31.2989, "lng": 120.5853, "timezone": "Asia/Shanghai"},
    {"name": "长沙", "province": "湖南省", "lat": 28.2282, "lng": 112.9388, "timezone": "Asia/Shanghai"},
    {"name": "青岛", "province": "山东省", "lat": 36.0671, "lng": 120.3826, "timezone": "Asia/Shanghai"},
    {"name": "大连", "province": "辽宁省", "lat": 38.9140, "lng": 121.6147, "timezone": "Asia/Shanghai"},
    {"name": "厦门", "province": "福建省", "lat": 24.4798, "lng": 118.0894, "timezone": "Asia/Shanghai"},
    {"name": "哈尔滨", "province": "黑龙江省", "lat": 45.8038, "lng": 126.5340, "timezone": "Asia/Shanghai"},
    {"name": "沈阳", "province": "辽宁省", "lat": 41.8057, "lng": 123.4315, "timezone": "Asia/Shanghai"},
    {"name": "济南", "province": "山东省", "lat": 36.6512, "lng": 117.1201, "timezone": "Asia/Shanghai"},
    {"name": "郑州", "province": "河南省", "lat": 34.7466, "lng": 113.6254, "timezone": "Asia/Shanghai"},
    {"name": "昆明", "province": "云南省", "lat": 25.0389, "lng": 102.7183, "timezone": "Asia/Shanghai"},
    {"name": "长春", "province": "吉林省", "lat": 43.8171, "lng": 125.3235, "timezone": "Asia/Shanghai"},
    {"name": "福州", "province": "福建省", "lat": 26.0745, "lng": 119.2965, "timezone": "Asia/Shanghai"},
    {"name": "合肥", "province": "安徽省", "lat": 31.8206, "lng": 117.2272, "timezone": "Asia/Shanghai"},
    {"name": "太原", "province": "山西省", "lat": 37.8706, "lng": 112.5489, "timezone": "Asia/Shanghai"},
    {"name": "南昌", "province": "江西省", "lat": 28.6820, "lng": 115.8579, "timezone": "Asia/Shanghai"},
    {"name": "石家庄", "province": "河北省", "lat": 38.0428, "lng": 114.5149, "timezone": "Asia/Shanghai"},
    {"name": "贵阳", "province": "贵州省", "lat": 26.6470, "lng": 106.6302, "timezone": "Asia/Shanghai"},
    {"name": "南宁", "province": "广西壮族自治区", "lat": 22.8170, "lng": 108.3665, "timezone": "Asia/Shanghai"},
    {"name": "兰州", "province": "甘肃省", "lat": 36.0611, "lng": 103.8343, "timezone": "Asia/Shanghai"},
    {"name": "海口", "province": "海南省", "lat": 20.0440, "lng": 110.1999, "timezone": "Asia/Shanghai"},
    {"name": "呼和浩特", "province": "内蒙古自治区", "lat": 40.8427, "lng": 111.7500, "timezone": "Asia/Shanghai"},
    {"name": "包头", "province": "内蒙古自治区", "lat": 40.6571, "lng": 109.8401, "timezone": "Asia/Shanghai"},
    {"name": "银川", "province": "宁夏回族自治区", "lat": 38.4872, "lng": 106.2309, "timezone": "Asia/Shanghai"},
    {"name": "西宁", "province": "青海省", "lat": 36.6171, "lng": 101.7782, "timezone": "Asia/Shanghai"},
    {"name": "乌鲁木齐", "province": "新疆维吾尔自治区", "lat": 43.8256, "lng": 87.6168, "timezone": "Asia/Urumqi"},
    {"name": "拉萨", "province": "西藏自治区", "lat": 29.6500, "lng": 91.1000, "timezone": "Asia/Shanghai"},
    {"name": "香港", "province": "香港特别行政区", "lat": 22.3193, "lng": 114.1694, "timezone": "Asia/Hong_Kong"},
    {"name": "澳门", "province": "澳门特别行政区", "lat": 22.1987, "lng": 113.5439, "timezone": "Asia/Macau"},
    {"name": "台北", "province": "台湾省", "lat": 25.0330, "lng": 121.5654, "timezone": "Asia/Taipei"},
]


class CommonCityResponse(BaseModel):
    """常用城市响应"""
    name: str
    province: str
    lat: float
    lng: float
    timezone: str
    display_name: str


@router.get("/common-cities/china", response_model=List[CommonCityResponse])
async def get_china_common_cities():
    """
    获取中国常用城市列表
    
    返回预定义的中国常用城市列表，包含经纬度和时区信息。
    用于前端快速选择，无需网络请求。
    """
    return [
        CommonCityResponse(
            name=city["name"],
            province=city["province"],
            lat=city["lat"],
            lng=city["lng"],
            timezone=city["timezone"],
            display_name=f"中国 · {city['province']} · {city['name']}",
        )
        for city in CHINA_COMMON_CITIES
    ]


# ==================== 省份-城市级联选择数据 ====================

# 中国省份列表（按分类排序）
CHINA_PROVINCES = [
    # 直辖市
    "北京市", "天津市", "上海市", "重庆市",
    # 省份
    "河北省", "山西省", "辽宁省", "吉林省", "黑龙江省",
    "江苏省", "浙江省", "安徽省", "福建省", "江西省",
    "山东省", "河南省", "湖北省", "湖南省", "广东省",
    "海南省", "四川省", "贵州省", "云南省", "陕西省",
    "甘肃省", "青海省", "台湾省",
    # 自治区
    "内蒙古自治区", "广西壮族自治区", "西藏自治区",
    "宁夏回族自治区", "新疆维吾尔自治区",
    # 特别行政区
    "香港特别行政区", "澳门特别行政区",
]


class ProvinceCitiesResponse(BaseModel):
    """省份下城市列表响应"""
    province: str
    cities: List[CommonCityResponse]


class ProvinceListResponse(BaseModel):
    """省份列表响应"""
    provinces: List[str]


@router.get("/provinces/china", response_model=ProvinceListResponse)
async def get_china_provinces():
    """
    获取中国省份列表
    
    用于级联选择器第一级
    """
    return ProvinceListResponse(provinces=CHINA_PROVINCES)


@router.get("/provinces/china/{province}/cities", response_model=ProvinceCitiesResponse)
async def get_cities_by_province(province: str):
    """
    获取指定省份下的城市列表
    
    用于级联选择器第二级。
    如果省份在常用城市列表中没有匹配，返回空列表。
    """
    cities = [
        CommonCityResponse(
            name=city["name"],
            province=city["province"],
            lat=city["lat"],
            lng=city["lng"],
            timezone=city["timezone"],
            display_name=f"中国 · {city['province']} · {city['name']}",
        )
        for city in CHINA_COMMON_CITIES
        if city["province"] == province
    ]
    
    return ProvinceCitiesResponse(province=province, cities=cities)
