import sys
import threading


class Node:
    def __init__(self):
        self.children = []


def compute_height(n, parents):
    nodes = [Node() for _ in range(n)]
    root = None
    for i, parent in enumerate(parents):
        if parent == -1:
            root = nodes[i]
        else:
            nodes[parent].children.append(nodes[i])
    
    if not root:
        return 0
    
    def dfs(node):
        if not node.children:
            return 1
        heights = [dfs(child) for child in node.children]
        return max(heights) + 1
    
    return dfs(root)


def main():
    input_type = input("Enter input type (F for file, K for keyboard): ")
    if input_type.lower() == "f":
        file_name = input("Enter file name: ")
        while "a" in file_name:
            file_name = input("Enter file name (cannot contain letter a): ")
        try:
            with open("inputs/" + file_name, "r") as file:
                n = int(file.readline())
                parents = list(map(int, file.readline().split()))
        except FileNotFoundError:
            print("File not found.")
            return
    elif input_type.lower() == "k":
        n = int(input("Enter number of nodes: "))
        parents = list(map(int, input("Enter parents separated by spaces: ").split()))
    else:
        print("Invalid input type.")
        return
    
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
