class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
       import heapq
       n=len(points)
       pq=[]
       heapq.heappush(pq,(0,0))
       visited=set()
       
       total=0
       while pq and len(visited)<n:
        cost,i=heapq.heappop(pq)
        if i in visited:
            continue
        visited.add(i)
        total+=cost
        x1,y1=points[i]
        for j in range(n):
            if j not in visited:
                x2,y2=points[j]
                distance=abs(x1-x2)+abs(y1-y2)
                heapq.heappush(pq,(distance,j))
       return total


        