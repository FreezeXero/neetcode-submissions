class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen = set()
        max_length = 0
        left = 0
        right = 0

        while right < len(s):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            max_length = max(max_length, len(seen))
            right += 1
            
        return max_length
            

        
       



        