class BST(object):
    def __init__(self, value=None):
        self.key = value
        self.left = None
        self.right = None

    def insert(self, data):
        if self.key == None:
            self.key = data
            return
        elif self.key == data:
            return
        elif self.key > data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = BST(data)
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right = BST(data)

    def print_tree(self, order):
        if order == "preorder":
            print(self.pre_order(""))
            return
        elif order == "inorder":
            print(self.in_order(""))
            return
        elif order == "postorder":
            print(self.post_order(""))
            return
        else:
            print("invalid")

    def pre_order(self, travarsal):
        travarsal += (str(self.key)+" ")
        if self.left:
            travarsal = self.left.pre_order(travarsal)
        if self.right:
            travarsal = self.right.pre_order(travarsal)
        return travarsal

    def in_order(self, travarsal):
        if self.left:
            travarsal = self.left.in_order(travarsal)
        travarsal += (str(self.key)+" ")
        if self.right:
            travarsal = self.right.in_order(travarsal)
        return travarsal

    def post_order(self, travarsal):
        if self.left:
            travarsal = self.left.post_order(travarsal)
        if self.right:
            travarsal = self.right.post_order(travarsal)
        travarsal += (str(self.key)+" ")
        return travarsal

    def search_bst(self, data):
        if self.key == data:
            print("Node is found.")
            return True
        if data < self.key:
            if self.left:
                self.left.search_bst(data)
            else:
                print("data is not present in tree.")
                return False
        else:
            if self.right:
                self.right.search_bst(data)
            else:
                print("data is not present in tree.")
                return False

    def delete(self, data):
        if self.key is None:
            print("Tree is empty.")
            return
        if data < self.key:
            if self.left:
                self.left = self.left.delete(data)
            else:
                print("given value is not present in tree.")
                return
        elif data > self.key:
            if self.right:
                self.right = self.right.delete(data)
            else:
                print("given value is not present in tree.")
                return
        else:
            if self.left is None:
                temp = self.right
                self = None
                return temp
            if self.right is None:
                temp = self.left
                self = None
                return temp
            node = self.right
            while node.left:
                node = node.left
            self.key = node.key
            self.right = self.right.delete(node.key)
        return self


tree = BST()
l = list(map(int, input("Enter the values to insert in BST:\n").split()))
for i in l:
    tree.insert(i)
tree.print_tree("preorder")
tree.print_tree("inorder")
tree.print_tree("postorder")
d = int(input("Enter the value to delete: "))
tree = tree.delete(d)
tree.print_tree("preorder")
