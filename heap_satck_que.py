from collections import deque
import heapq

# --- 1. STACK EXAMPLE (LIFO: Last In, First Out) ---
def stack_example():
    print("=== Stack Example (LIFO) ===")
    # A standard Python list can act as a stack
    stack = []
    
    # Pushing elements onto the stack
    stack.append(10)
    stack.append(20)
    stack.append(30)
    print(f"Stack after pushes: {stack}")
    
    # Popping the last element added (30)
    popped_element = stack.pop()
    print(f"Popped element: {popped_element}")
    print(f"Stack after pop: {stack}\n")


# --- 2. QUEUE EXAMPLE (FIFO: First In, First Out) ---
def queue_example():
    print("=== Queue Example (FIFO) ===")
    # Using collections.deque for efficient queue operations
    queue = deque()
    
    # Enqueuing (adding) elements to the back
    queue.append("Alice")
    queue.append("Bob")
    queue.append("Charlie")
    print(f"Queue after additions: {list(queue)}")
    
    # Dequeuing (removing) the first element added (Alice)
    served_element = queue.popleft()
    print(f"Served (removed) element: {served_element}")
    print(f"Queue after service: {list(queue)}\n")


# --- 3. HEAP EXAMPLE (Min-Heap) ---
def heap_example():
    print("=== Heap Example (Min-Heap) ===")
    # Python's heapq module implements a Min-Heap by default 
    # (parent <= children, with the smallest element always at index 0)
    min_heap = []
    
    # Inserting elements
    heapq.heappush(min_heap, 25)
    heapq.heappush(min_heap, 10)
    heapq.heappush(min_heap, 40)
    
    print(f"Heap structure: {min_heap}")
    print(f"Root (Smallest element): {min_heap[0]}")
    
    # Removing the smallest element
    smallest = heapq.heappop(min_heap)
    print(f"Popped smallest element: {smallest}")
    print(f"Heap after pop: {min_heap}\n")


# --- MAIN FUNCTION ---
if __name__ == "__main__":
    stack_example()
    queue_example()
    heap_example()