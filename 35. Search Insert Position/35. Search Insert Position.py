#
# Problem: 35. Search Insert Position
# Difficulty: Easy
# Link: https://leetcode.com/problems/search-insert-position/submissions/2168425426/
# Language: python3
# Date: 2026-10-10


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left=0
        n=len(nums)
        right=n-1
    
        while(left<=right):
            mid=(left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid]<target:
                left=mid+1
            elif nums[mid]>target:
                right=mid-1
        return left
