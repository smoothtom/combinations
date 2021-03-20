#!/usr/bin/env python3
import itertools
import sys
import os
import time 
import datetime 

# intro function 
def intro():
    print("\n")
    print("*" * 41)
    print("** Welcome to my Combination Programm! **")
    print("*" * 41)

# main function, where the main programm is written
def main():
    print("\n")
    s = input("Please Enter something for different combinations: ")
    print("\n")
    t = list(itertools.permutations(s,len(s)))

    # prints the length of the word from the user input
    print("Your input is" ,len(s), "words long\n")

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

    # ask the user after the loop, to save the combinations in a extra .txt file
    i = input("Do you want to save all these combinations ? Please Enter (y)es or (n)o: ")
    if i == "yes" or "y":
        print("\nYour combinations have been successfully saved in the file.txt")
        f = open("file.txt", "w")
        for element in t:
            f.write("".join(map(str,element)))
            f.write("\n")
    elif i == "no" or "n":
        print("You quit this programm, without saving all your combinations")
        sys.exit(0)
    # if user types no - then the programm will quit
    else:
        sys.exit(0)

def start():
    intro()
    main()

start()
