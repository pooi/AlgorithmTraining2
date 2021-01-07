class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        temp = ''
        result = ''

        for i in range(len(s)):
            index = temp.find(s[i])
            if index != -1:
                start = start + index + 1
            temp = s[start: i+1]
            if len(result) < len(temp):
                result = temp
        return len(result)


print(Solution().lengthOfLongestSubstring("aabcdeffgh1234567rr"))
