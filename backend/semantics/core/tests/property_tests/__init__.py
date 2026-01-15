"""
Property Tests for Semantic Core

使用 Hypothesis 进行属性测试，验证核心组件的不变性。

测试清单:
- Property 1: SemanticEntry Field Validation
- Property 2: Factor ID Format Validation
- Property 5: Registration Uniqueness
- Property 6: Query Consistency (by_book)
- Property 7: Query Consistency (by_factor)
- Property 8: Factor Query Mode 'all'
- Property 9: Factor Query Mode 'any'
- Property 10: Cache L1 Hit After Set
- Property 11: Cache Invalidation
- Property 12: Index Persistence Round-Trip
- Property 13: Snippet Parsing
- Property 14: Factor Trigger Handling
- Property 15: Parse-Print Round-Trip
- Property 19: to_factor_refs Completeness
"""
