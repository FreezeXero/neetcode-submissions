class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        frequency = {}

        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1
        
        bucket = []

        for i in range(len(nums) + 1):
            bucket.append([])
        
        for num, count in frequency.items():
            bucket[count].append(num)
        
        result = []

        for i in range(len(bucket)- 1, 0, -1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result




        
        

        