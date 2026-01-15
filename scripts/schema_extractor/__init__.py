"""
Schema Extractor - 从精校Markdown提取结构化数据

功能：
1. 从L1/L2/L2.5精校内容提取ConfigFactor、NarrativeSnippet等Schema
2. 通过Pydantic验证输出
3. 生成YAML文件供下游使用

使用方式：
    python -m schema_extractor extract <markdown_path>
    python -m schema_extractor batch <directory>
    python -m schema_extractor validate <yaml_directory>
"""

__version__ = "1.0.0"
