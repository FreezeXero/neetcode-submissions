class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        freq_s = {}
        freq_t = {}

        for count in s:
            freq_s[count] = freq_s.get(count, 0) + 1
        
        for count in t:
            freq_t[count] = freq_t.get(count, 0) + 1
        
        if freq_s == freq_t:
            return True
        else:
            return False

        