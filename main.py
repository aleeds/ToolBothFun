"""
This file is the main script of the simulation. It will move every car according to
road conditions (other cars, new lanes, stopping at toll booths, etc)
"""

from lane_segments import LaneSegment
from car_class import Car


class RoadNode:
    def __init__(self, car, leftWeight, midWeight, rightWeight):
        self.car = car
        self.leftWeight = leftWeight
        self.midWeight = midWeight
        self.rightWeight = rightWeight

    def __str__(self):
        if self.car != None:
            return "<" + "car" + "," + str(self.leftWeight) + "," + str(self.midWeight) + "," + str(self.rightWeight) + ">"
        else:
            return str((self.leftWeight, self.midWeight, self.rightWeight))


road = []

for x in range(0,20):
    lstToAdd = []
    for y in range(0,8):
        lstToAdd.append(RoadNode(None, 0, 0, 0))
    road.append(lstToAdd)

for x in range(0,20):
    lstToAdd = []
    for y in range(0,6):
        lstToAdd.append(RoadNode(None, 0, 0, 0))
    for y in range(0,2):
        lstToAdd.append(None)
    road.append(lstToAdd)

for x in range(0,20):
    lstToAdd = []
    for y in range(0,4):
        lstToAdd.append(RoadNode(None, 0, 0, 0))
    for y in range(0,4):
        lstToAdd.append(None)
    road.append(lstToAdd)


for x in range(0,20):
    lstToAdd = []
    for y in range(0,3):
        lstToAdd.append(RoadNode(None, 0, 0, 0))
    for y in range(0,5):
        lstToAdd.append(None)
    road.append(lstToAdd)




    
print ""
def printRoad(road):
    for row in road:
        print [str(n) for n in row]



#car: speed, recklessness[0,1], following_distance[1,5], acceleration[1,3], braking, law_abiding_speed[-2,2],law_abiding_lane_changes[0,10],lane_spot_index

cars = [Car(2, 0, 1, 1, -10, 0, 0, [0,0]), Car(1, 0, 1, 1, -10, 0, 0, [0, 1])]
road[0][0].car = cars[0]
road[0][1].car = cars[1]
printRoad(road)

def advancement(road, actions):
    #advances all cars in the road
    for action in actions:
        car = action[0]    
        carAction = action[1]
        road[car.lane_spot_index[0]][car.lane_spot_index[1]].car = None
        a = car.lane_spot_index[0] + carAction.speedChange          
        b = car.lane_spot_index[1] + carAction.laneChange
        print (a,b)
        car.lane_spot_index = [a,b]
        road[car.lane_spot_index[0]][car.lane_spot_index[1]].car = car


timeSteps = 100
curRoad = 0
for time in range(0, timeSteps):
    actions = []
    for car in cars:
        actions.append((car, car.move(road)))
    advancement(road, actions)
    print time
    printRoad(road)








