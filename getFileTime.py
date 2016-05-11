import os
time1 = os.stat('getFileTime.py').st_mtime
time2 = os.path.getmtime('getFileTime.py')
print(time1)
print(time2)
time1 = os.stat('tmp'+os.path.sep+'tmp.txt').st_mtime
time2 = os.path.getmtime('tmp'+os.path.sep+'tmp.txt')
print(time1)
print(time2)