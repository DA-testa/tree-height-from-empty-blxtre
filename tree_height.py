import sys
import threading
import numpy

def compute_height(n, parents):
    # Write this function
    max_height = 0
    # Create an array to hold each node's height
    heights = [0] * n 
    # Iterate through the parents array
    for i in range(n):
        # Check if the parent of the current node is the root node
        # If so, mark it as the height of the tree
        if parents[i] == -1:
            max_height = 1
        # Otherwise, calculate the height of the current node
        else:
            heights[i] = heights[parents[i]] + 1 
            # Check if the height of the current node is greater than the current maximum height
            if heights[i] > max_height:
                max_height = heights[i]
    return max_height

def main():
    # Read the number of elements from the input
    n = int(input())
    # Read the elements from the input
    parents = [int(x) for x in input().split()]
    # Call the function and output the result
    print(compute_height(n, parents))

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
main()
