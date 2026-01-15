#!/usr/bin/env python3
"""
补充 LogicChain 节点的 factor_refs

从节点关联的 snippet.factor_trigger 中推导因子，
添加到节点的 factor_refs 字段。
"""

import re
import yaml
from pathlib import Path
from datetime import datetime


def parse_factor_trigger(factor_trigger: str) -> list[str]:
    """解析 factor_trigger 字符串，提取因子ID"""
    if not factor_trigger:
        return []
    
    # 分割 AND/OR
    parts = re.split(r'\s+(?:AND|OR|and|or)\s+', factor_trigger)
    factors = []
    for p in parts:
        p = p.strip()
        if p and p.upper() not in ['AND', 'OR']:
            factors.append(p)
    return factors


def load_snippet_factors(store) -> dict:
    """加载所有 snippet 的 factor_trigger"""
    snippet_factors = {}
    for sid, snippet in store._snippets.items():
        if snippet.factor_trigger:
            snippet_factors[sid] = parse_factor_trigger(snippet.factor_trigger)
    return snippet_factors


def find_nodes_to_update(loader, snippet_factors: dict) -> dict:
    """找出需要更新的节点"""
    updates = {}  # {yaml_path: {node_id: [factors]}}
    
    # 构建文件名映射
    lc_dir = Path("data/logic_chains")
    file_map = {}
    for f in lc_dir.glob("*.yaml"):
        if ".bak" in f.name or ".failed" in f.name:
            continue
        # 去掉 .yaml 后缀作为 key
        key = f.stem.lower()
        file_map[key] = f
    
    # chain_id 到文件名的显式映射（处理缩写）
    chain_to_file = {
        "7dow": "78_degrees_of_wisdom",
        "taatcu": "the_archetypes_and_the_collective_unconscious",
        "wpkttt": "waite_pictorial_key_to_the_tarot",
        "tiod": "the_interpretation_of_dreams",
        "tbot": "the_book_of_thoth",
        "cav1a2": "christian_astrology,_vol._1_and_2",
        "tis": "the_inner_sky",
        "pit": "planets_in_transit",
        "aop": "astrology_of_personality",
        "ltt": "learning_the_tarot",
        "t": "tetrabiblos",
        "tah": "the_astrological_houses",
        "lcdod": "llewellyns_complete_dictionary_of_dreams",
        "三命通": "三命通会",
        "紫微斗": "紫微斗数全书",
        "渊海子": "渊海子平",
        "穷通宝": "穷通宝鉴",
        "子平真": "子平真诠",
        "周公解": "周公解梦",
    }
    
    for chain in loader:
        # 尝试多种方式匹配文件
        chain_name = chain.chain_id.replace('chain_', '')
        yaml_path = None
        
        # 1. 显式映射
        if chain_name.lower() in chain_to_file:
            mapped_name = chain_to_file[chain_name.lower()]
            if mapped_name.lower() in file_map:
                yaml_path = file_map[mapped_name.lower()]
        
        # 2. 直接匹配
        if not yaml_path and chain_name.lower() in file_map:
            yaml_path = file_map[chain_name.lower()]
        
        # 3. 部分匹配
        if not yaml_path:
            for key, path in file_map.items():
                if chain_name.lower() in key or key in chain_name.lower():
                    yaml_path = path
                    break
        
        if not yaml_path:
            continue
        
        for node in chain.nodes:
            if not node.factor_refs and node.snippet_ids:
                factors = set()
                for sid in node.snippet_ids:
                    if sid in snippet_factors:
                        factors.update(snippet_factors[sid])
                
                if factors:
                    if str(yaml_path) not in updates:
                        updates[str(yaml_path)] = {}
                    updates[str(yaml_path)][node.node_id] = list(factors)
    
    return updates


def update_yaml_file(yaml_path: Path, node_updates: dict) -> int:
    """更新单个 YAML 文件"""
    if not yaml_path.exists():
        print(f"  文件不存在: {yaml_path}")
        return 0
    
    with open(yaml_path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    
    if not data or 'nodes' not in data:
        print(f"  无效的 YAML 结构: {yaml_path}")
        return 0
    
    updated = 0
    for node in data['nodes']:
        node_id = node.get('node_id')
        if node_id in node_updates:
            # 合并现有 factor_refs 和新推导的
            existing = node.get('factor_refs', []) or []
            new_factors = node_updates[node_id]
            merged = list(set(existing + new_factors))
            node['factor_refs'] = merged
            updated += 1
    
    if updated > 0:
        # 备份原文件
        backup_path = yaml_path.with_suffix(f'.{datetime.now().strftime("%Y%m%d_%H%M%S")}.bak')
        yaml_path.rename(backup_path)
        
        # 写入更新后的内容
        with open(yaml_path, 'w', encoding='utf-8') as f:
            yaml.dump(data, f, allow_unicode=True, default_flow_style=False, sort_keys=False)
        
        print(f"  ✅ {yaml_path.name}: 更新 {updated} 个节点")
    
    return updated


def main():
    from scripts.rule_converter.loaders.logic_chain_loader import LogicChainLoader
    from scripts.rule_converter.loaders.snippet_store import SnippetStore
    
    print("=" * 60)
    print("补充 LogicChain 节点的 factor_refs")
    print("=" * 60)
    print()
    
    # 加载数据
    print("加载 SnippetStore...")
    store = SnippetStore(lazy_load=False)
    store.load_from_dir()
    
    print("加载 LogicChainLoader...")
    loader = LogicChainLoader()
    loader.load_all()
    
    # 解析 snippet 的 factor_trigger
    print("解析 snippet.factor_trigger...")
    snippet_factors = load_snippet_factors(store)
    print(f"  找到 {len(snippet_factors)} 个有 factor_trigger 的 snippet")
    
    # 找出需要更新的节点
    print("分析需要更新的节点...")
    updates = find_nodes_to_update(loader, snippet_factors)
    
    total_nodes = sum(len(nodes) for nodes in updates.values())
    print(f"  需要更新 {len(updates)} 个文件, {total_nodes} 个节点")
    print()
    
    # 执行更新
    print("执行更新...")
    total_updated = 0
    for yaml_path_str, node_updates in updates.items():
        yaml_path = Path(yaml_path_str)
        total_updated += update_yaml_file(yaml_path, node_updates)
    
    print()
    print("=" * 60)
    print(f"完成: 更新了 {total_updated} 个节点")
    print("=" * 60)


if __name__ == "__main__":
    main()
