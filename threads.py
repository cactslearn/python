# Simple Multithreading Example

import threading
import time

def download_file(file_name):
    print("Downloading", file_name)

    # Simulate waiting for a network response
    time.sleep(2)

    print(file_name, "download completed")


# Create threads
thread1 = threading.Thread(
    target=download_file,
    args=("File 1",)
)

thread2 = threading.Thread(
    target=download_file,
    args=("File 2",)
)

# Start both threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

print("All downloads completed.")