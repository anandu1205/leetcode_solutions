class Solution:

    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:

        from collections import deque

        q = deque([0])
        visited = [False] * len(s)
        visited[0] = True

        while q:

            index = q.popleft()

            if index == len(s) - 1:
                return True

            max_jumpos = min(index + maxJump, len(s) - 1)
            min_jumpos = index + minJump

            for i in range(min_jumpos, max_jumpos + 1):

                if s[i] == '0' and not visited[i]:
                    visited[i] = True
                    q.append(i)

        return False

        