#!/usr/bin/python

# written by Chris and Olivia Irwin, 2025
# TODO: 1. colored background (use curses module)
#       2. print total time taken at the end
#       3. give the option to do a fixed time length instead of fixed number of problems
#       4. display a countdown timer for when a fixed time is chosen, dpeends on 1 and 3
#       5. display a stopwatch timer for when a fixed number of problems is chosen, depends on 1
#       6. split curses window into problem area and answer area , depends on 1

from random import random
from math import floor
from time import time
import csv 
import sys 

#problem space here is defined by types of questions in "Rocket Math" homework 
def new_problem():
    x = [0,0,0]
    #make numbers such that x[2]-x[1]=x[0]
    for j in range(2):
         x[j] = floor(random()*9)+1  #maybe 0 should be allowed for x[1] or x[2]
    x[2]=x[0]+x[1]
    print(x[2],"-", x[1], "=")
    return x


with open('/home/apollo/Documents/Olivia-sub-rocket-math.csv','a') as f:
    #fieldnames = ['seconds','num1','num2','answer','correct']
    writer = csv.writer(f)    
    #writer.writerow(fieldnames)
    total = int(input("How many problems would you like? "))
    print('type "exit" to stop the program')
    print('type "pause" to pause the timer')
    score = 0
    for i in range(total):
        x = new_problem()
        s_time = time()
        user_input = ""
        user_input_int = -1
        while user_input_int == -1: 
            try:
                user_input = input()
                if user_input == "exit":
                    sys.exit()
                elif user_input == "pause":
                    input("Timer is paused.  Press Enter to continue...")
                    x = new_problem()
                    s_time = time()
                    continue
                user_input_int = int(user_input)
            except SystemExit:
                print("Bye!")
                raise
            except ValueError:
                print('oops, that doesn\'t look like a number')
        e_time = time() 
        seconds = round(e_time-s_time)
        if (user_input_int == x[0] ):
            score += 1
            print("Answered correctly in", seconds, "seconds")
            writer.writerow([seconds,x[2],x[1],user_input,'Y'])
        else:
            print("oops in", seconds, "seconds")
            writer.writerow([seconds,x[2],x[1],user_input,'N'])
    print("You got",score,"right out of",total,"problems!",str(int(score/total*100))+"%")
