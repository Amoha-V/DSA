class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tank=0
        index=0
        if sum(gas)<sum(cost):
            return -1
        for i in range(len(gas)):
            tank+=gas[i]-cost[i]
            if tank<0:
                index=i+1
                tank=0
        return index

        