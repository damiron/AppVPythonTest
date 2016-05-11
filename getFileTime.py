import os

print(os.stat('getFileTime.py').st_mtime)
print(os.path.getmtime('getFileTime.py'))

print(os.stat('tmp'+os.path.sep+'tmp.txt').st_mtime)
print(os.path.getmtime('tmp'+os.path.sep+'tmp.txt'))