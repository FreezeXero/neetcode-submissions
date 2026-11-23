class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # nums = [-1,0,1,2,-1,-4]
        nums.sort()
        
        # nums = [-4,-1,-1,0,1,2,]

        result = []

        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                
                total = nums[i] + nums[left] + nums[right]
                ts = [nums[i], nums[left] ,nums[right]]

                if total == 0:
                    if ts not in result:
                        result.append(ts)
                    
                    left += 1
                    right -= 1    
                
                if total < 0:
                    left += 1
                
                if total > 0:
                    right -= 1
        
        return result


        