import heapq
import threading

arr = [4, 3, 62, 4, 6, 334, 6, 5]
heapq.heapify(arr)
print(heapq.heappop(arr))

# This is an example of a race condition in python.for.
# Tested with python 3.7 since Python 3.10 fixed some race conditions for easy operations.
# The ouput will not always be a million.

# A shared variable
counter = 0


def increment():
    global counter
    for _ in range(100000):
        # The function call here can trigger the GIL to release
        # allowing another thread to run
        local = counter
        # This simulates some processing that might cause a thread switch
        local = local + 1
        counter = local


threads = []
# Create and start multiple threads
for _ in range(10):
    thread = threading.Thread(target=increment)
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

print(f"Final counter value: {counter}")
# Expected: 1,000,000
# Actual: Usually less due to race conditions
