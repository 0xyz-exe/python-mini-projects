"""Batch File Renamer - Core functionality."""
from pathlib import Path
from typing import List, Tuple, Optional
import re


class FileRenamer:
    """Batch rename files with preview."""
    
    def __init__(self, directory: Path):
        self.directory = Path(directory)
        self.operations: List[Tuple[Path, Path]] = []
    
    def add_prefix(self, prefix: str, extensions: Optional[List[str]] = None) -> List[Tuple[Path, Path]]:
        """Add prefix to files."""
        self.operations.clear()
        files = self._get_files(extensions)
        
        for file_path in files:
            new_name = prefix + file_path.name
            new_path = file_path.parent / new_name
            self.operations.append((file_path, new_path))
        
        return self.operations.copy()
    
    def add_suffix(self, suffix: str, extensions: Optional[List[str]] = None) -> List[Tuple[Path, Path]]:
        """Add suffix before extension."""
        self.operations.clear()
        files = self._get_files(extensions)
        
        for file_path in files:
            stem = file_path.stem
            ext = file_path.suffix
            new_name = f"{stem}{suffix}{ext}"
            new_path = file_path.parent / new_name
            self.operations.append((file_path, new_path))
        
        return self.operations.copy()
    
    def add_numbering(self, start: int = 1, extensions: Optional[List[str]] = None) -> List[Tuple[Path, Path]]:
        """Add sequential numbers."""
        self.operations.clear()
        files = sorted(self._get_files(extensions))
        
        for i, file_path in enumerate(files, start=start):
            ext = file_path.suffix
            new_name = f"{i:03d}{ext}"
            new_path = file_path.parent / new_name
            self.operations.append((file_path, new_path))
        
        return self.operations.copy()
    
    def find_replace(self, find: str, replace: str, extensions: Optional[List[str]] = None) -> List[Tuple[Path, Path]]:
        """Find and replace in filenames."""
        self.operations.clear()
        files = self._get_files(extensions)
        
        for file_path in files:
            new_name = file_path.name.replace(find, replace)
            if new_name != file_path.name:
                new_path = file_path.parent / new_name
                self.operations.append((file_path, new_path))
        
        return self.operations.copy()
    
    def execute(self, dry_run: bool = True) -> List[str]:
        """Execute rename operations."""
        if self._has_collisions():
            raise ValueError("Collision detected: some target names already exist")
        
        log = []
        if not dry_run:
            for old_path, new_path in self.operations:
                old_path.rename(new_path)
                log.append(f"Renamed {old_path.name} -> {new_path.name}")
        
        return log
    
    def _get_files(self, extensions: Optional[List[str]] = None) -> List[Path]:
        """Get files matching extensions."""
        if not self.directory.exists():
            raise ValueError(f"Directory does not exist: {self.directory}")
        
        files = [f for f in self.directory.iterdir() if f.is_file()]
        
        if extensions:
            extensions = [e.lower() if e.startswith('.') else f'.{e.lower()}' for e in extensions]
            files = [f for f in files if f.suffix.lower() in extensions]
        
        return files
    
    def _has_collisions(self) -> bool:
        """Check for naming collisions."""
        targets = [new_path for _, new_path in self.operations]
        
        # Check duplicates in target names
        if len(targets) != len(set(targets)):
            return True
        
        # Check if target already exists (excluding same-file renames)
        for old_path, new_path in self.operations:
            if new_path.exists() and new_path != old_path:
                return True
        
        return False
