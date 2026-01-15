#!/usr/bin/env python3
"""
将 cities500.txt 转换为前端静态资产

生成结构：
  frontend/public/data/cities/
    ├── countries.json          # 国家列表
    ├── CN.json                 # 中国所有城市（按admin1分组）
    ├── US.json                 # 美国所有城市
    └── ...                     # 其他国家

每个国家JSON结构：
{
  "country": "CN",
  "admin1s": {
    "01": {
      "name": "Anhui",
      "name_local": "安徽省",
      "cities": [
        {"n": "合肥", "a": "Hefei", "lat": 31.82, "lng": 117.23, "tz": "Asia/Shanghai", "p": 3500000},
        ...
      ]
    }
  }
}
"""

import json
import os
from collections import defaultdict
from pathlib import Path

# GeoNames admin1CodesASCII.txt 中国省份映射（正确映射）
CHINA_ADMIN1_NAMES = {
    "01": ("Anhui", "安徽省"),
    "02": ("Zhejiang", "浙江省"),
    "03": ("Jiangxi", "江西省"),
    "04": ("Jiangsu", "江苏省"),
    "05": ("Jilin", "吉林省"),
    "06": ("Qinghai", "青海省"),
    "07": ("Fujian", "福建省"),
    "08": ("Heilongjiang", "黑龙江省"),
    "09": ("Henan", "河南省"),
    "10": ("Hebei", "河北省"),
    "11": ("Hunan", "湖南省"),
    "12": ("Hubei", "湖北省"),
    "13": ("Xinjiang", "新疆维吾尔自治区"),
    "14": ("Tibet", "西藏自治区"),
    "15": ("Gansu", "甘肃省"),
    "16": ("Guangxi", "广西壮族自治区"),
    "18": ("Guizhou", "贵州省"),
    "19": ("Liaoning", "辽宁省"),
    "20": ("Inner Mongolia", "内蒙古自治区"),
    "21": ("Ningxia", "宁夏回族自治区"),
    "22": ("Beijing", "北京市"),
    "23": ("Shanghai", "上海市"),
    "24": ("Shanxi", "山西省"),
    "25": ("Shandong", "山东省"),
    "26": ("Shaanxi", "陕西省"),
    "28": ("Tianjin", "天津市"),
    "29": ("Yunnan", "云南省"),
    "30": ("Guangdong", "广东省"),
    "31": ("Hainan", "海南省"),
    "32": ("Sichuan", "四川省"),
    "33": ("Chongqing", "重庆市"),
}

# 国家名称映射（常用国家）
COUNTRY_NAMES = {
    "AD": ("Andorra", "安道尔"),
    "AE": ("United Arab Emirates", "阿联酋"),
    "AF": ("Afghanistan", "阿富汗"),
    "AG": ("Antigua and Barbuda", "安提瓜和巴布达"),
    "AL": ("Albania", "阿尔巴尼亚"),
    "AM": ("Armenia", "亚美尼亚"),
    "AO": ("Angola", "安哥拉"),
    "AR": ("Argentina", "阿根廷"),
    "AT": ("Austria", "奥地利"),
    "AU": ("Australia", "澳大利亚"),
    "AZ": ("Azerbaijan", "阿塞拜疆"),
    "BA": ("Bosnia and Herzegovina", "波黑"),
    "BB": ("Barbados", "巴巴多斯"),
    "BD": ("Bangladesh", "孟加拉国"),
    "BE": ("Belgium", "比利时"),
    "BF": ("Burkina Faso", "布基纳法索"),
    "BG": ("Bulgaria", "保加利亚"),
    "BH": ("Bahrain", "巴林"),
    "BI": ("Burundi", "布隆迪"),
    "BJ": ("Benin", "贝宁"),
    "BN": ("Brunei", "文莱"),
    "BO": ("Bolivia", "玻利维亚"),
    "BR": ("Brazil", "巴西"),
    "BS": ("Bahamas", "巴哈马"),
    "BT": ("Bhutan", "不丹"),
    "BW": ("Botswana", "博茨瓦纳"),
    "BY": ("Belarus", "白俄罗斯"),
    "BZ": ("Belize", "伯利兹"),
    "CA": ("Canada", "加拿大"),
    "CD": ("DR Congo", "刚果（金）"),
    "CF": ("Central African Republic", "中非"),
    "CG": ("Congo", "刚果（布）"),
    "CH": ("Switzerland", "瑞士"),
    "CI": ("Ivory Coast", "科特迪瓦"),
    "CL": ("Chile", "智利"),
    "CM": ("Cameroon", "喀麦隆"),
    "CN": ("China", "中国"),
    "CO": ("Colombia", "哥伦比亚"),
    "CR": ("Costa Rica", "哥斯达黎加"),
    "CU": ("Cuba", "古巴"),
    "CV": ("Cape Verde", "佛得角"),
    "CY": ("Cyprus", "塞浦路斯"),
    "CZ": ("Czechia", "捷克"),
    "DE": ("Germany", "德国"),
    "DJ": ("Djibouti", "吉布提"),
    "DK": ("Denmark", "丹麦"),
    "DM": ("Dominica", "多米尼克"),
    "DO": ("Dominican Republic", "多米尼加"),
    "DZ": ("Algeria", "阿尔及利亚"),
    "EC": ("Ecuador", "厄瓜多尔"),
    "EE": ("Estonia", "爱沙尼亚"),
    "EG": ("Egypt", "埃及"),
    "ER": ("Eritrea", "厄立特里亚"),
    "ES": ("Spain", "西班牙"),
    "ET": ("Ethiopia", "埃塞俄比亚"),
    "FI": ("Finland", "芬兰"),
    "FJ": ("Fiji", "斐济"),
    "FR": ("France", "法国"),
    "GA": ("Gabon", "加蓬"),
    "GB": ("United Kingdom", "英国"),
    "GD": ("Grenada", "格林纳达"),
    "GE": ("Georgia", "格鲁吉亚"),
    "GH": ("Ghana", "加纳"),
    "GM": ("Gambia", "冈比亚"),
    "GN": ("Guinea", "几内亚"),
    "GQ": ("Equatorial Guinea", "赤道几内亚"),
    "GR": ("Greece", "希腊"),
    "GT": ("Guatemala", "危地马拉"),
    "GW": ("Guinea-Bissau", "几内亚比绍"),
    "GY": ("Guyana", "圭亚那"),
    "HK": ("Hong Kong", "香港"),
    "HN": ("Honduras", "洪都拉斯"),
    "HR": ("Croatia", "克罗地亚"),
    "HT": ("Haiti", "海地"),
    "HU": ("Hungary", "匈牙利"),
    "ID": ("Indonesia", "印度尼西亚"),
    "IE": ("Ireland", "爱尔兰"),
    "IL": ("Israel", "以色列"),
    "IN": ("India", "印度"),
    "IQ": ("Iraq", "伊拉克"),
    "IR": ("Iran", "伊朗"),
    "IS": ("Iceland", "冰岛"),
    "IT": ("Italy", "意大利"),
    "JM": ("Jamaica", "牙买加"),
    "JO": ("Jordan", "约旦"),
    "JP": ("Japan", "日本"),
    "KE": ("Kenya", "肯尼亚"),
    "KG": ("Kyrgyzstan", "吉尔吉斯斯坦"),
    "KH": ("Cambodia", "柬埔寨"),
    "KI": ("Kiribati", "基里巴斯"),
    "KM": ("Comoros", "科摩罗"),
    "KN": ("Saint Kitts and Nevis", "圣基茨和尼维斯"),
    "KP": ("North Korea", "朝鲜"),
    "KR": ("South Korea", "韩国"),
    "KW": ("Kuwait", "科威特"),
    "KZ": ("Kazakhstan", "哈萨克斯坦"),
    "LA": ("Laos", "老挝"),
    "LB": ("Lebanon", "黎巴嫩"),
    "LC": ("Saint Lucia", "圣卢西亚"),
    "LI": ("Liechtenstein", "列支敦士登"),
    "LK": ("Sri Lanka", "斯里兰卡"),
    "LR": ("Liberia", "利比里亚"),
    "LS": ("Lesotho", "莱索托"),
    "LT": ("Lithuania", "立陶宛"),
    "LU": ("Luxembourg", "卢森堡"),
    "LV": ("Latvia", "拉脱维亚"),
    "LY": ("Libya", "利比亚"),
    "MA": ("Morocco", "摩洛哥"),
    "MC": ("Monaco", "摩纳哥"),
    "MD": ("Moldova", "摩尔多瓦"),
    "ME": ("Montenegro", "黑山"),
    "MG": ("Madagascar", "马达加斯加"),
    "MH": ("Marshall Islands", "马绍尔群岛"),
    "MK": ("North Macedonia", "北马其顿"),
    "ML": ("Mali", "马里"),
    "MM": ("Myanmar", "缅甸"),
    "MN": ("Mongolia", "蒙古"),
    "MO": ("Macau", "澳门"),
    "MR": ("Mauritania", "毛里塔尼亚"),
    "MT": ("Malta", "马耳他"),
    "MU": ("Mauritius", "毛里求斯"),
    "MV": ("Maldives", "马尔代夫"),
    "MW": ("Malawi", "马拉维"),
    "MX": ("Mexico", "墨西哥"),
    "MY": ("Malaysia", "马来西亚"),
    "MZ": ("Mozambique", "莫桑比克"),
    "NA": ("Namibia", "纳米比亚"),
    "NE": ("Niger", "尼日尔"),
    "NG": ("Nigeria", "尼日利亚"),
    "NI": ("Nicaragua", "尼加拉瓜"),
    "NL": ("Netherlands", "荷兰"),
    "NO": ("Norway", "挪威"),
    "NP": ("Nepal", "尼泊尔"),
    "NR": ("Nauru", "瑙鲁"),
    "NZ": ("New Zealand", "新西兰"),
    "OM": ("Oman", "阿曼"),
    "PA": ("Panama", "巴拿马"),
    "PE": ("Peru", "秘鲁"),
    "PG": ("Papua New Guinea", "巴布亚新几内亚"),
    "PH": ("Philippines", "菲律宾"),
    "PK": ("Pakistan", "巴基斯坦"),
    "PL": ("Poland", "波兰"),
    "PS": ("Palestine", "巴勒斯坦"),
    "PT": ("Portugal", "葡萄牙"),
    "PW": ("Palau", "帕劳"),
    "PY": ("Paraguay", "巴拉圭"),
    "QA": ("Qatar", "卡塔尔"),
    "RO": ("Romania", "罗马尼亚"),
    "RS": ("Serbia", "塞尔维亚"),
    "RU": ("Russia", "俄罗斯"),
    "RW": ("Rwanda", "卢旺达"),
    "SA": ("Saudi Arabia", "沙特阿拉伯"),
    "SB": ("Solomon Islands", "所罗门群岛"),
    "SC": ("Seychelles", "塞舌尔"),
    "SD": ("Sudan", "苏丹"),
    "SE": ("Sweden", "瑞典"),
    "SG": ("Singapore", "新加坡"),
    "SI": ("Slovenia", "斯洛文尼亚"),
    "SK": ("Slovakia", "斯洛伐克"),
    "SL": ("Sierra Leone", "塞拉利昂"),
    "SM": ("San Marino", "圣马力诺"),
    "SN": ("Senegal", "塞内加尔"),
    "SO": ("Somalia", "索马里"),
    "SR": ("Suriname", "苏里南"),
    "SS": ("South Sudan", "南苏丹"),
    "ST": ("Sao Tome and Principe", "圣多美和普林西比"),
    "SV": ("El Salvador", "萨尔瓦多"),
    "SY": ("Syria", "叙利亚"),
    "SZ": ("Eswatini", "斯威士兰"),
    "TD": ("Chad", "乍得"),
    "TG": ("Togo", "多哥"),
    "TH": ("Thailand", "泰国"),
    "TJ": ("Tajikistan", "塔吉克斯坦"),
    "TL": ("Timor-Leste", "东帝汶"),
    "TM": ("Turkmenistan", "土库曼斯坦"),
    "TN": ("Tunisia", "突尼斯"),
    "TO": ("Tonga", "汤加"),
    "TR": ("Turkey", "土耳其"),
    "TT": ("Trinidad and Tobago", "特立尼达和多巴哥"),
    "TV": ("Tuvalu", "图瓦卢"),
    "TW": ("Taiwan", "台湾"),
    "TZ": ("Tanzania", "坦桑尼亚"),
    "UA": ("Ukraine", "乌克兰"),
    "UG": ("Uganda", "乌干达"),
    "US": ("United States", "美国"),
    "UY": ("Uruguay", "乌拉圭"),
    "UZ": ("Uzbekistan", "乌兹别克斯坦"),
    "VA": ("Vatican City", "梵蒂冈"),
    "VC": ("Saint Vincent and the Grenadines", "圣文森特和格林纳丁斯"),
    "VE": ("Venezuela", "委内瑞拉"),
    "VN": ("Vietnam", "越南"),
    "VU": ("Vanuatu", "瓦努阿图"),
    "WS": ("Samoa", "萨摩亚"),
    "XK": ("Kosovo", "科索沃"),
    "YE": ("Yemen", "也门"),
    "ZA": ("South Africa", "南非"),
    "ZM": ("Zambia", "赞比亚"),
    "ZW": ("Zimbabwe", "津巴布韦"),
}


def parse_cities500(filepath: str):
    """解析 cities500.txt"""
    # 按国家分组
    countries = defaultdict(lambda: defaultdict(list))
    country_stats = defaultdict(int)
    
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split('\t')
            if len(parts) < 19:
                continue
            
            geonameid = parts[0]
            name = parts[1]
            asciiname = parts[2]
            alternatenames = parts[3]
            lat = float(parts[4])
            lng = float(parts[5])
            feature_class = parts[6]
            feature_code = parts[7]
            country_code = parts[8]
            admin1_code = parts[10] if len(parts) > 10 else ""
            population = int(parts[14]) if parts[14] else 0
            timezone = parts[17] if len(parts) > 17 else ""
            
            # 只要 P 类（人口聚集地）
            if feature_class != 'P':
                continue
            
            # 提取本地名称（从alternatenames中查找中文等）
            local_name = name
            if alternatenames:
                alt_list = alternatenames.split(',')
                # 对于中国，优先找中文名
                if country_code == 'CN':
                    for alt in alt_list:
                        if alt and '\u4e00' <= alt[0] <= '\u9fff':
                            local_name = alt
                            break
            
            city = {
                "id": geonameid,
                "n": local_name,  # 本地名称
                "a": asciiname,   # ASCII名称
                "lat": round(lat, 4),
                "lng": round(lng, 4),
                "tz": timezone,
                "p": population,
            }
            
            countries[country_code][admin1_code].append(city)
            country_stats[country_code] += 1
    
    return countries, country_stats


def build_country_json(country_code: str, admin1_data: dict, output_dir: Path):
    """为单个国家生成 JSON 文件"""
    
    # 获取国家名称
    name_en, name_zh = COUNTRY_NAMES.get(country_code, (country_code, country_code))
    
    # 构建 admin1 结构
    admin1s = {}
    for admin1_code, cities in admin1_data.items():
        # 按人口排序
        cities.sort(key=lambda x: x['p'], reverse=True)
        
        # 获取 admin1 名称（目前只有中国有完整映射）
        if country_code == 'CN' and admin1_code in CHINA_ADMIN1_NAMES:
            a1_name, a1_local = CHINA_ADMIN1_NAMES[admin1_code]
        else:
            a1_name = admin1_code
            a1_local = admin1_code
        
        admin1s[admin1_code] = {
            "name": a1_name,
            "name_local": a1_local,
            "cities": cities[:500]  # 每个admin1最多500个城市
        }
    
    data = {
        "country": country_code,
        "name": name_en,
        "name_zh": name_zh,
        "admin1s": admin1s,
    }
    
    output_file = output_dir / f"{country_code}.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, separators=(',', ':'))
    
    return len(admin1s), sum(len(a['cities']) for a in admin1s.values())


def build_countries_index(country_stats: dict, output_dir: Path):
    """生成国家索引文件"""
    countries = []
    
    for code in sorted(country_stats.keys()):
        name_en, name_zh = COUNTRY_NAMES.get(code, (code, code))
        countries.append({
            "code": code,
            "name": name_en,
            "name_zh": name_zh,
            "cities": country_stats[code],
        })
    
    # 按城市数量排序（常用国家排前面）
    countries.sort(key=lambda x: x['cities'], reverse=True)
    
    output_file = output_dir / "countries.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(countries, f, ensure_ascii=False, indent=2)
    
    return len(countries)


def main():
    # 路径配置
    project_root = Path(__file__).parent.parent
    cities_file = project_root / "data" / "cities500.txt"
    output_dir = project_root / "frontend" / "public" / "data" / "cities"
    
    # 创建输出目录
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"解析 {cities_file}...")
    countries, country_stats = parse_cities500(str(cities_file))
    
    print(f"发现 {len(countries)} 个国家/地区")
    
    # 生成各国家 JSON
    total_cities = 0
    for country_code, admin1_data in countries.items():
        admin1_count, city_count = build_country_json(country_code, admin1_data, output_dir)
        total_cities += city_count
        if city_count > 1000:
            print(f"  {country_code}: {admin1_count} admin1s, {city_count} cities")
    
    # 生成国家索引
    country_count = build_countries_index(country_stats, output_dir)
    
    print(f"\n完成！")
    print(f"  - 国家/地区: {country_count}")
    print(f"  - 城市总数: {total_cities}")
    print(f"  - 输出目录: {output_dir}")


if __name__ == "__main__":
    main()
