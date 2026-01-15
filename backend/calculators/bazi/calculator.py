# backend/calculators/bazi/calculator.py
"""
BaziCalculator - 八字计算器主类.

实现 Layer 1 Calculator 标准接口，提供完整的八字计算功能：
- 四柱排盘
- 藏干提取
- 十神推导
- 五行强度分析
- 大运计算

性能目标: < 10ms/次 (P95)
准确率目标: 四柱 100%, 十神 > 99%
"""

from __future__ import annotations

import time
from datetime import datetime, timedelta
from typing import Dict, List, Literal, Optional
from zoneinfo import ZoneInfo

from backend.calculators.bazi.models import (
    BaziInput,
    BaziFactors,
    Pillar,
    FourPillars,
    Dayun,
    HiddenStem,
    TenGod,
    ElementStrength,
    HEAVENLY_STEMS,
    EARTHLY_BRANCHES,
    STEM_ELEMENT,
    STEM_YINYANG,
    BRANCH_ELEMENT,
    FIVE_ELEMENTS,
)
from backend.calculators.bazi.hidden_stems import extract_hidden_stems
from backend.calculators.bazi.ten_gods import analyze_ten_gods
from backend.calculators.bazi.solar_terms import (
    get_season_from_date,
    get_solar_term_date,
    is_before_lichun,
    SOLAR_TERMS_FOR_MONTH,
)
from backend.calculators.bazi.dayun import (
    get_dayun_direction,
    calculate_start_dayun_age,
    generate_dayun_list,
)


class BaziCalculator:
    """
    八字计算器.
    
    符合架构文档 §4.1 Layer 1 Calculator 标准。
    
    Example:
        >>> from backend.calculators.bazi import BaziCalculator, BaziInput
        >>> 
        >>> calculator = BaziCalculator()
        >>> input_data = BaziInput(
        ...     birth_datetime=datetime(1990, 5, 15, 14, 30),
        ...     birth_location=(116.4, 39.9),
        ...     gender="male"
        ... )
        >>> bazi_factors = calculator.calculate(input_data)
        >>> factor_matrix = bazi_factors.to_factor_matrix()
    """
    
    # 日期范围限制
    MIN_YEAR = 1900
    MAX_YEAR = 2100
    
    def __init__(self):
        """初始化计算器."""
        pass
    
    def calculate(self, input_data: BaziInput) -> BaziFactors:
        """
        执行完整的八字计算.
        
        Args:
            input_data: 输入参数
            
        Returns:
            BaziFactors: 八字因子结果
            
        Raises:
            ValueError: 如果输入参数无效
        """
        start_time = time.perf_counter()
        
        # 1. 验证输入
        self._validate_input(input_data)
        
        # 2. 调整真太阳时
        adjusted_datetime = self._adjust_true_solar_time(
            input_data.birth_datetime,
            input_data.birth_location[0],  # 经度
            input_data.timezone  # 时区参数
        )
        
        # 3. 计算四柱
        four_pillars = self._calculate_four_pillars(adjusted_datetime)
        
        # 4. 提取藏干
        self._extract_all_hidden_stems(four_pillars)
        
        # 5. 分析十神
        ten_gods, ten_god_counts = analyze_ten_gods(four_pillars)
        
        # 6. 计算五行强度
        element_scores = self._calculate_element_strength(four_pillars)
        
        # 7. 判断日主强度
        day_master_strength, strength_category = self._calculate_day_master_strength(
            four_pillars.day.stem,
            element_scores,
            get_season_from_date(adjusted_datetime)
        )
        
        # 8. 计算大运
        dayun_direction = get_dayun_direction(
            four_pillars.year.stem,
            input_data.gender
        )
        start_age, start_months = calculate_start_dayun_age(
            adjusted_datetime,
            dayun_direction
        )
        dayun_list = generate_dayun_list(
            four_pillars.month,
            dayun_direction,
            start_age,
            count=12  # 覆盖120岁
        )
        
        # 9. 组装结果
        calculation_time = (time.perf_counter() - start_time) * 1000
        
        result = BaziFactors(
            four_pillars={
                "year": {"stem": four_pillars.year.stem, "branch": four_pillars.year.branch},
                "month": {"stem": four_pillars.month.stem, "branch": four_pillars.month.branch},
                "day": {"stem": four_pillars.day.stem, "branch": four_pillars.day.branch},
                "hour": {"stem": four_pillars.hour.stem, "branch": four_pillars.hour.branch},
            },
            day_master=four_pillars.day.stem,
            day_master_element=STEM_ELEMENT[four_pillars.day.stem],
            day_master_yinyang=STEM_YINYANG[four_pillars.day.stem],
            hidden_stems={
                "year": [{"stem": hs.stem, "weight": hs.weight, "role": hs.role} 
                         for hs in four_pillars.year.hidden_stems],
                "month": [{"stem": hs.stem, "weight": hs.weight, "role": hs.role} 
                          for hs in four_pillars.month.hidden_stems],
                "day": [{"stem": hs.stem, "weight": hs.weight, "role": hs.role} 
                        for hs in four_pillars.day.hidden_stems],
                "hour": [{"stem": hs.stem, "weight": hs.weight, "role": hs.role} 
                         for hs in four_pillars.hour.hidden_stems],
            },
            ten_gods=[
                {"name": tg.name, "stem": tg.stem, "pillar": tg.pillar, "is_hidden": tg.is_hidden}
                for tg in ten_gods
            ],
            ten_god_counts=ten_god_counts,
            element_scores=element_scores,
            day_master_strength=day_master_strength,
            strength_category=strength_category,
            birth_season=get_season_from_date(adjusted_datetime),
            dayun_list=[
                {"stem": d.stem, "branch": d.branch, "start_age": d.start_age, "end_age": d.end_age}
                for d in dayun_list
            ],
            dayun_direction=dayun_direction,
            start_dayun_age=start_age,
            start_dayun_months=start_months,
            calculation_time_ms=calculation_time,
        )
        
        return result
    
    def _validate_input(self, input_data: BaziInput) -> None:
        """
        验证输入参数.
        
        注意：此方法要求 birth_location 已解析。如果使用 birth_place，
        应先通过 LocationResolver 解析后再调用 calculate()。
        
        Raises:
            ValueError: 如果参数无效
        """
        # 日期范围验证
        year = input_data.birth_datetime.year
        if year < self.MIN_YEAR or year > self.MAX_YEAR:
            raise ValueError(
                f"Date out of supported range (1900-2100): {year}"
            )
        
        # 位置验证 - birth_location 必须已解析
        if input_data.birth_location is None:
            raise ValueError(
                "birth_location must be resolved before calculation. "
                "Use LocationResolver to resolve birth_place first."
            )
        
        longitude, latitude = input_data.birth_location
        if longitude < -180 or longitude > 180:
            raise ValueError(f"Longitude out of range (-180 to 180): {longitude}")
        if latitude < -90 or latitude > 90:
            raise ValueError(f"Latitude out of range (-90 to 90): {latitude}")
        
        # 性别验证（由 Pydantic Literal 保证，这里再次检查）
        if input_data.gender not in ("male", "female"):
            raise ValueError(f"Invalid gender: {input_data.gender}")
    
    def _adjust_true_solar_time(
        self,
        dt: datetime,
        longitude: float,
        timezone: Optional[str] = None
    ) -> datetime:
        """
        调整为真太阳时.
        
        步骤：
        1. 如果提供了timezone，先转换为北京时间
        2. 再根据经度计算真太阳时
        
        Args:
            dt: 原始日期时间
            longitude: 经度
            timezone: 可选时区标识（如 'America/New_York'）
            
        Returns:
            datetime: 调整后的真太阳时
        """
        # 步骤1：时区转换（如果提供了timezone）
        if timezone:
            # 将本地时间转换为UTC，再转换为北京时间
            local_tz = ZoneInfo(timezone)
            beijing_tz = ZoneInfo("Asia/Shanghai")
            
            # 假设输入的dt是naive datetime，附加本地时区
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=local_tz)
            
            # 转换为北京时间
            dt = dt.astimezone(beijing_tz).replace(tzinfo=None)
        
        # 步骤2：经度真太阳时调整
        # 北京时间基准经度是120度，每度4分钟时差
        offset_minutes = (longitude - 120) * 4
        return dt + timedelta(minutes=offset_minutes)
    
    def _calculate_four_pillars(self, dt: datetime) -> FourPillars:
        """
        计算四柱.
        
        Args:
            dt: 日期时间（真太阳时）
            
        Returns:
            FourPillars: 四柱信息
        """
        year_pillar = self._calculate_year_pillar(dt)
        month_pillar = self._calculate_month_pillar(dt, year_pillar.stem)
        day_pillar = self._calculate_day_pillar(dt)
        hour_pillar = self._calculate_hour_pillar(dt, day_pillar.stem)
        
        return FourPillars(
            year=year_pillar,
            month=month_pillar,
            day=day_pillar,
            hour=hour_pillar,
        )
    
    def _calculate_year_pillar(self, dt: datetime) -> Pillar:
        """
        计算年柱.
        
        注意：年柱以立春为界，立春前属于上一年。
        """
        year = dt.year
        
        # 检查是否在立春之前
        if is_before_lichun(dt):
            year -= 1
        
        # 计算天干地支
        # 公式：甲子年为基准，1984年是甲子年
        # 天干：(year - 4) % 10
        # 地支：(year - 4) % 12
        stem_idx = (year - 4) % 10
        branch_idx = (year - 4) % 12
        
        return Pillar(
            stem=HEAVENLY_STEMS[stem_idx],
            branch=EARTHLY_BRANCHES[branch_idx],
        )
    
    def _calculate_month_pillar(self, dt: datetime, year_stem: str) -> Pillar:
        """
        计算月柱.
        
        月柱以节气为界，需要判断当前所在的节气月份。
        月干由年干决定（五虎遁月）。
        """
        year = dt.year
        
        # 检查是否在立春之前（属于上一年的最后一个月）
        if is_before_lichun(dt):
            year -= 1
        
        # 找到当前所在的月份（基于节气）
        month = self._get_lunar_month_from_solar_terms(dt)
        
        # 月支：寅月(1月)对应地支"寅"
        # 地支索引：寅=2, 卯=3, ..., 丑=1
        branch_idx = (month + 1) % 12  # 1月→寅(2), 2月→卯(3), ...
        branch = EARTHLY_BRANCHES[branch_idx]
        
        # 月干：五虎遁月
        # 甲己年：丙寅月起
        # 乙庚年：戊寅月起
        # 丙辛年：庚寅月起
        # 丁壬年：壬寅月起
        # 戊癸年：甲寅月起
        year_stem_idx = HEAVENLY_STEMS.index(year_stem)
        base_stem_idx = ((year_stem_idx % 5) * 2 + 2) % 10
        stem_idx = (base_stem_idx + month - 1) % 10
        stem = HEAVENLY_STEMS[stem_idx]
        
        return Pillar(stem=stem, branch=branch)
    
    def _get_lunar_month_from_solar_terms(self, dt: datetime) -> int:
        """
        根据节气判断农历月份.
        
        Returns:
            int: 农历月份 (1-12)
        """
        from backend.calculators.bazi.solar_terms import _normalize_datetime_for_compare
        dt_naive = _normalize_datetime_for_compare(dt)
        year = dt_naive.year
        
        # 节气列表：立春(1月), 惊蛰(2月), ..., 小寒(12月)
        term_dates = []
        for term_name in SOLAR_TERMS_FOR_MONTH:
            try:
                # 小寒可能跨年
                if term_name == "小寒":
                    term_date = get_solar_term_date(year + 1, term_name)
                else:
                    term_date = get_solar_term_date(year, term_name)
                term_dates.append((term_name, term_date))
            except:
                pass
        
        # 按日期排序
        term_dates.sort(key=lambda x: x[1])
        
        # 找到当前日期所在的月份
        current_month = 12  # 默认为最后一个月
        for i, (term_name, term_date) in enumerate(term_dates):
            if dt_naive < term_date:
                # 在这个节气之前
                if i > 0:
                    current_month = i
                else:
                    current_month = 12
                break
        else:
            current_month = 12
        
        return current_month
    
    def _calculate_day_pillar(self, dt: datetime) -> Pillar:
        """
        计算日柱.
        
        使用儒略日算法计算日柱干支。
        基准日：2000年1月7日是甲子日（儒略日 2451551）
        """
        year = dt.year
        month = dt.month
        day = dt.day
        
        # 子时(23:00-01:00)跨日处理
        if dt.hour >= 23:
            # 晚上23点后算下一天
            next_day = dt + timedelta(days=1)
            year = next_day.year
            month = next_day.month
            day = next_day.day
        
        # 计算儒略日数
        y, m = year, month
        if m <= 2:
            y -= 1
            m += 12
        
        a = y // 100
        b = 2 - a + a // 4
        jd = int(365.25 * (y + 4716)) + int(30.6001 * (m + 1)) + day + b - 1524
        
        # 甲子日基准：2000年1月7日是甲子日，儒略日为 2451551
        base_jd = 2451551
        
        diff = jd - base_jd
        stem_idx = diff % 10
        branch_idx = diff % 12
        
        return Pillar(
            stem=HEAVENLY_STEMS[stem_idx],
            branch=EARTHLY_BRANCHES[branch_idx],
        )
    
    def _calculate_hour_pillar(self, dt: datetime, day_stem: str) -> Pillar:
        """
        计算时柱.
        
        时支由时辰决定（每两小时一个时辰）。
        时干由日干决定（五鼠遁时）。
        """
        hour = dt.hour
        
        # 时支：子时(23-1), 丑时(1-3), ..., 亥时(21-23)
        # 23点算子时
        if hour == 23:
            branch_idx = 0  # 子
        else:
            branch_idx = (hour + 1) // 2
        
        branch = EARTHLY_BRANCHES[branch_idx]
        
        # 时干：五鼠遁时
        # 甲己日：甲子时起
        # 乙庚日：丙子时起
        # 丙辛日：戊子时起
        # 丁壬日：庚子时起
        # 戊癸日：壬子时起
        day_stem_idx = HEAVENLY_STEMS.index(day_stem)
        base_stem_idx = (day_stem_idx % 5) * 2
        stem_idx = (base_stem_idx + branch_idx) % 10
        stem = HEAVENLY_STEMS[stem_idx]
        
        return Pillar(stem=stem, branch=branch)
    
    def _extract_all_hidden_stems(self, four_pillars: FourPillars) -> None:
        """
        提取所有柱的藏干.
        
        直接修改 FourPillars 对象。
        """
        for pillar in four_pillars.all_pillars():
            pillar.hidden_stems = extract_hidden_stems(pillar.branch)
    
    def _calculate_element_strength(
        self,
        four_pillars: FourPillars
    ) -> Dict[str, float]:
        """
        计算五行强度.
        
        综合天干、地支、藏干的五行力量。
        
        Returns:
            Dict[str, float]: 五行强度 (已归一化到 0.0-1.0)
        """
        scores = {element: 0.0 for element in FIVE_ELEMENTS}
        
        for pillar in four_pillars.all_pillars():
            # 天干贡献
            stem_element = STEM_ELEMENT[pillar.stem]
            scores[stem_element] += 1.0
            
            # 地支贡献（本气）
            branch_element = BRANCH_ELEMENT[pillar.branch]
            scores[branch_element] += 0.8
            
            # 藏干贡献
            for hs in pillar.hidden_stems:
                hs_element = STEM_ELEMENT[hs.stem]
                scores[hs_element] += hs.weight * 0.5
        
        # 归一化到 0.0-1.0
        total = sum(scores.values())
        if total > 0:
            scores = {k: v / total for k, v in scores.items()}
        
        return scores
    
    def _calculate_day_master_strength(
        self,
        day_master: str,
        element_scores: Dict[str, float],
        season: str
    ) -> tuple[float, Literal["strong", "weak", "neutral"]]:
        """
        计算日主强度.
        
        综合考虑：
        1. 日主五行在四柱中的比例
        2. 生我五行（印）的比例
        3. 季节对日主的影响
        
        Returns:
            tuple: (强度数值, 强弱分类)
        """
        dm_element = STEM_ELEMENT[day_master]
        
        # 日主五行得分
        dm_score = element_scores.get(dm_element, 0.0)
        
        # 生我五行（印）得分
        element_cycle = ["wood", "fire", "earth", "metal", "water"]
        dm_idx = element_cycle.index(dm_element)
        generating_element = element_cycle[(dm_idx - 1) % 5]  # 生我的五行
        gen_score = element_scores.get(generating_element, 0.0)
        
        # 季节加成
        season_bonus = 0.0
        season_element_map = {
            "spring": "wood",
            "summer": "fire",
            "autumn": "metal",
            "winter": "water",
        }
        # 四季月加土
        season_element = season_element_map.get(season, "earth")
        if season_element == dm_element:
            season_bonus = 0.15  # 当令加成
        elif season_element == generating_element:
            season_bonus = 0.08  # 印当令加成
        
        # 综合计算
        strength = dm_score * 0.5 + gen_score * 0.3 + season_bonus + 0.2
        strength = min(1.0, max(0.0, strength))
        
        # 分类
        if strength >= 0.6:
            category = "strong"
        elif strength <= 0.4:
            category = "weak"
        else:
            category = "neutral"
        
        return (strength, category)
