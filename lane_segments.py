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
    
    :arg left 
        LaneSegment to the Left, with costs (or nill)
    :type (LaneSegment, int)
    
    :arg right 
        LaneSegment to the right, with costs (or nill)
    :type (LaneSegment, int)

    :arg lane_end 
        What it can progress into. 0 if it ends
    :type (string, (LaneSegment, int) OR TollBooth OR 0)
          The string is to identify where it can move to
          string= "Lane" if LaneSegment
                = "Toll" if TollBooth
                = "Nill" if 0
    """
    def __init__(self, lane_spots, left, right, lane_end):
        self.lane_spots = lane_spots
        self.left = left
        self.right = right
        self.lane_end = lane_end
    def __str__(self):
        return str(self.lane_spots)

