"""
What is Thread Safety?
Thread safety ensures that multiple threads can access shared resources (e.g., variables, data structures) without conflicts. If a program is not thread-safe, race conditions or inconsistent data may occur.

Example of a Non-Thread-Safe Code
The following example increments a shared variable (counter) in multiple threads without synchronization, leading to incorrect results.

Non-Thread-Safe Example (Race Condition):
"""
import threading
import time
import random

counter = 0  # Shared resource
counter_lock = threading.Lock()  # Lock for thread safety

def increment():
    global counter
    for _ in range(1000000):
        time.sleep(random.uniform(0, 0.0001))  # Simulate context switching
        with counter_lock:  # Ensure thread safety
            counter += 1

threads = []
for _ in range(5):  # Create 5 threads
    t = threading.Thread(target=increment)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Final Counter Value:", counter)


#==================================================================
"""
Thread-Safe Solution
We can use a lock (mutex) to ensure only one thread modifies counter at a time.

Why is this thread-safe?
1. with lock: ensures that only one thread modifies counter at a time.
2. Prevents race conditions and data corruption.

Thread-Safe Example Using threading.Lock:
"""
import threading

counter = 0
lock = threading.Lock()  # Lock for synchronization

def increment():
    global counter
    for _ in range(1000000):
        with lock:  # Ensures only one thread accesses `counter`
            counter += 1

threads = []
for _ in range(5):
    t = threading.Thread(target=increment)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("********************")
print("Final Counter Value:", counter)

#===============================================
#===============================================
"""
                        Elaboration:
                        EXTRA (Self Learning)....................
 
                        Other Ways to Ensure Thread Safety:
                        
- Using threading.RLock (for reentrant locks)
- Using queue.Queue (which is thread-safe by design)
- Using concurrent.futures.ThreadPoolExecutor
- Using atomic variables (threading.local() or multiprocessing.Value)

# Example 1 threading.RLock

import threading

lock = threading.RLock()

def recursive_function(n):
    if n <= 0:
        return
    with lock:  # A thread can acquire the lock multiple times
        print(f"Lock acquired for {n}")
        recursive_function(n - 1)

thread = threading.Thread(target=recursive_function, args=(5,))
thread.start()
thread.join()
======================================================================

Using queue.Queue (Thread-Safe Data Structure)
queue.Queue is inherently thread-safe, so multiple threads can safely add and remove elements.

Example 2:

import threading
import queue

q = queue.Queue()

def worker():
    while not q.empty():
        item = q.get()  # Safely remove an item
        print(f"Processing item: {item}")
        q.task_done()

# Add items to the queue
for i in range(10):
    q.put(i)

threads = [threading.Thread(target=worker) for _ in range(3)]

for t in threads:
    t.start()

for t in threads:
    t.join()

print("All tasks completed.")
========================================================

Using concurrent.futures.ThreadPoolExecutor
This makes it easy to manage a pool of worker threads.

Example 3:

import concurrent.futures

def square(n):
    return n * n

with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(square, range(1, 6))

print(list(results))  
# Output: [1, 4, 9, 16, 25]
==============================================================

Using threading.local() (Thread-Local Storage)
Each thread gets its own independent storage.

Example 4:

import threading

thread_local_data = threading.local()

def process():
    thread_local_data.value = threading.get_ident()  # Unique ID for each thread
    print(f"Thread {threading.current_thread().name}: {thread_local_data.value}")

threads = [threading.Thread(target=process) for _ in range(3)]

for t in threads:
    t.start()

for t in threads:
    t.join()
================================================================

Using multiprocessing.Value (Atomic Shared Variable)
For safe variable access across multiple processes (not just threads).

Example 5:

import multiprocessing

counter = multiprocessing.Value('i', 0)  # 'i' means integer

def increment(shared_counter):
    for _ in range(1000000):
        with shared_counter.get_lock():  # Ensure atomic updates
            shared_counter.value += 1

processes = [multiprocessing.Process(target=increment, args=(counter,)) for _ in range(5)]

for p in processes:
    p.start()

for p in processes:
    p.join()

print("Final Counter Value:", counter.value)
# Correct result: 5000000
========================================================================
"""


