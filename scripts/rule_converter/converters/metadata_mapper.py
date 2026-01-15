"""
Metadata Mapper

映射 source_ref 到规则元数据。

Feature: rule-converter
Requirement Refs: Req 6.1-6.6
"""

import logging
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Dict, Optional

logger = logging.getLogger(__name__)


@dataclass
class SourceMetadata:
    """
    规则溯源元数据
    
    对应 backend/core/contracts/base.py 中的 SourceMetadata
    """
    book_id: str
    chapter: Optional[str]
    l1_anchor: str
    extraction_date: str
    extraction_tool_version: str = "rule_converter_v1.0"
    
    def to_dict(self) -> Dict:
        """转换为字典"""
        return {
            "book_id": self.book_id,
            "chapter": self.chapter,
            "l1_anchor": self.l1_anchor,
            "extraction_date": self.extraction_date,
            "extraction_tool_version": self.extraction_tool_version,
        }


class MetadataMapper:
    """
    元数据映射器
    
    从 LogicChainNode 的 source_ref 提取规则元数据。
    
    source_ref 格式：
    - 《滴天髓·通天论》#第1条
    - 《三命通会》卷一#甲木
    - 《滴天髓》通天论#2
    
    Requirement Refs: Req 6.1-6.6
    """
    
    # 书名到 book_id 的映射
    BOOK_ID_MAP: Dict[str, str] = {
        "滴天髓": "ditianshui",
        "子平真诠": "zipingzhenquan",
        "三命通会": "sanminghui",
        "渊海子平": "yuanhaiziping",
        "穷通宝鉴": "qiongtongbaojian",
        "紫微斗数全书": "ziweidoushu",
        "周易": "zhouyi",
        "周公解梦": "zhougongjiemeng",
        "梦林玄解": "menglinxuanjie",
        "the_inner_sky": "inner_sky",
        "christian_astrology": "christian_astrology",
        "tetrabiblos": "tetrabiblos",
        "planets_in_transit": "planets_transit",
        "the_astrological_houses": "astro_houses",
        "astrology_of_personality": "astro_personality",
        "78_degrees_of_wisdom": "78_degrees",
        "waite_pictorial_key": "waite_key",
        "learning_the_tarot": "learning_tarot",
        "the_book_of_thoth": "book_thoth",
        "the_archetypes_and_the_collective_unconscious": "jung_archetypes",
    }
    
    # 书名到缩写的映射（用于生成 l1_anchor）
    BOOK_ABBR_MAP: Dict[str, str] = {
        "滴天髓": "DTS",
        "子平真诠": "ZPZQ",
        "三命通会": "SMTH",
        "渊海子平": "YHZP",
        "穷通宝鉴": "QTBJ",
        "紫微斗数全书": "ZWDS",
        "周易": "ZY",
        "周公解梦": "ZGJM",
        "梦林玄解": "MLXJ",
        "the_inner_sky": "TIS",
        "christian_astrology": "CA",
        "tetrabiblos": "TTB",
        "planets_in_transit": "PIT",
        "the_astrological_houses": "TAH",
        "astrology_of_personality": "AOP",
        "78_degrees_of_wisdom": "78D",
        "waite_pictorial_key": "WPK",
        "learning_the_tarot": "LTT",
        "the_book_of_thoth": "BOT",
        "the_archetypes_and_the_collective_unconscious": "JACU",
    }
    
    # source_ref 解析正则
    # 格式1: 《书名·章节》#条目
    # 格式2: 《书名》章节#条目
    SOURCE_REF_PATTERNS = [
        r"《([^》]+)·([^》]+)》#(.+)",  # 《滴天髓·通天论》#第1条
        r"《([^》]+)》([^#]+)#(.+)",    # 《滴天髓》通天论#2
        r"《([^》]+)》#(.+)",            # 《三命通会》#甲木
    ]
    
    def __init__(self):
        self._l1_anchor_registry: Dict[str, int] = {}  # 用于确保唯一性
    
    def map(
        self,
        source_ref: Optional[str],
        node_id: str,
        book_id_hint: Optional[str] = None,
    ) -> SourceMetadata:
        """
        从 source_ref 映射元数据
        
        Args:
            source_ref: 来源引用，如 "《滴天髓·通天论》#第1条"
            node_id: 节点ID（作为 fallback）
            book_id_hint: 书籍ID提示（从 LogicChain 文件名推断）
            
        Returns:
            SourceMetadata
        """
        book_name = None
        chapter = None
        entry = None
        
        if source_ref:
            # 尝试解析 source_ref
            for pattern in self.SOURCE_REF_PATTERNS:
                match = re.match(pattern, source_ref)
                if match:
                    groups = match.groups()
                    if len(groups) == 3:
                        book_name, chapter, entry = groups
                    elif len(groups) == 2:
                        book_name, entry = groups
                    break
        
        # 确定 book_id
        if book_name:
            book_id = self._get_book_id(book_name)
        elif book_id_hint:
            book_id = self._normalize_book_id(book_id_hint)
        else:
            book_id = "unknown"
        
        # 生成 l1_anchor
        l1_anchor = self._generate_l1_anchor(book_name, chapter, entry, node_id)
        
        # 生成提取日期
        extraction_date = datetime.now(timezone.utc).isoformat()
        
        return SourceMetadata(
            book_id=book_id,
            chapter=chapter,
            l1_anchor=l1_anchor,
            extraction_date=extraction_date,
        )
    
    def _get_book_id(self, book_name: str) -> str:
        """获取 book_id"""
        # 移除书名中的章节部分
        clean_name = book_name.split("·")[0].strip()
        
        # 查找映射
        for name, book_id in self.BOOK_ID_MAP.items():
            if name in clean_name or clean_name in name:
                return book_id
        
        # 没找到，使用拼音化
        return self._normalize_book_id(clean_name)
    
    def _normalize_book_id(self, name: str) -> str:
        """规范化 book_id"""
        # 简单处理：小写，替换空格和特殊字符
        result = name.lower()
        result = re.sub(r"[^a-z0-9_\u4e00-\u9fff]", "_", result)
        result = re.sub(r"_+", "_", result)
        return result.strip("_")
    
    def _generate_l1_anchor(
        self,
        book_name: Optional[str],
        chapter: Optional[str],
        entry: Optional[str],
        node_id: str,
    ) -> str:
        """
        生成唯一的 l1_anchor
        
        格式: {BOOK_ABBR}_{CHAPTER_ABBR}_{SEQ}
        """
        # 获取书名缩写
        book_abbr = "UNK"
        if book_name:
            clean_name = book_name.split("·")[0].strip()
            book_abbr = self.BOOK_ABBR_MAP.get(clean_name, "UNK")
        
        # 生成章节缩写
        chapter_abbr = ""
        if chapter:
            # 提取章节关键字
            chapter_abbr = self._abbreviate_chapter(chapter)
        
        # 生成条目编号
        entry_num = ""
        if entry:
            # 提取数字
            nums = re.findall(r"\d+", entry)
            if nums:
                entry_num = nums[0]
        
        # 组合基础 anchor
        parts = [book_abbr]
        if chapter_abbr:
            parts.append(chapter_abbr)
        if entry_num:
            parts.append(entry_num)
        
        base_anchor = "_".join(parts)
        
        # 确保唯一性
        if base_anchor in self._l1_anchor_registry:
            self._l1_anchor_registry[base_anchor] += 1
            return f"{base_anchor}_{self._l1_anchor_registry[base_anchor]}"
        else:
            self._l1_anchor_registry[base_anchor] = 0
            return base_anchor
    
    def _abbreviate_chapter(self, chapter: str) -> str:
        """生成章节缩写"""
        # 常见章节名到缩写的映射
        chapter_abbrs = {
            "通天论": "TTL",
            "论官": "LG",
            "论财": "LC",
            "论印": "LY",
            "论食神": "LSS",
            "论伤官": "LSG",
            "论比劫": "LBJ",
            "卷一": "V1",
            "卷二": "V2",
            "卷三": "V3",
            "上卷": "SJ",
            "下卷": "XJ",
        }
        
        for name, abbr in chapter_abbrs.items():
            if name in chapter:
                return abbr
        
        # 默认取前两个字符
        return chapter[:2].upper() if chapter else ""
    
    def reset_registry(self):
        """重置 anchor 注册表"""
        self._l1_anchor_registry.clear()
