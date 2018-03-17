# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        s=newInterval.start
        e=newInterval.end
        i=0
        res=[]
        while i<len(intervals) and intervals[i].end<s:
            res.append(intervals[i])
            i+=1
        while i<len(intervals) and intervals[i].start<=e:
            s=min(intervals[i].start,s)
            e=max(intervals[i].end,e)
            i+=1
        res.append(Interval(s,e))
        res.extend(intervals[i:])
        return res