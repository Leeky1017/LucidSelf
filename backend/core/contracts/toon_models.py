"""
TOON Protocol Models for LucidSelf Contracts

TOON v1 协议模型定义，用于 LLM 边界的 Token 压缩。
对照文档: docs/数据契约_Schema定义规范_v1.md §11
"""

from typing import Dict, Literal

from pydantic import BaseModel, ConfigDict, Field


# =============================================================================
# TOON 协议常量 (§11.2, §11.3, §11.4)
# =============================================================================


TOON_SYNTAX: Dict[str, Dict] = {
    "rule": {
        "format": "rid:dim/lvl/conf/ev1,ev2,ev3",
        "example": "dts_jia_spring_001:C/+/0.8/dm,sn,st",
        "fields": {
            "rid": "规则ID",
            "dim": "维度缩写 (C=事业, H=健康, M=婚姻, W=财富)",
            "lvl": "等级 (++=大吉, +=吉, 0=中等, -=凶, --=大凶)",
            "conf": "置信度 (0.0-1.0)",
            "ev": "证据因子缩写列表 (逗号分隔)"
        }
    },
    "fusion": {
        "format": "T:theme1|theme2|theme3\\n[rules]\\nXV:score\\n[CF:count]",
        "example": "T:事业突破|财富积累\\ndts_jia_001:C/+/0.85/dm,sn\\nXV:0.87\\nCF:0",
        "lines": {
            "T": "主题行 (竖线分隔)",
            "rules": "各条规则的 TOON 简写",
            "XV": "交叉验证分数",
            "CF": "冲突数量 (可选)"
        }
    },
    "factor_matrix": {
        "format": "fid1:val1,fid2:val2,...",
        "example": "dm:jia,ssn:spring,str:0.75",
        "max_factors": 20
    }
}
"""TOON 语法规范定义"""


ABBREVIATIONS: Dict[str, str] = {
    # 维度缩写
    "事业": "C",    # Career
    "健康": "H",    # Health
    "婚姻": "M",    # Marriage
    "财富": "W",    # Wealth
    "人际": "R",    # Relationship
    "学业": "E",    # Education
    "性格": "P",    # Personality
    
    # 等级缩写
    "大吉": "++",
    "吉": "+",
    "中等": "0",
    "凶": "-",
    "大凶": "--",
    
    # 常用因子缩写
    "day_master": "dm",
    "day_master_jia": "dm_jia",
    "day_master_yi": "dm_yi",
    "season": "ssn",
    "season_spring": "ssn_sp",
    "season_summer": "ssn_su",
    "season_autumn": "ssn_au",
    "season_winter": "ssn_wi",
    "strength": "str",
    "strength_strong": "str_s",
    "strength_weak": "str_w",
    "ten_god_zhengguan": "zg",
    "ten_god_qisha": "qs",
    "ten_god_cai": "cai",
    "ten_god_bijian": "bj",
    
    # 塔罗因子缩写
    "major_arcana": "ma",
    "minor_arcana": "mi",
    "suit_wands": "sw",
    "suit_cups": "sc",
    "suit_swords": "ss",
    "suit_pentacles": "sp",
    "orientation_upright": "up",
    "orientation_reversed": "rv",
    
    # 占星因子缩写
    "sun_sign": "sun",
    "moon_sign": "moon",
    "ascendant": "asc",
    "house": "h",
}
"""缩写映射表 - 用于 TOON 序列化"""

# 反向映射（用于解析）
ABBREVIATIONS_REVERSE: Dict[str, str] = {v: k for k, v in ABBREVIATIONS.items()}


# =============================================================================
# TOON v2 扩展定义 - 原始盘面数据序列化
# =============================================================================

TOON_V2_PREFIXES = {
    # 通用
    "version": "V:",       # V:2
    "engines": "E:",       # E:bazi,astro
    
    # 八字 (Bazi)
    "bz_pillars": "BZ.P:",       # 四柱
    "bz_daymaster": "BZ.DM:",    # 日主
    "bz_dayun": "BZ.DY:",        # 大运
    "bz_liunian": "BZ.LN:",      # 流年
    "bz_tengod": "BZ.TG:",       # 十神
    "bz_season": "BZ.SSN:",      # 季节
    "bz_nayin": "BZ.NY:",        # 纳音
    
    # 占星 (Astro)
    "as_sun": "AS.SUN:",         # 太阳
    "as_moon": "AS.MON:",        # 月亮
    "as_asc": "AS.ASC:",         # 上升
    "as_mc": "AS.MC:",           # 中天
    "as_aspects": "AS.ASP:",     # 相位
    "as_retrograde": "AS.RET:",  # 逆行
    
    # 紫微 (Ziwei)
    "zw_ming": "ZW.MG:",         # 命宫
    "zw_shen": "ZW.SG:",         # 身宫
    "zw_wuxing": "ZW.WX:",       # 五行局
    "zw_sihua": "ZW.SH:",        # 四化
    "zw_daxian": "ZW.DX:",       # 大限
    "zw_sha": "ZW.SHA:",         # 煞星
    
    # 塔罗 (Tarot)
    "tr_spread": "TR.SP:",       # 牌阵
    "tr_card": "TR.C",           # 牌位 (TR.C1:, TR.C2:, ...)
    "tr_major": "TR.MA:",        # 大阿卡纳数
    "tr_reversed": "TR.RV:",     # 逆位数
    
    # 解梦 (Dream)
    "dr_symbols": "DR.SYM:",     # 符号
    "dr_themes": "DR.THM:",      # 主题
    "dr_emotions": "DR.EMO:",    # 情绪
    "dr_text": "DR.TXT:",        # 原文摘要
    
    # 易经 (Yijing)
    "yj_gua": "YJ.GUA:",         # 主卦
    "yj_trigrams": "YJ.TRI:",    # 上下卦
    "yj_mutual": "YJ.MUT:",      # 互卦
    "yj_changed": "YJ.CHG:",     # 变卦
    "yj_moving": "YJ.MOV:",      # 动爻
    "yj_method": "YJ.MTH:",      # 起卦法
    
    # 历史洞察 (Insight)
    "insight": "INS:",           # INS:dimension/strength/summary/count
}
"""TOON v2 行前缀定义"""

# 十神缩写映射 (用于 BZ.TG: 行)
TEN_GOD_ABBR = {
    "比肩": "bj", "劫财": "jc", "食神": "sn", "伤官": "sg",
    "偏财": "pc", "正财": "zc", "七杀": "qs", "正官": "zg",
    "偏印": "py", "正印": "zy",
}
"""十神缩写映射"""

TEN_GOD_ABBR_REVERSE = {v: k for k, v in TEN_GOD_ABBR.items()}


TOON_CONSTRAINTS: list[str] = [
    "TOON 中不得出现原始 PII (姓名、精确地址、身份证号等)",
    "所有枚举值必须来自 Factor/Rule 的注册表缩写映射",
    "默认一切 TOON 文本视为'一次性 prompt 上下文'，不做长期存储",
    "长期存储只能存结构化对象 (Pydantic 模型)",
    "单个 TOON payload 不得超过 1000 字符",
    "TOON 只能出现在 LLM 边界，禁止在 Engine Layer1-4 传递",
]
"""TOON 协议约束规则"""


# =============================================================================
# TOON 载体模型 (§11.1)
# =============================================================================


class ToonPayload(BaseModel):
    """
    TOON 协议顶层载体
    
    LLM 边界的 Token 压缩协议载体。
    对照文档 §11.1 ToonPayload
    """
    version: Literal["1"] = Field(
        default="1", 
        description="协议版本"
    )
    kind: Literal["rule", "fusion", "memory", "factor_matrix"] = Field(
        ..., 
        description="载体类型"
    )
    body: str = Field(
        ..., 
        max_length=1000, 
        description="TOON 文本内容，最多 1000 字符"
    )

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "version": "1",
                    "kind": "rule",
                    "body": "dts_jia_spring_001:C/+/0.8/dm,sn,st"
                },
                {
                    "version": "1",
                    "kind": "fusion",
                    "body": "T:事业突破|财富积累|团队建设\n"
                           "dts_jia_001:C/+/0.85/dm,sn\n"
                           "bazi_cai_002:W/++/0.9/cai,shn\n"
                           "XV:0.87\nCF:0"
                },
                {
                    "version": "1",
                    "kind": "factor_matrix",
                    "body": "dm:jia,ssn:spring,str:0.75"
                }
            ]
        }
    )
