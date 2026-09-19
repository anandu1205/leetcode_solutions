class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost)>sum(gas):
            return -1
        n=len(gas)
        start=0
        total=0
        for i in range(n):
            value=gas[i]-cost[i]
            total+=value
            if total<0:
                start=i+1
                total=0
                
        return start