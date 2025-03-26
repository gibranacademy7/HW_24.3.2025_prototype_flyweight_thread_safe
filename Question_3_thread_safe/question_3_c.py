# The Code:

import threading
import time
import random
from multiprocessing import Manager, freeze_support

# Main function that contains all the code
def main():
    # Create a Manager
    manager = Manager()
    # Create a thread-safe shared list
    shared_list = manager.list()

    def add_items(thread_id, count):
        """Add items to the shared list"""
        for i in range(count):
            # Append a new item (this operation is atomic/thread-safe)
            shared_list.append(f"Thread {thread_id} - Item {i}")
            # Simulate some processing time
            time.sleep(0.001)
            # Print progress occasionally
            if i % 10 == 0:
                print(f"Thread {thread_id} added item {i}")

    def remove_items(thread_id, count):
        """Remove items from the shared list"""
        for i in range(count):
            # We still need to handle potential emptiness
            if len(shared_list) > 0:  # This check is now thread-safe
                try:
                    # Pop is now thread-safe
                    item = shared_list.pop()
                    # Simulate some processing time
                    time.sleep(0.002)
                    # Print progress occasionally
                    if i % 10 == 0:
                        print(f"Thread {thread_id} removed item: {item}")
                except IndexError:
                    # This should be much less likely now
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

if __name__ == "__main__":
    # This line is critical for Windows multiprocessing
    freeze_support()
    main()
#=================================================
"""
Question 3c:
Are the add and remove functions here thread-safe?

Answer:

Yes, the add_items and remove_items functions are mostly thread-safe due to the use of Manager().list(), 
which provides a thread-safe shared list. 
However, there are still some potential race conditions to be aware of:

Why add_items is thread-safe:
The manager.list() is designed to be shared safely between processes and threads.
The .append() operation on a Manager().list() is handled in a way that ensures safe concurrent modification.

Why remove_items might not be fully safe:
The check if len(shared_list) > 0: and shared_list.pop() are not atomic. 
There is a small chance that another thread removes an item between these two operations, 
leading to an IndexError.
However, since the try-except block is handling the IndexError, the program won’t crash, 
but it could still lead to unexpected behavior.
"""
