#!/usr/bin/python

from random import random
from math import floor
from time import time
import csv 

with open('/home/apollo/Documents/Olivia-rocket-math.csv','a') as f:
    #fieldnames = ['seconds','num1','num2','answer','correct']
    writer = csv.writer(f)    
    #writer.writerow(fieldnames)

    for i in range(50):
        x = [0,0]
        for j in range(2):
             x[j] = floor(random()*9+1)   
        print(x[0],"+", x[1], "=")
        s_time = time()
        try:
            a = int(input())
        except:
            a=0
        e_time = time() 
        seconds = int(e_time-s_time)
        if (a == x[0]+x[1]):
            print("Answered correctly in", seconds, "seconds")
            writer.writerow([seconds,x[0],x[1],a,'Y'])
        else:
            print("oops in", seconds, "seconds")
            writer.writerow([seconds,x[0],x[1],a,'N'])

