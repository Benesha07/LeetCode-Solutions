#
# Problem: 162. Find Peak Element
# Difficulty: Medium
# Link: https://leetcode.com/problems/find-peak-element/submissions/2171403390/
# Language: python3
# Date: 2026-10-13


class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        right=len(nums)-1
        left=0
        while left<right:
            mid=(left+right)//2
            if nums[mid]<nums[mid+1]:
                left=mid+1
            else:
                right=mid
        return left
        
