# Simple GIL Example

import threading
import time

def calculate():
    total = 0

    for i in range(10_000_000):
        total += i

    print("Calculation completed:", total)


# Create two threads
thread1 = threading.Thread(target=calculate)
thread2 = threading.Thread(target=calculate)

# Start both threads
start = time.time()

thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

end = time.time()

print("Total time:", end - start, "seconds")