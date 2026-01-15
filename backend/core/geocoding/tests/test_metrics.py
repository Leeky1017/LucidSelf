"""
Unit Tests for Geocoding Metrics

地理编码服务指标的单元测试。

Requirements: 10.1, 10.2
"""

import pytest
import threading
from concurrent.futures import ThreadPoolExecutor

from backend.core.geocoding.metrics import (
    GeocodingMetrics,
    get_metrics,
    reset_metrics,
)


class TestGeocodingMetrics:
    """Tests for GeocodingMetrics class."""
    
    def setup_method(self):
        """Reset metrics before each test."""
        reset_metrics()
    
    def test_initial_values(self):
        """Test initial counter values are zero."""
        metrics = GeocodingMetrics()
        
        assert metrics.geo_requests_total == 0
        assert metrics.geo_requests_success_total == 0
        assert metrics.geo_requests_error_total == 0
        assert metrics.geo_external_calls_total == 0
        assert metrics.geo_external_calls_amap == 0
        assert metrics.geo_external_calls_nominatim == 0
        assert metrics.errors_by_type == {}
    
    def test_increment_request(self):
        """
        Test incrementing request counter.
        
        Requirement 10.1
        """
        metrics = GeocodingMetrics()
        
        metrics.increment_request()
        assert metrics.geo_requests_total == 1
        
        metrics.increment_request()
        assert metrics.geo_requests_total == 2
    
    def test_increment_success(self):
        """
        Test incrementing success counter.
        
        Requirement 10.1
        """
        metrics = GeocodingMetrics()
        
        metrics.increment_success()
        assert metrics.geo_requests_success_total == 1
        
        metrics.increment_success()
        assert metrics.geo_requests_success_total == 2
    
    def test_increment_error_without_type(self):
        """
        Test incrementing error counter without error type.
        
        Requirement 10.1
        """
        metrics = GeocodingMetrics()
        
        metrics.increment_error()
        assert metrics.geo_requests_error_total == 1
        assert metrics.errors_by_type == {}
    
    def test_increment_error_with_type(self):
        """
        Test incrementing error counter with error type.
        
        Requirement 10.1
        """
        metrics = GeocodingMetrics()
        
        metrics.increment_error("NotFoundError")
        assert metrics.geo_requests_error_total == 1
        assert metrics.errors_by_type == {"NotFoundError": 1}
        
        metrics.increment_error("NotFoundError")
        assert metrics.geo_requests_error_total == 2
        assert metrics.errors_by_type == {"NotFoundError": 2}
        
        metrics.increment_error("InvalidInputError")
        assert metrics.geo_requests_error_total == 3
        assert metrics.errors_by_type == {"NotFoundError": 2, "InvalidInputError": 1}
    
    def test_increment_external_call_amap(self):
        """
        Test incrementing Amap external call counter.
        
        Requirement 10.2
        """
        metrics = GeocodingMetrics()
        
        metrics.increment_external_call("amap")
        assert metrics.geo_external_calls_total == 1
        assert metrics.geo_external_calls_amap == 1
        assert metrics.geo_external_calls_nominatim == 0
    
    def test_increment_external_call_nominatim(self):
        """
        Test incrementing Nominatim external call counter.
        
        Requirement 10.2
        """
        metrics = GeocodingMetrics()
        
        metrics.increment_external_call("nominatim")
        assert metrics.geo_external_calls_total == 1
        assert metrics.geo_external_calls_amap == 0
        assert metrics.geo_external_calls_nominatim == 1
    
    def test_increment_external_call_unknown_provider(self):
        """
        Test incrementing external call counter for unknown provider.
        
        Requirement 10.2
        """
        metrics = GeocodingMetrics()
        
        metrics.increment_external_call("unknown")
        assert metrics.geo_external_calls_total == 1
        assert metrics.geo_external_calls_amap == 0
        assert metrics.geo_external_calls_nominatim == 0
    
    def test_reset(self):
        """Test resetting all counters."""
        metrics = GeocodingMetrics()
        
        # Increment various counters
        metrics.increment_request()
        metrics.increment_success()
        metrics.increment_error("TestError")
        metrics.increment_external_call("amap")
        metrics.increment_external_call("nominatim")
        
        # Reset
        metrics.reset()
        
        # Verify all counters are zero
        assert metrics.geo_requests_total == 0
        assert metrics.geo_requests_success_total == 0
        assert metrics.geo_requests_error_total == 0
        assert metrics.geo_external_calls_total == 0
        assert metrics.geo_external_calls_amap == 0
        assert metrics.geo_external_calls_nominatim == 0
        assert metrics.errors_by_type == {}
    
    def test_get_snapshot(self):
        """Test getting a snapshot of all metrics."""
        metrics = GeocodingMetrics()
        
        metrics.increment_request()
        metrics.increment_request()
        metrics.increment_success()
        metrics.increment_error()
        metrics.increment_external_call("amap")
        
        snapshot = metrics.get_snapshot()
        
        assert snapshot == {
            'geo_requests_total': 2,
            'geo_requests_success_total': 1,
            'geo_requests_error_total': 1,
            'geo_external_calls_total': 1,
            'geo_external_calls_amap': 1,
            'geo_external_calls_nominatim': 0,
        }
    
    def test_thread_safety(self):
        """Test that metrics are thread-safe."""
        metrics = GeocodingMetrics()
        num_threads = 10
        increments_per_thread = 100
        
        def increment_all():
            for _ in range(increments_per_thread):
                metrics.increment_request()
                metrics.increment_success()
                metrics.increment_error("TestError")
                metrics.increment_external_call("amap")
        
        with ThreadPoolExecutor(max_workers=num_threads) as executor:
            futures = [executor.submit(increment_all) for _ in range(num_threads)]
            for future in futures:
                future.result()
        
        expected_count = num_threads * increments_per_thread
        
        assert metrics.geo_requests_total == expected_count
        assert metrics.geo_requests_success_total == expected_count
        assert metrics.geo_requests_error_total == expected_count
        assert metrics.geo_external_calls_amap == expected_count
        assert metrics.errors_by_type["TestError"] == expected_count


class TestGlobalMetricsFunctions:
    """Tests for global metrics functions."""
    
    def setup_method(self):
        """Reset metrics before each test."""
        reset_metrics()
    
    def test_get_metrics_returns_singleton(self):
        """Test get_metrics returns the same instance."""
        metrics1 = get_metrics()
        metrics2 = get_metrics()
        
        assert metrics1 is metrics2
    
    def test_reset_metrics_clears_counters(self):
        """Test reset_metrics clears all counters."""
        metrics = get_metrics()
        
        metrics.increment_request()
        metrics.increment_success()
        
        reset_metrics()
        
        # Get metrics again - should be reset
        metrics = get_metrics()
        assert metrics.geo_requests_total == 0
        assert metrics.geo_requests_success_total == 0
    
    def test_metrics_persist_across_calls(self):
        """Test that metrics persist across get_metrics calls."""
        metrics1 = get_metrics()
        metrics1.increment_request()
        
        metrics2 = get_metrics()
        assert metrics2.geo_requests_total == 1
        
        metrics2.increment_request()
        assert metrics1.geo_requests_total == 2
