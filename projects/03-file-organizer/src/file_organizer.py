"""File Organizer - Core functionality."""
import shutil
from pathlib import Path
from typing import Dict, List
from collections import defaultdict


class FileOrganizer:
    """Organize files by extension, type, or date."""
    
    def __init__(self, source: Path, destination: Path):
        self.source = Path(source)
        self.destination = Path(destination)
        self.log: List[str] = []
    
    def organize_by_extension(self, dry_run: bool = True) -> Dict[str, List[Path]]:
        """Organize files by extension."""
        if not self.source.exists():
            raise ValueError(f"Source directory does not exist: {self.source}")
        
        organized = defaultdict(list)
        
        for file_path in self.source.rglob("*"):
            if file_path.is_file():
                ext = file_path.suffix.lower() or ".no_extension"
                organized[ext].append(file_path)
        
        if not dry_run:
            for ext, files in organized.items():
                dest_dir = self.destination / ext.lstrip(".")
                dest_dir.mkdir(parents=True, exist_ok=True)
                
                for file_path in files:
                    dest_path = self._get_unique_path(dest_dir / file_path.name)
                    shutil.copy2(file_path, dest_path)
                    self.log.append(f"Copied {file_path} -> {dest_path}")
        
        return dict(organized)
    
    def organize_by_type(self, dry_run: bool = True) -> Dict[str, List[Path]]:
        """Organize files by type category."""
        type_map = {
            "images": {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"},
            "documents": {".pdf", ".doc", ".docx", ".txt", ".odt", ".rtf"},
            "videos": {".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv"},
            "audio": {".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a"},
            "archives": {".zip", ".rar", ".7z", ".tar", ".gz", ".bz2"},
            "code": {".py", ".js", ".java", ".cpp", ".c", ".html", ".css", ".json"},
        }
        
        if not self.source.exists():
            raise ValueError(f"Source directory does not exist: {self.source}")
        
        organized = defaultdict(list)
        
        for file_path in self.source.rglob("*"):
            if file_path.is_file():
                ext = file_path.suffix.lower()
                category = "other"
                
                for cat, exts in type_map.items():
                    if ext in exts:
                        category = cat
                        break
                
                organized[category].append(file_path)
        
        if not dry_run:
            for category, files in organized.items():
                dest_dir = self.destination / category
                dest_dir.mkdir(parents=True, exist_ok=True)
                
                for file_path in files:
                    dest_path = self._get_unique_path(dest_dir / file_path.name)
                    shutil.copy2(file_path, dest_path)
                    self.log.append(f"Copied {file_path} -> {dest_path}")
        
        return dict(organized)
    
    def _get_unique_path(self, path: Path) -> Path:
        """Generate unique path to avoid collisions."""
        if not path.exists():
            return path
        
        stem = path.stem
        suffix = path.suffix
        parent = path.parent
        counter = 1
        
        while True:
            new_path = parent / f"{stem}_{counter}{suffix}"
            if not new_path.exists():
                return new_path
            counter += 1
    
    def get_log(self) -> List[str]:
        """Get operation log."""
        return self.log.copy()
