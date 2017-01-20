"""
This file will contain the Car class, and its move function, 
which returns an Action, the class which defines what the Car
does. The Car is mostly a shell class containing things about
the 'personality' of the driver, while its move function does the
heavy lifting.

"""


# The 'enums' for right, left, center
right  =  1
left   = -1
center =  0

# Action class, just used for constructing the actions.
class Action:
    def __init__(self, laneChange, speedChange, stopTime):
        self.laneChange = laneChange
        self.speedChange = speedChange
        self.stopTime = stopTime


