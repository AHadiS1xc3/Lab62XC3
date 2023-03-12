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

#-----------------------Experiment 4------------------------
#------------------Number of nodes pattern------------------
#fibonacci recursive Implementation
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
        
# running for loop from 0 to 25     
for i in range(26):
    tree = XC3Tree(i)
    current_node=tree.num_nodes()
    fibonacci_i=fibonacci(i+2)
    # i XC-tree nodes number is equal to (i+2)th fibonacci
    print(i," XC-3 Tree nodes: ",current_node)
    print(i+2, "th Fibonacci number: ",fibonacci_i)

# equation: nodes(i) = fib(i+2)
