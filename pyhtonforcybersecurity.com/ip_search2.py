#!/usr/bin/env python3
# this line opens the log file
f = open('access.log', "r")
# this line takes each line the log file and stores it as an element in th list
lines = f.readlines()
# this lines stores the IP that the user types as a var called userinput
userinput = input("Enter the IP you want to search for: ")
# this combination for loop and nested if statement looks for the IP in the list called lines and prints the entinre line if found
for ip in lines:
    if ip.find(userinput) != -1:
        print(ip)
f.close()
