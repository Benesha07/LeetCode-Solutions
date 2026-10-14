#
# Problem: 50. Pow(x, n)
# Difficulty: Medium
# Link: https://leetcode.com/problems/powx-n/submissions/2172249636/
# Language: python3
# Date: 2026-10-14


class Solution:
    def myPow(self, x: float, n: int) -> float:
        # sq=x**n
        # return sq
        # 2nd method
        # if n<0:
        #     x=1/x
        #     n=-n
        # ans=1
        # while n>0:
        #     if n%2==1:
        #         ans*=x
        #     x*=x
        #     n//=2
        # return ans

        negative = n < 0
        n = abs(n)

        ans = 1.0

        while n > 0:
            if n % 2 == 1:
                ans *= x

            x *= x
            n //= 2

        if negative:
            return 1 / ans

        return ans
