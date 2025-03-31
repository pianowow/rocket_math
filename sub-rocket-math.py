#!/usr/bin/python

# written by Chris and Olivia Irwin, 2025
# TODO: 
#       - print total time taken at the end
#       - give the option to do a fixed time length instead of fixed number of problems
#          - display a countdown timer for when a fixed time is chosen, depends on 3
#       - display a stopwatch timer for when a fixed number of problems is chosen
#       - combined operations, +, -, x, ➗

from random import random
from math import floor
from time import time
import curses
import csv 
import sys 

file_path='/home/apollo/Documents/Olivia-sub-rocket-math.csv'

#problem space here is defined by types of questions in "Rocket Math" homework 
def new_question():
    x = [0,0,0]
    #make numbers such that x[2]-x[1]=x[0]
    for j in range(2):
         x[j] = floor(random()*9)+1  #maybe 0 should be allowed for x[1] 
    x[2]=x[0]+x[1]
    return x

def win_print(win, msg, color):
    win.clear()
    win.addstr(0,0,msg,curses.color_pair(color))
    win.refresh()

def do_it(stdscr):
    # Create a custom color set that you might re-use frequently
    # Assign it a number (1-255), a foreground, and background color.
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_BLUE)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)
    stdscr.bkgd(' ', curses.color_pair(2))
    stdscr.refresh()
    curses.echo()
    max_line, max_col = curses.LINES-1, curses.COLS-1
    w_title_bar = curses.newwin(1,max_col,0,0) #height, width, starty, startx
    w_title_bar.bkgd(' ', curses.color_pair(1))
    w_instruction = curses.newwin(1,max_col,1,0)
    w_question = curses.newwin(3,max_col,3,0)
    w_question.bkgd(' ', curses.color_pair(2))
    w_answer = curses.newwin(1,max_col,6,0)
    w_answer.bkgd(' ', curses.color_pair(3))
    w_feedback = curses.newwin(1,max_col,max_line-2,0)
    w_feedback.bkgd(' ', curses.color_pair(1))
    w_summary = curses.newwin(1,max_col,max_line-1,0)
    w_summary.bkgd(' ', curses.color_pair(1))
    w_hints = curses.newwin(1,max_col,max_line,0)
    w_hints.bkgd(' ', curses.color_pair(1))


    win_print(w_title_bar, "Subtraction Rocket Math by Chris Irwin and Olivia Irwin, 2025", 1)
    win_print(w_question, "How many questions would you like?", 2)

    total = int(w_answer.getstr(0,0))
    w_answer.clear()

    win_print(w_hints, "Type q to quit and p to pause the practice.", 1)

    with open(file_path,'a') as f:
        #fieldnames = ['seconds','num1','num2','answer','correct']
        writer = csv.writer(f)    
        #writer.writerow(fieldnames)
        score = 0
        for i in range(total):
            x = new_question()
            win_print(w_question, "Question {}\n{} - {} =".format(i+1,x[2],x[1]), 2)
            s_time = time()
            user_input_int = -1
            while user_input_int == -1: 
                try:
                    #getstr returns bytes, which decode() turns into a string
                    user_input = w_answer.getstr(0,0).decode() 
                    w_answer.clear()
                    w_answer.refresh()
                    if user_input == "q":
                        sys.exit()
                    elif user_input == "p":
                        win_print(w_question, "Timer is paused.  Press any key to continue...", 2) 
                        w_answer.getch(0,0)
                        w_answer.clear()
                        w_answer.refresh()
                        x = new_question()
                        win_print(w_question, "Question {}\n{} - {} =".format(i+1,x[2],x[1]), 2)
                        s_time = time()
                        continue
                    user_input_int = int(user_input)
                except SystemExit:
                    raise
                except ValueError: #shouldn't mark a question wrong because the user mistyped
                    win_print(w_feedback, "oops, that doesn't look like a number", 1)
            e_time = time() 
            seconds = round(e_time-s_time)
            if (user_input_int == x[0] ):
                score += 1
                win_print(w_feedback,"Answered correctly in {} seconds".format(seconds), 1)
                writer.writerow([seconds,x[2],x[1],user_input,'Y'])
            else:
                win_print(w_feedback,"Opps!  {} seconds".format(seconds), 1)
                writer.writerow([seconds,x[2],x[1],user_input,'N'])
            win_print(w_summary, "You got {} right out of {} questions! {}%".format(score,i+1,int(score/(i+1)*100)), 1)
    w_hints.clear()
    w_hints.refresh()
    win_print(w_question, "Press any key to quit... ", 2)
    w_answer.getch()

if __name__ == '__main__':
    curses.wrapper(do_it)
