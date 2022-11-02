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
