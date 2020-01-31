import sys

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        #if greater than or equal to we will move to the right
        if value >= self.value:
            #set the current_node to the node to the right of current_node, recursive
            if self.right:
                self.right.insert(value)
            #if none on right, add it
            else:
                self.right = BinarySearchTree(value)
        #if less than, we will move to the left
        elif value < self.value:
            #set current_node to the left node, recursive
            if self.left:
                self.left.insert(value)
            #if no left node we add it
            else:
                self.left = BinarySearchTree(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        #when found return true
        #if no left or right return false
        #if given value is equal to default we return true
        if target == self.value:
            return True
        #if given value is greater than, move to right
        elif target > self.value:
            if self.right:
                return self.right.contains(target)
            else:
                return False
        #if given value is less than, move to left
        else:
            if self.left:
                return self.left.contains(target)
            else:
                return False