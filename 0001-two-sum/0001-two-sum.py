class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct = {}
        i = 0
        while True:
            dct[nums[i]] = i
            i += 1
            if target - nums[i] in dct:
                print(dct)

                return [dct[target - nums[i]], i]