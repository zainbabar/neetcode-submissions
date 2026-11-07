"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # add all meetings means that no meeting overlaps 
        # start and end of two meetings being the same is fine tho
        # so this means that the end of ith meeting has to be <= the start of the i+1th meanig
        # this means we should get the meetings in order 

        # sort the meetings by their start time 
        intervals.sort(key=lambda x: x.start)
        for i in range(len(intervals) - 1):
            if intervals[i].end > intervals[i+1].start:
                return False 
        
        return True

        