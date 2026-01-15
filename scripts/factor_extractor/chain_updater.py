"""LogicChain Factor Refs Updater - LogicChain因子引用更新工具

为LogicChain节点添加factor_refs字段。
"""

import re
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

import yaml


@dataclass
class ChainUpdateResult:
    """更新结果"""
    file_path: str
    nodes_updated: int = 0
    total_nodes: int = 0
    factor_refs_added: int = 0
    errors: List[str] = field(default_factory=list)


class LogicChainFactorUpdater:
    """LogicChain因子引用更新器
    
    为每个LogicChain节点生成factor_refs字段。
    """
    
    def __init__(self, certified_dir: Path, ontology_dir: Path):
        """初始化更新器
        
        Args:
            certified_dir: 认证因子目录
            ontology_dir: 因子本体目录
        """
        self.certified_dir = certified_dir
        self.ontology_dir = ontology_dir
        
        # 因子映射: display_zh -> factor_id
        self.factor_by_label: Dict[str, str] = {}
        # 因子映射: 关键词 -> factor_id
        self.factor_by_keyword: Dict[str, List[str]] = defaultdict(list)
        
        self._load_factors()
    
    def _load_factors(self):
        """加载因子本体和认证因子"""
        # 从因子本体加载
        for yaml_file in self.ontology_dir.rglob("*.yaml"):
            self._load_factors_from_file(yaml_file)
        
        # 从认证因子加载
        for yaml_file in self.certified_dir.glob("*_certified.yaml"):
            self._load_certified_factors(yaml_file)
    
    def _load_factors_from_file(self, yaml_file: Path):
        """从因子本体文件加载因子"""
        try:
            with open(yaml_file, encoding="utf-8") as f:
                data = yaml.safe_load(f)
            
            if not data:
                return
            
            factors = []
            if isinstance(data, dict):
                if "factors" in data:
                    factors = data["factors"]
                elif "neutral_tags" in data:
                    factors = data["neutral_tags"]
            
            for factor in factors:
                if not isinstance(factor, dict):
                    continue
                    
                factor_id = factor.get("id", "")
                display_zh = factor.get("display_zh", "")
                display_en = factor.get("display_en", "")
                
                if factor_id and display_zh:
                    self.factor_by_label[display_zh] = factor_id
                    # 提取关键词
                    self._extract_keywords(display_zh, factor_id)
                
                if factor_id and display_en:
                    self.factor_by_label[display_en.lower()] = factor_id
                    
        except Exception as e:
            print(f"警告: 加载因子失败 {yaml_file}: {e}")
    
    def _load_certified_factors(self, yaml_file: Path):
        """从认证因子文件加载"""
        try:
            with open(yaml_file, encoding="utf-8") as f:
                data = yaml.safe_load(f)
            
            if not data or "by_category" not in data:
                return
            
            for category, factors in data["by_category"].items():
                for factor in factors:
                    factor_id = factor.get("id", "")
                    display_zh = factor.get("display_zh", "")
                    
                    if factor_id and display_zh:
                        self.factor_by_label[display_zh] = factor_id
                        self._extract_keywords(display_zh, factor_id)
                        
        except Exception as e:
            print(f"警告: 加载认证因子失败 {yaml_file}: {e}")
    
    def _extract_keywords(self, label: str, factor_id: str):
        """从标签中提取关键词"""
        # 移除常见后缀
        keywords = re.split(r'[_\s\-/]', label)
        for kw in keywords:
            kw = kw.strip()
            if len(kw) >= 2:  # 至少2个字符
                self.factor_by_keyword[kw].append(factor_id)
    
    def update_chain(self, chain_file: Path) -> ChainUpdateResult:
        """更新单个LogicChain文件
        
        Args:
            chain_file: LogicChain文件路径
            
        Returns:
            ChainUpdateResult: 更新结果
        """
        result = ChainUpdateResult(file_path=str(chain_file))
        
        try:
            with open(chain_file, encoding="utf-8") as f:
                chain = yaml.safe_load(f)
        except Exception as e:
            result.errors.append(f"读取文件失败: {e}")
            return result
        
        if not chain or "nodes" not in chain:
            return result
        
        # 推断体系
        book_id = chain.get("book_id", "")
        system = self._infer_system(book_id)
        
        nodes = chain["nodes"]
        result.total_nodes = len(nodes)
        
        for node in nodes:
            if not isinstance(node, dict):
                continue
            
            # 如果已有factor_refs，跳过
            if node.get("factor_refs"):
                continue
            
            # 生成factor_refs
            factor_refs = self._generate_factor_refs(node, system)
            
            if factor_refs:
                node["factor_refs"] = factor_refs
                result.nodes_updated += 1
                result.factor_refs_added += len(factor_refs)
        
        # 保存更新后的文件
        if result.nodes_updated > 0:
            try:
                with open(chain_file, "w", encoding="utf-8") as f:
                    yaml.dump(
                        chain,
                        f,
                        allow_unicode=True,
                        default_flow_style=False,
                        sort_keys=False
                    )
            except Exception as e:
                result.errors.append(f"写入文件失败: {e}")
        
        return result
    
    def update_all(self, chains_dir: Path) -> List[ChainUpdateResult]:
        """更新所有LogicChain文件
        
        Args:
            chains_dir: LogicChain目录
            
        Returns:
            List[ChainUpdateResult]: 更新结果列表
        """
        results = []
        
        for chain_file in chains_dir.glob("*.yaml"):
            # 跳过备份文件
            if ".bak" in chain_file.name or "archive" in str(chain_file):
                continue
            
            result = self.update_chain(chain_file)
            results.append(result)
        
        return results
    
    def _generate_factor_refs(self, node: dict, system: str) -> List[str]:
        """为节点生成factor_refs
        
        Args:
            node: 节点数据
            system: 术数体系
            
        Returns:
            List[str]: 因子ID列表
        """
        factor_refs = set()
        
        # 从summary中匹配
        summary = node.get("summary", "")
        if summary:
            refs = self._match_factors(summary, system)
            factor_refs.update(refs)
        
        # 从role中匹配
        role = node.get("role", "")
        if role:
            refs = self._match_factors(role, system)
            factor_refs.update(refs)
        
        return list(factor_refs)[:10]  # 限制最多10个因子
    
    def _match_factors(self, text: str, system: str) -> Set[str]:
        """从文本中匹配因子
        
        Args:
            text: 待匹配文本
            system: 术数体系
            
        Returns:
            Set[str]: 匹配到的因子ID集合
        """
        matched = set()
        
        # 精确匹配标签
        for label, factor_id in self.factor_by_label.items():
            if label in text:
                matched.add(factor_id)
        
        # 关键词匹配（只取前5个最相关的）
        for kw, factor_ids in self.factor_by_keyword.items():
            if len(kw) >= 3 and kw in text:
                # 优先选择同体系的因子
                for fid in factor_ids[:3]:
                    if system in fid or system == "unknown":
                        matched.add(fid)
        
        return matched
    
    def _infer_system(self, book_id: str) -> str:
        """推断术数体系"""
        book_lower = book_id.lower()
        
        if any(k in book_lower for k in ["滴天髓", "子平", "三命", "穷通", "渊海", "bazi"]):
            return "bazi"
        if any(k in book_lower for k in ["紫微", "ziwei"]):
            return "ziwei"
        if any(k in book_lower for k in ["astro", "house", "planet", "zodiac"]):
            return "astro"
        if any(k in book_lower for k in ["dream", "梦", "freud", "jung"]):
            return "dream"
        if any(k in book_lower for k in ["tarot", "thoth", "arcana"]):
            return "tarot"
        if any(k in book_lower for k in ["周易", "易经", "yijing", "iching"]):
            return "yijing"
        
        return "unknown"
