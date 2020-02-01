import time
from bst import BinarySearchTree

#import my BST from this weeks project
bst = BinarySearchTree('names')
start_time = time.time()
duplicates = []

#going to use these to open and read txt file
f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

#for loop that inserts names into bst
for names in names_1:
    bst.insert(names)

#for loop to compare names_2 to bst, if name is found we will append to the given dup list we have
for names in names_2:
    if bst.contains(names):
        duplicates.append(names)

#go away slow code
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)



end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?
