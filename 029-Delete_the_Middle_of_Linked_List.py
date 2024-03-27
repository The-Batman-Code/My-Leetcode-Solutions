# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        l = 0
        temp = head
        temp2 = head
        while temp is not None:
            temp = temp.next
            l += 1
        if l == 2:
            head.next = None
            return head
        if l == 1:
            return None
        r = l // 2
        for _ in range(r - 1):
            temp2 = temp2.next
            print(temp2.val)
        temp2.next = temp2.next.next
        return head


# Time : 2155ms (5.03%) Space : 97.55 MB (6.93%)
