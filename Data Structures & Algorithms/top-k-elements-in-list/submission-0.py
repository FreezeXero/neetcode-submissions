class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}

        # Step 1: Count how often each number appears
        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1

        # Step 2: Create empty buckets
        buckets = []

        for i in range(len(nums) + 1):
            buckets.append([])

        # Step 3: Group numbers by their frequency
        for num, count in frequency.items():
            buckets[count].append(num)

        # Step 4: Collect the k most frequent numbers
        result = []

        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)

                if len(result) == k:
                    return result