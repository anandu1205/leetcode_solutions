class Solution:

    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:

        n = len(s)

        if s[-1] == '1':
            return False

        dp = [False] * n

        # dp[i] = True if position i is reachable
        dp[0] = True

        for i in range(1, n):

            if s[i] == '1':
                continue

            for j in range(minJump, maxJump + 1):

                if 0 <= i - j < n and dp[i - j]:
                    dp[i] = True
                    break

        return dp[n - 1]