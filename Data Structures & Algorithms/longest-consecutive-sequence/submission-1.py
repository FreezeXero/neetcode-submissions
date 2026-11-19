class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()

        right = 1
        max_length = 1
        length = 1

        while right < len(nums):
            if nums[right - 1] == nums[right]:
                right += 1
                continue

            if nums[right - 1] + 1 == nums[right]:
                length += 1
            else:
                length = 1

            max_length = max(max_length, length)
            right += 1

        return max_length



        