import random

def createRandom(arr, numSwaps):
    
    length = len(arr) - 1
    
    for s in range(numSwaps):
        rand1 = random.randint(0,length)
        rand2 = random.randint(0,length)
        
        while rand2 == rand1 and length > 1:
            rand2 = random.randint(0,length)
            
        elem1 = arr[rand1]
        arr[rand1] = arr[rand2]  
        arr[rand2] = elem1
        
        #print(arr)
        
    return arr    

'''
arr = [i for i in range(0,10)]

for i in range(10):
    print("\n\n", createRandom(arr, i)) '''
    
