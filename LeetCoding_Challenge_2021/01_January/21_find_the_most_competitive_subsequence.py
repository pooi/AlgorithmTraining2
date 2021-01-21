class Solution:
    def mostCompetitive(self, nums: list, k: int) -> list:
        l = len(nums)
        stack = []
        for i, n in enumerate(nums):
            remain = l - i
            while stack and stack[-1] > n and remain > 0 and len(stack) + (l - i) > k:
                stack.pop()
                remain -= 1
            if len(stack) < k:
                stack.append(n)
        return stack

print(Solution().mostCompetitive(nums = [2,4,3,3,5,4,9,6], k = 4))
