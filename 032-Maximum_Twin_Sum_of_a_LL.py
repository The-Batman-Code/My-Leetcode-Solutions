# Approach -1
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        l = 0
        temp = head
        while temp.next != None:
            l += 1
            temp = temp.next
        if l == 0:
            return 0
        if l == 1:
            return head.val + head.next.val
        print(l)
        temp2, temp3 = head, head
        s = []
        for i in range((l + 1) / 2):
            for j in range(0, l - 2 * i):
                temp3 = temp3.next

            s.append(temp2.val + temp3.val)
            temp3 = temp2.next
            temp2 = temp2.next
        print(s)
        return max(s)


# Approach -2
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow, fast = head, head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        res = 0
        while slow:
            res = max(res, prev.val + slow.val)
            prev = prev.next
            slow = slow.next
        return res


# Time : 624ms (96.40%) Space : 51.50 MB (88.25%)
