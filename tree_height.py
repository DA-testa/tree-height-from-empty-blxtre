# python3

import sys
import threading
import numpy


max_height = 0
    
    nodes = [0] * n
    
    for i in range(n):
        
        nodes[i] = parents[i]
    
    root = nodes[0]
    
    for i in range(n):
        
        height = 1
        
        curr_node = nodes[i]
        
        while (curr_node != root):
            
            curr_node = nodes[curr_node]
            
            height += 1
        
        max_height = max(max_height, height)

    return max_height


def main():
   
    filename = input("Enter filename: ")
    
    if "a" in filename:
        print("Filename cannot contain letter a")
        return
    
    file = open(filename, "r")
    
    lines = file.readlines()
    
    n = int(lines[0])
 
    parents = [int(x) for x in lines[1].split()]
    
    print(compute_height(n, parents))

if __name__ == "__main__":
    # In Python, the default limit on recursion depth is rather low,
    # so raise it here for this problem. Note that to take advantage
    # of bigger stack, we have to launch the computation in a new thread.
    sys.setrecursionlimit(10**7)  # max depth of recursion
    threading.stack_size(2**27)   # new thread will get stack of such size
    threading.Thread(target=main).start()
main()
# print(numpy.array([1,2,3]))
