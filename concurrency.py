# Concurrency using Multithreading

import threading
import time

def task(name):
    for i in range(3):
        print(name, "is working...")
        time.sleep(1)

# Create two threads
thread1 = threading.Thread(target=task, args=("Task 1",))
thread2 = threading.Thread(target=task, args=("Task 2",))

# Start both threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

print("All tasks completed.")