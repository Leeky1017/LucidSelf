"""
Geocoding Service Exceptions

地理编码服务的异常定义。
"""


class GeocodingError(Exception):
    """
    Base geocoding error.
    
    地理编码服务基类异常。
    """
    pass


class NotFoundError(GeocodingError):
    """
    Location could not be resolved.
    
    当所有解析步骤都无法找到匹配位置时抛出。
    """
    def __init__(self, query: str, hint_country: str | None = None):
        self.query = query
        self.hint_country = hint_country
        message = f"Location not found: '{query}'"
        if hint_country:
            message += f" (country hint: {hint_country})"
        super().__init__(message)


class InvalidInputError(GeocodingError):
    """
    Input text could not be parsed.
    
    当输入文本为空或无法解析时抛出。
    """
    def __init__(self, input_text: str, reason: str = ""):
        self.input_text = input_text
        self.reason = reason
        message = f"Invalid input: '{input_text}'"
        if reason:
            message += f" ({reason})"
        super().__init__(message)


class ProviderError(GeocodingError):
    """
    External provider failed.
    
    当外部地理编码提供商调用失败时抛出。
    """
    def __init__(self, provider: str, original_error: Exception):
        self.provider = provider
        self.original_error = original_error
        super().__init__(f"Provider '{provider}' failed: {original_error}")
