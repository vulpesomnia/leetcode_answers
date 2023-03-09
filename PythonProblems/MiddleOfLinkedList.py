# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):#https://leetcode.com/problems/middle-of-the-linked-list/
    def middleNode(self, head):
        size = 1
        currentNode = head
        while currentNode.next != None:
            size += 1
            currentNode = currentNode.next
        size = ceil(size/2)
        currentNode = head
        while size != 0:
            currentNode = currentNode.next
            size -= 1
        return currentNode