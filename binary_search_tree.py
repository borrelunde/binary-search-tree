class Node(object):
    def __init__(self, datum):
        self.datum = datum
        self.left = None
        self.right = None


class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, datum):
        if self.root is None:
            self.root = Node(datum)
        else:
            self._insert(datum, self.root)

    def _insert(self, datum, node: Node):
        if datum < node.datum:
            # go left
            if node.left is None:
                node.left = Node(datum)
            else:
                self._insert(datum, node.left)
        elif datum > node.datum:
            # go right
            if node.right is None:
                node.right = Node(datum)
            else:
                self._insert(datum, node.right)
        else:
            # datum is equal to an element in the tree
            print(f'Datum {datum} is already present in the tree.')

    def find(self, datum):
        if self.root is not None:
            return self._find(datum, self.root)
        return False

    def _find(self, datum, node: Node):
        if datum > node.datum and node.right is not None:
            return self._find(datum, node.right)
        elif datum < node.datum and node.left is not None:
            return self._find(datum, node.left)
        elif datum == node.datum:
            return True
        return False
