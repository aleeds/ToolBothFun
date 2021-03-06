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
        retRoad.append(rowToAdd)
    return retRoad



road = readInBoard("road1")
#road = readInBoard("road2")
#road = readInBoard("road3")
#road = readInBoard("road4")



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

def printWholeRoad(road):
    for row in road:
	print [str(spot) for spot in row]



printWholeRoad(road)



lenOfLane = 100
road = []

for L_p in [5, 8, 9, 10]:
   for B_p in [3, 4, 5]:
        road = []
        if B_p > L_p:
            break
	B = B_p
	L = L_p

	for i in range(0, L - B + 1):
		print(L - i)
		print(i)
		for x in range(0,lenOfLane):
		    lstToAdd = []
		    for y in range(0,L - i):
			lstToAdd.append(RoadNode(None, 0, 0, 0))
		    for y in range(0,i):
			lstToAdd.append(None)
		    road.append(lstToAdd)

	"""
	#shaves off lanes on the left

	B = 3
	L = 8


	for i in range(0, L - B + 1):
		for x in range(0,lenOfLane):
		    lstToAdd = []
		    for y in range(0,i):
			lstToAdd.append(RoadNode(None, 0, 0, 0))
		    for y in range(0,L - i):
			lstToAdd.append(None)
		    road.append(lstToAdd)
	"""



	"""
	#triangle shaped board
	B = 3
	L = 8
	for i in range(0, L - B + 1):
		for x in range(0,lenOfLane):
		    lstToAdd = []
		    for y in range(0,i):
			lstToAdd.append(None)
		    for y in range(i,L - i):
			lstToAdd.append(RoadNode(None, 0, 0, 0))
		    for y in range(L - i,8):
			lstToAdd.append(None)
		    road.append(lstToAdd)

	"""            









	#car: speed, recklessness[0,1], following_distance[1,5], acceleration[1,3], braking, law_abiding_speed[-2,2],law_abiding_lane_changes[0,10],index

        cars = []
	#printRoad(road)

	def gen_car():
	    return Car(0,0,1,3,-10,0,0,[0,0])

	js_data = {"car_lifespan":[], "hcri_inc":[], "hcri_total":[]}
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
	    #print laneEnds
	    return laneEnds


	#printRoad(road)


	road_ends = findNearestLaneEnd(road)


	lcst = 0
	lcgt = 0
	rest = 0
	regt = 0

	def findHCRI(cars, road):
	    # this is the rear end chunk
	    global lcst
	    global lcgt
	    global rest
	    global regt
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
		    #print "dist: " + str(dist) + " sD: " + str(speedDiff) + " RE: " + str(float(dist)/speedDiff)
		RE = float(dist)/speedDiff
		if 0 < RE < 2.3:
		    RE_serious += 1
		elif 2.3 <= RE < 4.7:
		    RE_general += 1
		#print (dist, str(car), RE)
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
	    lcst += LC_serious 
	    lcgt += LC_general
	    rest += RE_serious
	    regt += RE_general
	    return (0.65 * LC_serious + 0.35 * LC_general) * 0.46 + (0.62 * RE_serious + 0.38 * RE_general) * 0.54








	#printRoad(road)
	findHCRI(cars, road)
	print [(str(car), car.speed) for car in cars]

	#printWholeRoad(road)
	lane_probabilities = [1.0]*B ############
	total_HCRI = 0
	timeSteps = 360
	import random
	file = open("carPositions_" + str(B)+ "_" + str(L) + ".txt", "w")
        file.write("Height: " + str(len(road[0])) + "\n")
        file.write("Width: " + str(len(road)) + "\n")
	for time in range(0, timeSteps):
	    actions = []
	    for car in cars:
		actions.append((car, car.move(road)))
	    advancement(road, actions)
	    print time
	    #printRoad(road)
	    for i in range(len(lane_probabilities)):
                t = random.random() < lane_probabilities[i]
                assert(t)
		if  t and road[0][i].car == None:
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
	    js_data["hcri_inc"].append(t)
	    total_HCRI += t
	    js_data["hcri_total"].append(total_HCRI)

	    for car in cars:
		file.write(str(car) + "-")
	    file.write("\n")
	file.close()

	print("\n\n\n\n\n\n\n\n\ntotalHCRI\n\n\n\n\n\n\n\n\n")
	print(total_HCRI)
	print("Total RE Serious")
	print rest
	print "Total RE general"
	print regt
	print "Total LC serious"
	print lcst
	print "Total LC general"
	print lcgt


	print" "
	print" "
	print" "

	with open("data_" + str(B)+ "_" + str(L) + ".json", "w+") as f:
	    f.write(json.dumps(js_data))
