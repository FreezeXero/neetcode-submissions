class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        if len(nums) == 0:
            return None
        nums.sort()

        # [-4, -1, -1, 0, 1, 2]

        result = []

        # result = [[-1, -1, 2], [-1,0,1] ]

        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                total_i = [nums[i], nums[left],nums[right]]
                
                
                if total_i in result:
                    left += 1
                    right -= 1
                    continue
                
                if total == 0:
                    result.append(total_i)
                    left += 1
                    right -= 1
                
                if total > 0:
                    right -= 1
                
                if total < 0:
                    left += 1
        
        return result
                
            



        