
class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value == self.value:
            print(value, self.value)
        if value < self.value: 
            if not self.left: 
                self.left = BinarySearchTree(value)
            else: 
                self.left.insert(value)       
        elif value > self.value: 
            if not self.right: 
                self.right = BinarySearchTree(value)
            else: 
                self.right.insert(value)       

    def compare(self, value):
        if value == self.value:
            print(value, self.value) 
        if value < self.value: 
            if not self.left: 
                self.left = BinarySearchTree(value)
            else: 
                self.left.insert(value)       
        elif value > self.value: 
            if not self.right: 
                self.right = BinarySearchTree(value)
            else: 
                self.right.insert(value)   
        elif value == self.value:
            print(value, self.value)                   
                         

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        elif target < self.value:
            if self.left:
                return self.left.contains(target)
            else: 
                return False    
        elif target > self.value:
            if self.right:
                return self.right.contains(target)
            else: 
                return False 

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right == None: 
            return self.value
        else: 
            return self.right.get_max()    
            

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        if self.right != None and self.left != None:
            cb(self.value)
            self.left.for_each(cb)
            return self.right.for_each(cb)      
        if self.right == None and self.left != None:
            cb(self.value)
            return self.left.for_each(cb)    
        if self.right != None and self.left == None:
            cb(self.value)
            return self.right.for_each(cb) 
        if self.right == None and self.left == None:
            cb(self.value)
            return     