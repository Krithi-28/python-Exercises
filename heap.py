import heapq

# Create a list
data = [4, 7, 2, 9, 1, 5]

# Convert list into a heap
heapq.heapify(data)

# Pop and print the smallest element
print(heapq.heappop(data))  # Output: 1

# Push a new element onto the heap
heapq.heappush(data, 3)

# Pop and print the smallest element again
print(heapq.heappop(data))  # Output: 2
print(data)