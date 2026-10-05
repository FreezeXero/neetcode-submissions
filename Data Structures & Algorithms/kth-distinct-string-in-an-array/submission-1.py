class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        # Go through each string in the array in order
        for s in arr:
            # Check if the string appears only once (is distinct)
            if arr.count(s) == 1:
                # i found one distinct string, decrease k
                k -= 1
                # If this is the k-th distinct string, return it
                if k == 0:
                    return s
        
        # If there are fewer than k distinct strings, return empty string
        return ""
        
        