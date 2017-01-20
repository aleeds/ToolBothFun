"""
This file is the main script of the simulation. It will move every car according to
road conditions (other cars, new lanes, stopping at toll booths, etc)
"""


def advancement(actions, road):
    for action in actions:
        #todo

roadPieces1 = []
roadPieces2 = []
roads = (roadPieces1, roadPieces2)

curRoad = 0
timeDuration = 10
for x in range(0, timeDuration):
    actions = []
    for piece in roads[curRoad]:
        for spot in piece.lane_spots:
            if spot != 0:
                actions.append(spot.move(roads[1-curRoad]))
    advancement(actions, boards[1-curRoad])
    curRoad = 1 - curRoad 
