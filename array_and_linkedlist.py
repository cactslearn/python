# --- 1. ARRAY EXAMPLE ---
# Arrays store elements in contiguous memory locations,
# allowing fast, direct access by index.
def array_example():
    print("=== Array Example ===")
    
    # Creating an array (Python lists act as dynamic arrays)
    my_array = [10, 20, 30, 40, 50]
    print(f"Array elements: {my_array}")
    
    # Direct access by index (O(1) time complexity)
    # Because memory is contiguous, the computer can calculate the exact address instantly.
    print(f"Direct access at index 2: {my_array[2]}\n")


# --- 2. LINKED LIST EXAMPLE ---
# Linked lists store elements non-contiguously. 
# Each element (Node) contains data and a reference (tag) to the next element.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Reference to the next node

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) + " -> None")

def linked_list_example():
    print("=== Linked List Example ===")
    
    ll = LinkedList()
    
    # Creating individual nodes stored anywhere in memory
    node1 = Node(10)
    node2 = Node(20)
    node3 = Node(30)
    
    # Linking them together using references (.next tags)
    ll.head = node1
    node1.next = node2
    node2.next = node3
    
    print("Linked List structure (navigated via references):")
    ll.display()


# --- MAIN FUNCTION ---
if __name__ == "__main__":
    array_example()
    linked_list_example()