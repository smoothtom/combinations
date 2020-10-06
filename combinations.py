#!/usr/bin/env python3
import itertools
import sys
import os
import time 
import datetime 


print("\n")
print("*" * 41)
print("** Welcome to my Combination Programm! **")
print("*" * 41)

print("\n")
s = input("Please Enter something for different combinations: ")
print("\n")
t = list(itertools.permutations(s,len(s)))

print("loading the combinations...")
time.sleep(2)
x = 0

for i in range (0,len(t)):
    x += 1
    if len(s) == 3:
        print("".join(t[i]),"-->", x )
        time.sleep(0.04)
    elif len(s) == 4:
        print("".join(t[i]),"-->", x )
        time.sleep(0.03)
    elif len(s) == 5:
        print("".join(t[i]),"-->", x )
        time.sleep(0.02)
    elif len(s) == 6:
        print("".join(t[i]),"-->", x )
        time.sleep(0.01)
    elif len(s) == 7:
        print("".join(t[i]),"-->", x )
        time.sleep(0.001)
    elif len(s) > 7:
        print("".join(t[i]),"-->", x )

print("\n")
# print("You got", len(t) ,"different combinations")

ask_user = str(input("Do you want to safe all these combinations? (yes/no) : "))
if ask_user == "yes" or "y":
    f = open("file.txt", "w")
    for element in t:
        f.write("".join(map(str,element)))
        f.write("\n")
elif ask_user == "no" or "n":
    sys.exit(0)
else:
    sys.exit(0)

