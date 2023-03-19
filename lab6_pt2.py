import matplotlib.pyplot as plt
import math as m 
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
        
# running for loop from 0 to 25  (Figure 4.1.1 and figure 4.1.2)
for i in range(26):
    tree = XC3Tree(i)
    current_node=tree.num_nodes()
    fibonacci_i=fibonacci(i+2)
    # i XC-tree nodes number is equal to (i+2)th fibonacci
    print(i," XC-3 Tree nodes: ",current_node)
    print(i+2, "th Fibonacci number: ",fibonacci_i)

# equation: nodes(i) = fib(i+2)
# -----------------Argument on height bound---------------
def test_tree_height():
    for i in range(26):
        tree = XC3Tree(i)
        height=tree.height()
        h_approx = m.ceil(i /2)
        string = "degree:" + str(i) + " XC-3 Tree height"
        string2 = "the degree//2"
        print ("\n")
        print(string.ljust(30," ")+":",height)
        print(string2.ljust(30," ")+":",h_approx)

#test_tree_height()
# exp 4 arguement
def fib_iter (n):
    a,b = 0,1
    for i in range(n):
        a,b = b,a+b
    return a

def getFig42(n):
    fibs = []
    for i in range (n):
        fibs.append(fib_iter(i+2))
    plt.plot(fibs)
    plt.xlabel("n")
    plt.ylabel("fib(n+2)")
    plt.title("n vs fib(n+2)")

    plt.show()    

def getFig43(n):
    fibs = []
    for i in range (1,n):
        fibs.append(fib_iter(i+2)/fib_iter(i))
    plt.plot(fibs)
    plt.xlabel("n")
    plt.ylabel("fib(n+2)/fib(n+1)")
    plt.title("n vs fib(n+2)/fib(n+1)")

    plt.show()    

def get_log(n):

    heights = []
    num_nodes = []
    for  i in range (n):
        heights.append( m.ceil(i/2)  )
        num_nodes.append(fib_iter(i+2))
    plt.plot(num_nodes,heights)
    plt.xlabel("nodes(i)")
    plt.ylabel("h(i)")
    plt.title("h(i) vs nodes(i)")
    plt.show()  
    return

#code below generated fig 4.2
getFig42(30)
#----------------------------


#code below generated fig 4.3
getFig43(30)
#----------------------------

#code below generated fig 4.4
get_log(50)
#----------------------------
