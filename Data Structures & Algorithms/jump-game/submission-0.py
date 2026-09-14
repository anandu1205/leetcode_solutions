class Solution:
    def canJump(self, nums: List[int]) -> bool:

        n = len(nums)

        # dp[i] = True if we can reach index i
        dp = [False] * n

        # We start at index 0
        dp[0] = True

        for i in range(n):

            # If index i is reachable
            if dp[i]:

                # Try every position we can jump to
                for j in range(i + 1, min(n, i + nums[i] + 1)):
                    dp[j] = True

        return dp[n - 1]
        