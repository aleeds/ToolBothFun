"""
This file is the main script of the simulation. It will move every car according to
road conditions (other cars, new lanes, stopping at toll booths, etc)
"""

from lane_segments import LaneSegment
from car_class import Car


def advancement(actions):
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
timeDuration = 20
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





