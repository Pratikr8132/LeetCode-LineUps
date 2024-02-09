# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         nums=list(set(nums))
#         nums.sort()
#         ans=0
#         i=0
#         temp=1
#         print(nums)
#         while i<len(nums)-1:
    
            
#             if nums[i]==nums[i+1]-1:
#                 temp+=1
#                 i+=1
#             else:
                
#                 ans=max(ans,temp)
#                 temp=1
#                 i+=1
#         ans=max(ans,temp)
#         if len(nums)==0:
#             return 0
#         return ans
def longestConsecutive(nums):
    nums = set(nums)
    res = 0
    for num in nums:
        if num - 1 not in nums:
            nextNum = num + 1
            while nextNum in nums:
                nextNum += 1
            res = max(res, nextNum - num)
    return res

with open('user.out', 'w') as f:
    for case in map(loads, stdin):
        f.write(f"{longestConsecutive(case)}\n")
exit(0)

