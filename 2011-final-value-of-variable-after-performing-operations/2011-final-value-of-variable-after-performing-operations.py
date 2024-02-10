class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        dp={"++X":1 , "X++":1,"--X":-1 ,"X--":-1}
        
        ans=0
        for i in operations:
            ans+=dp[i]
        return ans