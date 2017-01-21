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

# speed change can be either max acceleration down to full stop. 
# A full stop is considered an accident.

class Car:
    """
     need to add a variety of parameters
     showing 
       recklessness in [0,1]
       following_distance in [1, 5]
       acceleration in [1, 3]
       law_abiding_speed in [-2,2]
       law abiding_lane_changes in [0, 1]
    """
    
    def __init__(self, speed, recklessness, following_distance,
                       acceleration, braking, law_abiding_speed, 
                       law_abiding_lane_changes,
                       lane_spot_index):
        self.speed = speed
        self.recklessness = recklessness
        self.following_distance = following_distance
        self.acceleration = acceleration
        self.law_abiding_speed = law_abiding_speed
        self.law_abiding_lane_changes = law_abiding_lane_changes
        
        self.lane_spot_index = lane_spot_index
    # add a variable for self driving cars for them being more likely
    # to prefer the truly best action.
    def move(self, lane):
        return Action(center, self.speed, 0)


    def all_actions(self):
        # return every possible action, even if it has low utility. 
        # Might eventually want to save this to a variable, no reason
        # to do it multiple times. 
        return "Incomplete"

    # need to incorporate the various parameters into the model
    def evaluate_action_blind(self, lane, action):
        """
        Checks the utility of the action ignoring the other cars. 
        It is used to predict the actions of other cars.

        Full stop is bad, but driving to the end of a lane is worse.
        """
        #        Prefer staying in the lane unless the lane they are in
        #          terminates soon.
        points = 0
        print("The first points, set to 0")
        print(points)
        if action.laneChange == center:
            points += 10

        print("Center points added")
        print(points)
        # Next to 'ifs' compute the 'cost' to switch to the lane
        if action.laneChange == right:
            points += 8 / (1 + lane.right[1])
        print("Points added for moving right ")
        print(points)

        if action.laneChange == left:
            points += 8 / (1 + lane.left[1])
        
        print("Points for moving left")
        print(points)
        desired_speed = 6 + self.law_abiding_speed
        after_action_speed = self.speed + action.speedChange
        # penalized for not being at the speed you like. 
        # The *5 is to make sure that people want to change lanes if 
        # they go too slow. Might want to make that a personality variable.
        points += (6 - abs(desired_speed - after_action_speed)) * 5

        print("Points for speed")
        print(points)

        # will never ever slam into the end of a lane
        if after_action_speed == 0:
            if action.laneChange == center:
                return -10
            else:
                return -15
        # gets the lane to be the right one
        lane_approaching = lane
        if action.laneChange == right:
            lane_approaching = lane.right
        elif action.laneChange == left:
            lane_approaching = lane.left
        # The next two 'ifs' set up whether the lane you are moving to (or are in)
        # is a good place to be.
        if lane_approaching == 0:
            return -10001
        if lane_approaching.lane_end == 0 and \
           len(lane.lane_spots) < after_action_speed + self.lane_spot_index:
               return -10002
        # if they are near the end of a lane, they get penalities, and want to leave it.
        if lane_approaching.lane_end == 0 and \
           len(lane.lane_spots) < 3 * (after_action_speed + self.lane_spot_index):
               points += -3 
        if lane_approaching.lane_end == 0 and \
           len(lane.lane_spots) < 2 * (after_action_speed + self.lane_spot_index):
               points += -5

        return points
 
    def evaluate_action(self, lane, action):
        # returns the utility of the action, evaluating it relative
        #  to the other cars. 
        # Notes: Crash == 0
        # gets neighboring cars (2 lanes left, 2 right, 1 forward)
        #     This should be an argument       
        # guesses where they will go, anywhere they will crash gets a
        #   0. 
        return "Incomplete"
