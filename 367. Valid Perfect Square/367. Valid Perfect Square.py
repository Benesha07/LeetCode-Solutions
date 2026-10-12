#
# Problem: 367. Valid Perfect Square
# Difficulty: Easy
# Link: https://leetcode.com/problems/valid-perfect-square/submissions/2170051474/
# Language: python3
# Date: 2026-10-12


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left =1
        right=num
        while left<=right:
            mid=(left+right)//2
            if mid*mid==num:
                return True
            elif mid*mid>num:
                right=mid-1
            else:
                left=mid+1
        return False
