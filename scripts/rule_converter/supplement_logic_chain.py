#!/usr/bin/env python3
"""
为未被引用的 snippet 创建 LogicChain 节点

这些 snippet 有 factor_trigger 但未被任何 LogicChain 节点引用，
需要创建新的节点将它们纳入规则转换流程。
"""

import re
import yaml
from pathlib import Path
from datetime import datetime


def parse_factor_trigger(factor_trigger: str) -> list[str]:
    """解析 factor_trigger 字符串，提取因子ID"""
    if not factor_trigger:
        return []
    
    parts = re.split(r'\s+(?:AND|OR|and|or)\s+', factor_trigger)
    factors = []
    for p in parts:
        p = p.strip()
        if p and p.upper() not in ['AND', 'OR']:
            factors.append(p)
    return factors


def create_node_from_snippet(snippet, existing_node_ids: set) -> dict:
    """从 snippet 创建 LogicChain 节点"""
    # 生成唯一的 node_id
    base_id = f"n_smth_supp_{snippet.snippet_id.replace('ns_smth_01_', '')}"
    node_id = base_id
    counter = 1
    while node_id in existing_node_ids:
        node_id = f"{base_id}_{counter}"
        counter += 1
    
    existing_node_ids.add(node_id)
    
    # 解析 factor_refs
    factor_refs = parse_factor_trigger(snippet.factor_trigger)
    
    # 构建节点
    node = {
        "node_id": node_id,
        "role": snippet.role or "主干",
        "snippet_ids": [snippet.snippet_id],
        "factor_refs": factor_refs,
        "condition": snippet.trigger,
        "conclusion": snippet.content[:200] if snippet.content else "",
        "source_ref": snippet.source_ref,
    }
    
    return node


def supplement_三命通会(store, loader):
    """补充三命通会的 LogicChain"""
    # 收集已引用的 snippet_ids
    all_referenced = set()
    for chain in loader:
        for node in chain.nodes:
            if node.snippet_ids:
                all_referenced.update(node.snippet_ids)
    
    # 找出未引用的 ns_smth_01_xxx
    unreferenced = []
    for sid in store._snippets.keys():
        if sid.startswith('ns_smth_01_') and sid not in all_referenced:
            unreferenced.append(store.get(sid))
    
    if not unreferenced:
        print("  三命通会: 无需补充")
        return 0
    
    print(f"  三命通会: 需补充 {len(unreferenced)} 个 snippet")
    
    # 加载现有 YAML
    yaml_path = Path("data/logic_chains/三命通会.yaml")
    if not yaml_path.exists():
        print(f"  错误: {yaml_path} 不存在")
        return 0
    
    with open(yaml_path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    
    # 收集现有 node_ids
    existing_node_ids = set()
    for node in data.get('nodes', []):
        existing_node_ids.add(node.get('node_id'))
    
    # 创建新节点
    new_nodes = []
    for snippet in unreferenced:
        node = create_node_from_snippet(snippet, existing_node_ids)
        new_nodes.append(node)
    
    # 备份并写入
    backup_path = yaml_path.with_suffix(f'.{datetime.now().strftime("%Y%m%d_%H%M%S")}.bak')
    yaml_path.rename(backup_path)
    
    data['nodes'].extend(new_nodes)
    
    with open(yaml_path, 'w', encoding='utf-8') as f:
        yaml.dump(data, f, allow_unicode=True, default_flow_style=False, sort_keys=False)
    
    print(f"  ✅ 添加了 {len(new_nodes)} 个新节点")
    return len(new_nodes)


def supplement_jung(store, loader):
    """补充 The Collected Works 的 LogicChain"""
    # 收集已引用的 snippet_ids
    all_referenced = set()
    for chain in loader:
        for node in chain.nodes:
            if node.snippet_ids:
                all_referenced.update(node.snippet_ids)
    
    # 找出未引用的 ns_jung_xxx
    unreferenced = []
    for sid in store._snippets.keys():
        if sid.startswith('ns_jung_') and sid not in all_referenced:
            unreferenced.append(store.get(sid))
    
    if not unreferenced:
        print("  Jung Collected Works: 无需补充")
        return 0
    
    print(f"  Jung Collected Works: 需补充 {len(unreferenced)} 个 snippet")
    
    # 检查是否有现有的 LogicChain 文件
    yaml_path = Path("data/logic_chains/the_collected_works.yaml")
    
    if yaml_path.exists():
        with open(yaml_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        existing_node_ids = set(node.get('node_id') for node in data.get('nodes', []))
    else:
        # 创建新文件
        data = {
            "chain_id": "chain_the_collected_works",
            "book_id": "the_collected_works",
            "system": "psych",
            "nodes": [],
            "edges": [],
        }
        existing_node_ids = set()
    
    # 创建新节点
    new_nodes = []
    for snippet in unreferenced:
        # 生成 node_id
        base_id = f"n_jung_{snippet.snippet_id.replace('ns_jung_', '')}"
        node_id = base_id
        counter = 1
        while node_id in existing_node_ids:
            node_id = f"{base_id}_{counter}"
            counter += 1
        existing_node_ids.add(node_id)
        
        factor_refs = parse_factor_trigger(snippet.factor_trigger)
        
        node = {
            "node_id": node_id,
            "role": snippet.role or "主干",
            "snippet_ids": [snippet.snippet_id],
            "factor_refs": factor_refs,
            "condition": snippet.trigger,
            "conclusion": snippet.content[:200] if snippet.content else "",
            "source_ref": snippet.source_ref,
        }
        new_nodes.append(node)
    
    # 备份（如果存在）并写入
    if yaml_path.exists():
        backup_path = yaml_path.with_suffix(f'.{datetime.now().strftime("%Y%m%d_%H%M%S")}.bak')
        yaml_path.rename(backup_path)
    
    data['nodes'].extend(new_nodes)
    
    with open(yaml_path, 'w', encoding='utf-8') as f:
        yaml.dump(data, f, allow_unicode=True, default_flow_style=False, sort_keys=False)
    
    print(f"  ✅ 添加了 {len(new_nodes)} 个新节点")
    return len(new_nodes)


def main():
    from scripts.rule_converter.loaders.logic_chain_loader import LogicChainLoader
    from scripts.rule_converter.loaders.snippet_store import SnippetStore
    
    print("=" * 60)
    print("补充 LogicChain 节点（覆盖未引用的 snippet）")
    print("=" * 60)
    print()
    
    # 加载数据
    print("加载 SnippetStore...")
    store = SnippetStore(lazy_load=False)
    store.load_from_dir()
    
    print("加载 LogicChainLoader...")
    loader = LogicChainLoader()
    loader.load_all()
    
    print()
    print("执行补充:")
    
    total_added = 0
    total_added += supplement_三命通会(store, loader)
    total_added += supplement_jung(store, loader)
    
    print()
    print("=" * 60)
    print(f"完成: 共添加 {total_added} 个新节点")
    print("=" * 60)


if __name__ == "__main__":
    main()
