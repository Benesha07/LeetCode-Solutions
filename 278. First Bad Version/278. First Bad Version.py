#
# Problem: 278. First Bad Version
# Difficulty: Easy
# Link: https://leetcode.com/problems/first-bad-version/submissions/2169203226/
# Language: python3
# Date: 2026-10-11


# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        right=n
        left=1
        while left<right :
            mid=(left+right)//2
            if isBadVersion(mid):
                right= mid
            else:
                left=mid+1
        return left
