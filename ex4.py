import random

# Heap class: uses Python array as a storage backend for heap nodes.
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

# Writing 3 Tests for the cases
# ChatGPT was used to write the following 3 Tests

# Test 1: Input array is already a sorted heap
def test_sorted_heap():
    heap = Heap()
    input_array = [1, 2, 3, 4, 5, 6, 7]
    heap.heapify(input_array)
    assert heap.storage == input_array, "Heapify failed on already sorted heap"

# Test 2: Input array is empty
def test_empty_heap():
    heap = Heap()
    input_array = []
    heap.heapify(input_array)
    assert heap.storage == [], "Heapify failed on empty array"
            
# Test 3: Input array is a long, randomly shuffled list of integers
def test_random_heap():
    heap = Heap()
    input_array = list(range(1, 101))  # Create a list of integers 1 through 100
    random.shuffle(input_array)  # Shuffle the list to randomize the order
    heap.heapify(input_array)
    sorted_array = sorted(input_array)  # The expected result after complete dequeue operations

    for expected_value in sorted_array:
        assert heap.dequeue() == expected_value, "Heap did not dequeue the expected value in sorted order"

# Calling the test functions
test_sorted_heap()
test_empty_heap()
test_random_heap()
print("All tests passed successfully!")
