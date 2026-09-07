class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = [0] * 26

        l = 0
        maxLength = 0
        mostF = 0

        for r in range(len(s)):
            c = ord(s[r]) - ord('A')
            counter[c] += 1
            mostF = max(mostF, counter[c])

            if (r - l + 1) - mostF <= k:
                maxLength = max(maxLength, (r - l + 1))
            else:
                c = ord(s[l]) - ord('A')
                counter[c] -= 1
                l += 1
        
        return maxLength
