class XC3Node:
    def __init__(self, children):
        self.children = children
        
    def degree(self):
        return len(self.children)
    
    def height(self):
        if self.degree() == 0:
            return 0
        else:
            return 1 + max(child.height() for child in self.children)
        
    def num_nodes(self):
        if self.degree() == 0:
            return 1
        else:
            return 1 + sum(child.num_nodes() for child in self.children)
           
class XC3Tree:
    def __init__(self, degree):
        self.degree = degree
        self.root = self.build_tree(degree)
    
    def build_tree(self, degree):
        if degree == 0:
            return XC3Node([])
        children = []
        for i in range(1,degree+1):
            child_degree = i - 2 if i > 2 else 0
            child = self.build_tree(child_degree)
            children.append(child)
        return XC3Node(children)
        
    def height(self):
        return self.root.height()
    
    def num_nodes(self):
        return self.root.num_nodes()

#------------------testing---------------------
tree = XC3Tree(4)
print(tree.degree)   # output: 4
print(tree.height()) # output: 2
print(tree.num_nodes()) # output: 8
for child in tree.root.children:
    print(child.degree())
