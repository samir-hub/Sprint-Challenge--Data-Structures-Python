import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('./names/names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('./names/names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()


my_bst1 = BinarySearchTree('a')

for item in names_1:
    my_bst1.insert(item)

for item in names_2:
    my_bst1.contains(item)

end_time = time.time()

print (f"runtime: {end_time - start_time} seconds")


    


# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?

#Original runtime complexity: O(n^2)