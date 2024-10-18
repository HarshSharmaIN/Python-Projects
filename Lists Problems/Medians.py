#level: Medium

'''
Question:
We have N integers V1, V2. VN and for each integer Vi, we know that Ai<=Vi<=Bi. We need to find the number of distinct values, the sorted median of V can take.

Input:

	1.	An integer  N  representing the number of nodes in the linked list.
	2.	A list of  N  integers, where each integer represents the value of a node in the linked list

Constraints:

	1 \leq N \leq 10^5 
	0 \leq \text{Node value} \leq 10^9 

Output:
	The linked list with even elements appearing first, followed by odd elements, while maintaining their original relative order.

Code:
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def separateEvenOdd(head):
    if not head:
        return None
    
    even_dummy = ListNode(0)
    odd_dummy = ListNode(0)
    
    even_tail = even_dummy
    odd_tail = odd_dummy
    
    current = head
    while current:
        if current.val % 2 == 0:  # Add to even list
            even_tail.next = current
            even_tail = even_tail.next
        else:  # Add to odd list
            odd_tail.next = current
            odd_tail = odd_tail.next
        current = current.next
    
    even_tail.next = odd_dummy.next  # Connect even list to odd list
    odd_tail.next = None  # End the list
    
    return even_dummy.next

def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# Taking input for the linked list
n = int(input("Enter the number of elements: "))
values = list(map(int, input("Enter the elements: ").split()))

# Create the linked list
head = ListNode(values[0])
current = head
for val in values[1:]:
    current.next = ListNode(val)
    current = current.next

# Separate even and odd elements
new_head = separateEvenOdd(head)

# Print the modified list
printList(new_head)