import numpy as np
import timeit

# Binary Search Tree implementation from notes in class
class Node:
    def __init__(self, data, parent=None):
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return

        current = self.root
        parent = None

        while current is not None:
            parent = current
            if data <= current.data:
                current = current.left
            else:
                current = current.right

        new_node = Node(data, parent)

        if data <= parent.data:
            parent.left = new_node
        else:
            parent.right = new_node
    
    def search(self, data, root=None):
        if root is None:
            root = self.root

        current = root
        while current is not None:
            if data == current.data:
                return current
            elif data < current.data:
                current = current.left
            else:
                current = current.right
        return None

# Binary search implementation from ChatGPT
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

vector = np.arange(1, 100000)
shuffled_vector = vector.copy()
np.random.shuffle(shuffled_vector)

binary_search_time = 0
binary_search_avg_times = []

for element in vector:
    binary_search_avg_time = 0
    for _ in range(10):
        total_time = timeit.timeit(lambda: binary_search(vector, element), number=1)
        binary_search_avg_time += total_time
        binary_search_time += total_time
    binary_search_avg_times.append(binary_search_avg_time / 10)

binary_search_avg_time = sum(binary_search_avg_times) / len(vector)



bst_shuffled = BinarySearchTree()

for element in shuffled_vector:
    bst_shuffled.insert(element)

shuffled_search_time = 0
shuffled_avg_times = []

for i in shuffled_vector:
    shuffled_avg_time = 0
    for _ in range(10):
        time_taken = timeit.timeit(lambda: bst_shuffled.search(i), number = 1)
        shuffled_avg_time += time_taken
        shuffled_search_time += time_taken
    shuffled_avg_times.append(shuffled_avg_time / 10)

shuffled_avg_time = sum(shuffled_avg_times) / len(shuffled_vector)


print(f"Total time for shuffled binary tree search: {shuffled_search_time} seconds")
print(f"Average time per instruction: {shuffled_avg_time} seconds")

print(f"Total time for binary search: {binary_search_time} seconds")
print(f"Average time per instruction: {binary_search_avg_time} seconds")

"""
Question 4:
Although both binary search in a sorted array and searching in a binary search tree that is balanced (assumed since we inserted a 
vector of shuffled elements) is both O(log(n)), the binary search tree is faster than the binary search in a sorted array. This could
be attributed to multiple factors like how the binary search tree is balanced from the shuffled insertion of elements, or how there is 
an extra step in implementation for binary search (when it has to calculate the midpoint, low and high). Another reason could be that
since the binary search tree uses nodes which are scattered in memory unlike the array which is contiguous, the binary search tree
could be faster due to cache locality.
"""

