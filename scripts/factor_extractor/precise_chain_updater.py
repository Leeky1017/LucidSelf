"""LogicChain Factor Refs 精确补全工具

策略：
1. 从精校文档提取 snippet_id → factor_trigger 映射
2. 加载已认证因子ID白名单
3. 通过LogicChain节点的snippet_ids反查因子
4. 只添加白名单中存在的因子ID
"""

import re
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Set, Tuple

import yaml


@dataclass
class PreciseUpdateResult:
    """精确更新结果"""
    file_path: str
    total_nodes: int = 0
    nodes_updated: int = 0
    nodes_already_have: int = 0
    nodes_no_match: int = 0
    factor_refs_added: int = 0
    errors: List[str] = field(default_factory=list)


class PreciseChainUpdater:
    """LogicChain因子引用精确更新器
    
    基于精校文档中的factor_trigger标记进行精确匹配。
    """
    
    # 书籍ID到精校目录的映射
    BOOK_TO_DOCS = {
        "滴天髓": "典籍/中文典籍/滴天髓/编辑",
        "子平真诠": "典籍/中文典籍/子平真诠/编辑",
        "三命通会": "典籍/中文典籍/三命通会/编辑",
        "渊海子平": "典籍/中文典籍/渊海子平/编辑",
        "穷通宝鉴": "典籍/中文典籍/穷通宝鉴/编辑",
        "紫微斗数全书": "典籍/中文典籍/紫微斗数全书/编辑",
        "周易": "典籍/中文典籍/周易/编辑",
        "周公解梦": "典籍/中文典籍/周公解梦/编辑",
        "梦林玄解": "典籍/中文典籍/梦林玄解/编辑",
    }
    
    # 英文书籍映射 (book_id -> 实际目录路径)
    ENGLISH_BOOK_TO_DOCS = {
        "the_inner_sky": "典籍/texts/The Inner Sky",
        "planets_in_transit": "典籍/texts/Planets in Transit",
        "78_degrees_of_wisdom": "典籍/texts/78 Degrees of Wisdom",
        "christian_astrology,_vol._1_and_2": "典籍/texts/Christian Astrology, vol. 1 and 2",
        "learning_the_tarot": "典籍/texts/Learning the Tarot",
        "the_book_of_thoth": "典籍/texts/The book of Thoth",
        "the_interpretation_of_dreams": "典籍/texts/The Interpretation of Dreams",
        "waite_pictorial_key_to_the_tarot": "典籍/texts/Waite Pictorial Key to the Tarot",
        "the_archetypes_and_the_collective_unconscious": "典籍/texts/The Archetypes and the Collective Unconscious",
        "dreams_visions_symbol_dictionary": "典籍/texts/The Dreams & Visions Symbol Dictionary",
        "the_dreams_&_visions_symbol_dictionary": "典籍/texts/The Dreams & Visions Symbol Dictionary",
        "astrology_of_personality": "典籍/texts/astrology of personality",
        "tetrabiblos": "典籍/texts/Tetrabiblos",
        "the_astrological_houses": "典籍/texts/The Astrological Houses",
        "llewellyns_complete_dictionary_of_dreams": "典籍/texts/Llewellyns Complete Dictionary of Dreams",
    }
    
    def __init__(self, workspace_root: Path):
        """初始化更新器
        
        Args:
            workspace_root: 工作区根目录
        """
        self.workspace_root = workspace_root
        self.certified_dir = workspace_root / "data/factor_ontology/certified"
        
        # snippet_id -> [factor_id, ...]
        self.snippet_to_factors: Dict[str, List[str]] = defaultdict(list)
        # 已认证因子ID白名单
        self.certified_factor_ids: Set[str] = set()
        # summary关键词 -> factor_id 映射(备用)
        self.keyword_to_factors: Dict[str, Set[str]] = defaultdict(set)
        
        self._load_certified_factors()
    
    def _load_certified_factors(self):
        """加载已认证因子ID白名单"""
        for yaml_file in self.certified_dir.glob("*_certified.yaml"):
            try:
                with open(yaml_file, encoding="utf-8") as f:
                    data = yaml.safe_load(f)
                
                if not data or "by_category" not in data:
                    continue
                
                for category, factors in data["by_category"].items():
                    for factor in factors:
                        factor_id = factor.get("id", "")
                        display_zh = factor.get("display_zh", "")
                        description_zh = factor.get("description_zh", "")
                        if factor_id:
                            self.certified_factor_ids.add(factor_id)
                            # 建立关键词映射
                            if display_zh:
                                self._build_keyword_map(display_zh, factor_id)
                            # 从描述中也提取关键词
                            if description_zh:
                                self._build_keyword_map(description_zh, factor_id)
                                
            except Exception as e:
                print(f"警告: 加载认证因子失败 {yaml_file}: {e}")
        
        print(f"已加载 {len(self.certified_factor_ids)} 个认证因子ID")
    
    def _build_keyword_map(self, display_zh: str, factor_id: str):
        """建立关键词到因子的映射"""
        # 提取关键词（至少2个字符）
        keywords = re.split(r'[_\s\-/（）()【】]', display_zh)
        for kw in keywords:
            kw = kw.strip()
            if len(kw) >= 2:
                self.keyword_to_factors[kw].add(factor_id)
    
    def _load_doc_factors(self, book_id: str) -> Dict[str, List[str]]:
        """从精校文档加载snippet到factor的映射
        
        Args:
            book_id: 书籍ID
            
        Returns:
            Dict[snippet_id, [factor_id, ...]]
        """
        snippet_factors: Dict[str, List[str]] = defaultdict(list)
        
        # 确定精校文档目录
        book_key = book_id.lower().replace(".yaml", "")
        doc_dir = None
        
        if book_id in self.BOOK_TO_DOCS:
            doc_dir = self.workspace_root / self.BOOK_TO_DOCS[book_id]
        elif book_key in self.ENGLISH_BOOK_TO_DOCS:
            doc_dir = self.workspace_root / self.ENGLISH_BOOK_TO_DOCS[book_key]
        
        if not doc_dir or not doc_dir.exists():
            print(f"  未找到精校文档目录: {book_id}")
            return snippet_factors
        
        # 遍历目录下所有md文件
        for md_file in doc_dir.rglob("*.md"):
            self._extract_snippet_factors(md_file, snippet_factors)
        
        return snippet_factors
    
    def _extract_snippet_factors(self, md_file: Path, snippet_factors: Dict[str, List[str]]):
        """从单个精校文档提取snippet到factor的映射
        
        策略1: 从factor_trigger直接提取简单因子ID
        策略2: 从L1块关联FACTOR块的因子ID
        """
        try:
            content = md_file.read_text(encoding="utf-8")
        except Exception:
            return
        
        # 修复：移除snippet ID中的换行符（部分文档存在格式问题）
        content = re.sub(r'\[ns_([a-z_]+)\n+_', r'[ns_\1_', content, flags=re.IGNORECASE)
        
        # 策略1: 直接匹配简单的factor_trigger (单个因子ID)
        # 格式: `[ns_dts_004]` `[trigger: xxx]` `[factor_trigger: wuxing_bias_pattern]`
        pattern = r'\[ns_([a-z_][a-z_0-9]+)\].*?\[factor_trigger:\s*([a-z_][a-z_0-9]*)\s*\]'
        
        for match in re.finditer(pattern, content, re.IGNORECASE):
            snippet_id = f"ns_{match.group(1)}"
            factor_trigger = match.group(2).strip()
            
            # 验证factor_trigger是否在白名单中
            if factor_trigger in self.certified_factor_ids:
                if factor_trigger not in snippet_factors[snippet_id]:
                    snippet_factors[snippet_id].append(factor_trigger)
        
        # 策略2: 基于L1块关联FACTOR块
        # 找到所有L1块和对应的FACTOR块，建立snippet到因子的关联
        self._extract_l1_block_factors(content, snippet_factors)
    
    def _extract_l1_block_factors(self, content: str, snippet_factors: Dict[str, List[str]]):
        """从L1块关联到FACTOR块的因子
        
        将L1块中的snippet关联到相邻FACTOR块中的因子ID
        """
        # 提取所有snippet_id
        snippet_pattern = r'\[ns_([a-z_]+\d+)\]'
        all_snippets = [f"ns_{m.group(1)}" for m in re.finditer(snippet_pattern, content, re.IGNORECASE)]
        
        # 提取FACTOR块中的所有因子ID
        factor_ids_in_doc = set()
        factor_block_pattern = r'<!-- FACTOR_BEGIN -->(.*?)<!-- FACTOR_END -->'
        for block_match in re.finditer(factor_block_pattern, content, re.DOTALL):
            block = block_match.group(1)
            # 从表格中提取因子ID (第3列)
            row_pattern = r'\|\s*[^|]+\s*\|\s*[^|]+\s*\|\s*([a-z_][a-z_0-9]+)\s*\|'
            for row_match in re.finditer(row_pattern, block, re.IGNORECASE):
                factor_id = row_match.group(1).strip()
                if factor_id in self.certified_factor_ids:
                    factor_ids_in_doc.add(factor_id)
        
        # 将文档级因子关联到所有snippet (作为备选)
        # 这是一种宽松策略，因为同一文档的snippet通常共享相关因子
        if factor_ids_in_doc and all_snippets:
            for snippet_id in all_snippets:
                for factor_id in factor_ids_in_doc:
                    if factor_id not in snippet_factors[snippet_id]:
                        snippet_factors[snippet_id].append(factor_id)
    
    def update_chain(self, chain_file: Path) -> PreciseUpdateResult:
        """更新单个LogicChain文件
        
        Args:
            chain_file: LogicChain文件路径
            
        Returns:
            PreciseUpdateResult: 更新结果
        """
        result = PreciseUpdateResult(file_path=str(chain_file.name))
        
        try:
            with open(chain_file, encoding="utf-8") as f:
                chain = yaml.safe_load(f)
        except Exception as e:
            result.errors.append(f"读取文件失败: {e}")
            return result
        
        if not chain or "nodes" not in chain:
            return result
        
        book_id = chain.get("book_id", chain_file.stem)
        print(f"\n处理: {book_id}")
        
        # 加载该书的snippet到factor映射
        snippet_factors = self._load_doc_factors(book_id)
        print(f"  提取到 {len(snippet_factors)} 个snippet-factor映射")
        
        nodes = chain["nodes"]
        result.total_nodes = len(nodes)
        modified = False
        
        for node in nodes:
            if not isinstance(node, dict):
                continue
            
            # 如果已有factor_refs，跳过
            if node.get("factor_refs"):
                result.nodes_already_have += 1
                continue
            
            # 从snippet_ids反查factor
            snippet_ids = node.get("snippet_ids", [])
            factor_refs = set()
            
            for sid in snippet_ids:
                if sid in snippet_factors:
                    for fid in snippet_factors[sid]:
                        factor_refs.add(fid)
            
            # 如果snippet没找到因子，尝试从summary关键词匹配
            if not factor_refs:
                summary = node.get("summary", "")
                factor_refs = self._match_by_summary(summary, book_id)
            
            if factor_refs:
                node["factor_refs"] = sorted(list(factor_refs))[:10]  # 最多10个
                result.nodes_updated += 1
                result.factor_refs_added += len(node["factor_refs"])
                modified = True
            else:
                result.nodes_no_match += 1
        
        # 保存更新后的文件
        if modified:
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
    
    def _match_by_summary(self, summary: str, book_id: str) -> Set[str]:
        """通过summary关键词匹配因子（备用方案）
        
        只匹配完全精确的关键词，宁缺勿滥。
        """
        matched = set()
        
        # 体系特定的核心因子映射
        system_core_factors = self._get_system_core_factors(book_id)
        
        for keyword, factor_ids in self.keyword_to_factors.items():
            # 只匹配长度>=3的关键词，且必须是完整词
            if len(keyword) >= 3 and keyword in summary:
                for fid in factor_ids:
                    # 优先同体系因子
                    if self._is_same_system(fid, book_id):
                        matched.add(fid)
                        break
        
        # 添加体系核心因子（如果summary包含关键词）
        for keyword, factor_id in system_core_factors.items():
            if keyword in summary and factor_id in self.certified_factor_ids:
                matched.add(factor_id)
        
        return matched
    
    def _get_system_core_factors(self, book_id: str) -> Dict[str, str]:
        """获取体系核心因子映射"""
        book_lower = book_id.lower()
        
        # 八字核心因子
        if any(k in book_lower for k in ["滴天髓", "子平", "三命", "穷通", "渊海"]):
            return {
                "日主": "day_master",
                "日干": "day_master",
                "格局": "geju_pattern",
                "用神": "yongshen",
                "月令": "month_order",
                "官": "guanxing",
                "印": "yinxing",
                "财": "caixing",
                "伤官": "shangguan",
                "食神": "shishen",
                "比劫": "bijie",
                "阴阳": "yinyang_polarity",
                "五行": "wuxing",
                "旺衰": "wangshuai",
                "冲": "chong",
                "合": "he",
                "刑": "xing",
                "大运": "dayun",
                "流年": "liunian",
            }
        
        # 紫微核心因子
        if any(k in book_lower for k in ["紫微"]):
            return {
                "紫微": "star_ziwei",
                "天府": "star_tianfu",
                "命宫": "palace_ming",
                "四化": "sihua",
                "庙": "star_state_miao",
                "旺": "star_state_wang",
                "陷": "star_state_xian",
            }
        
        # 占星核心因子
        if any(k in book_lower for k in ["astro", "inner_sky", "planet", "christian"]):
            return {
                "Sun": "planet_sun",
                "Moon": "planet_moon",
                "Mercury": "planet_mercury",
                "Venus": "planet_venus",
                "Mars": "planet_mars",
                "Jupiter": "planet_jupiter",
                "Saturn": "planet_saturn",
                "House": "house",
                "Aspect": "aspect",
                "Sign": "sign",
            }
        
        # 梦境核心因子
        if any(k in book_lower for k in ["dream", "梦", "周公"]):
            return {
                "梦象": "dream_symbol",
                "符号": "dream_symbol",
                "情绪": "dream_emotion",
                "场景": "dream_scene",
            }
        
        # 塔罗核心因子
        if any(k in book_lower for k in ["tarot", "thoth", "arcana"]):
            return {
                "Major": "major_arcana",
                "Minor": "minor_arcana",
                "Wand": "suit_wands",
                "Cup": "suit_cups",
                "Sword": "suit_swords",
                "Pentacle": "suit_pentacles",
            }
        
        return {}
    
    def _is_same_system(self, factor_id: str, book_id: str) -> bool:
        """检查因子是否属于同一体系"""
        book_lower = book_id.lower()
        fid_lower = factor_id.lower()
        
        if any(k in book_lower for k in ["滴天髓", "子平", "三命", "穷通", "渊海"]):
            return "bazi" in fid_lower or not any(s in fid_lower for s in ["astro", "dream", "tarot", "ziwei"])
        if "紫微" in book_lower:
            return "ziwei" in fid_lower or "star" in fid_lower or "palace" in fid_lower
        if any(k in book_lower for k in ["astro", "inner_sky", "planet"]):
            return "astro" in fid_lower or "planet" in fid_lower or "house" in fid_lower
        if any(k in book_lower for k in ["dream", "梦"]):
            return "dream" in fid_lower
        if any(k in book_lower for k in ["tarot", "thoth"]):
            return "tarot" in fid_lower or "arcana" in fid_lower
        
        return True
    
    def update_all(self, chains_dir: Path, priority_files: List[str] = None) -> List[PreciseUpdateResult]:
        """更新所有LogicChain文件
        
        Args:
            chains_dir: LogicChain目录
            priority_files: 优先处理的文件列表
            
        Returns:
            List[PreciseUpdateResult]: 更新结果列表
        """
        results = []
        
        # 获取所有需要处理的文件
        all_files = list(chains_dir.glob("*.yaml"))
        files_to_process = []
        
        # 排除特殊文件
        for f in all_files:
            if any(x in f.name for x in ["quality", "failed", "archive", ".bak"]):
                continue
            files_to_process.append(f)
        
        # 按优先级排序
        if priority_files:
            def sort_key(f):
                for i, pf in enumerate(priority_files):
                    if pf in f.name:
                        return i
                return len(priority_files)
            files_to_process.sort(key=sort_key)
        
        for chain_file in files_to_process:
            result = self.update_chain(chain_file)
            results.append(result)
            
            # 打印进度
            print(f"  结果: 总{result.total_nodes}节点, "
                  f"已有{result.nodes_already_have}, "
                  f"更新{result.nodes_updated}, "
                  f"无匹配{result.nodes_no_match}")
        
        return results


def main():
    """主函数"""
    workspace = Path("/home/leeky/work/LucidSelf")
    chains_dir = workspace / "data/logic_chains"
    
    # P1优先文件
    priority_files = [
        "滴天髓.yaml",
        "子平真诠.yaml",
        "三命通会.yaml",
        "紫微斗数全书.yaml",
        "周易.yaml",
        "planets_in_transit.yaml",
        "the_inner_sky.yaml",
    ]
    
    updater = PreciseChainUpdater(workspace)
    results = updater.update_all(chains_dir, priority_files)
    
    # 汇总统计
    print("\n" + "="*60)
    print("补全完成统计:")
    print("="*60)
    
    total_nodes = 0
    total_updated = 0
    total_already = 0
    total_no_match = 0
    total_refs_added = 0
    
    for r in results:
        total_nodes += r.total_nodes
        total_updated += r.nodes_updated
        total_already += r.nodes_already_have
        total_no_match += r.nodes_no_match
        total_refs_added += r.factor_refs_added
    
    print(f"总节点数: {total_nodes}")
    print(f"已有factor_refs: {total_already}")
    print(f"本次更新: {total_updated}")
    print(f"无法匹配: {total_no_match}")
    print(f"新增因子引用: {total_refs_added}")
    
    if total_nodes > 0:
        coverage = (total_already + total_updated) / total_nodes * 100
        print(f"最终覆盖率: {coverage:.1f}%")


if __name__ == "__main__":
    main()
