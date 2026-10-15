#
# Problem: 779. K-th Symbol in Grammar
# Difficulty: Medium
# Link: https://leetcode.com/problems/k-th-symbol-in-grammar/submissions/2173215591/
# Language: python3
# Date: 2026-10-15


class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n==1:
            return 0
        ans=0
        while n>1:
            mid=2**(n-2)

            if k>mid:
                ans=1-ans
                k-=mid
            n-=1
        return ans

            

        
