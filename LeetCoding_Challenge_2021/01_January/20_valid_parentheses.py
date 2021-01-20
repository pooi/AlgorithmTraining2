class Solution:
    def isValid(self, s: str) -> bool:
        open = {"(", "[", "{"}
        close = {")": "(", "]": "[", "}": "{"}
        stack = []
        for c in s:
            if c in open:
                stack.append(c)
            elif len(stack) > 0:
                p = stack.pop()
                if close.get(c) != p:
                    return False
            else:
                return False
        return len(stack) == 0


print(Solution().isValid(""))
