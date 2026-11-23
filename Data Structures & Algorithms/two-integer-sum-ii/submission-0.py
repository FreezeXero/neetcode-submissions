class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:

        # [2,3,4]  target = 7

        index1 = 0
        index2 = len(numbers) - 1

        
        while index1 < index2:
            total = numbers[index1] + numbers[index2]
            if total == target:
                return [index1 + 1, index2 + 1]
            
            if total > target:
                index2 -= 1
            
            if total < target:
                index1 += 1