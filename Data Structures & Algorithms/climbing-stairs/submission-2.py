class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def helper(i):
            # base case
            if i == 1 or i == 2:
                return i
            # already computed? look it up
            if i in memo:
                return memo[i]
            # compute, store, then return
            memo[i] = helper(i - 1) + helper(i - 2)
            return memo[i]

        return helper(n)