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
    

vector = np.arange(1, 10001)
shuffled_vector = vector.copy()
np.random.shuffle(shuffled_vector)


bst_sorted = BinarySearchTree()
bst_shuffled = BinarySearchTree()
for element in vector:
    bst_sorted.insert(element)

for element in shuffled_vector:
    bst_shuffled.insert(element)

sorted_search_time = 0

sorted_avg_times = []

for i in vector:
    sorted_avg_time = 0
    for _ in range(10):
        time_taken = timeit.timeit(lambda: bst_sorted.search(i), number=1)
        sorted_avg_time += time_taken
        sorted_search_time += time_taken
    sorted_avg_time /= 10
    sorted_avg_times.append(sorted_avg_time)

sorted_avg_time = sum(sorted_avg_times) / len(vector)

shuffled_search_time = 0

shuffled_avg_times = []

for i in shuffled_vector:
    shuffled_avg_time = 0
    for _ in range(10):
        time_taken = timeit.timeit(lambda: bst_shuffled.search(i), number=1)
        shuffled_avg_time += time_taken
        shuffled_search_time += time_taken
    shuffled_avg_time = shuffled_search_time / 10
    shuffled_avg_times.append(shuffled_avg_time)

shuffled_avg_time = sum(shuffled_avg_times) / len(shuffled_vector)

print(f"Total time for sorted vector: {sorted_search_time} seconds")
print(f"Average time per instruction: {sorted_avg_time} seconds")

print(f"Total time for shuffled vector: {shuffled_search_time} seconds")
print(f"Average time per instruction: {shuffled_avg_time} seconds")


"""
Question 4:
From the results, we can see that the shuffled data that was inserted into the tree is more efficient.
One of the reasons is that when you insert sorted data into a tree, it begins to resemble a 
linked list which degrades the search time from O(log(n)) to O(n). On the other hand, inserting random data
ensures that the tree is more balanced, which ensures that the search time is O(log(n)).
Thus, inserting random data into a tree is more efficient than inserting sorted data for searching due to 
balancing issues.
"""