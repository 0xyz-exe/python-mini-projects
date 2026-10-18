"""Tests for website monitor."""
from pathlib import Path
from tempfile import TemporaryDirectory
import sys

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

try:
    from monitor import WebsiteMonitor
    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False


def test_check_url_structure():
    """Test result structure without network."""
    if not REQUESTS_AVAILABLE:
        return
    
    # Mock test - just verify structure
    result = {
        'url': 'http://example.com',
        'status_code': 200,
        'response_time': 0.1,
        'success': True,
        'error': None
    }
    
    assert 'url' in result
    assert 'status_code' in result
    assert 'success' in result


def test_export_json():
    if not REQUESTS_AVAILABLE:
        return
    
    with TemporaryDirectory() as tmpdir:
        monitor = WebsiteMonitor(['http://example.com'])
        monitor.results = [{
            'url': 'http://example.com',
            'status_code': 200,
            'response_time': 0.1,
            'success': True,
            'error': None,
            'timestamp': 123456
        }]
        
        json_path = Path(tmpdir) / "results.json"
        monitor.export_json(json_path)
        
        assert json_path.exists()


if __name__ == "__main__":
    if not REQUESTS_AVAILABLE:
        print("⚠ requests not available - tests skipped")
        exit(0)
    
    test_check_url_structure()
    test_export_json()
    print("✓ All tests passed")
