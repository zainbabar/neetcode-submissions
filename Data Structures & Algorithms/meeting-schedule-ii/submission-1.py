"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        rooms = []
        for interval in intervals:
            # no room yet i.e. we are the first interval
            if not rooms:
                heapq.heappush(rooms, interval.end)
                continue

            # meetings are sorted by start time, so we want the soonest
            # free room b/c any meeting after this starts later

            # look at the soonest free room and see if its free before we start
            if interval.start >= rooms[0]:
                # if it is then replace that soonest end time with our end time
                heapq.heappop(rooms)
                heapq.heappush(rooms, interval.end)
            # no room is free before we end so we should add our end time 
            # as another orom
            else:
                heapq.heappush(rooms, interval.end)
           
        return len(rooms)
                
            


