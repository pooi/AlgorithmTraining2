# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/579/week-1-january-1st-january-7th/3593/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        checkSum = [0 for _ in range(0, 201)]
        while head is not None:
            checkSum[head.val + 100] += 1
            head = head.next
        result = [idx - 100 for idx, val in enumerate(checkSum) if val == 1]

        answer = None
        answerTail = None
        for val in result:
            if answer is None:
                answer = ListNode()
                answer.val = val
                answerTail = answer
            else:
                temp = ListNode()
                temp.val = val
                answerTail.next = temp
                answerTail = temp
        return answer


node = None
tail = None
for val in [1, 2, 2, 3, 3, 4, 5]:
    if node is None:
        node = ListNode()
        node.val = val
        tail = node
    else:
        temp = ListNode()
        temp.val = val
        tail.next = temp
        tail = temp

solution = Solution()
print(solution.deleteDuplicates(node))