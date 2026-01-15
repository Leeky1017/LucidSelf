# backend/calculators/ziwei/calculator.py
"""
ZiweiCalculator - 紫微斗数计算器主类.

实现 Layer 1 Calculator 标准接口，提供完整的紫微斗数计算功能：
- 农历转换
- 十二宫安置
- 星曜安置
- 四化飞星（生年+大限+流年）
- 大限计算

性能目标: < 50ms/次 (P95)
准确率目标: 排盘 > 99%, 四化 100%
"""

from __future__ import annotations

import time
from datetime import datetime
from typing import Dict, List, Literal, Optional, Any

from backend.calculators.ziwei.models import (
    ZiweiInput,
    ZiweiFactors,
    ZiweiChart,
    Palace,
    Star,
    SiHua,
    LunarDate,
    PALACE_NAMES,
    EARTHLY_BRANCHES,
)
from backend.calculators.ziwei.lunar_calendar import (
    solar_to_lunar,
    convert_to_beijing_time,
)
from backend.calculators.ziwei.palace_system import (
    build_twelve_palaces,
    get_body_palace_name,
)
from backend.calculators.ziwei.star_placement import (
    calculate_five_element,
    place_all_stars,
    create_star_objects,
)
from backend.calculators.ziwei.sihua import (
    calculate_natal_sihua,
    calculate_decade_sihua,
    calculate_annual_sihua,
    sihua_to_dict,
    get_annual_stem,
)
from backend.calculators.ziwei.decade import (
    get_decade_direction,
    calculate_start_decade_age,
    generate_decade_list,
    get_current_decade,
    calculate_age,
)


class ZiweiCalculator:
    """
    紫微斗数计算器.
    
    符合架构文档 §4.1 Layer 1 Calculator 标准。
    
    Example:
        >>> from backend.calculators.ziwei import ZiweiCalculator, ZiweiInput
        >>> 
        >>> calculator = ZiweiCalculator()
        >>> input_data = ZiweiInput(
        ...     birth_datetime=datetime(1990, 5, 15, 14, 30),
        ...     birth_location=(116.4, 39.9),
        ...     gender="male"
        ... )
        >>> ziwei_factors = calculator.calculate(input_data)
        >>> factor_matrix = ziwei_factors.to_factor_matrix()
    """
    
    # 日期范围限制
    MIN_YEAR = 1900
    MAX_YEAR = 2100
    
    def __init__(self):
        """初始化计算器."""
        pass
    
    def calculate(
        self,
        input_data: ZiweiInput,
        target_year: Optional[int] = None
    ) -> ZiweiFactors:
        """
        执行完整的紫微斗数计算.
        
        Args:
            input_data: 输入参数
            target_year: 目标流年（可选，默认为当前年）
            
        Returns:
            ZiweiFactors: 紫微斗数因子结果
            
        Raises:
            ValueError: 如果输入参数无效
        """
        start_time = time.perf_counter()
        
        # 1. 验证输入
        self._validate_input(input_data)
        
        # 2. 时区转换
        beijing_dt = convert_to_beijing_time(
            input_data.birth_datetime,
            input_data.timezone
        )
        
        # 3. 公历转农历
        lunar_date = solar_to_lunar(beijing_dt)
        
        # 4. 构建十二宫
        palaces, ming_idx, body_idx = build_twelve_palaces(
            lunar_date,
            lunar_date.year_stem
        )
        
        # 5. 计算五行局
        ming_branch_idx = EARTHLY_BRANCHES.index(palaces[ming_idx].branch)
        five_element_name, five_element_num = calculate_five_element(
            ming_branch_idx,
            lunar_date.year_stem
        )
        
        # 6. 安置星曜
        star_positions, star_brightness = place_all_stars(
            lunar_date,
            five_element_num
        )
        
        # 7. 将星曜分配到宫位
        self._assign_stars_to_palaces(palaces, star_positions)
        
        # 8. 计算生年四化
        natal_sihua = calculate_natal_sihua(lunar_date.year_stem)
        
        # 9. 计算大限
        decade_direction = get_decade_direction(
            lunar_date.year_stem,
            input_data.gender
        )
        
        # 起运岁数 = 五行局数（紫微斗数只认岁级，不做月级修正）
        start_decade_age = calculate_start_decade_age(five_element_num)
        
        decade_list = generate_decade_list(
            palaces,
            ming_idx,
            decade_direction,
            start_decade_age,
            count=12
        )
        
        # 10. 计算当前大限四化
        current_age = calculate_age(input_data.birth_datetime)
        current_decade = get_current_decade(decade_list, current_age)
        sihua_decade = {}
        if current_decade:
            sihua_decade = sihua_to_dict(current_decade.sihua_list)
        
        # 11. 计算流年四化
        if target_year is None:
            target_year = datetime.now().year
        annual_stem = get_annual_stem(target_year)
        annual_sihua = calculate_annual_sihua(annual_stem)
        sihua_annual = sihua_to_dict(annual_sihua)
        
        # 12. 组装结果
        calculation_time = (time.perf_counter() - start_time) * 1000
        
        result = self._build_result(
            lunar_date=lunar_date,
            gender=input_data.gender,
            five_element_name=five_element_name,
            five_element_num=five_element_num,
            palaces=palaces,
            ming_idx=ming_idx,
            body_idx=body_idx,
            star_positions=star_positions,
            star_brightness=star_brightness,
            natal_sihua=natal_sihua,
            sihua_decade=sihua_decade,
            sihua_annual=sihua_annual,
            decade_list=decade_list,
            current_decade=current_decade,
            decade_direction=decade_direction,
            start_decade_age=start_decade_age,
            calculation_time=calculation_time,
        )
        
        return result

    
    def _validate_input(self, input_data: ZiweiInput) -> None:
        """
        验证输入参数.
        
        Raises:
            ValueError: 如果参数无效
        """
        # 日期范围验证
        year = input_data.birth_datetime.year
        if year < self.MIN_YEAR or year > self.MAX_YEAR:
            raise ValueError(
                f"Date out of supported range (1900-2100): {year}"
            )
        
        # 位置验证
        longitude, latitude = input_data.birth_location
        if longitude < -180 or longitude > 180:
            raise ValueError(f"Longitude out of range (-180 to 180): {longitude}")
        if latitude < -90 or latitude > 90:
            raise ValueError(f"Latitude out of range (-90 to 90): {latitude}")
        
        # 性别验证（由 Pydantic Literal 保证，这里再次检查）
        if input_data.gender not in ("male", "female"):
            raise ValueError(f"Invalid gender: {input_data.gender}")
    
    def _assign_stars_to_palaces(
        self,
        palaces: List[Palace],
        star_positions: Dict[str, int]
    ) -> None:
        """
        将星曜分配到宫位.
        
        直接修改 palaces 列表。
        """
        from backend.calculators.ziwei.models import (
            MAIN_STARS,
            AUXILIARY_STARS,
            SHA_STARS,
        )
        
        for star_name, branch_idx in star_positions.items():
            # 找到对应的宫位
            for palace in palaces:
                palace_branch_idx = EARTHLY_BRANCHES.index(palace.branch)
                if palace_branch_idx == branch_idx:
                    if star_name in MAIN_STARS:
                        palace.main_stars.append(star_name)
                    elif star_name in AUXILIARY_STARS:
                        palace.auxiliary_stars.append(star_name)
                    elif star_name in SHA_STARS:
                        palace.sha_stars.append(star_name)
                    break
    
    def _build_result(
        self,
        lunar_date: LunarDate,
        gender: Literal["male", "female"],
        five_element_name: str,
        five_element_num: int,
        palaces: List[Palace],
        ming_idx: int,
        body_idx: int,
        star_positions: Dict[str, int],
        star_brightness: Dict[str, str],
        natal_sihua: List[SiHua],
        sihua_decade: Dict[str, str],
        sihua_annual: Dict[str, str],
        decade_list: List,
        current_decade: Optional[Any],
        decade_direction: Literal["forward", "backward"],
        start_decade_age: int,
        calculation_time: float,
    ) -> ZiweiFactors:
        """构建结果对象."""
        
        # 构建宫位信息字典
        palaces_dict = {}
        for palace in palaces:
            palaces_dict[palace.name] = {
                "branch": palace.branch,
                "stem": palace.stem,
                "main_stars": palace.main_stars,
                "auxiliary_stars": palace.auxiliary_stars,
                "sha_stars": palace.sha_stars,
            }
        
        # 构建主星位置字典
        main_stars_dict = {}
        for star_name, branch_idx in star_positions.items():
            from backend.calculators.ziwei.models import MAIN_STARS
            if star_name in MAIN_STARS:
                # 找到宫位名称
                for palace in palaces:
                    if EARTHLY_BRANCHES.index(palace.branch) == branch_idx:
                        main_stars_dict[star_name] = palace.name
                        break
        
        # 构建辅星位置字典
        auxiliary_stars_dict = {}
        for star_name, branch_idx in star_positions.items():
            from backend.calculators.ziwei.models import AUXILIARY_STARS
            if star_name in AUXILIARY_STARS:
                for palace in palaces:
                    if EARTHLY_BRANCHES.index(palace.branch) == branch_idx:
                        auxiliary_stars_dict[star_name] = palace.name
                        break
        
        # 构建煞星位置字典
        sha_stars_dict = {}
        for star_name, branch_idx in star_positions.items():
            from backend.calculators.ziwei.models import SHA_STARS
            if star_name in SHA_STARS:
                for palace in palaces:
                    if EARTHLY_BRANCHES.index(palace.branch) == branch_idx:
                        sha_stars_dict[star_name] = palace.name
                        break
        
        # 构建大限列表
        decade_list_dict = []
        for decade in decade_list:
            decade_list_dict.append({
                "palace_name": decade.palace_name,
                "stem": decade.stem,
                "branch": decade.branch,
                "start_age": decade.start_age,
                "end_age": decade.end_age,
            })
        
        # 当前大限
        current_decade_dict = None
        if current_decade:
            current_decade_dict = {
                "palace_name": current_decade.palace_name,
                "stem": current_decade.stem,
                "branch": current_decade.branch,
                "start_age": current_decade.start_age,
                "end_age": current_decade.end_age,
            }
        
        return ZiweiFactors(
            lunar_year=lunar_date.year,
            lunar_month=lunar_date.month,
            lunar_day=lunar_date.day,
            is_leap_month=lunar_date.is_leap_month,
            year_stem=lunar_date.year_stem,
            year_branch=lunar_date.year_branch,
            hour_branch=lunar_date.hour_branch,
            gender=gender,
            five_element_type=five_element_name,
            five_element_number=five_element_num,
            palaces=palaces_dict,
            ming_palace_branch=palaces[ming_idx].branch,
            body_palace_name=get_body_palace_name(body_idx),
            main_stars=main_stars_dict,
            auxiliary_stars=auxiliary_stars_dict,
            sha_stars=sha_stars_dict,
            star_brightness=star_brightness,
            sihua_natal=sihua_to_dict(natal_sihua),
            sihua_decade=sihua_decade,
            sihua_annual=sihua_annual,
            decade_list=decade_list_dict,
            current_decade=current_decade_dict,
            decade_direction=decade_direction,
            start_decade_age=start_decade_age,
            calculation_time_ms=calculation_time,
        )
