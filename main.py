"""
This file is the main script of the simulation. It will move every car according to
road conditions (other cars, new lanes, stopping at toll booths, etc)
"""


def advancement(actions, laneSegment):
    for action in actions:
        car = action[0]    
        carAction = action[1]
        if carAction.stopTime != 0:
            laneSegment[car.lane_spot_index] = 0
            nextIdx = car.lane_spot_index + carAction.speedChange          #####
            if nextIdx > len(laneSegment.lane_spots):
                nextIdx %= len(laneSegment.lane_spots)
            if carAction.laneChange == -1:
                laneSegment = laneSegment.lane_end[0]
            elif carAction.laneChange == -1:
                laneSegment = laneSegment.lane_end[1]
            elif carAction.laneChange == -1:
                laneSegment = laneSegment.lane_end[2]
            laneSegment[nextIdx] = car
        else:
            carAction.stopTime -= 1



roadPieces1 = []  #list of lane_segments
roadPieces2 = []  #list of land_segments
roads = (roadPieces1, roadPieces2)

curRoad = 0
timeDuration = 10
for x in range(0, timeDuration):
    actions = []
    for piece in roads[curRoad]:
        for spot in piece.lane_spots:
            if spot != 0:
                actions.append([spot, spot.move(piece)])
    advancement(actions, boards[1-curRoad])
    curRoad = 1 - curRoad 
