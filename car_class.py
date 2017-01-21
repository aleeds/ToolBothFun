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
    def __repr__(self):
        return "Action(" + str(self.laneChange) + ", " + str(self.speedChange) + ")"

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
       law abiding_lane_changes in [0, 10]
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
        self.action_list = self.all_actions()
        
    # add a variable for self driving cars for them being more likely
    # to prefer the truly best action.
    def move(self, lane):
       return Action(center, 1, 0)


    def return_ten_best_actions(self, lane):
        ls = [(action, self.evaluate_action_blind(lane, action))
              for action in self.action_list]
        ls = sorted(ls, key = lambda (a,b) : -b)
        return ls[0:10]

    def all_actions(self):
        all_speeds = range(self.speed + self.acceleration + 1)
        all_lanes = [-1,0,1]
        return [Action(lane, speed, 0) for lane in all_lanes for speed in all_speeds]
    # need to redo speed calculations, action_speed or whatever is the NEW SPEED
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
        if action.laneChange == center:
            points += 10

        # Next to 'ifs' compute the 'cost' to switch to the lane
        if action.laneChange == right:
            points += 8 / (2 ** lane.right[1])

        if action.laneChange == left:
            points += 8 / (2 ** lane.left[1])
        # add a bit about -50 if the lane change cost is greater than lane_change_abiding
        desired_speed = 6 + self.law_abiding_speed
        after_action_speed = self.speed + action.speedChange
        # penalized for not being at the speed you like. 
        # The *1 is to make sure that people want to change lanes if 
        # they go too slow. Might want to make that a personality variable.
        points += (6 - abs(desired_speed - after_action_speed)) * 1


        # will never ever slam into the end of a lane
        if after_action_speed == 0:
            if action.laneChange == center:
                return -10
            else:
                return -15
        # gets the lane to be the right one
        lane_approaching = (lane, 0)
        if action.laneChange == right:
            lane_approaching = lane.right
        elif action.laneChange == left:
            lane_approaching = lane.left
        # The next two 'ifs' set up whether the lane you are moving to (or are in)
        # is a good place to be.
        if lane_approaching == 0:
            return -10001
        if lane_approaching[0].lane_end == 0 and \
           len(lane.lane_spots) < after_action_speed + self.lane_spot_index:
               return -10002
        # if they are near the end of a lane, they get penalities, and want to leave it.
        if lane_approaching[0].lane_end == 0 and \
           len(lane.lane_spots) < 2 * after_action_speed + self.lane_spot_index:
               points += -5 
        if lane_approaching[0].lane_end == 0 and \
           len(lane.lane_spots) < 3 * after_action_speed + self.lane_spot_index:
               points += -3

        return points
    
    def get_adjacent_cars_likely_destinations(self, lane):
        
 
    def evaluate_action(self, lane, action):
        # returns the utility of the action, evaluating it relative
        #  to the other cars. 
        # Notes: Crash == 0
        # gets neighboring cars (2 lanes left, 2 right, 1 forward)
        #     This should be an argument       
        # guesses where they will go, anywhere they will crash gets a
        #   0. 
        return "Incomplete"
