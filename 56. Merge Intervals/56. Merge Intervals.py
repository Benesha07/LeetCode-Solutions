#
# Problem: 56. Merge Intervals
# Difficulty: Medium
# Link: https://leetcode.com/problems/merge-intervals/submissions/
# Language: python3
# Date: 2026-10-09


class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()

        i = 0

        while i < len(intervals) - 1:

            if intervals[i][1] >= intervals[i+1][0]:
                intervals[i][1] = max(intervals[i][1], intervals[i+1][1])
                intervals.pop(i+1)
            else:
                i += 1

        return intervals
