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
            return "<" + str(self.car) + "," + str((self.leftWeight, self.midWeight,self.rightWeight)) + ">"
        else:
            return "< Road    " + str((self.leftWeight, self.midWeight, self.rightWeight)) + ">"


lenOfLane = 20
road = []
"""
#shaves off lanes on the right

for x in range(0,lenOfLane):
    lstToAdd = []
    for y in range(0,8):
        lstToAdd.append(RoadNode(None, 0, 0, 0))
    road.append(lstToAdd)

for x in range(0,lenOfLane):
    lstToAdd = []
    for y in range(0,7):
        lstToAdd.append(RoadNode(None, 0, 0, 0))
    for y in range(0,1):
        lstToAdd.append(None)
    road.append(lstToAdd)

for x in range(0,lenOfLane):
    lstToAdd = []
    for y in range(0,6):
        lstToAdd.append(RoadNode(None, 0, 0, 0))
    for y in range(0,2):
        lstToAdd.append(None)
    road.append(lstToAdd)

for x in range(0,lenOfLane):
    lstToAdd = []
    for y in range(0,5):
        lstToAdd.append(RoadNode(None, 0, 0, 0))
    for y in range(0,3):
        lstToAdd.append(None)
    road.append(lstToAdd)

for x in range(0,lenOfLane):
    lstToAdd = []
    for y in range(0,4):
        lstToAdd.append(RoadNode(None, 0, 0, 0))
    for y in range(0,4):
        lstToAdd.append(None)
    road.append(lstToAdd)

for x in range(0,lenOfLane):
    lstToAdd = []
    for y in range(0,3):
        lstToAdd.append(RoadNode(None, 0, 0, 0))
    for y in range(0,5):
        lstToAdd.append(None)
    road.append(lstToAdd)


"""

"""
#shaves off lanes on the left

for x in range(0,lenOfLane):
    lstToAdd = []
    for y in range(0,8):
        lstToAdd.append(RoadNode(None, 0, 0, 0))
    road.append(lstToAdd)

for x in range(0,lenOfLane):
    lstToAdd = []
    for y in range(0,1):
        lstToAdd.append(None)
    for y in range(0,7):
        lstToAdd.append(RoadNode(None, 0, 0, 0))
    road.append(lstToAdd)

for x in range(0,lenOfLane):
    lstToAdd = []
    for y in range(0,2):
        lstToAdd.append(None)
    for y in range(0,6):
        lstToAdd.append(RoadNode(None, 0, 0, 0))
    road.append(lstToAdd)

for x in range(0,lenOfLane):
    lstToAdd = []
    for y in range(0,3):
        lstToAdd.append(None)
    for y in range(0,5):
        lstToAdd.append(RoadNode(None, 0, 0, 0))
    road.append(lstToAdd)

for x in range(0,lenOfLane):
    lstToAdd = []
    for y in range(0,4):
        lstToAdd.append(None)
    for y in range(0,4):
        lstToAdd.append(RoadNode(None, 0, 0, 0))
    road.append(lstToAdd)

for x in range(0,lenOfLane):
    lstToAdd = []
    for y in range(0,5):
        lstToAdd.append(None)
    for y in range(0,3):
        lstToAdd.append(RoadNode(None, 0, 0, 0))
    road.append(lstToAdd)

"""




"""
#triangle shaped board
for x in range(0,lenOfLane):
    lstToAdd = []
    for y in range(0,8):
        lstToAdd.append(RoadNode(None, 0, 0, 0))
    road.append(lstToAdd)
for x in range(0,lenOfLane):
    lstToAdd = []
    for y in range(0,1):
        lstToAdd.append(None)
    for y in range(1,7):
        lstToAdd.append(RoadNode(None, 0, 0, 0))
    for y in range(7,8):
        lstToAdd.append(None)
    road.append(lstToAdd)
for x in range(0,lenOfLane):
    lstToAdd = []
    for y in range(0,2):
        lstToAdd.append(None)
    for y in range(2,6):
        lstToAdd.append(RoadNode(None, 0, 0, 0))
    for y in range(6,8):
        lstToAdd.append(None)
    road.append(lstToAdd)
for x in range(0,lenOfLane):
    lstToAdd = []
    for y in range(0,3):
        lstToAdd.append(None)
    for y in range(3,6):
        lstToAdd.append(RoadNode(None, 0, 0, 0))
    for y in range(6,8):
        lstToAdd.append(None)
    road.append(lstToAdd)
"""            



def readInBoard(fileName):
    retRoad = []
    file = open(fileName, "r")
    allTwos = {}
    xIdx = 0
    for line in file:
        rowToAdd = []
        yIdx = 0
        for spot in line:
            if spot == "0":
                rowToAdd.append(None)
            elif spot == "1" or spot == "2":
                rN = RoadNode(None, 0, 0, 0)
                if spot == "2":
                    rN.leftWeight = 5
                    rN.rightWeight = 5
                rowToAdd.append(rN)
            yIdx += 1
        xIdx += 1
        print allTwos
        retRoad.append(rowToAdd)
    return retRoad


#road = readInBoard("road1")
road = readInBoard("road2")


print ""
def printRoad(road):
    i = len(road) - 1
    row = road[i]
    while all(road == None or road.car == None for road in row):
        i += -1
        if i == -1:
            break
        row = road[i]
    for q in range(0, i):
        print [str(n) for n in road[q]]

print "========"

def printWholeRoad(road):
    for row in road:
        print [str(spot) for spot in row]



printWholeRoad(road)



file = open("board.txt", "w")
for row in road:
    file.write(str([str(n) for n in row]))
    file.write("\n")
file.close()


#car: speed, recklessness[0,1], following_distance[1,5], acceleration[1,3], braking, law_abiding_speed[-2,2],law_abiding_lane_changes[0,10],index

cars = [Car(0, 0, 1, 3, -10, 0, 0, [3,1]), Car(0, 0, 1, 3, -10, 0, 0, [0, 1]),
        Car(0, 0, 1, 3, -10, 0, 0, [5,1]), Car(0, 0, 1, 3, -10, 0, 0, [7, 1]),
        Car(0, 0, 1, 3, -10, 0, 0, [9,1]), Car(0, 0, 1, 3, -10, 0, 0, [11, 1]),
        Car(0, 0, 1, 3, -10, 0, 0, [0,0]), Car(0, 0, 1, 3, -10, 0, 0, [1, 2]),
        Car(0, 0, 1, 3, -10, 0, 0, [0,4]), Car(0, 0, 1, 3, -10, 0, 0, [0, 6]),
        Car(0, 0, 1, 3, -10, 0, 0, [3,5]), Car(0, 0, 1, 3, -10, 0, 0, [1, 7])]
for car in cars:
   road[car.index[0]][car.index[1]].car = car
#printRoad(road)

def gen_car():
    return Car(0,0,1,3,-10,0,0,[0,0])

js_data = {"car_lifespan":[]}
def advancement(road, actions):
    #advances all cars in the road
    #print("Moves:\n\n")
    actions = sorted(actions, key = lambda (car, carAction) : -(car.index[0] + carAction.speedChange))
    for (car, carAction) in actions:
        road[car.index[0]][car.index[1]].car = None
        a = car.index[0] + carAction.speedChange          
        b = car.index[1] + carAction.laneChange
        car.index = [a,b]
        #print("Where da car goes")
        #print (a,b)
        try:
            road[car.index[0]][car.index[1]].car = car
        except IndexError:
            print "REMOVING: " + str(car)
            print "Car - speed: " + str(car.speed)
            print "      recklessness: " + str(car.recklessness)
            print "      following dist: " + str(car.following_distance)
            print "      accel: " + str(car.acceleration)
            js_data["car_lifespan"].append(car.alive)
            cars.remove(car)



import json
def findNearestLaneEnd(road):
    laneEnds = {}
    xLen = len(road)
    yLen = len(road[0])
    for y in range(0, yLen):
        laneEnds[y] = 100000000
        for x in range(0, len(road)):
            if road[x][y] == None:
                laneEnds[y] = x
                break
    print laneEnds
    return laneEnds


#printRoad(road)


road_ends = findNearestLaneEnd(road)

def findHCRI(cars, road):
    # this is the rear end chunk


    RE_serious = 0
    RE_general = 0
    for car in cars:
        nearestCar = None
        for curIdx in range(car.index[0]+1, len(road)):
            if road[curIdx][car.index[1]] == None:
                break
            if road[curIdx][car.index[1]].car:
                nearestCar = road[curIdx][car.index[1]].car
                break
        dist = 0
        speedDiff = 1
        if nearestCar and nearestCar.speed < car.speed:
            dist = nearestCar.index[0] - car.index[0] - 1
            speedDiff = car.speed - nearestCar.speed
            print "dist: " + str(dist) + " sD: " + str(speedDiff) + " RE: " + str(float(dist)/speedDiff)
        RE = float(dist)/speedDiff
        if 0 < RE < 2.3:
            RE_serious += 1
        elif 2.3 <= RE < 4.7:
            RE_general += 1
        print (dist, str(car), RE)
    # for lane change issues

    LC_serious = 0
    LC_general = 0
    for car in cars:
        if car.speed == 0:
            break
        cars_nearby = car.get_nearest_cars(road, range(-5,1), range(-1,2))
        cars_near_speed = [car_near for car_near in cars_nearby 
                                        if car_near.speed == car.speed]
        
        for car_near in cars_near_speed:
            v =  (0.0 + road_ends[car.index[1]])/car.speed 
            if 0 < v < 2.8:
                LC_serious += 1
            elif 2.8 <= v < 4.7:
                LC_general += 1
    return (0.65 * LC_serious + 0.35 * LC_general) * 0.46 + (0.62 * RE_serious + 0.38 * RE_general) * 0.54








printRoad(road)
findHCRI(cars, road)
print [(str(car), car.speed) for car in cars]


lane_probabilities = [1.0]*8
total_HCRI = 0
timeSteps = 360
import random
file = open("carPositions.txt", "w")
for time in range(0, timeSteps):
    actions = []
    for car in cars:
        actions.append((car, car.move(road)))
    advancement(road, actions)
    print time
    printRoad(road)
    for i in range(len(lane_probabilities)):
        if random.random() < lane_probabilities[i] and road[0][i].car == None:
            car = gen_car()
            car.index[0] = 0
            car.index[1] = i
            road[0][car.index[1]].car = car
            cars.append(car)
            lane_probabilities[i] = 1.0
        else:
            lane_probabilities[i] += 1.0/4
    
    print("THE HCRI \n\n")
    t = findHCRI(cars, road)
    total_HCRI += t

    for car in cars:
        file.write(str(car) + "-")
    file.write("\n")
file.close()

print("\n\n\n\n\n\n\n\n\ntotalHCRI\n\n\n\n\n\n\n\n\n")
print(total_HCRI)

print" "
print" "
print" "

with open("data.json", "w+") as f:
    f.write(json.dumps(js_data))







