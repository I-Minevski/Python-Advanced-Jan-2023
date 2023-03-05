import os
try:
    os.remove('toxt.txt')
except FileNotFoundError:
    print("File not found")