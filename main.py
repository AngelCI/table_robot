'''
CODE FOR THE MICHAEL PAGE SELECTION PROCESS
  by:       Àngel Calvo
  email:    angel.c.iglesia@gmail.com
'''

'''
Function requisites:
PLACE X,Y,F
MOVE
LEFT
RIGHT
REPORT
'''


class Robot:
    def __init__(self, x=0, y=0, dir='NORTH'):
        self.position = [x, y]
        self.dir = dir
        self.report()

    def place(self, x, y, f):
        pass

    def move(self):
        pass

    def left(self):
        pass

    def right(self):
        pass

    def report(self):
        f'{self.position[0]}, {self.position[1]}, {dir}'


test = Robot(1, 1, 'WEST')
test.report()
