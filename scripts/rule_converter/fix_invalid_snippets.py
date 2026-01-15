#!/usr/bin/env python3
"""
修复无效 snippet 问题

问题1: Learning the Tarot 49 个 snippet 缺少 → source_ref
问题2: The Inner Sky 1 个 snippet 格式错误
问题3: 三命通会 LogicChain 15 个 snippet_id 命名不一致
"""

import re
from pathlib import Path


def fix_learning_tarot():
    """修复 Learning the Tarot 缺少 source_ref 的问题"""
    file_path = Path("典籍/texts/Learning the Tarot/编辑/Tarot_Practice_Method_v2.1.md")
    
    if not file_path.exists():
        print(f"文件不存在: {file_path}")
        return 0
    
    content = file_path.read_text(encoding="utf-8")
    
    # 匹配没有 → 的 snippet 行
    # 格式: - `[ns_ltt_xxx]` `[trigger: xxx]` `[factor_trigger: xxx]` `[role: xxx]` content
    pattern = re.compile(
        r'(- `\[ns_ltt_\d+\]` `\[trigger: [^\]]+\]` `\[factor_trigger: [^\]]+\]` `\[role: [^\]]+\]` )([^→\n]+)$',
        re.MULTILINE
    )
    
    def add_source_ref(match):
        prefix = match.group(1)
        content_text = match.group(2).strip()
        return f"{prefix}{content_text} → Learning the Tarot"
    
    new_content, count = pattern.subn(add_source_ref, content)
    
    if count > 0:
        file_path.write_text(new_content, encoding="utf-8")
        print(f"✅ Learning the Tarot: 修复了 {count} 个缺少 source_ref 的 snippet")
    else:
        print("⚠️ Learning the Tarot: 没有找到需要修复的内容")
    
    return count


def fix_inner_sky():
    """修复 The Inner Sky 格式错误的问题"""
    file_path = Path("典籍/texts/The Inner Sky/编辑/Inner_Sky_Natal_v2.1_Part3.md")
    
    if not file_path.exists():
        print(f"文件不存在: {file_path}")
        return 0
    
    content = file_path.read_text(encoding="utf-8")
    
    # 修复: `[factor_trigger: xxx] [role: xxx]` → `[factor_trigger: xxx]` `[role: xxx]`
    # 即在 ] 和 [role 之间添加 ` `
    pattern = re.compile(r'(\[factor_trigger: [^\]]+\]) (\[role:)')
    
    new_content, count = pattern.subn(r'\1` `\2', content)
    
    if count > 0:
        file_path.write_text(new_content, encoding="utf-8")
        print(f"✅ The Inner Sky: 修复了 {count} 个格式错误的 snippet")
    else:
        print("⚠️ The Inner Sky: 没有找到需要修复的内容")
    
    return count


def fix_sanmingtong_logicchain():
    """修复三命通会 LogicChain 中的 snippet_id 命名不一致"""
    import yaml
    
    file_path = Path("data/logic_chains/三命通会.yaml")
    
    if not file_path.exists():
        print(f"文件不存在: {file_path}")
        return 0
    
    content = file_path.read_text(encoding="utf-8")
    
    # 将 ns_smth_01_xxx 改为 ns_smth_xxx
    # ns_smth_01_001 → ns_smth_001
    # ns_smth_01_086 → ns_smth_086
    pattern = re.compile(r'ns_smth_01_(\d+)')
    
    new_content, count = pattern.subn(r'ns_smth_\1', content)
    
    if count > 0:
        file_path.write_text(new_content, encoding="utf-8")
        print(f"✅ 三命通会 LogicChain: 修复了 {count} 个 snippet_id 命名")
    else:
        print("⚠️ 三命通会 LogicChain: 没有找到需要修复的内容")
    
    return count


def main():
    print("=" * 50)
    print("修复无效 snippet 问题")
    print("=" * 50)
    print()
    
    total = 0
    
    # 1. 修复 Learning the Tarot
    total += fix_learning_tarot()
    
    # 2. 修复 The Inner Sky
    total += fix_inner_sky()
    
    # 3. 修复三命通会 LogicChain
    total += fix_sanmingtong_logicchain()
    
    print()
    print("=" * 50)
    print(f"总共修复: {total} 处")
    print("=" * 50)


if __name__ == "__main__":
    main()
