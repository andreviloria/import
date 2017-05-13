# a BinarySearchTree is one of
# - comes_before
# - BSTNode

# a BSTNode is one of
# - root
# - left
# - right
# - None

class BSTNode:
    def __init__(self, root, left, right):
        self.root = root
        self.left = left
        self.right = right
    def __eq__(self, other):
        return type(other) == BSTNode and self.root == other.root and self.left == other.left and self.right == other.right
    def __repr__(self):
        return ("BSTNode(%r, %r, %r)" % (self.root, self.left, self.right))

class BinarySearchTree:
    def __init__(self, comes_before, bst_node = None):
        self.comes_before = comes_before
        self.bst_node = bst_node
    def __eq__(self, other):
        return type(other) == BinarySearchTree and self.comes_before == other.comes_before and self.bst_node == other.bst_node
    def __repr__(self):
        return ("BinarySearchTree(%r, %r)" % (self.comes_before, self.bst_node))

# value value -> boolean
# compares the two given values and returns a boolean 
# on whether the first value comes before the second
def comes_before(a,b):
    if a is None:
        return False
    if b is None:
        return False
    return a < b

# BinarySearchTree -> boolean
# returns a boolean if given tree is None
def is_empty(BinarySearchTree):
    return BinarySearchTree.bst_node is None

# BinarySearchTree value -> BinarySearchTree
# takes in a tree and value and returns a new tree with the value in the correct place
def insert(bst, val):
    if is_empty(bst):
        return BinarySearchTree(False, BSTNode(val, None, None))
    return BinarySearchTree(False, insert_helper(bst.bst_node, val))

# BSTNode value -> BSTNode
# takes in a node and value then returns a new node with the value in the correct place
def insert_helper(bst_node, val):
    if bst_node is None:
        return BSTNode(val, None, None)
    if comes_before(val, bst_node.root):
        return BSTNode(bst_node.root, insert_helper(bst_node.left, val), bst_node.right)
    return BSTNode(bst_node.root, bst_node.left, insert_helper(bst_node.right, val))

# BinarySearchTree value -> boolean
# takes in a tree and value and returns true or false if the value is in the tree
def lookup(bst, val):
    if is_empty(bst):
        return False
    return lookup_helper(bst.bst_node, val)

# BSTNode value -> boolean
# takes in a node and value and returns true or false if the value is in the nodes 
def lookup_helper(bst_node, val):
    if bst_node is None:
        return False
    if comes_before(val, bst_node.root):
        return lookup_helper(bst_node.left, val)
    if (not(comes_before(val, bst_node.root)) and not (comes_before(bst_node.root, val))):
        return True
    return lookup_helper(bst_node.right,val)
    

# BinarySearchTree value -> BinarySearchTree
# takes in a tree and value and returns a new tree after deleting the value given
def delete(bst, val):
    if is_empty(bst):
        return BinarySearchTree(bst.comes_before)
    return BinarySearchTree(False, delete_helper(bst.bst_node, val))


# BSTNode value -> BSTNode
# takes in a node and value and returns a new node ofter deleting the value given
def delete_helper(bst_node, val):
    if bst_node is None:
        return None
    if comes_before(val, bst_node.root):
        return BSTNode(bst_node.root, delete_helper(bst_node.left, val), bst_node.right)
    if (not(comes_before(val, bst_node.root)) and not (comes_before(bst_node.root, val))):
        if bst_node.left is not None:
            return BSTNode(bst_node.left.root, bst_node.left.left, bst_node.right)
        elif bst_node.right is not None:
            return BSTNode(bst_node.right.root, bst_node.left, bst_node.right.right)
        return None
    return BSTNode(bst_node.root, bst_node.left, delete_helper(bst_node.right, val))
