#!/usr/bin/python

# written by Chris Irwin, 2025

import curses

def do_it(stdscr):
    #curses.echo()
    max_line, max_col = curses.LINES-1, curses.COLS-1
    #w_title_bar = curses.newwin(1,max_col,0,0) #height, width, starty, startx
    # Create a custom color set that you might re-use frequently
    # Assign it a number (1-255), a foreground, and background color.
    # curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_MAGENTA)
    #screen.addstr("RED ALERT!\n", curses.color_pair(1))

    # Colors 	        Code
    # COLOR_BLACK 	    0
    # COLOR_RED 	    1
    # COLOR_GREEN 	    2
    # COLOR_YELLOW 	    3
    # COLOR_BLUE 	    4
    # COLOR_MAGENTA 	5
    # COLOR_CYAN 	    6
    # COLOR_WHITE 	    7

    # initialize all color pairs (1-64)
    # background * 8 + foreground 
    wins = []
    width = max_col // 8
    height = max_line // 8
    for bg in range(8):
        wins.append([])
        starty = height*bg
        for fg in range(8):
            color = bg*8+fg+1
            curses.init_pair(bg*8+fg+1, fg, bg )
            startx = width*fg            
            wins[bg].append(curses.newwin(height, width, starty, startx))
            wins[bg][fg].addstr(0,0,("0"*(width-1)+"\n")*(height-1),curses.color_pair(color))
            wins[bg][fg].refresh()
    wins[0][0].getch()

if __name__ == '__main__':
    curses.wrapper(do_it)
