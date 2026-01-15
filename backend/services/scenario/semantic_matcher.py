"""
语义匹配器

基于 embedding 向量的语义相似度匹配。

支持多种 embedding 后端:
1. sentence-transformers (本地，推荐)
2. OpenAI embeddings (远程)
3. 自定义模型

对照文档: docs/ls_roadmap_executable.md §四、场景系统设计

注意: 此模块需要安装额外依赖:
  pip install sentence-transformers numpy
或
  pip install openai numpy
"""

import logging
from typing import Any, Dict, List, Optional, Tuple, TYPE_CHECKING

# 延迟导入 numpy，避免未安装时报错
try:
    import numpy as np
    NUMPY_AVAILABLE = True
except ImportError:
    np = None  # type: ignore
    NUMPY_AVAILABLE = False

from backend.core.contracts.unified_dimensions import LifeDomain

logger = logging.getLogger(__name__)



# 场景语义描述（用于生成 embedding）
DOMAIN_DESCRIPTIONS: Dict[LifeDomain, str] = {
    LifeDomain.CAREER: "职业发展、工作变动、事业规划、升职加薪、跳槽转行、创业、职场关系、行业前景",
    LifeDomain.WEALTH: "财务状况、投资理财、收入支出、财富积累、股票基金、房产、贷款债务、经济规划",
    LifeDomain.RELATIONSHIP: "恋爱感情、婚姻关系、伴侣选择、约会交往、分手复合、相亲配对、情感疗愈",
    LifeDomain.HEALTH: "身体健康、疾病预防、养生保健、运动锻炼、睡眠质量、饮食营养、心理健康",
    LifeDomain.FAMILY: "家庭关系、亲子教育、父母赡养、家族事务、婆媳相处、兄弟姐妹、子女成长",
    LifeDomain.CREATIVITY: "学习提升、考试升学、技能培养、创意灵感、艺术创作、写作设计、知识积累",
    LifeDomain.SPIRITUAL: "精神境界、内心成长、修行冥想、心理调适、情绪管理、人生意义、自我认知",
}


class SemanticMatcher:
    """
    语义匹配器
    
    使用 embedding 向量计算用户问题与场景的语义相似度。
    """
    
    def __init__(
        self,
        model_name: str = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
        use_openai: bool = False,
        cache_embeddings: bool = True,
    ):
        """
        初始化语义匹配器
        
        Args:
            model_name: sentence-transformers 模型名称
            use_openai: 是否使用 OpenAI embeddings
            cache_embeddings: 是否缓存场景 embeddings
        """
        self._model_name = model_name
        self._use_openai = use_openai
        self._cache_embeddings = cache_embeddings
        
        self._model = None
        self._domain_embeddings: Dict[LifeDomain, Any] = {}  # np.ndarray when available
        self._initialized = False
    
    def _ensure_initialized(self) -> bool:
        """确保模型已初始化"""
        if self._initialized:
            return True
        
        # 检查 numpy 是否可用
        if not NUMPY_AVAILABLE:
            logger.warning("numpy not available, semantic matching disabled")
            return False
        
        try:
            if self._use_openai:
                self._init_openai()
            else:
                self._init_sentence_transformers()
            
            # 预计算场景 embeddings
            if self._cache_embeddings:
                self._precompute_domain_embeddings()
            
            self._initialized = True
            return True
        
        except Exception as e:
            logger.warning(f"Failed to initialize semantic matcher: {e}")
            return False
    
    def _init_sentence_transformers(self) -> None:
        """初始化 sentence-transformers 模型"""
        try:
            from sentence_transformers import SentenceTransformer
            
            self._model = SentenceTransformer(self._model_name)
            logger.info(f"Loaded sentence-transformers model: {self._model_name}")
        
        except ImportError:
            logger.warning(
                "sentence-transformers not installed. "
                "Install with: pip install sentence-transformers"
            )
            raise
    
    def _init_openai(self) -> None:
        """初始化 OpenAI embeddings"""
        try:
            import openai
            self._model = "openai"  # 标记使用 OpenAI
            logger.info("Using OpenAI embeddings")
        
        except ImportError:
            logger.warning("openai package not installed")
            raise
    
    def _precompute_domain_embeddings(self) -> None:
        """预计算所有场景的 embeddings"""
        for domain, desc in DOMAIN_DESCRIPTIONS.items():
            embedding = self._get_embedding(desc)
            if embedding is not None:
                self._domain_embeddings[domain] = embedding
        
        logger.info(f"Precomputed embeddings for {len(self._domain_embeddings)} domains")
    
    def _get_embedding(self, text: str) -> Optional[Any]:
        """获取文本 embedding"""
        if self._model is None:
            return None
        
        try:
            if self._use_openai:
                return self._get_openai_embedding(text)
            else:
                return self._get_st_embedding(text)
        
        except Exception as e:
            logger.warning(f"Failed to get embedding: {e}")
            return None
    
    def _get_st_embedding(self, text: str) -> Any:
        """使用 sentence-transformers 获取 embedding"""
        embedding = self._model.encode(text, convert_to_numpy=True)
        return embedding / np.linalg.norm(embedding)  # 归一化
    
    def _get_openai_embedding(self, text: str) -> Any:
        """使用 OpenAI 获取 embedding"""
        import openai
        
        response = openai.embeddings.create(
            model="text-embedding-3-small",
            input=text,
        )
        embedding = np.array(response.data[0].embedding)
        return embedding / np.linalg.norm(embedding)
    
    def match(
        self,
        query: str,
        top_k: int = 3,
    ) -> List[Tuple[LifeDomain, float]]:
        """
        语义匹配用户问题到场景
        
        Args:
            query: 用户问题
            top_k: 返回前 k 个最匹配的场景
            
        Returns:
            [(domain, similarity_score), ...] 按相似度降序排列
        """
        if not self._ensure_initialized():
            return []
        
        if not self._domain_embeddings:
            return []
        
        # 获取查询 embedding
        query_embedding = self._get_embedding(query)
        if query_embedding is None:
            return []
        
        # 计算与各场景的相似度
        scores: List[Tuple[LifeDomain, float]] = []
        
        for domain, domain_embedding in self._domain_embeddings.items():
            similarity = np.dot(query_embedding, domain_embedding)
            scores.append((domain, float(similarity)))
        
        # 排序取 top_k
        scores.sort(key=lambda x: x[1], reverse=True)
        return scores[:top_k]
    
    def match_with_threshold(
        self,
        query: str,
        threshold: float = 0.5,
    ) -> List[Tuple[LifeDomain, float]]:
        """
        返回超过阈值的匹配结果
        
        Args:
            query: 用户问题
            threshold: 相似度阈值
            
        Returns:
            [(domain, similarity_score), ...] 仅返回超过阈值的
        """
        results = self.match(query, top_k=len(DOMAIN_DESCRIPTIONS))
        return [(d, s) for d, s in results if s >= threshold]
    
    def is_available(self) -> bool:
        """检查语义匹配器是否可用"""
        return self._ensure_initialized()


# =============================================================================
# 单例
# =============================================================================

_matcher: Optional[SemanticMatcher] = None


def get_semantic_matcher(
    model_name: str = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
    use_openai: bool = False,
) -> SemanticMatcher:
    """获取语义匹配器单例"""
    global _matcher
    if _matcher is None:
        _matcher = SemanticMatcher(model_name=model_name, use_openai=use_openai)
    return _matcher
