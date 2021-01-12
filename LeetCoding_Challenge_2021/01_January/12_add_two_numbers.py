# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = None
        tail = None
        isUp = False
        while l1 is not None and l2 is not None:
            n1 = l1.val
            n2 = l2.val
            sum_val = (n1 + n2 + (1 if isUp else 0))
            add = sum_val % 10
            isUp = sum_val >= 10

            if head is None:
                head = ListNode()
                head.val = add
                tail = head
            else:
                tmp = ListNode()
                tmp.val = add
                tail.next = tmp
                tail = tmp
            l1 = l1.next
            l2 = l2.next

        while l1 is not None:
            n1 = l1.val
            sum_val = (n1 + (1 if isUp else 0))
            add = sum_val % 10
            isUp = sum_val >= 10
            if head is None:
                head = ListNode()
                head.val = add
                tail = head
            else:
                tmp = ListNode()
                tmp.val = add
                tail.next = tmp
                tail = tmp
            l1 = l1.next

        while l2 is not None:
            n2 = l2.val
            sum_val = (n2 + (1 if isUp else 0))
            add = sum_val % 10
            isUp = sum_val >= 10
            if head is None:
                head = ListNode()
                head.val = add
                tail = head
            else:
                tmp = ListNode()
                tmp.val = add
                tail.next = tmp
                tail = tmp
            l2 = l2.next
        if isUp:
            if head is None:
                head = ListNode()
                head.val = 1
                tail = head
            else:
                tmp = ListNode()
                tmp.val = 1
                tail.next = tmp
                tail = tmp

        return head

head1 = None
tail1 = None
head2 = None
tail2 = None

for n in [9,9,9,9,9,9,9]:
    if head1 is None:
        head1 = ListNode()
        head1.val = n
        tail1 = head1
    else:
        tmp = ListNode()
        tmp.val = n
        tail1.next = tmp
        tail1 = tmp

for n in [9,9,9,9]:
    if head2 is None:
        head2 = ListNode()
        head2.val = n
        tail2 = head2
    else:
        tmp = ListNode()
        tmp.val = n
        tail2.next = tmp
        tail2 = tmp

solution = Solution()
result = solution.addTwoNumbers(head1, head2)
print(result)
