# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/579/week-1-january-1st-january-7th/3591/

class Solution:
    def __init__(self):
        self.result = 0

    def make_cases(self, arr: list, index=0):
        size = len(arr)
        if size == 0:
            self.result += 1
        else:
            for _ in range(size):
                item = arr.pop(0)
                idx = index + 1
                if item % idx == 0 or idx % item == 0:
                    self.make_cases(arr, idx)
                arr.append(item)

    def countArrangement(self, n: int) -> int:
        self.make_cases([i for i in range(1, n + 1)])
        return self.result


solution = Solution()
print(solution.countArrangement(15))
