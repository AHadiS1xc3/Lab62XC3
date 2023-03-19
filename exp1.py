from BST import BSTtree
from randomList import createRandom
import random
import matplotlib.pyplot as plot
import numpy as np

import sys
sys.setrecursionlimit(10000)

class RBNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.colour = "R"

    def get_uncle(self):
        return

    def is_leaf(self):
        return self.left == None and self.right == None

    def is_left_child(self):
        return self == self.parent.left

    def is_right_child(self):
        return not self.is_left_child()

    def is_red(self):
        return self.colour == "R"

    def is_black(self):
        return not self.is_red()

    def make_black(self):
        self.colour = "B"

    def make_red(self):
        self.colour = "R"

    def get_brother(self):
        if self.parent.right == self:
            return self.parent.left
        return self.parent.right

    def get_uncle(self):
        return self.parent.get_brother()

    def uncle_is_black(self):
        if self.get_uncle() == None:
            return True
        return self.get_uncle().is_black()

    def __str__(self):
        return "(" + str(self.value) + "," + self.colour + ")"

    def __repr__(self):
         return "(" + str(self.value) + "," + self.colour + ")"

    def rotate_right(self):
        x = self.left
        self.left = x.right
        if x.right != None:
            x.right.parent = self
        x.parent = self.parent
        if self.parent==None:
            self.parent=x
        if self.is_right_child() :
            self.parent.right = x
        elif self.is_left_child() :
            self.parent.left = x
        x.right = self
        self.parent = x
        
    def rotate_left(self):
        x = self.right
        self.right = x.left
        if x.left != None:
            x.left.parent = self
        x.parent = self.parent
        if self.parent == None :                           
            self.parent=x 
        elif self.is_left_child() :
            self.parent.left = x
        elif self.is_right_child():
            self.parent.right = x
        x.left = self
        self.parent = x
        

class RBTree:
    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root == None

    def get_height(self):
        if self.is_empty():
            return 0
        return self.__get_height(self.root)

    def __get_height(self, node):
        if node == None:
            return 0
        return 1 + max(self.__get_height(node.left), self.__get_height(node.right))

    def insert(self, value):
        if self.is_empty():
            self.root = RBNode(value)
            self.root.make_black()
        else:
            self.__insert(self.root, value)

    def __insert(self, node, value):
        if value < node.value:
            if node.left == None:
                node.left = RBNode(value)
                node.left.parent = node
                self.fix(node.left)
            else:
                self.__insert(node.left, value)
        else:
            if node.right == None:
                node.right = RBNode(value)
                node.right.parent = node
                self.fix(node.right)
            else:
                self.__insert(node.right, value)
        
    def fix(self, node):
        # fixing until we reach the root or a black node with a red parent
        while node != None and node.parent != None and node.parent.is_red():

            # uncle is black and node is a right child
            if node.parent.is_right_child() and node.uncle_is_black():
                # node is left child, set node to parent and rotate right
                if node.is_left_child():
                    node = node.parent
                    node.rotate_right()
                #make make parent black, grandparent red
                node.parent.make_black()
                node.parent.parent.make_red()
                #then rotate grand parent left
                node.parent.parent.rotate_left()

            # uncle is black and node is a left child
            elif node.parent.is_left_child() and node.uncle_is_black():
                if node.is_right_child():
                    # then we need to set node to it parent and rotate left
                    node = node.parent
                    node.rotate_left()
                # then they line up, we mark parent black and grand parent red(no red adjecent)
                node.parent.make_black()
                node.parent.parent.make_red()
                #then node.grandparent needs to rotate right(path has same number of black node)
                node.parent.parent.rotate_right()
            elif node.get_uncle().is_red():
                #make both parent and uncle black, make grand parent right
                node.parent.make_black()
                node.get_uncle().make_black()
                node.parent.parent.make_red()
                node = node.parent.parent
                
        # keep going up until we reach the root and update the root 
        while self.root.parent != None:
            self.root = self.root.parent
        # recoloring the node to blcak
        self.root.make_black()

    def __str__(self):
        if self.is_empty():
            return "[]"
        return "[" + self.__str_helper(self.root) + "]"

    def __str_helper(self, node):
        if node.is_leaf():
            return "[" + str(node) + "]"
        if node.left == None:
            return "[" + str(node) + " -> " + self.__str_helper(node.right) + "]"
        if node.right == None:
            return "[" +  self.__str_helper(node.left) + " <- " + str(node) + "]"
        return "[" + self.__str_helper(node.left) + " <- " + str(node) + " -> " + self.__str_helper(node.right) + "]"

# testing max and average height for BST
total_height = 0
max_height = 0
for _ in range(100):
    randomArray = createRandom(10001)
    bstTree = BSTtree()
    for element in randomArray:    
        bstTree.insert(element)
    total_height += bstTree.get_height()
    max_height = max(bstTree.get_height(), max_height)

print("Average Height of Binary Search Trees:")
print(total_height/100)
print("Maximum Height of Binary Search Trees:")
print(max_height)

# testing max and average height for Red Black Trees
total_height = 0
max_height = 0
for _ in range(100):
    randomArray = createRandom(10001)
    rbtTree = RBTree()
    for element in randomArray:    
        rbtTree.insert(element)
    total_height += rbtTree.get_height()
    max_height = max(rbtTree.get_height(), max_height)

print("\n\n")
print("Average Height of Red black Trees:")
print(total_height/100)
print("Maximum Height of Red black Trees:")
print(max_height)
              
