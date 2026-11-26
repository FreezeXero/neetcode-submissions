class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
                return 0
        
        nums.sort()

        p = 0
        length = 1
        max_length = 1

        # 0, 1, 2, 3, 4

        while p < len(nums) - 1:
            
            if nums[p + 1] == nums[p]:
                p += 1
                continue
            
            if nums[p + 1] - 1 == nums[p]:
                length += 1
            
            else:
                length = 1
            
            max_length = max(max_length, length)
            p += 1
        
        return max_length
            


        