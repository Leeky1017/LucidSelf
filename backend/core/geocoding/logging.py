"""
Geocoding Service Structured Logging

地理编码服务的结构化日志模块。
提供带有上下文信息的错误日志记录。

Requirements: 10.3
"""

import logging
import json
from typing import Any, Dict, Optional
from dataclasses import dataclass, asdict


# Configure module logger
logger = logging.getLogger("geocoding")


@dataclass
class LogContext:
    """
    Structured log context for geocoding operations.
    
    地理编码操作的结构化日志上下文。
    """
    operation: str
    input_text: Optional[str] = None
    country_code: Optional[str] = None
    user_id: Optional[str] = None
    hint_label: Optional[str] = None
    provider: Optional[str] = None
    cache_key: Optional[str] = None
    place_id: Optional[str] = None
    error_type: Optional[str] = None
    error_message: Optional[str] = None
    extra: Optional[Dict[str, Any]] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary, excluding None values."""
        result = {}
        for key, value in asdict(self).items():
            if value is not None:
                result[key] = value
        return result


class GeocodingLogger:
    """
    Structured logger for geocoding service.
    
    地理编码服务的结构化日志记录器。
    
    Requirement 10.3: Log errors with error_type and context
    """
    
    def __init__(self, logger_instance: Optional[logging.Logger] = None):
        """
        Initialize geocoding logger.
        
        Args:
            logger_instance: Optional custom logger instance
        """
        self._logger = logger_instance or logger
    
    def _format_message(self, message: str, context: Optional[LogContext] = None) -> str:
        """Format log message with context."""
        if context is None:
            return message
        
        context_dict = context.to_dict()
        if context_dict:
            return f"{message} | context={json.dumps(context_dict, ensure_ascii=False)}"
        return message
    
    def info(self, message: str, context: Optional[LogContext] = None) -> None:
        """Log info message with optional context."""
        self._logger.info(self._format_message(message, context))
    
    def warning(self, message: str, context: Optional[LogContext] = None) -> None:
        """Log warning message with optional context."""
        self._logger.warning(self._format_message(message, context))
    
    def error(
        self,
        message: str,
        error_type: str,
        context: Optional[LogContext] = None,
        exc_info: bool = False
    ) -> None:
        """
        Log error message with error_type and context.
        
        Args:
            message: Error message
            error_type: Type of error (e.g., 'NotFoundError', 'ProviderError')
            context: Optional log context
            exc_info: Whether to include exception info
            
        Requirement 10.3
        """
        if context is None:
            context = LogContext(operation="unknown")
        
        context.error_type = error_type
        context.error_message = message
        
        self._logger.error(self._format_message(message, context), exc_info=exc_info)
    
    def debug(self, message: str, context: Optional[LogContext] = None) -> None:
        """Log debug message with optional context."""
        self._logger.debug(self._format_message(message, context))
    
    def log_request_start(
        self,
        input_text: str,
        country_code: Optional[str] = None,
        user_id: Optional[str] = None,
        hint_label: Optional[str] = None
    ) -> None:
        """Log the start of a geocoding request."""
        context = LogContext(
            operation="resolve_place",
            input_text=input_text,
            country_code=country_code,
            user_id=user_id,
            hint_label=hint_label
        )
        self.debug("Starting place resolution", context)
    
    def log_request_success(
        self,
        input_text: str,
        place_id: str,
        source: str,
        country_code: Optional[str] = None
    ) -> None:
        """Log successful place resolution."""
        context = LogContext(
            operation="resolve_place",
            input_text=input_text,
            place_id=place_id,
            provider=source,
            country_code=country_code
        )
        self.info("Place resolved successfully", context)
    
    def log_request_error(
        self,
        input_text: str,
        error_type: str,
        error_message: str,
        country_code: Optional[str] = None,
        exc_info: bool = False
    ) -> None:
        """
        Log failed place resolution.
        
        Requirement 10.3
        """
        context = LogContext(
            operation="resolve_place",
            input_text=input_text,
            country_code=country_code
        )
        self.error(error_message, error_type, context, exc_info=exc_info)
    
    def log_provider_call(
        self,
        provider: str,
        city: str,
        country: Optional[str] = None
    ) -> None:
        """Log external provider API call."""
        context = LogContext(
            operation="provider_call",
            provider=provider,
            input_text=city,
            country_code=country
        )
        self.debug(f"Calling external provider: {provider}", context)
    
    def log_provider_success(
        self,
        provider: str,
        place_id: str,
        city: str
    ) -> None:
        """Log successful provider response."""
        context = LogContext(
            operation="provider_call",
            provider=provider,
            place_id=place_id,
            input_text=city
        )
        self.info(f"Provider {provider} returned result", context)
    
    def log_provider_error(
        self,
        provider: str,
        error_type: str,
        error_message: str,
        city: str,
        exc_info: bool = False
    ) -> None:
        """
        Log provider error.
        
        Requirement 10.3
        """
        context = LogContext(
            operation="provider_call",
            provider=provider,
            input_text=city
        )
        self.error(error_message, error_type, context, exc_info=exc_info)
    
    def log_cache_hit(
        self,
        cache_type: str,
        cache_key: str,
        place_id: str
    ) -> None:
        """Log cache hit."""
        context = LogContext(
            operation="cache_lookup",
            cache_key=cache_key,
            place_id=place_id,
            extra={"cache_type": cache_type}
        )
        self.debug(f"Cache hit: {cache_type}", context)
    
    def log_cache_miss(
        self,
        cache_type: str,
        cache_key: str
    ) -> None:
        """Log cache miss."""
        context = LogContext(
            operation="cache_lookup",
            cache_key=cache_key,
            extra={"cache_type": cache_type}
        )
        self.debug(f"Cache miss: {cache_type}", context)


# Global logger instance
_geocoding_logger: Optional[GeocodingLogger] = None


def get_logger() -> GeocodingLogger:
    """
    Get the global geocoding logger instance.
    
    Returns:
        GeocodingLogger singleton instance
    """
    global _geocoding_logger
    if _geocoding_logger is None:
        _geocoding_logger = GeocodingLogger()
    return _geocoding_logger
