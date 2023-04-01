"""
Google API Client, Discovery Hook
"""

from PyInstaller.utils.hooks import (
    collect_data_files
)

datas = collect_data_files("googleapiclient.discovery_cache")