"""Local Document Search Engine."""
import json
from pathlib import Path
from typing import List, Dict, Set
import re


class DocumentSearchEngine:
    """Index and search local documents."""
    
    def __init__(self, index_path: Path):
        self.index_path = Path(index_path)
        self.index: Dict[str, Dict] = {}
        self.inverted_index: Dict[str, Set[str]] = {}
        self.load_index()
    
    def load_index(self):
        """Load existing index."""
        if self.index_path.exists():
            with open(self.index_path) as f:
                data = json.load(f)
                self.index = data.get('documents', {})
                # Rebuild inverted index
                for doc_id, doc in self.index.items():
                    for token in doc.get('tokens', []):
                        if token not in self.inverted_index:
                            self.inverted_index[token] = set()
                        self.inverted_index[token].add(doc_id)
    
    def save_index(self):
        """Save index to disk."""
        with open(self.index_path, 'w') as f:
            json.dump({'documents': self.index}, f, indent=2)
    
    def tokenize(self, text: str) -> List[str]:
        """Tokenize and normalize text."""
        text = text.lower()
        tokens = re.findall(r'\w+', text)
        return [t for t in tokens if len(t) > 2]
    
    def index_file(self, file_path: Path):
        """Index a single file."""
        if not file_path.exists():
            return
        
        content = file_path.read_text(encoding='utf-8', errors='ignore')
        tokens = self.tokenize(content)
        
        doc_id = str(file_path)
        self.index[doc_id] = {
            'path': str(file_path),
            'tokens': list(set(tokens)),
            'preview': content[:200]
        }
        
        for token in set(tokens):
            if token not in self.inverted_index:
                self.inverted_index[token] = set()
            self.inverted_index[token].add(doc_id)
    
    def index_directory(self, directory: Path, extensions: List[str] = None):
        """Index all files in directory."""
        if extensions is None:
            extensions = ['.txt', '.md']
        
        for file_path in directory.rglob('*'):
            if file_path.is_file() and file_path.suffix in extensions:
                self.index_file(file_path)
        
        self.save_index()
    
    def search(self, query: str, limit: int = 10) -> List[Dict]:
        """Search indexed documents."""
        query_tokens = self.tokenize(query)
        if not query_tokens:
            return []
        
        # Find documents containing query tokens
        matching_docs = None
        for token in query_tokens:
            docs = self.inverted_index.get(token, set())
            if matching_docs is None:
                matching_docs = docs
            else:
                matching_docs = matching_docs.intersection(docs)
        
        if not matching_docs:
            return []
        
        # Score by token count
        results = []
        for doc_id in matching_docs:
            doc = self.index[doc_id]
            score = sum(1 for t in query_tokens if t in doc['tokens'])
            results.append({
                'path': doc['path'],
                'score': score,
                'preview': doc['preview']
            })
        
        results.sort(key=lambda x: -x['score'])
        return results[:limit]
