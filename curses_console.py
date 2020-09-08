import curses

class companion():
    def __init__(self, size_y, size_x, pos_y, pos_x):
        self.w = stdscr.subwin(size_y, size_x, pos_y, pos_x)
        self.size_y = size_y
        self.size_x = size_x
        self.pos_y = pos_y
        self.pos_x = pos_x
        self.audit = []

    def print(self, str):
        self.w.addstr(self.pos_y, self.pos_x, str)
        self.audit.append(str)
        self.w.refresh()

    def getkey(self):
        return self.w.getkey()


stdscr = curses.initscr()

w1 = companion(20, 60, 0, 0)
w1.print("Coucou.")

keypressed = w1.getkey()

curses.endwin()

print(keypressed)

