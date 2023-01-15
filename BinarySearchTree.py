# _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

# DATA STRUCTURES AND ALGORITHMS
# PROGRAMMED BY: Nikka Pauline D. Generalao
# BSCOE 2-2

# _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def findMax(self):
        if self.right == None:
            return self.data
        return self.right.findMax()

    def findMin(self):
        if self.left == None:
            return self.data
        return self.left.findMin()

    def calculateSum(self):
        left_sum = self.left.calculateSum() if self.left else 0
        right_sum = self.right.calculateSum() if self.right else 0
        return self.data + left_sum + right_sum

    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements

    def pre_order_traversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    ## part 2
    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.right

           # min_val = self.right.findMin()
           # self.data = min_val
           # self.right = self.right.delete(min_val)
        # return self

            # exercise part 2
            max_val = self.left.findMax()
            self.data = max_val
            self.left = self.left.delete(max_val)
        return self

def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == '__main__':
    numbers = [1, 5, 3, 10, 34, 4, 8, 15]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.in_order_traversal())
    print("\nBINARY SEARCH TREE"
          "\n---------------------------------------------")
    print("\nThe elements in this binary search tree are: ", "\n\t", numbers)
    print("\nMaximum element is", numbers_tree.findMax())
    print("Minimum element is", numbers_tree.findMin())
    print("The total sum of all elements is", numbers_tree.calculateSum())
    print("Element 10 is present:", numbers_tree.search(10))
    print("In Order Traversal:", numbers_tree.in_order_traversal())
    print("Post Order Traversal:", numbers_tree.post_order_traversal())
    print("Pre Order Traversal:", numbers_tree.pre_order_traversal())
    numbers_tree.delete(10)
    print("After deleting 10:", numbers_tree.in_order_traversal())

    ## For Demo
    name = ["N", "I", "K", "K", "A", "P", "A", "U", "L", "I", "N", "E", "D",
            "G", "E", "N", "E", "R", "A", "L", "A", "O"]
    name_lst = str(name)[1:-1]
    names_tree = build_tree(name)
    print("\n---------------------------------------------")
    print("\nThe elements in this binary search tree are: ", "\n\t", name_lst)
    print("\nMaximum element is", names_tree.findMax())
    print("Minimum element is", names_tree.findMin())
    print("Element A is present:", names_tree.search("A"))
    print("In Order Traversal: ", names_tree.in_order_traversal())
    print("Post Order Traversal:", names_tree.post_order_traversal())
    print("Pre Order Traversal:", names_tree.pre_order_traversal())
    names_tree.delete("A")
    print("After deleting A:", names_tree.in_order_traversal())

