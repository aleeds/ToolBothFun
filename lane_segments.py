class LaneSegment:
    """
    This will represent a segment of a lane. It shall have a few components.
    First, a list of spots a car could be in. 
        They will be 0 if no car is there, and have a car object otherwise.
    Second, a list of lanes they can move to.
        They will be represented as (pointers to) the object themsleves, so 
        no fiddling needing. We might additionally have a cost factor for this
        so some lanes are 'more expensive' to go into, as if they were on the
        other side of a double white line.
    Third, what the lanes progress into, as direct objects (as in the second one).
        These can be more lanes, if the geometry is shifting (geometry refers to both
          the shape and the cost). It also records what spot in the lane it would shift
          to.
        Toll Booths
        End of the road
    
     
    
    
    :arg lane_spots 
        These are the places a car could be.
    :type List[Car OR 0]
    
    :arg adjacent_lanes 
        These are the lanes next the lane object, with costs
    :type List[(LaneSegment, double)]
    
    :arg lane_end 
        What it can progress into.
    :type List[(LaneSegment, int)] OR List[TollBooth] OR 0
    """
    def __init__(self, lane_spots, adjacent_lanes, lane_end):
        self.lane_spots = lane_spots
        self.adjacent_lanes = adjacent_lanes
        self.lane_end = lane_end



