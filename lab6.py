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

    '''def rotate_right(self):
        x = self.left
        self.left = x.right
        if x.right is not None:
            x.right.parent = self
        x.parent = self.parent
        if self.is_left_child():
            self.parent.left = x
        if self.is_right_child():
            self.parent.right = x
        x.right = self
        self.parent = x
        x.colour=self.colour
        self.colour="R"
        return x
    
    def rotate_left(self):
        x = self.right
        self.right = x.left
        if x.right is not None:
            x.right.parent = self
        x.parent = self.parent
        if self.is_left_child():
            self.parent.left = x
        if self.is_right_child():
            self.parent.right = x
        x.left = self
        self.parent = x
        x.colour=self.colour
        self.colour="R"
        return x
    '''
    def LR ( self , x ) :
        y = x.right                                      # Y = Right child of x
        x.right = y.left                                 # Change right child of x to left child of y
        if y.left != self.NULL :
            y.left.parent = x

        y.parent = x.parent                              # Change parent of y as parent of x
        if x.parent == None :                            # If parent of x == None ie. root node
            self.root = y                                # Set y as root
        elif x == x.parent.left :
            x.parent.left = y
        else :
            x.parent.right = y
        y.left = x
        x.parent = y


    # Code for right rotate
    def RR ( self , x ) :
        y = x.left                                       # Y = Left child of x
        x.left = y.right                                 # Change left child of x to right child of y
        if y.right != self.NULL :
            y.right.parent = x

        y.parent = x.parent                              # Change parent of y as parent of x
        if x.parent == None :                            # If x is root node
            self.root = y                                # Set y as root
        elif x == x.parent.right :
            x.parent.right = y
        else :
            x.parent.left = y
        y.right = x
        x.parent = y
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
            # Parent's brother is red
            if node.get_uncle() != None and node.get_uncle().is_red():
                node.parent.make_black()
                node.get_uncle().make_black()
                node.parent.parent.make_red()
                node = node.parent.parent

            # Parent's brother is black and node is a right child
            elif node.is_right_child() and node.uncle_is_black():
                node = node.parent
                node.rotate_left()

            # Parent's brother is black and node is a left child
            elif node.is_left_child() and node.uncle_is_black():
                node.parent.make_black()
                node.parent.parent.make_red()
                node.rotate_right()

        # recoloring the root to black
        if node == None or node.parent == None:
            if node != None:
                node.make_black()
            else:
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

tree = RBTree()
print(tree)
tree.insert(4)
print(tree)
tree.insert(1)
print(tree)
tree.insert(3)
print(tree)
tree.insert(6)
print(tree)
tree.insert(8)
print(tree)
tree.insert(0)
print(tree)
