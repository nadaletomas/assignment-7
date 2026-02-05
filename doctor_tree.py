class DoctorNode:
    """
    Represents a doctor in the reporting tree.
    """
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


class DoctorTree:
    """
    Manages the doctor reporting structure using a binary tree.
    """
    def __init__(self):
        self.root = None

    def _find(self, node, parent_name):
        if node is None:
            return None
        if node.name == parent_name:
            return node
        return self._find(node.left, parent_name) or self._find(node.right, parent_name)

    def insert(self, parent_name, doctor_name, side):
        parent = self._find(self.root, parent_name)

        if parent is None:
            raise ValueError("Parent doctor not found")

        if side == "left":
            if parent.left is not None:
                raise ValueError("Left child already exists")
            parent.left = DoctorNode(doctor_name)

        elif side == "right":
            if parent.right is not None:
                raise ValueError("Right child already exists")
            parent.right = DoctorNode(doctor_name)

        else:
            raise ValueError("Side must be 'left' or 'right'")

    def preorder(self, node):
        if node is None:
            return []
        return (
            [node.name]
            + self.preorder(node.left)
            + self.preorder(node.right)
        )

    def inorder(self, node):
        if node is None:
            return []
        return (
            self.inorder(node.left)
            + [node.name]
            + self.inorder(node.right)
        )

    def postorder(self, node):
        if node is None:
            return []
        return (
            self.postorder(node.left)
            + self.postorder(node.right)
            + [node.name]
        )


# Test your DoctorTree and DoctorNode classes here
if __name__ == "__main__":
    tree = DoctorTree()
    tree.root = DoctorNode("Dr. Croft")

    tree.insert("Dr. Croft", "Dr. Goldsmith", "right")
    tree.insert("Dr. Croft", "Dr. Phan", "left")
    tree.insert("Dr. Phan", "Dr. Carson", "right")
    tree.insert("Dr. Phan", "Dr. Morgan", "left")

    print(tree.preorder(tree.root))
    # ['Dr. Croft', 'Dr. Phan', 'Dr. Morgan', 'Dr. Carson', 'Dr. Goldsmith']

    print(tree.inorder(tree.root))
    # ['Dr. Morgan', 'Dr. Phan', 'Dr. Carson', 'Dr. Croft', 'Dr. Goldsmith']

    print(tree.postorder(tree.root))
    # ['Dr. Morgan', 'Dr. Carson', 'Dr. Phan', 'Dr. Goldsmith', 'Dr. Croft']
