class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if(max(nums)<=0):
            return 1
        elif(min(nums)>1):
            return 1
        else:
            nums.sort()
            s=set(nums)
            for i in range(1,max(nums)):
                if(i not in s ):
                    return i
            return max(s)+1
        