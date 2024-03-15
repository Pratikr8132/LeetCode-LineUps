class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
		# calculates total product of the array
        product = reduce(lambda a, b : a * b, nums)
		
		# if product == 0, that means 0 is present
        if product == 0:
			
			# create a zero array of same length
            res = [0] * len(nums)
            
			# find locations of zeros
            idx = [idx for idx, e in enumerate(nums) if e == 0]
            
			# if more than one zero is present then return zeros or res
            if len(idx) > 1:
                return res
            
			# replace zero with 1, to calculate total product
            nums[idx[0]] = 1
            
			# again calculate the product after replacing the 
			# single zero present by 1
            product = reduce(lambda a, b : a * b, nums)
			
			# calculate result
            res[idx[0]] = product
            
            return res
            
		# if there is no zero present, we can just replace each element 
		# by dividing the total product with the respective element's value.
        else: 
            for i in range(len(nums)):
                nums[i] = product // nums[i]
                
            return nums