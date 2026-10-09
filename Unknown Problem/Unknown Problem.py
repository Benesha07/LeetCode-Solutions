#
# Problem: Unknown Problem
# Difficulty: Medium
# Link: https://leetcode.com/problems/non-overlapping-intervals/submissions/2167486677/
# Language: python3
# Date: 2026-10-09


class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort()
        add=0
        end=intervals[0][1]
        for i in range(1,len(intervals)):
            if intervals[i][0]<end:
                add+=1
                end=min(end,intervals[i][1])
            else:
                end=intervals[i][1]
        return add

        
