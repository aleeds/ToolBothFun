"""
This file is the main script of the simulation. It will move every car according to
road conditions (other cars, new lanes, stopping at toll booths, etc)
"""

from lane_segments import LaneSegment
from car_class import Car


"""def advancement(actions):
    #advances all cars in the road
    for action in actions:
        car = action[0]    
        carAction = action[1]
        laneSegment = action[2]
        laneSegment.lane_spots[car.lane_spot_index] = 0
        nextIdx = car.lane_spot_index + carAction.speedChange          #####
        print nextIdx
        if nextIdx >= len(laneSegment.lane_spots):
            nextIdx %= len(laneSegment.lane_spots)
            if laneSegment.lane_end != 0:
                if carAction.laneChange == -1:
                    laneSegment = laneSegment.lane_end[0]
                elif carAction.laneChange == 0:
                    laneSegment = laneSegment.lane_end[1]
                elif carAction.laneChange == 1:
                    laneSegment = laneSegment.lane_end[2]
            else:
                print "=========END OF LINE========"
        laneSegment.lane_spots[nextIdx] = car
        car.lane_spot_index = nextIdx


lst1 = [Car(1, 0, 1, 1, 0, 0, 0, 0),0,0,0,0,0,0,0,0,0]
lst2 = [Car(1, 0, 1, 1, 0, 0, 0, 0),0,0,0,0,0,0,0,0,0]
empty1 = [0,0,0,0,0,0,0,0,0,0]
empty2 = [0,0,0,0,0,0,0,0,0,0]

ls2 = LaneSegment(empty1, None, None, 0)  #list of lane_segments
ls1 = LaneSegment(lst1, None, None, [None, ls2, None])


roadPieces1 = [ls1, ls2]
roadPieces2 = [ls1, ls2]
roads = (roadPieces1, roadPieces2)



curRoad = 0
timeDuration = 1
for x in range(0, timeDuration):
    print x
    actions = []
    for laneSeg in roads[curRoad]:
        for spot in laneSeg.lane_spots:
            if spot != 0:
                actions.append([spot, spot.move(laneSeg), laneSeg])
    advancement(actions)
    print (roads[0][0].lane_spots, roads[0][1].lane_spots)
    curRoad = 1 - curRoad 
"""


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

from copy import copy
timeSteps = 100
roads = (road, copy(road))
curRoad = 0
for time in range(0, timeSteps):
    actions = []
    for car in cars:
        actions.append((car, car.move(roads[curRoad])))
    advancement(road, actions)
    print time
    printRoad(road)








