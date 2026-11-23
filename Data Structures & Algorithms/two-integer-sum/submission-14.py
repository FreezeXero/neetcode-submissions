class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}

        for i, num in enumerate(nums):
            #seen[num] = seen.get(i, 0) + 1
            needed = target - num
            if needed in seen:
                return [seen[needed], i]
            else:
                seen[num] = i

                
        