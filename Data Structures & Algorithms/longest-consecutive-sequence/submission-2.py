class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        #Edge Case 1: empty list
        if len(nums) == 0:
            return 0
        
        nums.sort()
        #2,3,5,10,20
        
        pointer = 1
        length = 1
        max_length = 1

        while pointer < len(nums):
            
            #Edge Case 2: duplicate values
            if nums[pointer] == nums[pointer - 1]:
                pointer += 1
                continue
            
            if nums[pointer - 1] + 1 == nums[pointer]:
                length += 1
                pointer += 1
            else:
                length = 1
                pointer += 1
            
            max_length = max(max_length, length)

        return max_length
            
        
            
            
            

