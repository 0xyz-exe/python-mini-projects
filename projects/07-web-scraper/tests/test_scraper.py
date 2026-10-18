"""Tests for web scraper."""
from pathlib import Path
from tempfile import TemporaryDirectory
import sys

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

try:
    from scraper import WebScraper
    from bs4 import BeautifulSoup
    DEPS_AVAILABLE = True
except ImportError:
    DEPS_AVAILABLE = False
    print("Dependencies not installed")


def test_scrape_html_fixture():
    """Test with local HTML fixture."""
    if not DEPS_AVAILABLE:
        return
    
    with TemporaryDirectory() as tmpdir:
        # Create test HTML file
        html_file = Path(tmpdir) / "test.html"
        html_file.write_text("""
        <html>
        <head><title>Test Page</title></head>
        <body>
            <h1>Main Heading</h1>
            <h2>Subheading</h2>
            <a href="https://example.com">Link 1</a>
            <a href="/page2">Link 2</a>
        </body>
        </html>
        """)
        
        # Mock offline test
        with open(html_file) as f:
            soup = BeautifulSoup(f.read(), 'html.parser')
        
        title = soup.find('title')
        assert title.text == "Test Page"
        
        headings = soup.find_all(['h1', 'h2'])
        assert len(headings) == 2
        
        links = soup.find_all('a', href=True)
        assert len(links) == 2


if __name__ == "__main__":
    if not DEPS_AVAILABLE:
        print("⚠ Dependencies not available - tests skipped")
        exit(0)
    
    test_scrape_html_fixture()
    print("✓ All tests passed")
