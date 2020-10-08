#!/usr/bin/env python3
import itertools
import sys
import os
import time 
import datetime 

def intro():
    print("\n")
    print("*" * 41)
    print("** Welcome to my Combination Programm! **")
    print("*" * 41)

def main():
    print("\n")
    s = input("Please Enter something for different combinations: ")
    print("\n")
    t = list(itertools.permutations(s,len(s)))

    print("loading the combinations...")
    time.sleep(2)
    x = 0

    for i in range (0,len(t)):
        x += 1
        if len(s) <= 3:
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
    i = input("Do you want to save all these combinations ? Please Enter yes or no: ")
    if i == "yes":
        f = open("file.txt", "w")
        for element in t:
            f.write("".join(map(str,element)))
            f.write("\n")
    else:
        sys.exit(0)

def start():
    intro()
    main()

start()
