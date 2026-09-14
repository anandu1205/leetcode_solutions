class Solution:
    def jump(self, nums: List[int]) -> int:

        # dp[i] = minimum number of jumps needed to reach index i

        n = len(nums)

        INF = float('inf')
        dp = [INF] * n

        # Already at index 0
        dp[0] = 0

        for i in range(n):

            for j in range(i + 1, min(n, i + nums[i] + 1)):

                dp[j] = min(dp[j], dp[i] + 1)

        return dp[n - 1]
        