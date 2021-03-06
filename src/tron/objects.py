import curses

class Car:

    def __init__(self, x, y, player, direction=0):
        self.x = x
        self.y = y
        self.player = player
        self.direction = direction
        self.dead = False

    def update(self, window, keys):
        if curses.KEY_LEFT in keys and self.direction != 1:
            self.direction = 3
        elif curses.KEY_UP in keys and self.direction != 2:
            self.direction = 0
        elif curses.KEY_RIGHT in keys and self.direction != 3:
            self.direction = 1
        elif curses.KEY_DOWN in keys and self.direction != 0:
            self.direction = 2

        if self.direction == 3:
            self.x -= 1
        elif self.direction == 0:
            self.y -= 1
        elif self.direction == 1:
            self.x += 1
        elif self.direction == 2:
            self.y += 1

    def draw(self, window):
        window.attron(curses.color_pair(self.player))
        #window.addch(self.y, self.x, "%")
        window.attroff(curses.color_pair(self.player))

    def serialize(self):
        return {k: v for k, v in self.__dict__.items()}

    def populate(self, dict):
        for k, v in dict.items():
            setattr(self, k, v)
