"""
TOON Serializer

将结构化数据序列化为 TOON 格式，用于 LLM 边界的 Token 压缩。

复用已有模型: backend/core/contracts/toon_models.py

对照 requirements.md 2.1.1-2.3.3
对照 pitfalls.md 2.1, 2.2
"""

import logging
from datetime import datetime
from typing import Any, Dict, List, Optional

from backend.core.contracts import RuntimeRuleResult, FusionResult
from backend.core.contracts.toon_models import (
    ToonPayload,
    ABBREVIATIONS,
    ABBREVIATIONS_REVERSE,
    TOON_SYNTAX,
    TEN_GOD_ABBR,
)

logger = logging.getLogger(__name__)


class TOONSerializer:
    """
    TOON 序列化器
    
    将 RuntimeRuleResult, FusionResult 等结构化数据
    序列化为 TOON 格式，实现 Token 压缩。
    
    对照 requirements.md 2.1.1-2.1.4
    """
    
    MAX_BODY_LENGTH = 1000
    MAX_EVIDENCE_RULES = 10
    MAX_FACTORS_PER_RULE = 5
    MAX_THEMES = 5
    
    def serialize_rule(self, result: RuntimeRuleResult) -> str:
        """
        规则 → TOON 格式
        
        格式: rid:dim/lvl/conf/ev1,ev2,ev3
        例如: dts_jia_spring_001:C/+/0.8/dm,sn,st
        
        对照 requirements.md 2.1.1
        """
        # 维度缩写
        dim = ABBREVIATIONS.get(result.dimension, "")
        if not dim and result.dimension:
            dim = result.dimension[:1].upper()
        
        # 等级缩写
        lvl = ABBREVIATIONS.get(result.level, "0") if result.level else "0"
        
        # 置信度
        conf = f"{result.confidence:.2f}"
        
        # 证据因子缩写
        factors = []
        for factor in (result.evidence_factors or [])[:self.MAX_FACTORS_PER_RULE]:
            abbr = ABBREVIATIONS.get(factor, factor[:3] if factor else "")
            factors.append(abbr)
        factors_str = ",".join(factors)
        
        return f"{result.rule_id}:{dim}/{lvl}/{conf}/{factors_str}"
    
    def serialize_fusion(self, fusion: FusionResult) -> str:
        """
        融合结果 → TOON 格式
        
        格式:
        T:theme1|theme2|theme3
        [rules]
        XV:score
        CF:count
        
        对照 requirements.md 2.1.2
        """
        lines = []
        
        # 主题行
        themes = fusion.primary_themes[:self.MAX_THEMES]
        lines.append(f"T:{('|'.join(themes))}")
        
        # 证据规则
        for evidence in fusion.evidence_chain[:self.MAX_EVIDENCE_RULES]:
            lines.append(self.serialize_rule(evidence))
        
        # 交叉验证分数
        lines.append(f"XV:{fusion.cross_validation_score:.2f}")
        
        # 冲突数
        lines.append(f"CF:{len(fusion.conflicts)}")
        
        body = "\n".join(lines)
        
        # 硬截断保护
        if len(body) > self.MAX_BODY_LENGTH:
            logger.warning(
                f"TOON body truncated from {len(body)} to {self.MAX_BODY_LENGTH}"
            )
            body = body[:self.MAX_BODY_LENGTH - 3] + "..."
        
        return body
    
    def serialize_factor_matrix(self, factors: Dict[str, any]) -> str:
        """
        因子矩阵 → TOON 格式
        
        格式: fid1:val1,fid2:val2,...
        例如: dm:jia,ssn:spring,str:0.75
        
        对照 requirements.md 2.1.3
        """
        parts = []
        
        for key, value in list(factors.items())[:20]:  # 最多 20 个因子
            # 缩写 key
            abbr_key = ABBREVIATIONS.get(key, key[:3] if key else "")
            
            # 格式化 value
            if isinstance(value, float):
                abbr_value = f"{value:.2f}"
            elif isinstance(value, bool):
                abbr_value = "1" if value else "0"
            else:
                abbr_value = str(value)[:10]  # 截断长值
            
            parts.append(f"{abbr_key}:{abbr_value}")
        
        body = ",".join(parts)
        
        if len(body) > self.MAX_BODY_LENGTH:
            body = body[:self.MAX_BODY_LENGTH - 3] + "..."
        
        return body
    
    def to_payload(
        self,
        kind: str,
        body: str,
    ) -> ToonPayload:
        """
        创建 ToonPayload
        
        对照 requirements.md 2.3.2
        """
        # 确保不超长
        if len(body) > self.MAX_BODY_LENGTH:
            body = body[:self.MAX_BODY_LENGTH - 3] + "..."
        
        return ToonPayload(version="1", kind=kind, body=body)
    
    def serialize_to_payload(
        self,
        data: RuntimeRuleResult | FusionResult | Dict,
        kind: Optional[str] = None,
    ) -> ToonPayload:
        """
        自动检测类型并序列化为 ToonPayload
        """
        if isinstance(data, RuntimeRuleResult):
            body = self.serialize_rule(data)
            return self.to_payload(kind or "rule", body)
        elif isinstance(data, FusionResult):
            body = self.serialize_fusion(data)
            return self.to_payload(kind or "fusion", body)
        elif isinstance(data, dict):
            body = self.serialize_factor_matrix(data)
            return self.to_payload(kind or "factor_matrix", body)
        else:
            raise ValueError(f"Unsupported data type: {type(data)}")
    
    # =========================================================================
    # TOON v2 - 原始盘面数据序列化
    # =========================================================================
    
    MAX_V2_BODY_LENGTH = 2000  # v2 扩大上限
    MAX_PER_ENGINE = 500       # 单体系上限
    
    # 天干地支常量
    STEMS = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
    BRANCHES = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]
    
    def serialize_bazi_v2(self, factors: Any) -> str:
        """
        八字因子 → TOON v2 格式
        
        输出示例:
        BZ.P:癸未|壬戌|癸亥|己未
        BZ.DM:癸/water/yin/0.51/neutral
        BZ.DY:己未/22-31/current
        BZ.LN:甲辰/2024
        BZ.TG:bj1|jc2|qs3|pc3
        BZ.SSN:autumn
        """
        lines = []
        
        try:
            # BZ.P: 四柱
            p = factors.four_pillars
            pillars = (f"{p['year']['stem']}{p['year']['branch']}|"
                      f"{p['month']['stem']}{p['month']['branch']}|"
                      f"{p['day']['stem']}{p['day']['branch']}|"
                      f"{p['hour']['stem']}{p['hour']['branch']}")
            lines.append(f"BZ.P:{pillars}")
            
            # BZ.DM: 日主
            lines.append(f"BZ.DM:{factors.day_master}/"
                        f"{factors.day_master_element}/"
                        f"{factors.day_master_yinyang}/"
                        f"{factors.day_master_strength:.2f}/"
                        f"{factors.strength_category}")
            
            # BZ.DY: 当前大运
            current_dayun = self._get_current_dayun(factors.dayun_list, factors.start_dayun_age)
            if current_dayun:
                lines.append(f"BZ.DY:{current_dayun['stem']}{current_dayun['branch']}/"
                            f"{current_dayun['start_age']}-{current_dayun['end_age']}/current")
            
            # BZ.LN: 流年
            year = datetime.now().year
            ganzhi = self._year_to_ganzhi(year)
            lines.append(f"BZ.LN:{ganzhi}/{year}")
            
            # BZ.TG: 十神分布
            if factors.ten_god_counts:
                tg_parts = []
                for god, count in factors.ten_god_counts.items():
                    if count > 0:
                        abbr = TEN_GOD_ABBR.get(god, god[:2])
                        tg_parts.append(f"{abbr}{count}")
                if tg_parts:
                    lines.append(f"BZ.TG:{'|'.join(tg_parts[:8])}")
            
            # BZ.SSN: 季节
            lines.append(f"BZ.SSN:{factors.birth_season}")
            
        except Exception as e:
            logger.warning(f"Bazi v2 serialization partial failure: {e}")
        
        return "\n".join(lines)
    
    def serialize_astro_v2(self, factors: Any) -> str:
        """
        占星因子 → TOON v2 格式
        
        输出示例:
        AS.SUN:libra/7/24.5
        AS.MON:cancer/4/12.3
        AS.ASC:scorpio/1
        AS.ASP:sun_trine_moon/2.3|venus_square_saturn/1.8
        AS.RET:mercury,saturn
        """
        lines = []
        
        try:
            # AS.SUN: 太阳
            if hasattr(factors, 'planets') and 'sun' in factors.planets:
                sun = factors.planets['sun']
                lines.append(f"AS.SUN:{sun.sign}/{sun.house}/{sun.degree_in_sign:.1f}")
            
            # AS.MON: 月亮
            if hasattr(factors, 'planets') and 'moon' in factors.planets:
                moon = factors.planets['moon']
                lines.append(f"AS.MON:{moon.sign}/{moon.house}/{moon.degree_in_sign:.1f}")
            
            # AS.ASC: 上升
            if hasattr(factors, 'ascendant_sign'):
                lines.append(f"AS.ASC:{factors.ascendant_sign}/1")
            
            # AS.MC: 中天
            if hasattr(factors, 'midheaven_sign'):
                lines.append(f"AS.MC:{factors.midheaven_sign}/10")
            
            # AS.ASP: 相位 (前5个)
            if hasattr(factors, 'aspects') and factors.aspects:
                asp_parts = []
                for asp in factors.aspects[:5]:
                    asp_parts.append(f"{asp.planet1}_{asp.aspect_type}_{asp.planet2}/{asp.orb:.1f}")
                if asp_parts:
                    lines.append(f"AS.ASP:{'|'.join(asp_parts)}")
            
            # AS.RET: 逆行
            if hasattr(factors, 'planets'):
                ret_planets = [p for p, pos in factors.planets.items() 
                              if hasattr(pos, 'retrograde') and pos.retrograde]
                if ret_planets:
                    lines.append(f"AS.RET:{','.join(ret_planets)}")
            
        except Exception as e:
            logger.warning(f"Astro v2 serialization partial failure: {e}")
        
        return "\n".join(lines)
    
    def serialize_dream_v2(self, factors: Any) -> str:
        """
        解梦因子 → TOON v2 格式
        
        输出示例:
        DR.SYM:sea/nature/0.95,flying/scene/0.9
        DR.THM:flying,water
        DR.EMO:joy,peace
        """
        lines = []
        
        try:
            # DR.SYM: 符号
            if hasattr(factors, 'symbols') and factors.symbols:
                sym_parts = []
                for s in factors.symbols[:5]:
                    if hasattr(s, 'symbol'):
                        conf = getattr(s, 'confidence', 1.0)
                        cat = getattr(s, 'category', 'unknown')
                        sym_parts.append(f"{s.symbol}/{cat}/{conf:.2f}")
                if sym_parts:
                    lines.append(f"DR.SYM:{','.join(sym_parts)}")
            
            # DR.THM: 主题
            if hasattr(factors, 'themes') and factors.themes:
                lines.append(f"DR.THM:{','.join(factors.themes[:5])}")
            
            # DR.EMO: 情绪
            if hasattr(factors, 'emotions') and factors.emotions:
                lines.append(f"DR.EMO:{','.join(factors.emotions[:3])}")
            
        except Exception as e:
            logger.warning(f"Dream v2 serialization partial failure: {e}")
        
        return "\n".join(lines)
    
    def serialize_tarot_v2(self, factors: Any) -> str:
        """
        塔罗因子 → TOON v2 格式
        
        输出示例:
        TR.SP:three_card
        TR.C1:the_fool/upright/past
        TR.C2:the_magician/reversed/present
        TR.MA:2
        TR.RV:1
        """
        lines = []
        
        try:
            # TR.SP: 牌阵
            if hasattr(factors, 'spread_type'):
                lines.append(f"TR.SP:{factors.spread_type}")
            
            # TR.Cn: 各牌位
            if hasattr(factors, 'cards'):
                major_count = 0
                reversed_count = 0
                for i, card in enumerate(factors.cards[:10], 1):
                    name = getattr(card, 'card_name', str(card)).lower().replace(" ", "_")
                    is_reversed = getattr(card, 'reversed', False)
                    orientation = "reversed" if is_reversed else "upright"
                    position = getattr(card, 'position', f'pos{i}')
                    lines.append(f"TR.C{i}:{name}/{orientation}/{position}")
                    
                    if getattr(card, 'is_major', False):
                        major_count += 1
                    if is_reversed:
                        reversed_count += 1
                
                # TR.MA: 大阿卡纳数
                lines.append(f"TR.MA:{major_count}")
                
                # TR.RV: 逆位数
                lines.append(f"TR.RV:{reversed_count}")
            
        except Exception as e:
            logger.warning(f"Tarot v2 serialization partial failure: {e}")
        
        return "\n".join(lines)
    
    def serialize_ziwei_v2(self, factors: Any) -> str:
        """
        紫微因子 → TOON v2 格式
        
        输出示例:
        ZW.MG:寅/紫微,天府/庙
        ZW.SG:财帛宫
        ZW.WX:水二局
        ZW.SH:禄=廉贞/权=紫微/科=天机/忌=太阳
        ZW.DX:官禄宫/22-31
        """
        lines = []
        
        try:
            # ZW.MG: 命宫
            if hasattr(factors, 'ming_palace_branch'):
                branch = factors.ming_palace_branch
                main_stars = ""
                brightness = ""
                if hasattr(factors, 'palaces') and '命宫' in factors.palaces:
                    palace = factors.palaces['命宫']
                    if palace.get('main_stars'):
                        main_stars = ','.join(palace['main_stars'][:2])
                    # 星曜亮度
                    if hasattr(factors, 'star_brightness') and palace.get('main_stars'):
                        first_star = palace['main_stars'][0]
                        brightness = factors.star_brightness.get(first_star, '')
                lines.append(f"ZW.MG:{branch}/{main_stars}/{brightness}")
            
            # ZW.SG: 身宫
            if hasattr(factors, 'body_palace_name'):
                lines.append(f"ZW.SG:{factors.body_palace_name}")
            
            # ZW.WX: 五行局
            if hasattr(factors, 'five_element_type'):
                lines.append(f"ZW.WX:{factors.five_element_type}")
            
            # ZW.SH: 四化
            if hasattr(factors, 'sihua_natal') and factors.sihua_natal:
                sihua_parts = []
                for hua, star in factors.sihua_natal.items():
                    sihua_parts.append(f"{hua}={star}")
                if sihua_parts:
                    lines.append(f"ZW.SH:{'/'.join(sihua_parts)}")
            
            # ZW.DX: 大限
            if hasattr(factors, 'current_decade') and factors.current_decade:
                cd = factors.current_decade
                palace_name = cd.get('palace_name', '')
                start_age = cd.get('start_age', '')
                end_age = cd.get('end_age', '')
                lines.append(f"ZW.DX:{palace_name}/{start_age}-{end_age}")
            
        except Exception as e:
            logger.warning(f"Ziwei v2 serialization partial failure: {e}")
        
        return "\n".join(lines)
    
    def serialize_yijing_v2(self, factors: Any) -> str:
        """
        易经因子 → TOON v2 格式
        
        输出示例:
        YJ.GUA:1/乾/qian
        YJ.TRI:乾/乾
        YJ.MUT:1/乾
        YJ.CHG:44/姤
        YJ.MOV:2,5
        YJ.MTH:coin
        """
        lines = []
        
        try:
            # YJ.GUA: 主卦
            if hasattr(factors, 'main_hexagram') and factors.main_hexagram:
                hex = factors.main_hexagram
                number = getattr(hex, 'number', 0)
                name_zh = getattr(hex, 'name_zh', '')
                name_pinyin = getattr(hex, 'name_pinyin', '')
                lines.append(f"YJ.GUA:{number}/{name_zh}/{name_pinyin}")
            
            # YJ.TRI: 上下卦
            if hasattr(factors, 'main_hexagram') and factors.main_hexagram:
                hex = factors.main_hexagram
                upper = getattr(hex, 'upper_trigram', '')
                lower = getattr(hex, 'lower_trigram', '')
                if upper and lower:
                    lines.append(f"YJ.TRI:{upper}/{lower}")
            
            # YJ.MUT: 互卦
            if hasattr(factors, 'mutual_hexagram') and factors.mutual_hexagram:
                mut = factors.mutual_hexagram
                lines.append(f"YJ.MUT:{getattr(mut, 'number', 0)}/{getattr(mut, 'name_zh', '')}")
            
            # YJ.CHG: 变卦 (可能为空)
            if hasattr(factors, 'changed_hexagram') and factors.changed_hexagram:
                chg = factors.changed_hexagram
                lines.append(f"YJ.CHG:{getattr(chg, 'number', 0)}/{getattr(chg, 'name_zh', '')}")
            
            # YJ.MOV: 动爻
            if hasattr(factors, 'moving_lines'):
                moving = factors.moving_lines
                if moving:
                    lines.append(f"YJ.MOV:{','.join(str(m) for m in moving)}")
                else:
                    lines.append("YJ.MOV:0")  # 静卦
            
            # YJ.MTH: 起卦法
            if hasattr(factors, 'divination_method'):
                lines.append(f"YJ.MTH:{factors.divination_method}")
            
        except Exception as e:
            logger.warning(f"Yijing v2 serialization partial failure: {e}")
        
        return "\n".join(lines)
    
    def serialize_full_v2(
        self,
        fusion: FusionResult,
        raw_factors: Dict[str, Any],
        insights: Optional[List[Any]] = None,
    ) -> str:
        """
        完整 TOON v2 序列化
        
        Args:
            fusion: 融合结果
            raw_factors: 原始因子对象字典 {'bazi-calculator': BaziFactors, ...}
            insights: 历史洞察列表 (可选)
            
        Returns:
            完整 TOON v2 字符串
        """
        lines = ["V:2"]
        
        # 引擎列表
        engine_names = [k.split("-")[0] for k in raw_factors.keys()]
        lines.append(f"E:{','.join(engine_names)}")
        lines.append("")
        
        # 各体系盘面块
        for engine_id, factors in raw_factors.items():
            engine_block = ""
            if engine_id == "bazi-calculator":
                engine_block = self.serialize_bazi_v2(factors)
            elif engine_id == "astro-calculator":
                engine_block = self.serialize_astro_v2(factors)
            elif engine_id == "dream-extractor":
                engine_block = self.serialize_dream_v2(factors)
            elif engine_id == "tarot-interpreter":
                engine_block = self.serialize_tarot_v2(factors)
            elif engine_id == "ziwei-calculator":
                engine_block = self.serialize_ziwei_v2(factors)
            elif engine_id == "yijing-calculator":
                engine_block = self.serialize_yijing_v2(factors)
            
            if engine_block:
                # 截断单体系
                if len(engine_block) > self.MAX_PER_ENGINE:
                    engine_block = engine_block[:self.MAX_PER_ENGINE - 3] + "..."
                lines.append(engine_block)
                lines.append("")
        
        # WP-02: 历史洞察行（最多5条）
        if insights:
            for insight in insights[:5]:  # 最多5条
                ins_line = self._serialize_insight(insight)
                if ins_line:
                    lines.append(ins_line)
        
        # 规则块 (复用 v1)
        lines.append(self.serialize_fusion(fusion))
        
        body = "\n".join(lines)
        
        # 截断保护
        if len(body) > self.MAX_V2_BODY_LENGTH:
            logger.warning(f"TOON v2 body truncated from {len(body)} to {self.MAX_V2_BODY_LENGTH}")
            body = body[:self.MAX_V2_BODY_LENGTH - 3] + "..."
        
        return body
    
    def _serialize_insight(self, insight: Any) -> Optional[str]:
        """
        WP-02: 序列化单条洞察为 INS: 行
        
        格式: INS:{dimension}/{strength}/{summary_short}/{factors_count}
        - dimension: 维度名（转义 / 字符）
        - strength: 强度 0.00-1.00
        - summary_short: 摘要（最多20字符，转义 / 字符）
        - factors_count: 相关因子数
        """
        try:
            # 获取并清洗字段
            dimension = str(getattr(insight, 'dimension', 'unknown'))
            strength = float(getattr(insight, 'strength', 0.0))
            summary = str(getattr(insight, 'summary', ''))
            related_factors = getattr(insight, 'related_factors', [])
            factors_count = len(related_factors) if related_factors else 0
            
            # WP-02: 转义 / 字符避免破坏解析
            dimension = dimension.replace('/', '|')
            summary_short = summary[:20].replace('/', '|')
            
            # 验证强度范围
            strength = max(0.0, min(1.0, strength))
            
            return f"INS:{dimension}/{strength:.2f}/{summary_short}/{factors_count}"
        except Exception as e:
            logger.warning(f"Failed to serialize insight: {e}")
            return None
    
    def _get_current_dayun(
        self, 
        dayun_list: List[Dict], 
        start_age: int
    ) -> Optional[Dict]:
        """根据当前年龄找到对应的大运"""
        if not dayun_list:
            return None
        # 简化: 返回第二个大运（通常是当前运）或第一个
        if len(dayun_list) > 1:
            return dayun_list[1]
        return dayun_list[0] if dayun_list else None
    
    def _year_to_ganzhi(self, year: int) -> str:
        """年份转干支"""
        stem_idx = (year - 4) % 10
        branch_idx = (year - 4) % 12
        return f"{self.STEMS[stem_idx]}{self.BRANCHES[branch_idx]}"


class TOONParser:
    """
    TOON 解析器
    
    将 TOON 格式解析回结构化数据。
    注意: 部分信息会丢失，只能恢复关键字段。
    
    对照 requirements.md 2.2.1-2.2.3
    """
    
    def parse_rule(self, toon: str) -> RuntimeRuleResult:
        """
        解析规则 TOON
        
        格式: rid:dim/lvl/conf/ev1,ev2,ev3
        """
        try:
            # 分割 rule_id 和其他部分
            parts = toon.split(":", 1)
            if len(parts) != 2:
                return self._create_fallback_result(toon)
            
            rule_id = parts[0]
            rest = parts[1].split("/")
            
            if len(rest) < 3:
                return self._create_fallback_result(toon, rule_id=rule_id)
            
            # 解析各字段
            dim_abbr = rest[0]
            lvl_abbr = rest[1]
            conf_str = rest[2]
            factors_str = rest[3] if len(rest) > 3 else ""
            
            # 反查维度
            dimension = ABBREVIATIONS_REVERSE.get(dim_abbr, dim_abbr)
            
            # 反查等级
            level = ABBREVIATIONS_REVERSE.get(lvl_abbr, lvl_abbr)
            
            # 解析置信度
            try:
                confidence = float(conf_str)
            except ValueError:
                confidence = 0.0
            
            # 解析因子
            factors = []
            if factors_str:
                for abbr in factors_str.split(","):
                    factor = ABBREVIATIONS_REVERSE.get(abbr, abbr)
                    factors.append(factor)
            
            return RuntimeRuleResult(
                rule_id=rule_id,
                matched=True,
                dimension=dimension,
                level=level,
                confidence=confidence,
                weight=1.0,  # 默认权重
                evidence_factors=factors,
                execution_time_ms=0.0,  # 解析时无此信息
            )
        
        except Exception as e:
            logger.warning(f"Failed to parse TOON rule: {e}")
            return self._create_fallback_result(toon)
    
    def parse_fusion(self, toon: str) -> Dict:
        """
        解析融合 TOON
        
        返回字典形式，因为无法完全恢复 FusionResult。
        """
        result = {
            "themes": [],
            "rules": [],
            "cross_validation_score": 0.0,
            "conflicts_count": 0,
        }
        
        for line in toon.strip().split("\n"):
            line = line.strip()
            if not line:
                continue
            
            if line.startswith("T:"):
                result["themes"] = line[2:].split("|")
            elif line.startswith("XV:"):
                try:
                    result["cross_validation_score"] = float(line[3:])
                except ValueError:
                    pass
            elif line.startswith("CF:"):
                try:
                    result["conflicts_count"] = int(line[3:])
                except ValueError:
                    pass
            elif ":" in line and "/" in line:
                # 尝试解析为规则
                rule = self.parse_rule(line)
                result["rules"].append(rule)
        
        return result
    
    def _create_fallback_result(
        self,
        toon: str,
        rule_id: Optional[str] = None,
    ) -> RuntimeRuleResult:
        """创建降级结果"""
        return RuntimeRuleResult(
            rule_id=rule_id or f"parsed_{hash(toon) % 10000}",
            matched=True,
            confidence=0.0,
            weight=1.0,
            execution_time_ms=0.0,
            description=f"Parsed from TOON: {toon[:50]}...",
        )
