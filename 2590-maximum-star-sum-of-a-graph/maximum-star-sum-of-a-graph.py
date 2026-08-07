class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        # if len(vals)==1 or 0:
        #     return vals[0]
        graph=defaultdict(list)
        for u,v in edges:
            graph[u].append(vals[v])
            graph[v].append(vals[u])
        # ans=0
        ans = float("-inf")
        for i in range(len(vals)):
            neighbours=sorted(graph[i],reverse=True)
            curr=vals[i]
            for j in range(min(k,len(neighbours))):
                if neighbours[j]>0:
                    curr+=neighbours[j]
            ans=max(ans,curr)
        return ans
        
        

        