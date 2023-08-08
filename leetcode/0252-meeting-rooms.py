# https://www.lintcode.com/problem/920/

from typing import List


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """

    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda item: item.start)
        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i - 1].end:
                return False
        return True


sol = Solution()
assert (
    sol.can_attend_meetings(
        intervals=[Interval(0, 30), Interval(15, 20), Interval(5, 10)]
    )
    == False
)
assert sol.can_attend_meetings(intervals=[Interval(5, 8), Interval(9, 15)]) == True
