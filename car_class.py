"""
This file will contain the Car class, and its move function, 
which returns an Action, the class which defines what the Car
does. The Car is mostly a shell class containing things about
the 'personality' of the driver, while its move function does the
heavy lifting.

"""


# The 'enums' for right, left, center
right  = -1
left   =  1
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
        
        self.index = index
        self.action_list = self.all_actions()
        
    # add a variable for self driving cars for them being more likely
    # to prefer the truly best action.
    def move(self, board):
        action = Action(center, self.speed, 0)
        self.speed = action.speedChange
        self.action_list = self.all_actions()
        likely_destinations = self.get_adjacent_cars_likely_destinations(board)
        best_actions = self.return_ten_best_actions(board)
        return max([self.evaluate_action(action, utility, likely_destinations) for 
                    (action, utility) in best_actions], key=lambda (m, u) :  -u)


    def return_ten_best_actions(self, board):
        ls = [(action, self.evaluate_action_blind(board, action))
              for action in self.action_list]
        ls = [(a,b) for (a,b) in ls if b > -100]
        ls = sorted(ls, key = lambda (a,b) : -b)
        return ls[0:min(10, len(ls))]

    def all_actions(self):
        all_speeds = range(self.speed + self.acceleration + 1)
        all_lanes = [-1,0,1]
        return [Action(lane, speed, 0) for lane in all_lanes for speed in all_speeds]



    # TODO need to incorporate the various parameters into the model
    # TODO fix issues with lane_end (new type)
    def evaluate_action_blind(self, board, action):
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
            points += 8 / (2 ** board[car.index[0]][car.index[1]].rightWeight)

        if action.laneChange == left:
            points += 8 /  (2 ** board[car.index[0]][car.index[1]].leftWeight)
        # add a bit about -50 if the lane change cost is greater than lane_change_abiding
        desired_speed = 6 + self.law_abiding_speed
        after_action_speed = action.speedChange
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
        # puts the right lane spot for examining how far too go. 
        lane_index = car.index[1] + action.laneChange
        # The next two 'ifs' set up whether the lane you are moving to (or are in)
        # is a good place to be.
        if lane_index > len(board[0]) or lane_index < 0:
            return -10001
        # This says: If the lane in front of you ends, and you go over it, its bad.
        # If the lane 'continues' which means it doesn't end in a None, 
        # its a happy place to go.
        if board[-1][lane_index] is None:
            if len(board) < (self.index[0] + after_action_speed):
                return -10003
            #if it is an illegal space, bad.
            if board[self.index[0] + after_action_speed][lane_index] is None:
                return -10002
            # if they are near the end of a lane, they get penalities, and want to leave it.
            if len(board) < 2 * after_action_speed + self.index[0]:
                points += -5 
            if len(board) < 3 * after_action_speed + self.index[0]:
                  points += -3

        return points
    
    def get_adjacent_cars_likely_destinations(self, board):
         # find rad 2 cars.
         pos_s = [(x,y) for x in range(-2,3) for y in range(-2,3)
                  if 0 <= self.index[0] + x <= len(board) and 
                     0 <= self.index[1] + y <= len(board[0])
                     and (x,y) == (0,0) ]
         cars = [board[x][y] for (x,y) in pos_s if board[x][y] is not None]
         possible_moves = [(car, car.return_ten_best_actions(board)) for car in cars]
         places = {}
         for (car, car_moves) in possible_moves:
             for (action, utility) in car_moves:
                 x = car.index[0] + action.laneChange
                 y = car.index[1] + action.speedChange
                 if (x,y) in places:
                     places[(x,y)] += utility
                 else:
                     places[(x,y)] = utility
         # make dict saying where they will go, with counts
         # return that shit.
         return places
 
    def evaluate_action(self, action, utility,  actions_of_others):
        pos_x  = self.index[0] + action.speedChange
        pos_y = self.index[1] + action.laneChange
        o_score = 0
        if (pos_x, pos_y) in actions_of_others:
            o_score = actions_of_others[(pos_x,pos_y)] 
        return (action, utility - o_score/2)

