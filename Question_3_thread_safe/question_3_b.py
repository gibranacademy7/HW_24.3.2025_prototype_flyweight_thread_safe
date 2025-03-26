#The Code:

import threading
import time
import random

# Shared list - NOT thread safe
shared_list = []

def add_items(thread_id, count):
    """Add items to the shared list"""
    for i in range(count):
        # Get current length
        current_length = len(shared_list)
        # Simulate some processing time to increase chances of race condition
        time.sleep(0.001)
        # Append a new item
        shared_list.append(f"Thread {thread_id} - Item {i}")
        # Print progress occasionally
        if i % 10 == 0:
            print(f"Thread {thread_id} added item {i}")

def remove_items(thread_id, count):
    """Remove items from the shared list"""
    for i in range(count):
        if shared_list:  # Check if list is not empty
            # Simulate some processing time
            time.sleep(0.002)
            try:
                # Try to remove the last item
                item = shared_list.pop()
                # Print progress occasionally
                if i % 10 == 0:
                    print(f"Thread {thread_id} removed item: {item}")
            except IndexError:
                # This can happen if the list becomes empty between the check and pop
                print(f"Thread {thread_id} - List was empty!")

# Create and start threads
threads = []

# Add two threads that add items
for i in range(2):
    t = threading.Thread(target=add_items, args=(i, 50))
    threads.append(t)
    t.start()

# Add two threads that remove items
for i in range(2):
    t = threading.Thread(target=remove_items, args=(i+2, 40))
    threads.append(t)
    t.start()

# Wait for all threads to complete
for t in threads:
    t.join()

print(f"Final list length: {len(shared_list)}")
print(f"Expected length: {2*50 - 2*40} = 20")
#====================================================
"""
Question 3b:
Are the add and remove functions here thread-safe?

Answer:
No, the add_items and remove_items functions in your code are not thread-safe. 
This means that concurrent execution of these functions by multiple threads can lead to 
race conditions, data corruption, or unexpected behavior. 

Elaboration:
1. Race Conditions in add_items:
The function reads the current length of shared_list (current_length = len(shared_list)).
It then sleeps for a short time (time.sleep(0.001)) before appending an item.
During this time, another thread may modify shared_list, making the recorded length outdated.
This could lead to situations where multiple threads try to append items at nearly the same 
time, potentially causing inconsistent list states.

2. Race Conditions in remove_items:
The function checks if shared_list is not empty (if shared_list:).
Then it sleeps for a while (time.sleep(0.002)), creating a window where another thread 
might remove items before this thread calls pop().
When pop() is finally executed, the list might already be empty, causing an IndexError 
if not handled properly (you do catch it, but this still indicates a race condition).

3. Why These Issues Happen:
The operations len(shared_list), append(), and pop() are not atomic in Python.
Since multiple threads access and modify shared_list concurrently, 
there is no guarantee of a consistent view of the list at any moment.
The sleep calls (time.sleep(0.001)) increase the likelihood of these conflicts.

Make It Thread-Safe:
Useing a Lock:
"""
import threading
import time

shared_list = []
list_lock = threading.Lock()  # Create a lock

def add_items(thread_id, count):
    """Thread-safe addition of items to the shared list"""
    for i in range(count):
        time.sleep(0.001)  # Simulate processing delay
        with list_lock:  # Lock the critical section
            shared_list.append(f"Thread {thread_id} - Item {i}")
        if i % 10 == 0:
            print(f"Thread {thread_id} added item {i}")

def remove_items(thread_id, count):
    """Thread-safe removal of items from the shared list"""
    for i in range(count):
        time.sleep(0.002)  # Simulate processing delay
        with list_lock:  # Lock the critical section
            if shared_list:
                item = shared_list.pop()
                if i % 10 == 0:
                    print(f"Thread {thread_id} removed item: {item}")

threads = []
for i in range(2):
    t = threading.Thread(target=add_items, args=(i, 50))
    threads.append(t)
    t.start()

for i in range(2):
    t = threading.Thread(target=remove_items, args=(i+2, 40))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"Final list length: {len(shared_list)}")
print(f"Expected length: {2*50 - 2*40} = 20")
