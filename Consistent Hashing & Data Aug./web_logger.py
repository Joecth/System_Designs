# Implement a web logger, which provide two methods:

# hit(timestamp), record a hit at given timestamp.
# get_hit_count_in_last_5_minutes(timestamp), get hit count in last 5 minutes.
# the two methods will be called with non-descending timestamp (in sec).

# Example
# Example 1:

# Input:
#   hit(1);
#   hit(2);
#   get_hit_count_in_last_5_minutes(3);
#   hit(300);
#   get_hit_count_in_last_5_minutes(300);
#   get_hit_count_in_last_5_minutes(301);
# Output:
#   2
#   3
#   2
# Example 2:

# Input:
#   hit(1)
#   hit(1)
#   hit(1)
#   hit(2)
#   get_hit_count_in_last_5_minutes(3)
#   hit(300)
#   get_hit_count_in_last_5_minutes(300)
#   get_hit_count_in_last_5_minutes(301)
#   get_hit_count_in_last_5_minutes(302)
#   get_hit_count_in_last_5_minutes(900)
#   get_hit_count_in_last_5_minutes(900)
# Output:
#   4
#   5
#   2
#   1
#   0
#   0
# Notice
# The unit of timestamp is seconds.

# The call to the function is in chronological order, that is to say, timestamp is in ascending order.

from collections import deque
class WebLogger:
    
    def __init__(self):
        # do intialization if necessary
        self.Q = deque()

    """
    @param: timestamp: An integer
    @return: nothing
    """
    def hit(self, timestamp):
        # write your code here
        self.Q.append(timestamp)
        
    """
    @param: timestamp: An integer
    @return: An integer
    """
    def get_hit_count_in_last_5_minutes(self, timestamp):
        # write your code here
        # 对函数的调用是按照时间顺序的, 就是说, timestamp是递增的, 所以單純多了！
        Q = self.Q
        
        while Q and list(Q)[0] <= timestamp - 300:
            Q.popleft()
            
        return len(Q)            
wl = WebLogger()
wl.hit(1)
wl.hit(1)
wl.hit(1)
wl.hit(2)
wl.get_hit_count_in_last_5_minutes(3)
wl.hit(300)
wl.get_hit_count_in_last_5_minutes(300)
wl.get_hit_count_in_last_5_minutes(301)
wl.get_hit_count_in_last_5_minutes(302)
wl.get_hit_count_in_last_5_minutes(900)
wl.get_hit_count_in_last_5_minutes(900)