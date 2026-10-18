"""Duplicate File Finder."""
import hashlib
from pathlib import Path
from typing import Dict, List
from collections import defaultdict


class DuplicateFinder:
    """Find duplicate files by hash."""
    
    def __init__(self, directory: Path):
        self.directory = Path(directory)
        self.duplicates: Dict[str, List[Path]] = defaultdict(list)
    
    def find_duplicates(self, min_size: int = 0) -> Dict[str, List[Path]]:
        """Find duplicate files by MD5 hash."""
        if not self.directory.exists():
            raise ValueError(f"Directory not found: {self.directory}")
        
        file_hashes = defaultdict(list)
        
        for file_path in self.directory.rglob("*"):
            if file_path.is_file():
                file_size = file_path.stat().st_size
                if file_size < min_size:
                    continue
                
                file_hash = self._hash_file(file_path)
                file_hashes[file_hash].append(file_path)
        
        # Keep only duplicates
        self.duplicates = {h: files for h, files in file_hashes.items() if len(files) > 1}
        return dict(self.duplicates)
    
    def _hash_file(self, path: Path, chunk_size: int = 8192) -> str:
        """Calculate MD5 hash with streaming."""
        hasher = hashlib.md5()
        with open(path, 'rb') as f:
            while chunk := f.read(chunk_size):
                hasher.update(chunk)
        return hasher.hexdigest()
    
    def get_summary(self) -> Dict:
        """Get duplicate summary."""
        total_files = sum(len(files) for files in self.duplicates.values())
        total_size = 0
        
        for files in self.duplicates.values():
            if files:
                total_size += files[0].stat().st_size * (len(files) - 1)
        
        return {
            'duplicate_groups': len(self.duplicates),
            'total_duplicate_files': total_files,
            'wasted_space_bytes': total_size
        }
