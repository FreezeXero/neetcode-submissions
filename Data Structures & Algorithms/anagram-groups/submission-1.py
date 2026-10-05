class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_groups = {}

        for word in strs:
            sorted_word = "".join(sorted(word))

            if sorted_word in word_groups:
                word_groups[sorted_word].append(word)
            else:
                word_groups[sorted_word] = [word]
            
        return list(word_groups.values())


            


        