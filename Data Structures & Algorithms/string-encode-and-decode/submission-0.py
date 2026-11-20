class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for word in strs:
            result += str(len(word)) + "#" + word

        return result

    def decode(self, result: str) -> List[str]:
        res = []
        left = 0
        right = 0

        while left < len(result):

            # Move right until we find the hashtag
            while result[right] != "#":
                right += 1

            # Extract the length of the word
            length = int(result[left:right])

            # Find where the word starts and ends
            start = right + 1
            end = start + length

            # Append the decoded word
            res.append(result[start:end])

            # Move both pointers to the next encoded word
            left = end
            right = end

        return res
