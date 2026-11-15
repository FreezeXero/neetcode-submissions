class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}

        for i, num in enumerate(nums):
            x = target - num
            if x not in seen:
                seen[num] = i
            else:
                return [seen[x], i]
        
        


            

        