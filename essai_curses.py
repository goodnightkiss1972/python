# au prealable mettre a jour PIP : python3 -m pip install pip --upgrade
# puis python3 -m pip install windows-curses
# ou encore mieux pip install windows-curses

import curses
import time

stdscr = curses.initscr()


stdscr.keypad(True)

stdscr.addstr(5, 5, "hello world!")
time.sleep(3)


stdscr.keypad(False)

curses.endwin()


