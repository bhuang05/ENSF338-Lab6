import timeit
import random

"""
4. After running the code multiple times, the heap implementation is faster than the list implementation.

This is because heaps have (log(n) complexity for traversing to find the right position to enqueue/dequeue and lists have an n complexity for traversing to find the right position to enqueue/dequeue.
"""

# implements a priority queue using a linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class ListPriorityQueue:
    def __init__(self):
        self.head = None
    
    # enqueue method to insert an element in order.
    def enqueue(self, item):
        new_node = Node(item)
        # If the list is empty or item is smaller than the head node
        if not self.head or item < self.head.value:
            new_node.next = self.head
            self.head = new_node
        else:
            # Traverse the list to find the correct insert position
            current = self.head
            while current.next and current.next.value < item:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    # dequeue method to retrieve the smallest element on the list
    def dequeue(self):
        if not self.head:
            return None 
        smallest = self.head.value
        self.head = self.head.next 
        return smallest

# implemenets a priority queue using a Heap. 
# Implementation of Heap copied from ex4.py
class Heap:
    def __init__(self):
        self.storage = []

    # heapify method
    def heapify(self, input_array):
        self.storage = input_array[:]
        n = len(self.storage)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify_down(i)
   
    # enqueue method
    def enqueue(self, item):
        self.storage.append(item)
        # After adding the item to the end of the array we have to heapify up
        self.heapify_up(len(self.storage) - 1)

    # dequeue method
    def dequeue(self):
        if not self.storage:
            return None
        root = self.storage[0]
        last_item = self.storage.pop()
        # We need to heapify down after removing an item
        if self.storage:
            self.storage[0] = last_item
            self.heapify_down(0)
        return root

    # heapify up and heapify down helper methods to help with enqueuing and dequeuing
    def heapify_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.storage[index] < self.storage[parent_index]:
            self.storage[index], self.storage[parent_index] = self.storage[parent_index], self.storage[index]
            self.heapify_up(parent_index)

    def heapify_down(self, index):
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2
        if left < len(self.storage) and self.storage[left] < self.storage[smallest]:
            smallest = left
        if right < len(self.storage) and self.storage[right] < self.storage[smallest]:
            smallest = right
        if smallest != index:
            self.storage[index], self.storage[smallest] = self.storage[smallest], self.storage[index]
            self.heapify_down(smallest)

class HeapPriorityQueue:
    def __init__(self):
        self.heap = Heap()

    def enqueue(self, item):
        self.heap.enqueue(item)

    def dequeue(self):
        return self.heap.dequeue()

# Measuring the execution time of both implementations. 
# ChatGPT was used to measure the execution time and generate a random list of 1000 tasks

lpq = ListPriorityQueue()
hpq = HeapPriorityQueue()

# Function to simulate tasks for ListPriorityQueue
def simulate_list_priority_queue(tasks):
    for task in tasks:
        if task[0] == "enqueue":
            lpq.enqueue(task[1])
        else:
            lpq.dequeue()

# Function to simulate tasks for HeapPriorityQueue
def simulate_heap_priority_queue(tasks):
    for task in tasks:
        if task[0] == "enqueue":
            hpq.enqueue(task[1])
        else:
            hpq.dequeue()

# Generate the list of tasks
tasks = [("enqueue", random.randint(0, 1000)) if random.random() < 0.7 else ("dequeue",) for _ in range(1000)]

# Measure execution time for ListPriorityQueue
list_queue_time = timeit.timeit(lambda: simulate_list_priority_queue(tasks), number=1)

# Measure execution time for HeapPriorityQueue
heap_queue_time = timeit.timeit(lambda: simulate_heap_priority_queue(tasks), number=1)

list_queue_time, heap_queue_time, list_queue_time / 1000, heap_queue_time / 1000

# Print the data

print(f"ListPriorityQueue Time: {list_queue_time} seconds, Avg Time/Task: {list_queue_time / 1000} seconds")
print(f"HeapPriorityQueue Time: {heap_queue_time} seconds, Avg Time/Task: {heap_queue_time / 1000} seconds")

