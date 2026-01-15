"""
Pytest配置和共享fixtures

优化hypothesis测试速度
"""

from hypothesis import settings, Verbosity

# 全局配置hypothesis：限制测试用例数量以加快测试速度
settings.register_profile(
    "fast",
    max_examples=10,
    deadline=None,
)
settings.register_profile(
    "ci",
    max_examples=50,
    deadline=None,
)
settings.register_profile(
    "full",
    max_examples=100,
    deadline=None,
)

# 默认使用fast profile
settings.load_profile("fast")
