import os, sys
print(" Update Checking")
os.system("git pull")
try:
    __import__("Random").Main()
except Exception as e:
    exit(str(e))
