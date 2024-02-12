# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         from collections import Counter

#         counterr=Counter(nums)

#         itemm,valuee=0,0
#         for item,value in counterr.items():


#             if value>valuee:
#                 itemm=item
#                 valuee=value
#         return itemm
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        np = sorted(nums)
        return np[n//2]