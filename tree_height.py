import sys
import threading
import numpy

def compute_height(n, parents):
    # Write this function
    max_height = 0
    # Create a dictionary to store the parent and its children
    parent_dict = dict()
    # Loop through the parents array to store the parent and its children
    for i in range(n):
        # If the parent is -1, the node is the root
        if parents[i] == -1:
            root = i
        # Otherwise, store the parent and its children in the dictionary
        else:
            if parents[i] not in parent_dict:
                parent_dict[parents[i]] = [i]
            else:
                parent_dict[parents[i]].append(i)

    # Use a queue to traverse the tree
    queue = [root]
    # Keep track of the level of each node
    level_dict = {root: 0}
    # Traverse the tree
    while queue:
        node = queue.pop(0)
        # Get the level of the current node
        level = level_dict[node]
        # Update the maximum height
        max_height = max(max_height, level)
        # Get the children of the current node
        if node in parent_dict:
            for child in parent_dict[node]:
                queue.append(child)
                level_dict[child] = level + 1
    return max_height


def main():
    # implement input form keyboard and from files

    # Ask user to input from keyboard or file
    while True:
        user_input = input("Please input 'k' to input from keyboard or 'f' to input from file: ")
        if user_input == 'k':
            break
        elif user_input == 'f':
            # Ask user to enter file name
            while True:
                file_name = input("Please enter file name: ")
                # Check if the file name contains letter 'a'
                if 'a' in file_name:
                    print("File name cannot contain letter 'a'!")
                    continue
                # Open the file
                try:
                    f = open(file_name, 'r')
                    break
                except FileNotFoundError:
                    print("File not found!")
                    continue
            # Read the file
            content = f.read().split('\n')
            f.close()
            # Get the number of nodes and parents array
            n = int(content[0])
            parents = list(map(int, content[1].split(' ')))
            break
        else:
            print("Please input either 'k' or 'f'!")
            continue
    # Call the function and output it's result
    print(compute_height(n, parents))


if __name__ == "__main__":
    sys.setrecursionlimit(10**7)  # max depth of recursion
    threading.stack_size(2**27)   # new thread will get stack of such size
    threading.Thread(target=main).start()
main()
