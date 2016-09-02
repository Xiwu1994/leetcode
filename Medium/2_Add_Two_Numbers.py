# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
            ListNode相当于用C的列表，有value和next
        """
        divisor = 0; root = rtype = ListNode(0)
        while l1 or l2 or divisor:
            x1, x2 = 0, 0
            if l1: x1 = l1.val; l1 = l1.next
            if l2: x2 = l2.val; l2 = l2.next
            divisor, remainder = divmod(x1 + x2 + divisor, 10) #divmod得到除数和余数
            listnode = ListNode(remainder) #余数是需要的值
            rtype.next = listnode; rtype = listnode
        return root.next
