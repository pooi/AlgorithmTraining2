class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        start, length = 0, 0
        for j in range(len(s)):
            new_start = j - length
            if s[new_start: j + 1] == s[new_start: j + 1][::-1]:
                start = new_start
                length += 1
            elif new_start > 0 and s[new_start - 1: j + 1] == s[new_start - 1: j + 1][::-1]:
                start = new_start - 1
                length += 2
        return s[start: start + length]


print(Solution().longestPalindrome2("forgeeksskeegfor"))
