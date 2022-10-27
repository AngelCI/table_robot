"""
CODE FOR THE MICHAEL PAGE SELECTION PROCESS
  by:       Àngel Calvo
  email:    angel.c.iglesia@gmail.com
"""

import logging

"""
Function requisites:
PLACE X,Y,F
MOVE
LEFT
RIGHT
REPORT
"""

# Logging configuration
logging.basicConfig(filename='table_robot_log.log', encoding='utf-8',
                    level=logging.DEBUG, format='%(asctime)s : %(message)s')


# Definition of the 'Robot' class used for the control of the toy robot on the table
class Robot:
    def __init__(self, x=0, y=0, direction='NORTH'):
        self.position = [int(x), int(y)]
        self.dir = str(direction)
        # self.report()

    def set_x(self, x):
        self.position[0] = int(x)

    def get_x(self):
        return self.position[0]

    def set_y(self, y):
        self.position[1] = int(y)

    def get_y(self):
        return self.position[1]

    def set_dir(self, d):
        self.dir = d

    def get_dir(self):
        return self.dir

    def report(self):
        """
        Function used to report the current state of the toy robot.
        Shows the X and Y position and the facing direction.
        """
        print(f'{self.get_x()}, {self.get_y()}, {self.get_dir()}')


# Set of possible facing directions
dirs_set = {'NORTH', 'EAST', 'SOUTH', 'WEST'}

# Start of the working cycle
while 1:
    # A message is shown on the console asking for an order from the list.
    order = input(
        """
        Introduce your command:
        > PLACE X,Y,F   (X and Y in [0-5] | F in {NORTH, EAST, SOUTH, WEST}
        > MOVE
        > LEFT
        > RIGHT
        > REPORT
        """
    ).upper()

    # `MOVE` will move the toy robot one unit forward in the direction it is currently facing.
    if order == 'MOVE':
        if myRobot.get_dir() == 'NORTH' and myRobot.get_y() < 5:
            myRobot.set_y(myRobot.get_y() + 1)
            logging.debug('The robot moved NORTH.')
        elif myRobot.get_dir() == 'WEST' and myRobot.get_x() > 0:
            myRobot.set_x(myRobot.get_x() - 1)
            logging.debug('The robot moved WEST.')
        elif myRobot.get_dir() == 'SOUTH' and myRobot.get_y() > 0:
            myRobot.set_y(myRobot.get_y() - 1)
            logging.debug('The robot moved SOUTH.')
        elif myRobot.get_dir() == 'EAST' and myRobot.get_x() < 5:
            myRobot.set_x(myRobot.get_x() + 1)
            logging.debug('The robot moved EAST.')
        else:
            print('Robot on the edge!')
            logging.warning('The toy robot was pushed to the edge.')
            continue

    # `LEFT` will rotate the robot 90 degrees in the left direction without changing the position of the robot.
    elif order == 'LEFT':
        if myRobot.get_dir() == 'NORTH':
            myRobot.set_dir('WEST')
        elif myRobot.get_dir() == 'WEST':
            myRobot.set_dir('SOUTH')
        elif myRobot.get_dir() == 'SOUTH':
            myRobot.set_dir('EAST')
        elif myRobot.get_dir() == 'EAST':
            myRobot.set_dir('NORTH')
        logging.debug('The robot turned LEFT.')

    # `RIGHT` will rotate the robot 90 degrees in the right direction without changing the position of the robot.
    elif order == 'RIGHT':
        if myRobot.get_dir() == 'NORTH':
            myRobot.set_dir('EAST')
        elif myRobot.get_dir() == 'EAST':
            myRobot.set_dir('SOUTH')
        elif myRobot.get_dir() == 'SOUTH':
            myRobot.set_dir('WEST')
        elif myRobot.get_dir() == 'WEST':
            myRobot.set_dir('NORTH')
        logging.debug('The robot turned RIGHT.')

    # `REPORT` will announce the X,Y and F of the robot.
    elif order == 'REPORT':
        myRobot.report()
        logging.debug('The robot REPORTED its position.')

    elif 'PLACE' in order:
        order_x = order[6]
        order_y = order[8]
        order_f = order[10:]
        if order_x.isdecimal() and order_y.isdecimal() and order_f in dirs_set:
            myRobot = Robot(order_x, order_y, order_f)
            logging.debug('The robot was placed in %d,%d,%s.',order_x,order_y,order_f)
        else:
            print("""
            Wrong PLACE format!
            The input format is "PLACE [0-5],[0-5],{NORTH,EAST,SOUTH,WEST}"
            Please, try again.
            """)
            logging.warning('Wrong format for PLACE command inputted.')
            continue

    else:
        print('\n Wrong command! \n')
        logging.warning('Wrong command inputted.')
        continue
