#
# Problem: 179. Largest Number
# Difficulty: Medium
# Link: https://leetcode.com/problems/largest-number/description/
# Language: python3
# Date: 2026-10-09


class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        n=len(nums)
        for i in range(n):
            nums[i]=str(nums[i])
        
        for i in range(n):
            for j in range(n-1-i):
                if nums[j+1]+nums[j]>nums[j]+nums[j+1]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]
        result=''.join(nums)
        
        if result[0]=='0':
            return "0"
        return result
