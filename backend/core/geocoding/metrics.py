"""
Geocoding Service Metrics

地理编码服务的指标收集模块。
提供请求计数、成功/错误计数、外部调用计数等指标。

Requirements: 10.1, 10.2
"""

from dataclasses import dataclass, field
from typing import Dict, Optional
import threading


@dataclass
class GeocodingMetrics:
    """
    Metrics counters for geocoding service.
    
    地理编码服务的指标计数器。
    
    Requirements:
    - 10.1: Increment counters for geocoding operations
    - 10.2: Track external provider calls
    """
    
    # Request counters (Requirement 10.1)
    _geo_requests_total: int = field(default=0, repr=False)
    _geo_requests_success_total: int = field(default=0, repr=False)
    _geo_requests_error_total: int = field(default=0, repr=False)
    
    # External call counters (Requirement 10.2)
    _geo_external_calls_total: int = field(default=0, repr=False)
    _geo_external_calls_amap: int = field(default=0, repr=False)
    _geo_external_calls_nominatim: int = field(default=0, repr=False)
    
    # Error type counters
    _errors_by_type: Dict[str, int] = field(default_factory=dict, repr=False)
    
    # Thread lock for thread-safe operations
    _lock: threading.Lock = field(default_factory=threading.Lock, repr=False)
    
    # Properties for read access
    @property
    def geo_requests_total(self) -> int:
        """Total number of geocoding requests."""
        return self._geo_requests_total
    
    @property
    def geo_requests_success_total(self) -> int:
        """Total number of successful geocoding requests."""
        return self._geo_requests_success_total
    
    @property
    def geo_requests_error_total(self) -> int:
        """Total number of failed geocoding requests."""
        return self._geo_requests_error_total
    
    @property
    def geo_external_calls_total(self) -> int:
        """Total number of external API calls."""
        return self._geo_external_calls_total
    
    @property
    def geo_external_calls_amap(self) -> int:
        """Total number of Amap API calls."""
        return self._geo_external_calls_amap
    
    @property
    def geo_external_calls_nominatim(self) -> int:
        """Total number of Nominatim API calls."""
        return self._geo_external_calls_nominatim
    
    @property
    def errors_by_type(self) -> Dict[str, int]:
        """Error counts by error type."""
        return dict(self._errors_by_type)
    
    def increment_request(self) -> None:
        """
        Increment total request counter.
        
        Requirement 10.1
        """
        with self._lock:
            self._geo_requests_total += 1
    
    def increment_success(self) -> None:
        """
        Increment success counter.
        
        Requirement 10.1
        """
        with self._lock:
            self._geo_requests_success_total += 1
    
    def increment_error(self, error_type: Optional[str] = None) -> None:
        """
        Increment error counter.
        
        Args:
            error_type: Optional error type for categorization
            
        Requirement 10.1
        """
        with self._lock:
            self._geo_requests_error_total += 1
            if error_type:
                self._errors_by_type[error_type] = self._errors_by_type.get(error_type, 0) + 1
    
    def increment_external_call(self, provider: str) -> None:
        """
        Increment external call counter for a specific provider.
        
        Args:
            provider: Provider name ('amap' or 'nominatim')
            
        Requirement 10.2
        """
        with self._lock:
            self._geo_external_calls_total += 1
            if provider == 'amap':
                self._geo_external_calls_amap += 1
            elif provider == 'nominatim':
                self._geo_external_calls_nominatim += 1
    
    def reset(self) -> None:
        """Reset all counters to zero. Useful for testing."""
        with self._lock:
            self._geo_requests_total = 0
            self._geo_requests_success_total = 0
            self._geo_requests_error_total = 0
            self._geo_external_calls_total = 0
            self._geo_external_calls_amap = 0
            self._geo_external_calls_nominatim = 0
            self._errors_by_type.clear()
    
    def get_snapshot(self) -> Dict[str, int]:
        """
        Get a snapshot of all metrics.
        
        Returns:
            Dictionary with all metric values
        """
        with self._lock:
            return {
                'geo_requests_total': self._geo_requests_total,
                'geo_requests_success_total': self._geo_requests_success_total,
                'geo_requests_error_total': self._geo_requests_error_total,
                'geo_external_calls_total': self._geo_external_calls_total,
                'geo_external_calls_amap': self._geo_external_calls_amap,
                'geo_external_calls_nominatim': self._geo_external_calls_nominatim,
            }


# Global metrics instance
_metrics: Optional[GeocodingMetrics] = None


def get_metrics() -> GeocodingMetrics:
    """
    Get the global metrics instance.
    
    Returns:
        GeocodingMetrics singleton instance
    """
    global _metrics
    if _metrics is None:
        _metrics = GeocodingMetrics()
    return _metrics


def reset_metrics() -> None:
    """Reset the global metrics instance. Useful for testing."""
    global _metrics
    if _metrics is not None:
        _metrics.reset()
