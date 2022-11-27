# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        value = []
        temp = head
        
        while temp:
            value.append(temp.val)
            temp = temp.next
        
        ans = []
        for r in range(len(value)):
            
            while ans and value[r] > ans[-1]:
                ans.pop()
            ans.append(value[r])
                
        if len(ans) == len(value):
            return head
        
        prev = ListNode(ans[0])
        res = prev
        for i in ans[1:]:
            curr = ListNode(i)
            prev.next = curr
            prev = curr
          
        return res
                
        