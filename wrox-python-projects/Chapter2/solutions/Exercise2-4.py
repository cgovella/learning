import ctypes as ct
# libc = ct.CDLL('libc.so.6')    # in Linux/MacOS
libc = ct.cdll.msvcrt    # in Windows

for c in range(128):
   print(c, ' is a ctrl char' if libc.iscntrl(c) else 'is not a ctrl char')


