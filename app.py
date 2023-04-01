from binary_search_tree import BinarySearchTree


tree = BinarySearchTree()

tree.insert(4)
tree.insert(2)
tree.insert(8)
tree.insert(5)
tree.insert(10)
tree.insert(10)

print(tree.find(4))
print(tree.find(5))
print(tree.find(10))
print(tree.find(11))

"""
Output:
Datum 10 is already present in the tree.
True
True
True
False
"""
