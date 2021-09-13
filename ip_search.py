#!/usr/bin/env python3
f = open("access.log")
strUsrinput = input("Enter IP address: ")
for line in iter(f):
    ip = line.split(" - ")[0]
    if ip == strUsrinput:
        print(line)
f.close()
