#!/usr/bin/env python3
import os
import time
import shutil
from datetime import datetime, timedelta

# Configuration
UPLOAD_FOLDER = 'uploads'
MAX_FILE_AGE_HOURS = 5  # Delete files older than 1 hours

def cleanup_old_files():
    """Clean up files older than the specified age"""
    now = time.time()
    max_age_seconds = MAX_FILE_AGE_HOURS * 60
    
    # Ensure the upload directory exists
    if not os.path.exists(UPLOAD_FOLDER):
        print(f"Upload folder {UPLOAD_FOLDER} does not exist.")
        return
    
    # Get all files in the upload directory
    files_removed = 0
    for filename in os.listdir(UPLOAD_FOLDER):
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        
        # Skip directories
        if os.path.isdir(file_path):
            continue
        
        # Check file age
        file_age = now - os.path.getmtime(file_path)
        if file_age > max_age_seconds:
            try:
                os.remove(file_path)
                files_removed += 1
                print(f"Removed old file: {file_path}")
            except Exception as e:
                print(f"Error removing file {file_path}: {str(e)}")
    
    print(f"Cleanup completed: removed {files_removed} old files")

if __name__ == "__main__":
    print(f"Starting cleanup of files older than {MAX_FILE_AGE_HOURS} hours...")
    cleanup_old_files()