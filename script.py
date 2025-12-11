#!/usr/bin/env python3
import os
import re
import shutil
from pathlib import Path

import piexif
from mutagen.mp4 import MP4

# --- Configuration ---
SRC_DIR = Path('.')          # directory containing your .jpg and .mp4 files
OUT_DIR = SRC_DIR / 'out'    # destination subfolder
FAIL_DIR = SRC_DIR / 'failed' # folder for files that fail to process

# Create output and failed directories if they don't exist
OUT_DIR.mkdir(exist_ok=True)
FAIL_DIR.mkdir(exist_ok=True)

# Regex to capture date prefix: YYYY-MM-DD
DATE_RE = re.compile(r'^(?P<date>\d{4}-\d{2}-\d{2})_')

def process_jpg(src_path: Path, date_str: str):
    """
    Copy JPEG to out/ and set the EXIF DateTimeOriginal tag to date_str.
    """
    dst_path = OUT_DIR / src_path.name
    fail_path = FAIL_DIR / src_path.name
    
    try:
        shutil.copy2(src_path, dst_path)
        # Prepare EXIF payload
        exif_dict = piexif.load(str(dst_path))
        # Format required by EXIF: "YYYY:MM:DD HH:MM:SS"
        dt_value = date_str.replace('-', ':') + " 00:00:00"
        exif_dict["Exif"][piexif.ExifIFD.DateTimeOriginal] = dt_value.encode('utf-8')
        
        # Insert updated EXIF back into file
        exif_bytes = piexif.dump(exif_dict)
        piexif.insert(exif_bytes, str(dst_path))
        print(f"[JPEG]  {src_path.name} → out/{dst_path.name} (DateTimeOriginal={dt_value})")
    except:
        shutil.copy2(src_path, fail_path)
        print(f"FAILED {src_path.name}")
    
def process_mp4(src_path: Path, date_str: str):
    """
    Copy MP4 to out/ and set the ©day tag to date_str.
    """
    dst_path = OUT_DIR / src_path.name
    fail_path = FAIL_DIR / src_path.name
    
    try:
        shutil.copy2(src_path, dst_path)
        mp4file = MP4(str(dst_path))
        # The ©day atom stores the release/creation date as "YYYY-MM-DD"
        mp4file["\xa9day"] = [date_str]
        mp4file.save()
        print(f"[MP4]   {src_path.name} → out/{dst_path.name} (©day={date_str})")
    except:
        shutil.copy2(src_path, fail_path)
        print(f"FAILED {src_path.name}")

def main():
    for entry in SRC_DIR.iterdir():
        if not entry.is_file():
            continue
        
        # only target .jpg, .jpeg and .mp4
        if entry.suffix.lower() not in ('.jpg', '.jpeg', '.mp4'):
            continue
        
        m = DATE_RE.match(entry.name)
        if not m:
            print(f"[SKIP]  filename does not match pattern: {entry.name}")
            continue
        
        date_str = m.group('date')
        
        if entry.suffix.lower() in ('.jpg', '.jpeg'):
            process_jpg(entry, date_str)
        else:
            process_mp4(entry, date_str)

if __name__ == "__main__":
    main()
