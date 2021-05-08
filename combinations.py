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
    print("** Welcome to my Combination Program! **")
    print("*" * 41)

# main function, where the main programm is written
def main():
    print("\n")
    s = input("Please Enter something for different combinations: ")

    # max 11 letters
    if len(s) > 11:
        print("\nProgramm can't take this long word")
        sys.exit(0)

    print("\n")
    t = list(itertools.permutations(s,len(s)))

    # prints the length of the word from the user input
    print("Your input is" ,len(s), "letters long\n")

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

    # while loop for the user input
    while True:
        i = str(input("\nDo you want to save all the combinations ? Please enter yes or no: "))
        if i == "yes":
            f = open("file.txt", "w")
            for element in t:
                f.write("".join(map(str,element)))
                f.write("\n")
            print("\nYour combinations have been successfully saved in the file.txt")
            sys.exit(0)
        elif i == "no":
            print("\nYou quit the program and the combinations are not saved!")
            sys.exit(0)

def start():
    intro()
    main()

start()
