class BinTreeNode:
    """class BiNode provide interface to set up a BiTree Node and to interact"""
    def __init__(self, val=None, left=None, right=None):
        """set up a node """
        self.val = val
        self.left = left
        self.right = right

    def get_element(self):
        """return node.element"""
        return self.val

    def dict_form(self):
        """return node as dict form"""
        dict_set = {
            "element": self.val,
            "left": self.left,
            "right": self.right,
        }
        return dict_set

    def __str__(self):
        """when print a node , print it's element"""
        return str(self.val)
