#!/usr/bin/python

# written by Chris Irwin, 2025

import curses

def do_it(stdscr):
    #curses.echo()
    max_line, max_col = curses.LINES-1, curses.COLS-1
    #w_title_bar = curses.newwin(1,max_col,0,0) #height, width, start_y, start_x
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
    windows = []
    width = max_col // 8
    height = max_line // 8
    for background_color in range(8):
        windows.append([])
        start_y = height*background_color
        for foreground_color in range(8):
            color = background_color*8+foreground_color+1
            curses.init_pair(color, foreground_color, background_color)
            start_x = width*foreground_color
            windows[background_color].append(curses.newwin(height, width, start_y, start_x))
            windows[background_color][foreground_color].addstr(0,0,("0"*(width-1)+"\n")*(height-1),curses.color_pair(color))
            windows[background_color][foreground_color].refresh()
    windows[0][0].getch()

if __name__ == '__main__':
    curses.wrapper(do_it)
