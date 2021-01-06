# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/579/week-1-january-1st-january-7th/3592/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def setValue(self, head, tail, node):
        if head is None:
            head = ListNode()
            head.val = node.val
            tail = head
        else:
            temp = ListNode()
            temp.val = node.val
            tail.next = temp
            tail = temp
        return head, tail, node.next

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = None
        tail = None
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                head, tail, l1 = self.setValue(head, tail, l1)
            else:
                head, tail, l2 = self.setValue(head, tail, l2)
        while l1 is not None:
            head, tail, l1 = self.setValue(head, tail, l1)
        while l2 is not None:
            head, tail, l2 = self.setValue(head, tail, l2)
        return head


head1 = ListNode()
tail1 = head1
head2 = ListNode()
tail2 = head2

for val in [1, 3, 5]:
    tail1.val = val
    tail1.next = ListNode()
    tail1 = tail1.next
tail1 = None

for val in [2, 4, 6]:
    tail2.val = val
    tail2.next = ListNode()
    tail2 = tail2.next
tail2 = None

solution = Solution()
result = solution.mergeTwoLists(head1, head2)
while result is not None:
    print(result.val, end=' ')
    result = result.next
