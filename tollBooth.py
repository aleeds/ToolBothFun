class TollBooth:
    """
    This class will be the abstract representation of a TollBooth.
    It will have a variety of arguments.
    First, it will have the wait time. This will represent how long a
      car has to wait before it can move on. This should be some
      kind of abstract type which will make it easy to be random. 
    Second, how much the toll costs. This will likely be fixed, but
      we could do something exotic where different lanes cost different
      amounts.
    Third, in the case of moving tolls, how fast they can move through it.
    
    Fourth, whether the toll booth is on or off.
    
    """
    def __init__(self, wait_time, cost, maximum_speed, active):
        self.wait_time = wait_time
        self.cost = cost
        self.maximum_speed = maximum_speed
        self.active = active
        self.occupied = False
%history -f tollBooth.py
