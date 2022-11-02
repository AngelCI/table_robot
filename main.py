"""
CODE FOR THE MICHAEL PAGE SELECTION PROCESS
  by:       Àngel Calvo
  email:    angel.c.iglesia@gmail.com
"""

import logging
import robot_class

# Logging configuration
logging.basicConfig(filename='table_robot_log.log', level=logging.DEBUG, format='[%(asctime)s] %(levelname)s : %(message)s')

# Robot object initialization as None
myRobot = None

# Sets of possible positions and facing directions
pos_set = {'0', '1', '2', '3', '4'}
dirs_set = {'NORTH', 'EAST', 'SOUTH', 'WEST'}

# Initial message
print("""
---------------------------------------------------------------------
----------------------- TOY ROBOT APPLICATION -----------------------
---------------------------------------------------------------------
    1) PLACE DE ROBOT IN A POSSIBLE POSITION.
    2) MOVE IT AROUND OR PLACE IT AGAIN, ALWAYS AVOIDING FALLS.
    3) EXIT WHEN YOU WANT TO STOP THE APPLICATION.
""")

logging.debug('Application started.')

# Start of the working cycle
while 1:
    # A message is shown on the console asking for an order from the list.
    order = input(
        """
Introduce your command:
    > PLACE X,Y,F   ( X and Y in [0-4] | F in {NORTH, EAST, SOUTH, WEST} )
    > MOVE
    > LEFT
    > RIGHT
    > REPORT
    > EXIT
        """
    ).upper()

    # `PLACE` will put the toy robot on the table in position X, Y and facing NORTH, SOUTH, EAST or WEST.
    if 'PLACE' in order and len(order) >= len("PLACE X,Y,EAST"):  # MIN length constraint
        # order[6] is the X
        # order[8] is the Y
        # order[10:] is the F
        if order[6] in pos_set and order[8] in pos_set and order[10:] in dirs_set:
            myRobot = robot_class.Robot(order[6], order[8], order[10:])
            logging.debug('The robot was placed in %s,%s,%s.', order[6], order[8], order[10:])
        else:
            print("""
Wrong PLACE format!
        The input format is "PLACE [0-4],[0-4],{NORTH,EAST,SOUTH,WEST}"
        Please, try again.
                    """)
            logging.warning('Wrong format for PLACE command inputted. (\'%s\')', order)
            continue

    elif not myRobot and order in {'MOVE', 'LEFT', 'RIGHT', 'REPORT'}:
        print('First place a robot on the table!')
        logging.warning('Command inputted before placing a robot. (\'%s\')', order)
    # `MOVE` will move the toy robot one unit forward in the direction it is currently facing.
    elif order == 'MOVE':
        if myRobot.get_dir() == 'NORTH' and myRobot.get_y() < 4:
            myRobot.set_y(myRobot.get_y() + 1)
            # Message
            print('The robot moved NORTH.')
            logging.debug('The robot moved NORTH. [%d,%d,%s]', myRobot.get_x(), myRobot.get_y(), myRobot.get_dir())
        elif myRobot.get_dir() == 'WEST' and myRobot.get_x() > 0:
            myRobot.set_x(myRobot.get_x() - 1)
            # Message
            print('The robot moved WEST. ')
            logging.debug('The robot moved WEST. [%d,%d,%s]', myRobot.get_x(), myRobot.get_y(), myRobot.get_dir())
        elif myRobot.get_dir() == 'SOUTH' and myRobot.get_y() > 0:
            myRobot.set_y(myRobot.get_y() - 1)
            # Message
            print('The robot moved SOUTH.')
            logging.debug('The robot moved SOUTH. [%d,%d,%s]', myRobot.get_x(), myRobot.get_y(), myRobot.get_dir())
        elif myRobot.get_dir() == 'EAST' and myRobot.get_x() < 4:
            myRobot.set_x(myRobot.get_x() + 1)
            # Message
            print('The robot moved EAST.')
            logging.debug('The robot moved EAST. [%d,%d,%s]', myRobot.get_x(), myRobot.get_y(), myRobot.get_dir())
        else:
            print('Robot on the edge!')
            print('Current position: [', myRobot.get_x(),',', myRobot.get_y(),',', myRobot.get_dir(),'].')
            logging.warning('The toy robot was pushed to the edge. [%d,%d,%s]', myRobot.get_x(), myRobot.get_y(), myRobot.get_dir())
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
        # Message
        print('The robot turned LEFT.')
        logging.debug('The robot turned LEFT. [%d,%d,%s]', myRobot.get_x(), myRobot.get_y(), myRobot.get_dir())

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
        # Message
        print('The robot turned RIGHT.')
        logging.debug('The robot turned RIGHT. [%d,%d,%s]', myRobot.get_x(), myRobot.get_y(), myRobot.get_dir())

    # `REPORT` will announce the X,Y and F of the toy robot.
    elif order == 'REPORT':
        myRobot.report()
        logging.debug('The robot REPORTED its position. [%d,%d,%s]', myRobot.get_x(), myRobot.get_y(), myRobot.get_dir())

    elif order == 'EXIT':
        logging.debug('Program stopped by the user.')
        break

    else:
        print('\n Wrong command! \n')
        logging.warning('Wrong command inputted. (\'%s\')', order)
        continue
