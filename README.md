# table_robot
Technical test for Altair.

## Requisites
The requisite was to create an app to simulate a toy robot on a 5x5 tiles table. The origin (0,0) can be considered to be the SOUTH WEST most corner.
The robot should answer to the following commands:

 - `PLACE X,Y,F`
    - Puts the toy robot on the table in position X,Y and facing NORTH, SOUTH, EAST or WEST.
 - `MOVE`
    - Moves the toy robot one unit forward in the direction it is currently facing.
 - `LEFT`
    - Rotates the robot 90 degrees left without changing the position of the robot.
 - `RIGHT`
    - Rotates the robot 90 degrees right without changing the position of the robot.
 - `REPORT`
    - Announces the X,Y and F of the robot.
A robot that is not on the table can choose to ignore the `MOVE`, `LEFT`, `RIGHT` and `REPORT` commands.   

## Constraints
 - The toy robot must not fall off the table during movement. This also includes the initial placement of the toy robot.
 - Any move that would cause the robot to fall must be ignored. 
 - The first valid command to the robot is a `PLACE` command, after that, any sequence of commands may be issued, in any order, including another `PLACE` command. The application should discard all commands in the sequence until a valid `PLACE` command has been executed.
 ___
 The test logs are also included.
