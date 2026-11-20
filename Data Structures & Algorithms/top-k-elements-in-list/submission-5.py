class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        bucket = [[] for i in range(len(nums) + 1)]

        for c in count:
            bucket[count[c]].append(c)
        
        result = []

        for numlist in reversed(bucket):
            for num in numlist:
                result.append(num)

                if len(result) == k:
                    return result





        