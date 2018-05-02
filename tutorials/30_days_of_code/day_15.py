class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next
	# Solution method.		
    def insert(self,head,data):
        current = head
        if current:
            while current.next:
                current = current.next
            else:
                current.next = Node(data)
        else:
            head = Node(data)
        
        return head
		
mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head); 