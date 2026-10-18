"""Web Scraper - Core functionality."""
from pathlib import Path
from typing import Dict, List
import json
import time


try:
    import requests
    from bs4 import BeautifulSoup
    DEPS_AVAILABLE = True
except ImportError:
    DEPS_AVAILABLE = False


class WebScraper:
    """Scrape web pages responsibly."""
    
    def __init__(self, timeout: int = 10, delay: float = 1.0):
        if not DEPS_AVAILABLE:
            raise ImportError("Install: python3 -m pip install requests beautifulsoup4 --user")
        self.timeout = timeout
        self.delay = delay
    
    def scrape(self, url: str) -> Dict:
        """Scrape page and extract basic elements."""
        response = requests.get(url, timeout=self.timeout, headers={
            'User-Agent': 'Mozilla/5.0 (Educational Web Scraper)'
        })
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        title = soup.find('title')
        headings = soup.find_all(['h1', 'h2', 'h3'])
        links = soup.find_all('a', href=True)
        
        result = {
            'url': url,
            'title': title.text.strip() if title else '',
            'headings': [h.text.strip() for h in headings[:20]],
            'links': [{'text': a.text.strip(), 'href': a['href']} for a in links[:50]],
            'status_code': response.status_code
        }
        
        time.sleep(self.delay)
        return result
    
    def export_json(self, data: Dict, output_path: Path):
        """Export scraped data to JSON."""
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    
    def export_csv(self, data: Dict, output_path: Path):
        """Export links to CSV."""
        import csv
        with open(output_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['text', 'href'])
            for link in data.get('links', []):
                writer.writerow([link['text'], link['href']])
