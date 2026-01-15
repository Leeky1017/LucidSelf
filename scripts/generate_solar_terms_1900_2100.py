#!/usr/bin/env python3
"""
Generate complete solar terms data for 1900-2100 using sxtwl library.

This script generates a JSON file containing 24 solar terms for each year
from 1900 to 2100, formatted as ISO 8601 timestamps in Beijing time (UTC+08:00).
"""
from __future__ import annotations
import json
from pathlib import Path
from datetime import datetime, timezone, timedelta
import sxtwl

# Solar terms in order (starting from Lichun)
SOLAR_TERMS = [
    "Lichun",      # 立春
    "Yushui",      # 雨水
    "Jingzhe",     # 惊蛰
    "Chunfen",     # 春分
    "Qingming",    # 清明
    "Guyu",        # 谷雨
    "Lixia",       # 立夏
    "Xiaoman",     # 小满
    "Mangzhong",   # 芒种
    "Xiazhi",      # 夏至
    "Xiaoshu",     # 小暑
    "Dashu",       # 大暑
    "Liqiu",       # 立秋
    "Chushu",      # 处暑
    "Bailu",       # 白露
    "Qiufen",      # 秋分
    "Hanlu",       # 寒露
    "Shuangjiang", # 霜降
    "Lidong",      # 立冬
    "Xiaoxue",     # 小雪
    "Daxue",       # 大雪
    "Dongzhi",     # 冬至
    "Xiaohan",     # 小寒
    "Dahan",       # 大寒
]

# Beijing timezone offset
BEIJING_TZ = timezone(timedelta(hours=8))


def jqindex_to_name(jq_idx: int) -> str:
    """Map sxtwl jqIndex (0-23) to solar term name."""
    # sxtwl jqIndex mapping:
    # 0=小寒, 1=大寒, 2=立春, 3=雨水, 4=惊蛰, 5=春分,
    # 6=清明, 7=谷雨, 8=立夏, 9=小满, 10=芒种, 11=夏至,
    # 12=小暑, 13=大暑, 14=立秋, 15=处暑, 16=白露, 17=秋分,
    # 18=寒露, 19=霜降, 20=立冬, 21=小雪, 22=大雪, 23=冬至
    mapping = {
        0: "Xiaohan", 1: "Dahan", 2: "Lichun", 3: "Yushui",
        4: "Jingzhe", 5: "Chunfen", 6: "Qingming", 7: "Guyu",
        8: "Lixia", 9: "Xiaoman", 10: "Mangzhong", 11: "Xiazhi",
        12: "Xiaoshu", 13: "Dashu", 14: "Liqiu", 15: "Chushu",
        16: "Bailu", 17: "Qiufen", 18: "Hanlu", 19: "Shuangjiang",
        20: "Lidong", 21: "Xiaoxue", 22: "Daxue", 23: "Dongzhi",
    }
    return mapping[jq_idx]


def generate_solar_terms(start_year: int = 1900, end_year: int = 2100) -> dict[str, dict[str, str]]:
    """
    Generate solar terms data for the specified year range.
    
    Args:
        start_year: Starting year (inclusive)
        end_year: Ending year (inclusive)
    
    Returns:
        Dictionary with year strings as keys, each containing 24 solar terms
        with ISO 8601 timestamp strings in Beijing time.
    """
    result = {}
    
    for year in range(start_year, end_year + 1):
        year_data = {}
        
        # Get solar terms from previous year and current year
        # to ensure we capture all terms within the calendar year
        prev_jieqi = sxtwl.getJieQiByYear(year - 1)
        curr_jieqi = sxtwl.getJieQiByYear(year)
        
        # Combine and filter for terms within the calendar year
        all_terms = []
        for jieqi_info in list(prev_jieqi) + list(curr_jieqi):
            jd = jieqi_info.jd
            day = sxtwl.JD2DD(jd)
            
            # Only include if the date falls within the target year
            if day.Y == year:
                dt = datetime(
                    year=day.Y,
                    month=day.M,
                    day=day.D,
                    hour=int(day.h),
                    minute=int(day.m),
                    second=int(day.s),
                    tzinfo=BEIJING_TZ
                )
                term_name = jqindex_to_name(jieqi_info.jqIndex)
                all_terms.append((term_name, dt.isoformat()))
        
        # Convert to dictionary (should have exactly 24 terms)
        for term_name, iso_str in all_terms:
            year_data[term_name] = iso_str
        
        # Validate we have exactly 24 terms
        if len(year_data) != 24:
            print(f"Warning: Year {year} has {len(year_data)} terms instead of 24")
        
        result[str(year)] = year_data
    
    return result


def main():
    """Generate and write solar terms data to JSON file."""
    print("Generating solar terms data for 1900-2100...")
    
    data = generate_solar_terms(1900, 2100)
    
    # Determine output path
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    output_path = project_root / "data" / "solar_terms" / "solar_terms_1900_2100.json"
    
    # Ensure directory exists
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Write JSON with proper formatting
    with output_path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"✓ Generated {len(data)} years of solar terms data")
    print(f"✓ Output written to: {output_path}")
    
    # Print sample data for verification
    sample_years = ["1900", "1990", "2000", "2100"]
    print("\nSample data (Lichun dates):")
    for year in sample_years:
        if year in data and "Lichun" in data[year]:
            lichun = data[year]["Lichun"]
            print(f"  {year}: {lichun}")
        elif year in data:
            print(f"  {year}: Lichun not found (has {len(data[year])} terms)")


if __name__ == "__main__":
    main()
