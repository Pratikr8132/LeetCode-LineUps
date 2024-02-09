class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=list(set(nums))
        nums.sort()
        ans=0
        i=0
        temp=1
        print(nums)
        while i<len(nums)-1:
    
            
            if nums[i]==nums[i+1]-1:
                temp+=1
                i+=1
            else:
                
                ans=max(ans,temp)
                temp=1
                i+=1
        ans=max(ans,temp)
        if len(nums)==0:
            return 0
        return ans

