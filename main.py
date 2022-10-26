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
        self.position = [int(x), int(y)]
        self.dir = str(dir)
        self.report()

    def set_x(self, x):
        self.position[0] = int(x)

    def set_y(self, y):
        self.position[1] = int(y)

    def get_x(self):
        return self.position[0]

    def get_y(self):
        return self.position[1]

    def set_dir(self, d):
        self.dir = d

    def get_dir(self):
        return self.dir

    def report(self):
        print(f'{self.get_x()}, {self.get_y()}, {self.get_dir()}')


dirs_set = {'NORTH', 'EAST', 'SOUTH', 'WEST'}

# Start of the working cycle
while (1):
    order = input(
        '''
        Introduce your command:
        > PLACE X,Y,F   (X and Y in [0-5] | F in {NORTH, EAST, SOUTH, WEST}
        > MOVE
        > LEFT
        > RIGHT
        > REPORT
        '''
    ).upper()

    if order == 'MOVE':
        if myRobot.get_dir() == 'NORTH' and myRobot.position[1] < 5:
            myRobot.position[1] += 1
        elif myRobot.get_dir() == 'WEST' and myRobot.position[0] > 0:
            myRobot.position[0] -= 1
        elif myRobot.get_dir() == 'SOUTH' and myRobot.position[1] > 0:
            myRobot.position[1] -= 1
        elif myRobot.get_dir() == 'EAST' and myRobot.position[0] < 5:
            myRobot.position[0] += 1
        else:
            print('Robot on the edge!')
            continue

    elif order == 'LEFT':
        if myRobot.get_dir() == 'NORTH':
            myRobot.set_dir('WEST')
        elif myRobot.get_dir() == 'WEST':
            myRobot.set_dir('SOUTH')
        elif myRobot.get_dir() == 'SOUTH':
            myRobot.set_dir('EAST')
        elif myRobot.get_dir() == 'EAST':
            myRobot.set_dir('NORTH')

    elif order == 'RIGHT':
        if myRobot.get_dir() == 'NORTH':
            myRobot.set_dir('EAST')
        elif myRobot.get_dir() == 'EAST':
            myRobot.set_dir('SOUTH')
        elif myRobot.get_dir() == 'SOUTH':
            myRobot.set_dir('WEST')
        elif myRobot.get_dir() == 'WEST':
            myRobot.set_dir('NORTH')

    elif order == 'REPORT':
        myRobot.report()

    elif 'PLACE' in order:
        if order[6].isdecimal() and order[8].isdecimal() and order[10:] in dirs_set:
            myRobot = Robot(order[6], order[8], order[10:])
        else:
            print('\n Wrong command! \n')
            continue

    else:
        print('\n Wrong command! \n')
        continue
