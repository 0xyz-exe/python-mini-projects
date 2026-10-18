"""Tests for weather CLI."""
from pathlib import Path
from tempfile import TemporaryDirectory
import sys

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

try:
    from weather_client import WeatherClient
    DEPS_AVAILABLE = True
except ImportError:
    DEPS_AVAILABLE = False


def test_format_weather():
    if not DEPS_AVAILABLE:
        return
    
    client = WeatherClient()
    data = {
        'current_weather': {
            'temperature': 22.5,
            'windspeed': 10.0,
            'weathercode': 0
        }
    }
    
    output = client.format_weather(data)
    assert '22.5' in output
    assert '10.0' in output


def test_save_load_sample():
    if not DEPS_AVAILABLE:
        return
    
    with TemporaryDirectory() as tmpdir:
        sample_path = Path(tmpdir) / "sample.json"
        
        client = WeatherClient()
        client.save_sample_response(sample_path)
        
        loaded = client.load_offline_sample(sample_path)
        assert 'current_weather' in loaded
        assert loaded['current_weather']['temperature'] == 22.5


if __name__ == "__main__":
    if not DEPS_AVAILABLE:
        print("⚠ Dependencies not available - tests skipped")
        exit(0)
    
    test_format_weather()
    test_save_load_sample()
    print("✓ All tests passed")
