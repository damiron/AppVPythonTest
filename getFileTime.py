import os

print(os.stat('getFileTime.py').st_mtime)
print(os.path.getmtime('getFileTime.py'))