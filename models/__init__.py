# models/__init__.py
"""
Module for initializing unique FileStorage instance
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()

