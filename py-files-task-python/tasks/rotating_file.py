"""Template for programming assignment: Rotating file"""
import os
from types import TracebackType
from typing import List, Optional, Type

class RotatingFile:
    def __init__(self, filepath: str, mode: str, max_size: int, max_backups: int) -> None:
        self.filepath = filepath
        self.mode = mode
        self.max_size = max_size
        self.max_backups = max_backups
        self.file = open(filepath, mode)
        
    def read(self) -> str:
        result = []
        # First read backup files in descending order
        for i in range(self.max_backups, 0, -1):
            backup = f"{self.filepath}.{i}"
            if os.path.exists(backup):
                with open(backup, 'r') as f:
                    content = f.read().strip()
                    if content:
                        result.append(content)
        
        # Then read main file
        self.file.seek(0)
        content = self.file.read().strip()
        if content:
            result.append(content)
        
        return '\n'.join(result)
    
    def rollover(self) -> None:
        self.file.close()
        
        # Remove oldest backup if exists
        oldest = f"{self.filepath}.{self.max_backups}"
        if os.path.exists(oldest):
            os.remove(oldest)
            
        # Shift existing backups
        for i in range(self.max_backups - 1, 0, -1):
            current = f"{self.filepath}.{i}"
            new = f"{self.filepath}.{i + 1}"
            if os.path.exists(current):
                os.rename(current, new)
                
        # Move current file to .1
        os.rename(self.filepath, f"{self.filepath}.1")
        
        # Open new file
        self.file = open(self.filepath, self.mode)
    
    def write(self, s: str) -> None:
        if len(s) > self.max_size:
            raise Exception("Input string exceeds maximum file size")
            
        current_pos = self.file.tell()
        if current_pos + len(s) > self.max_size:
            self.rollover()
        
        self.file.write(s)
        self.file.flush()
    
    def __enter__(self) -> 'RotatingFile':
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> bool:

        self.file.close()
        if exc_val:
            raise exc_val

        return True
