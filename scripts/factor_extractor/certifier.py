"""Factor Certifier - 因子认证工具

将new_candidate因子认证为existing因子，分配符合规范的factor_id。
"""

import re
import unicodedata
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

import yaml

from .models import DivinationSystem, FactorCandidate


# 中文到英文的因子类型映射
FACTOR_TYPE_MAPPING = {
    # 结构类
    "结构类": "structure",
    "地支类": "structure",
    "天干类": "structure",
    "十神类": "structure",
    "宫位类": "structure",
    "星曜类": "structure",
    "位置类": "structure",
    "组合类": "structure",
    # 状态类
    "状态类": "state",
    "态势类": "state",
    "强度类": "state",
    "等级类": "state",
    "程度类": "state",
    "性质类": "state",
    "性质层": "state",
    "水平类": "state",
    "资质类": "state",
    # 关系类
    "关系类": "relation",
    "配合类": "relation",
    "生克类": "relation",
    "刑冲类": "relation",
    "合化类": "relation",
    # 时间类
    "时间类": "temporal",
    "时机类": "temporal",
    "流年类": "temporal",
    "大运类": "temporal",
    "年龄类": "temporal",
    # 能量类
    "能量类": "energy",
    "情绪类": "energy",
    "气势类": "energy",
    # 边界类
    "边界类": "boundary",
    "条件类": "condition",
    "失效类": "condition",
    # 功能类
    "功能类": "function",
    "效应类": "effect",
    "评价类": "evaluation",
    # 其他
    "修正类": "modifier",
    "数量类": "quantity",
    "特质类": "trait",
    "特殊类": "special",
    "动态类": "dynamic",
    "稳定类": "stable",
    "顺序类": "order",
    "性别类": "gender",
    "模式类": "pattern",
}

# 常见中文词到英文的映射
TERM_MAPPING = {
    # 八字术语
    "日主": "day_master",
    "月令": "month_command",
    "时柱": "hour_pillar",
    "年柱": "year_pillar",
    "月柱": "month_pillar",
    "日柱": "day_pillar",
    "天干": "stem",
    "地支": "branch",
    "正官": "zhenguan",
    "七杀": "qisha",
    "正印": "zhengyin",
    "偏印": "pianyin",
    "正财": "zhengcai",
    "偏财": "piancai",
    "食神": "shishen",
    "伤官": "shangguan",
    "比肩": "bijian",
    "劫财": "jiecai",
    "用神": "yongshen",
    "忌神": "jishen",
    "喜神": "xishen",
    "格局": "geju",
    "强弱": "qiangruo",
    "旺衰": "wangshuai",
    "得令": "deling",
    "失令": "shiling",
    "通根": "tonggen",
    "透干": "tougan",
    "合化": "hehua",
    "冲克": "chongke",
    "刑害": "xinghai",
    "三合": "sanhe",
    "六合": "liuhe",
    "六冲": "liuchong",
    "墓库": "muku",
    "驿马": "yima",
    "桃花": "taohua",
    "禄神": "lushen",
    "羊刃": "yangren",
    "阳支": "yangzhi",
    "阴支": "yinzhi",
    "阳干": "yanggan",
    "阴干": "yingan",
    "五行": "wuxing",
    "木": "wood",
    "火": "fire",
    "土": "earth",
    "金": "metal",
    "水": "water",
    "甲": "jia",
    "乙": "yi",
    "丙": "bing",
    "丁": "ding",
    "戊": "wu",
    "己": "ji",
    "庚": "geng",
    "辛": "xin",
    "壬": "ren",
    "癸": "gui",
    "子": "zi",
    "丑": "chou",
    "寅": "yin",
    "卯": "mao",
    "辰": "chen",
    "巳": "si",
    "午": "wu",
    "未": "wei",
    "申": "shen",
    "酉": "you",
    "戌": "xu",
    "亥": "hai",
    # 紫微术语
    "紫微": "ziwei",
    "天机": "tianji",
    "太阳": "taiyang",
    "武曲": "wuqu",
    "天同": "tiantong",
    "廉贞": "lianzhen",
    "天府": "tianfu",
    "太阴": "taiyin",
    "贪狼": "tanlang",
    "巨门": "jumen",
    "天相": "tianxiang",
    "天梁": "tianliang",
    "破军": "pojun",
    "命宫": "minggong",
    "兄弟宫": "xiongdigong",
    "夫妻宫": "fuqigong",
    "子女宫": "zinvgong",
    "财帛宫": "caibaogong",
    "疾厄宫": "jiegong",
    "迁移宫": "qianyigong",
    "交友宫": "jiaoyougong",
    "官禄宫": "guanlugong",
    "田宅宫": "tianzhigong",
    "福德宫": "fudegong",
    "父母宫": "fumugong",
    "四化": "sihua",
    "化禄": "hualu",
    "化权": "huaquan",
    "化科": "huake",
    "化忌": "huaji",
    "庙旺": "miaowang",
    "落陷": "luoxian",
    "大限": "daxian",
    "小限": "xiaoxian",
    # 周易术语
    "乾": "qian",
    "坤": "kun",
    "震": "zhen",
    "巽": "xun",
    "坎": "kan",
    "离": "li",
    "艮": "gen",
    "兑": "dui",
    "阴阳": "yinyang",
    "爻": "yao",
    "卦": "gua",
    "变卦": "biangua",
    "互卦": "hugua",
    "上卦": "shanggua",
    "下卦": "xiagua",
    # 梦境术语
    "梦境": "dream",
    "场景": "scene",
    "符号": "symbol",
    "情绪": "emotion",
    "焦虑": "anxiety",
    "恐惧": "fear",
    "喜悦": "joy",
    "原型": "archetype",
    "阴影": "shadow",
    "阿尼玛": "anima",
    "阿尼姆斯": "animus",
    "自性": "self",
    # 通用术语
    "强度": "strength",
    "程度": "degree",
    "级别": "level",
    "类型": "type",
    "模式": "pattern",
    "状态": "state",
    "关系": "relation",
    "条件": "condition",
    "边界": "boundary",
    "效应": "effect",
    "评价": "evaluation",
    "指数": "index",
    "标记": "marker",
    "触发": "trigger",
    "互动": "interaction",
    "配置": "config",
    "组合": "combo",
}


@dataclass
class CertificationResult:
    """因子认证结果"""
    system: str
    total_candidates: int = 0
    certified_count: int = 0
    skipped_count: int = 0
    duplicate_ids: List[str] = field(default_factory=list)
    certified_factors: List[Dict] = field(default_factory=list)
    errors: List[str] = field(default_factory=list)


class FactorCertifier:
    """因子认证器
    
    将new_candidate因子认证为existing因子。
    """
    
    def __init__(self, ontology_dir: Path, existing_ids: Optional[Set[str]] = None):
        """初始化认证器
        
        Args:
            ontology_dir: 因子本体目录
            existing_ids: 已存在的因子ID集合
        """
        self.ontology_dir = ontology_dir
        self.existing_ids = existing_ids or set()
        self.new_ids: Set[str] = set()
        
        # 加载已有的因子ID
        self._load_existing_ids()
    
    def _load_existing_ids(self):
        """从因子本体目录加载已有的因子ID"""
        for yaml_file in self.ontology_dir.rglob("*.yaml"):
            try:
                with open(yaml_file, encoding="utf-8") as f:
                    data = yaml.safe_load(f)
                    if not data:
                        continue
                    
                    # 处理factors列表格式
                    if isinstance(data, dict) and "factors" in data:
                        for factor in data["factors"]:
                            if isinstance(factor, dict) and "id" in factor:
                                self.existing_ids.add(factor["id"])
            except Exception:
                continue
    
    def certify_candidates(self, candidates_file: Path) -> CertificationResult:
        """认证候选因子文件
        
        Args:
            candidates_file: 候选因子YAML文件路径
            
        Returns:
            CertificationResult: 认证结果
        """
        with open(candidates_file, encoding="utf-8") as f:
            data = yaml.safe_load(f)
        
        system = data.get("system", "unknown")
        result = CertificationResult(system=system)
        result.total_candidates = data.get("total_candidates", 0)
        
        by_type = data.get("by_type", {})
        
        for factor_type, factors in by_type.items():
            for factor_data in factors:
                try:
                    certified = self._certify_factor(factor_data, system)
                    if certified:
                        result.certified_factors.append(certified)
                        result.certified_count += 1
                    else:
                        result.skipped_count += 1
                except Exception as e:
                    result.errors.append(f"认证失败: {factor_data.get('factor_label', '?')}: {e}")
        
        return result
    
    def _certify_factor(self, factor_data: Dict, system: str) -> Optional[Dict]:
        """认证单个因子
        
        Args:
            factor_data: 因子数据
            system: 术数体系
            
        Returns:
            Optional[Dict]: 认证后的因子定义，无法认证返回None
        """
        label = factor_data.get("factor_label", "")
        existing_id = factor_data.get("factor_id", "")
        factor_type = factor_data.get("factor_type", "")
        
        if not label:
            return None
        
        # 生成因子ID
        if existing_id and self._validate_id(existing_id):
            factor_id = existing_id
        else:
            factor_id = self._generate_id(label, factor_type, system)
        
        # 确保ID唯一
        factor_id = self._ensure_unique_id(factor_id)
        
        # 确定分类
        category = self._determine_category(factor_type)
        
        # 构建认证后的因子
        certified = {
            "id": factor_id,
            "status": "existing",
            "display_zh": label,
            "display_en": self._generate_english_name(label),
            "description_zh": factor_data.get("notes", ""),
            "category": category,
            "value_type": self._infer_value_type(factor_data),
            "applicable_systems": [system] if system != "unknown" else [],
        }
        
        # 添加可选字段
        if factor_data.get("value_constraints"):
            certified["value_range"] = factor_data["value_constraints"]
        
        return certified
    
    def _validate_id(self, factor_id: str) -> bool:
        """验证因子ID是否符合规范"""
        if not factor_id:
            return False
        # 必须是小写字母、数字、下划线
        if not re.match(r"^[a-z][a-z0-9_]*$", factor_id):
            return False
        # 不能有中文
        if any("\u4e00" <= c <= "\u9fff" for c in factor_id):
            return False
        return True
    
    def _generate_id(self, label: str, factor_type: str, system: str) -> str:
        """生成因子ID"""
        # 确定前缀
        prefix = f"{system}_" if system and system != "unknown" else ""
        
        # 确定类别
        category = FACTOR_TYPE_MAPPING.get(factor_type, "")
        if category:
            prefix += f"{category}_"
        
        # 转换标签为英文
        name = self._translate_to_english(label)
        
        # 清理和规范化
        name = name.lower()
        name = re.sub(r"[^a-z0-9_]", "_", name)
        name = re.sub(r"_+", "_", name)
        name = name.strip("_")
        
        if not name:
            name = "unnamed"
        
        return prefix + name
    
    def _translate_to_english(self, chinese_text: str) -> str:
        """将中文文本转换为英文ID片段"""
        result = chinese_text
        
        # 应用术语映射
        for zh, en in sorted(TERM_MAPPING.items(), key=lambda x: -len(x[0])):
            result = result.replace(zh, f"_{en}_")
        
        # 清理多余的下划线和空格
        result = re.sub(r"[\s\-（）()【】\[\]]+", "_", result)
        result = re.sub(r"_+", "_", result)
        result = result.strip("_")
        
        # 如果还有中文字符，使用拼音或音译
        # 这里简化处理，直接移除中文字符
        result = re.sub(r"[\u4e00-\u9fff]+", "", result)
        result = re.sub(r"_+", "_", result)
        result = result.strip("_")
        
        return result if result else "factor"
    
    def _ensure_unique_id(self, factor_id: str) -> str:
        """确保因子ID唯一"""
        original_id = factor_id
        counter = 1
        
        while factor_id in self.existing_ids or factor_id in self.new_ids:
            factor_id = f"{original_id}_{counter}"
            counter += 1
        
        self.new_ids.add(factor_id)
        return factor_id
    
    def _determine_category(self, factor_type: str) -> str:
        """确定因子分类"""
        return FACTOR_TYPE_MAPPING.get(factor_type, "structure")
    
    def _generate_english_name(self, chinese_name: str) -> str:
        """生成英文显示名"""
        # 简单的术语替换
        result = chinese_name
        for zh, en in TERM_MAPPING.items():
            result = result.replace(zh, en.replace("_", " ").title())
        
        # 保留原中文作为备用
        if result == chinese_name:
            return f"[{chinese_name}]"
        
        return result.strip()
    
    def _infer_value_type(self, factor_data: Dict) -> str:
        """推断取值类型"""
        constraints = factor_data.get("value_constraints", "")
        
        if not constraints:
            return "boolean"
        
        constraints_lower = constraints.lower()
        
        # 检查是否是布尔值
        if constraints_lower in ["true/false", "yes/no", "on/off", "有/无"]:
            return "boolean"
        
        # 检查是否是数值范围
        if re.match(r"[\d.]+\s*[-~至到]\s*[\d.]+", constraints):
            return "numeric"
        
        # 检查是否是枚举
        if "/" in constraints or "、" in constraints or "|" in constraints:
            return "enum"
        
        return "string"
    
    def save_certified_factors(
        self, result: CertificationResult, output_dir: Path
    ) -> Path:
        """保存认证后的因子
        
        Args:
            result: 认证结果
            output_dir: 输出目录
            
        Returns:
            Path: 输出文件路径
        """
        system = result.system
        output_file = output_dir / f"{system}_certified.yaml"
        
        # 按类别分组
        by_category: Dict[str, List[Dict]] = defaultdict(list)
        for factor in result.certified_factors:
            category = factor.get("category", "structure")
            by_category[category].append(factor)
        
        output_data = {
            "system": system,
            "certified_time": datetime.now().isoformat(),
            "total_certified": result.certified_count,
            "by_category": dict(by_category),
        }
        
        output_dir.mkdir(parents=True, exist_ok=True)
        with open(output_file, "w", encoding="utf-8") as f:
            yaml.dump(
                output_data,
                f,
                allow_unicode=True,
                default_flow_style=False,
                sort_keys=False
            )
        
        return output_file
