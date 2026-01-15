#!/usr/bin/env python3
"""
Logic Chain Query Tool - 逻辑链查询验证工具

用于验证逻辑链的实际效果，可以：
1. 按关键词搜索相关节点
2. 查看节点的原文内容
3. 沿边追溯推理路径
4. 展示推理依据
"""

import yaml
from pathlib import Path
from typing import List, Dict, Optional
import sys


class LogicChainQuery:
    def __init__(self, book_id: str):
        self.book_id = book_id
        self.base_dir = Path(__file__).parent.parent / "data"
        
        # 加载逻辑链
        chain_file = self.base_dir / "logic_chains" / f"{book_id}.yaml"
        if not chain_file.exists():
            raise FileNotFoundError(f"逻辑链文件不存在: {chain_file}")
        
        with open(chain_file, 'r', encoding='utf-8') as f:
            self.chain = yaml.safe_load(f)
        
        # 加载 snippets
        snippets_file = self.base_dir / "schema_staging" / "snippets" / f"{book_id}_snippets.yaml"
        if snippets_file.exists():
            with open(snippets_file, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
                self.snippets = {s['snippet_id']: s for s in data.get('snippets', [])}
        else:
            self.snippets = {}
        
        # 建立节点索引
        self.nodes = {n['node_id']: n for n in self.chain.get('nodes', [])}
        
        # 建立边的索引（from_node -> [edges]）
        self.edges_from = {}
        self.edges_to = {}
        for edge in self.chain.get('edges', []):
            fn, tn = edge['from_node'], edge['to_node']
            self.edges_from.setdefault(fn, []).append(edge)
            self.edges_to.setdefault(tn, []).append(edge)
    
    def search_nodes(self, keyword: str, limit: int = 10) -> List[Dict]:
        """按关键词搜索节点"""
        results = []
        for node in self.chain.get('nodes', []):
            # 搜索 summary、source_ref、snippet 内容
            text = node.get('summary', '') + ' ' + node.get('metadata', {}).get('source_ref', '')
            
            # 也搜索 snippet 内容
            for sid in node.get('snippet_ids', []):
                if sid in self.snippets:
                    text += ' ' + self.snippets[sid].get('snippet_text', '')
                    text += ' ' + self.snippets[sid].get('trigger', '')
            
            if keyword.lower() in text.lower():
                results.append(node)
                if len(results) >= limit:
                    break
        
        return results
    
    def get_node_content(self, node_id: str) -> Dict:
        """获取节点的完整内容"""
        node = self.nodes.get(node_id)
        if not node:
            return None
        
        # 获取所有 snippet 内容
        snippets_content = []
        for sid in node.get('snippet_ids', []):
            if sid in self.snippets:
                s = self.snippets[sid]
                snippets_content.append({
                    'id': sid,
                    'trigger': s.get('trigger'),
                    'factor_trigger': s.get('factor_trigger'),
                    'text': s.get('snippet_text'),
                    'source_ref': s.get('source_ref'),
                })
        
        return {
            'node_id': node_id,
            'summary': node.get('summary'),
            'role': node.get('role'),
            'condition': node.get('condition'),
            'source_ref': node.get('metadata', {}).get('source_ref'),
            'snippets': snippets_content,
        }
    
    def trace_reasoning(self, node_id: str, direction: str = 'backward', depth: int = 3) -> List[Dict]:
        """
        追溯推理路径
        direction: 'backward' (向上游追溯依赖) 或 'forward' (向下游追溯推导)
        """
        visited = set()
        path = []
        
        def dfs(nid, d):
            if d <= 0 or nid in visited:
                return
            visited.add(nid)
            
            node = self.nodes.get(nid)
            if not node:
                return
            
            edges = self.edges_to.get(nid, []) if direction == 'backward' else self.edges_from.get(nid, [])
            
            for edge in edges:
                next_nid = edge['from_node'] if direction == 'backward' else edge['to_node']
                next_node = self.nodes.get(next_nid)
                
                if next_node and next_nid not in visited:
                    path.append({
                        'from': edge['from_node'],
                        'to': edge['to_node'],
                        'relation': edge.get('relation'),
                        'condition': edge.get('condition'),
                        'inferred_from': edge.get('metadata', {}).get('inferred_from'),
                        'source_ref': edge.get('metadata', {}).get('source_ref'),
                        'from_summary': self.nodes.get(edge['from_node'], {}).get('summary'),
                        'to_summary': self.nodes.get(edge['to_node'], {}).get('summary'),
                    })
                    dfs(next_nid, d - 1)
        
        dfs(node_id, depth)
        return path
    
    def explain_inference(self, node_id: str) -> str:
        """生成节点的推理解释"""
        node = self.nodes.get(node_id)
        if not node:
            return "节点不存在"
        
        content = self.get_node_content(node_id)
        backward = self.trace_reasoning(node_id, 'backward', 2)
        forward = self.trace_reasoning(node_id, 'forward', 2)
        
        lines = []
        lines.append(f"=" * 60)
        lines.append(f"【节点】{node_id}")
        lines.append(f"【摘要】{content['summary']}")
        lines.append(f"【出处】{content['source_ref']}")
        lines.append(f"【角色】{content['role']}")
        lines.append("")
        
        lines.append("【原文内容】")
        for s in content['snippets'][:3]:  # 只显示前3条
            lines.append(f"  - [{s['trigger']}] {s['text'][:80]}...")
            lines.append(f"    因子: {s['factor_trigger']}")
        
        if backward:
            lines.append("")
            lines.append("【上游依赖（为什么这样判断）】")
            for e in backward[:3]:
                lines.append(f"  ← {e['from_summary']} ({e['inferred_from']})")
                if e['condition']:
                    lines.append(f"     条件: {e['condition']}")
        
        if forward:
            lines.append("")
            lines.append("【下游推导（可以得出什么）】")
            for e in forward[:3]:
                lines.append(f"  → {e['to_summary']} ({e['inferred_from']})")
                if e['condition']:
                    lines.append(f"     条件: {e['condition']}")
        
        lines.append(f"=" * 60)
        return "\n".join(lines)


def demo_query(book_id: str, keyword: str):
    """演示查询"""
    print(f"\n📚 加载逻辑链: {book_id}")
    
    try:
        q = LogicChainQuery(book_id)
    except FileNotFoundError as e:
        print(f"❌ {e}")
        return
    
    print(f"   节点数: {len(q.nodes)}")
    print(f"   边数: {len(q.chain.get('edges', []))}")
    print(f"   Snippets: {len(q.snippets)}")
    
    print(f"\n🔍 搜索关键词: '{keyword}'")
    results = q.search_nodes(keyword, limit=5)
    
    if not results:
        print("   未找到相关节点")
        return
    
    print(f"   找到 {len(results)} 个相关节点\n")
    
    # 展示第一个结果的详细推理
    for i, node in enumerate(results[:2]):
        print(q.explain_inference(node['node_id']))
        print()


if __name__ == "__main__":
    # 示例查询
    examples = [
        ("滴天髓", "月令"),
        ("滴天髓", "用神"),
        ("周公解梦", "龙"),
        ("梦林玄解", "吉凶"),
        ("78_degrees_of_wisdom", "Fool"),
    ]
    
    if len(sys.argv) > 2:
        book_id, keyword = sys.argv[1], sys.argv[2]
        demo_query(book_id, keyword)
    else:
        print("=" * 60)
        print("逻辑链查询验证工具")
        print("=" * 60)
        print("\n用法: python logic_chain_query.py <book_id> <keyword>")
        print("\n示例查询:\n")
        
        # 只演示第一个
        demo_query(examples[0][0], examples[0][1])
