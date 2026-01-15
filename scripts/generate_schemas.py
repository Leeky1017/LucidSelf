#!/usr/bin/env python3
"""
生成 JSON Schema 文件和因子字典
Task 3.1 + 3.2 + 3.3: 为 InferenceResult 生成 JSON Schema，并创建最小因子字典
"""

import json
import sys
from pathlib import Path
from typing import Dict, Any, Set

# 添加 backend 到路径以便导入模型
sys.path.insert(0, str(Path(__file__).parent.parent / 'backend'))

from models.semantic import InferenceResult, InferenceConclusion, InferenceEvidence
from models.bazi import BaziFactors, BaziChart, PillarModel
from models.pattern import GePatternFactors
from models.yongshen import YongShenFactors
from models.yunshi import YunShiFactors


def generate_inference_result_schema() -> Dict[str, Any]:
    """生成 InferenceResult 的 JSON Schema"""
    try:
        # Pydantic v2
        schema = InferenceResult.model_json_schema()
    except AttributeError:
        # Pydantic v1
        schema = InferenceResult.schema()
    
    # 添加元数据
    schema['$schema'] = 'http://json-schema.org/draft-07/schema#'
    schema['title'] = 'LucidSelf Inference Result Schema'
    schema['description'] = 'JSON Schema for inference result returned by /api/inference endpoints'
    
    return schema


def extract_fields_from_model(model_class, prefix='') -> Dict[str, Dict[str, Any]]:
    """从 Pydantic 模型中提取字段信息"""
    fields = {}
    
    try:
        # Pydantic v2
        model_fields = model_class.model_fields
    except AttributeError:
        # Pydantic v1
        model_fields = model_class.__fields__
    
    for field_name, field_info in model_fields.items():
        full_name = f"{prefix}{field_name}" if prefix else field_name
        
        # 获取字段类型
        try:
            # Pydantic v2
            field_type = field_info.annotation
        except AttributeError:
            # Pydantic v1
            field_type = field_info.outer_type_
        
        type_str = str(field_type)
        
        # 简化类型表示
        if 'int' in type_str:
            simple_type = 'integer'
        elif 'float' in type_str:
            simple_type = 'number'
        elif 'str' in type_str:
            simple_type = 'string'
        elif 'bool' in type_str:
            simple_type = 'boolean'
        elif 'List' in type_str or 'list' in type_str:
            simple_type = 'array'
        elif 'Dict' in type_str or 'dict' in type_str:
            simple_type = 'object'
        else:
            simple_type = 'any'
        
        # 获取描述
        try:
            description = field_info.description
        except AttributeError:
            try:
                description = field_info.field_info.description
            except AttributeError:
                description = None
        
        fields[full_name] = {
            'type': simple_type,
            'source_model': model_class.__name__,
            'description': description or f'Field {field_name} from {model_class.__name__}'
        }
    
    return fields


def generate_factors_dictionary() -> Dict[str, Any]:
    """生成最小因子字典"""
    
    dictionary = {
        '$schema': 'http://json-schema.org/draft-07/schema#',
        'title': 'LucidSelf Factors Dictionary',
        'description': '最小因子字典，覆盖当前已实现的因子字段（BaziFactors + GePattern + YongShen + YunShi）',
        'version': '0.1.0',
        'generated_at': None,  # 将在保存时填充
        'factors': {}
    }
    
    # 收集所有因子字段
    all_fields = {}
    
    # 1. BaziFactors 基础字段
    bazi_fields = extract_fields_from_model(BaziFactors)
    all_fields.update(bazi_fields)
    
    # 2. GePatternFactors（通过 ge. 前缀访问）
    ge_fields = extract_fields_from_model(GePatternFactors, prefix='ge.')
    all_fields.update(ge_fields)
    
    # 3. YongShenFactors（通过 use_god. 前缀访问）
    use_god_fields = extract_fields_from_model(YongShenFactors, prefix='use_god.')
    all_fields.update(use_god_fields)
    
    # 4. YunShiFactors（通过 yun. 或直接访问）
    yun_fields = extract_fields_from_model(YunShiFactors, prefix='yun.')
    all_fields.update(yun_fields)
    
    # 5. 添加常用扁平访问字段（来自规则扫描）
    manual_flat_fields = {
        'day_master.stem': {
            'type': 'string',
            'source_model': 'BaziFactors',
            'description': '日主天干（嵌套访问 day_master 对象的 stem 属性）'
        },
        'day_master.strength': {
            'type': 'number',
            'source_model': 'BaziFactors',
            'description': '日主强度（嵌套访问）'
        },
        'fire_presence': {
            'type': 'boolean',
            'source_model': 'BaziFactors',
            'description': '火元素存在标记（对应 fire_present 字段）'
        },
        'metal_presence': {
            'type': 'number',
            'source_model': 'BaziFactors',
            'description': '金元素强度'
        },
        'water_presence': {
            'type': 'number',
            'source_model': 'BaziFactors',
            'description': '水元素强度'
        },
        'wealth_star.presence': {
            'type': 'boolean',
            'source_model': 'BaziFactors',
            'description': '财星存在（从 ten_gods_counts 推导）'
        },
        'season': {
            'type': 'string',
            'source_model': 'BaziFactors',
            'description': '季节（对应 birth_season）'
        },
        'current_age': {
            'type': 'integer',
            'source_model': 'YunShiFactors',
            'description': '当前年龄（通过 yun.current_age 访问）'
        },
        'static.use_god_resolved': {
            'type': 'boolean',
            'source_model': 'YongShenFactors',
            'description': '用神已确定标记（通过 static.use_god_resolved 或 use_god.identified 访问）'
        },
        'static.month_has_usable_yongshen': {
            'type': 'boolean',
            'source_model': 'YongShenFactors',
            'description': '月有可用用神（通过 static 或 use_god.month_has_usable 访问）'
        },
    }
    all_fields.update(manual_flat_fields)
    
    dictionary['factors'] = all_fields
    dictionary['total_fields'] = len(all_fields)
    
    return dictionary


def main():
    print("=== Generating Schemas ===\n")
    
    # 1. 生成 InferenceResult JSON Schema
    print("1. Generating InferenceResult JSON Schema...")
    inference_schema = generate_inference_result_schema()
    
    inference_schema_path = Path('/home/leeky/work/LucidSelf/backend/schemas/inference_result.schema.json')
    inference_schema_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(inference_schema_path, 'w', encoding='utf-8') as f:
        json.dump(inference_schema, f, indent=2, ensure_ascii=False)
    
    print(f"   ✓ Saved to: {inference_schema_path}")
    print(f"   Fields: {len(inference_schema.get('properties', {}))} top-level properties\n")
    
    # 2. 生成因子字典
    print("2. Generating Factors Dictionary...")
    factors_dict = generate_factors_dictionary()
    
    # 添加生成时间
    from datetime import datetime
    factors_dict['generated_at'] = datetime.utcnow().isoformat() + 'Z'
    
    factors_dict_path = Path('/home/leeky/work/LucidSelf/backend/schemas/factors.dictionary.json')
    factors_dict_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(factors_dict_path, 'w', encoding='utf-8') as f:
        json.dump(factors_dict, f, indent=2, ensure_ascii=False)
    
    print(f"   ✓ Saved to: {factors_dict_path}")
    print(f"   Total fields: {factors_dict['total_fields']}\n")
    
    # 3. 按来源分类统计
    print("3. Factors by Source Model:")
    by_model = {}
    for field_name, field_info in factors_dict['factors'].items():
        model = field_info['source_model']
        if model not in by_model:
            by_model[model] = []
        by_model[model].append(field_name)
    
    for model, fields in sorted(by_model.items()):
        print(f"   - {model}: {len(fields)} fields")
    
    print("\n=== Schema Generation Complete ===")


if __name__ == '__main__':
    main()
