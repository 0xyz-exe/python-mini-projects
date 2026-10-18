"""Website Availability Monitor."""
from pathlib import Path
from typing import Dict, List
import time
import json


try:
    import requests
    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False


class WebsiteMonitor:
    """Monitor website availability."""
    
    def __init__(self, urls: List[str], timeout: int = 10):
        if not REQUESTS_AVAILABLE:
            raise ImportError("Install: python3 -m pip install requests --user")
        self.urls = urls
        self.timeout = timeout
        self.results: List[Dict] = []
    
    def check(self) -> Dict[str, Dict]:
        """Check all URLs once."""
        timestamp = time.time()
        results = {}
        
        for url in self.urls:
            result = self._check_url(url)
            result['timestamp'] = timestamp
            results[url] = result
            self.results.append(result)
        
        return results
    
    def _check_url(self, url: str) -> Dict:
        """Check single URL."""
        start = time.time()
        
        try:
            response = requests.get(url, timeout=self.timeout)
            elapsed = time.time() - start
            
            return {
                'url': url,
                'status_code': response.status_code,
                'response_time': elapsed,
                'success': 200 <= response.status_code < 400,
                'error': None
            }
        except Exception as e:
            elapsed = time.time() - start
            return {
                'url': url,
                'status_code': None,
                'response_time': elapsed,
                'success': False,
                'error': str(e)
            }
    
    def export_json(self, path: Path):
        """Export results to JSON."""
        with open(path, 'w') as f:
            json.dump(self.results, f, indent=2)
    
    def export_csv(self, path: Path):
        """Export results to CSV."""
        import csv
        with open(path, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['url', 'timestamp', 'status_code', 
                                                   'response_time', 'success', 'error'])
            writer.writeheader()
            writer.writerows(self.results)
