class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        l=[i for i in stones]
        ans=0
        for i in l:
            if jewels.find(i)!=-1:
                ans+=1
        return ans
        
        