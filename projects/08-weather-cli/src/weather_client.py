"""Weather CLI - Core functionality."""
from pathlib import Path
from typing import Dict
import json


try:
    import requests
    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False


class WeatherClient:
    """Weather client using Open-Meteo API (free, no key required)."""
    
    def __init__(self, api_url: str = "https://api.open-meteo.com/v1/forecast"):
        if not REQUESTS_AVAILABLE:
            raise ImportError("Install: python3 -m pip install requests --user")
        self.api_url = api_url
    
    def get_weather(self, latitude: float, longitude: float) -> Dict:
        """Get current weather and forecast."""
        params = {
            'latitude': latitude,
            'longitude': longitude,
            'current_weather': True,
            'daily': 'temperature_2m_max,temperature_2m_min',
            'timezone': 'auto'
        }
        
        response = requests.get(self.api_url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    
    def format_weather(self, data: Dict) -> str:
        """Format weather data for display."""
        current = data.get('current_weather', {})
        
        output = []
        output.append(f"Temperature: {current.get('temperature', 'N/A')}°C")
        output.append(f"Wind Speed: {current.get('windspeed', 'N/A')} km/h")
        output.append(f"Weather Code: {current.get('weathercode', 'N/A')}")
        
        return '\n'.join(output)
    
    def save_sample_response(self, path: Path):
        """Save sample response for offline demo."""
        sample = {
            'current_weather': {
                'temperature': 22.5,
                'windspeed': 10.3,
                'weathercode': 0,
                'time': '2026-10-18T12:00'
            },
            'daily': {
                'temperature_2m_max': [25.0, 24.0, 23.5],
                'temperature_2m_min': [18.0, 17.5, 17.0]
            }
        }
        with open(path, 'w') as f:
            json.dump(sample, f, indent=2)
    
    def load_offline_sample(self, path: Path) -> Dict:
        """Load saved sample for offline use."""
        with open(path) as f:
            return json.load(f)
