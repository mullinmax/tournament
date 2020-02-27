#!/usr/bin/env python3
import sys

data = sys.stdin.readlines()
f = open('temp.txt', 'w')
f.write(str(data))
f.write("fin")
f.close()
print(0)