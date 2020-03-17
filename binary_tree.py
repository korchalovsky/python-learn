class Leaf:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def min_left_in_right(current_elem):
    current_elem = current_elem.right
    while current_elem.left:
        current_elem = current_elem.left
    return current_elem


def min_left_in_right_parent(parent):
    current_elem = parent.right
    if current_elem.left.left is None:
        parent = current_elem
        return parent
    else:
        while current_elem.left.left:
            current_elem = current_elem.left
        parent = current_elem
        return parent


class Tree:
    def __init__(self):
        self.first = None

    def add(self, new_value, current_elem=None):
        if current_elem is None:
            current_elem = self.first
        if self.first is None:
            self.first = Leaf(new_value)
        elif new_value < current_elem.value:
            if current_elem.left is not None:
                return self.add(new_value, current_elem.left)
            if current_elem.left is None:
                current_elem.left = Leaf(new_value)
        elif new_value > current_elem.value:
            if current_elem.right is not None:
                return self.add(new_value, current_elem.right)
            if current_elem.right is None:
                current_elem.right = Leaf(new_value)

    def print(self, current_elem=None):
        if current_elem is None and self.first is not None:
            current_elem = self.first
        if current_elem.left is not None:
            self.print(current_elem.left)
        if current_elem.left is None:
            print(current_elem.value)
        if current_elem.right is not None:
            if current_elem.right is not None and current_elem.left is not None:
                print(current_elem.value)
            self.print(current_elem.right)
        if current_elem.right is None and current_elem.left is not None:
            print(current_elem.value)

    def search(self, value, current_elem=None):
        if current_elem is None and self.first is not None:
            current_elem = self.first
            if current_elem.value == value:
                return print(value)
        if current_elem.left is not None:
            if current_elem.left.value == value:
                return print(value)
            else:
                self.search(value, current_elem.left)
        if current_elem.right is not None:
            if current_elem.right.value == value:
                return print(value)
            else:
                self.search(value, current_elem.right)

    def remove(self, value, current_elem=None):
        if current_elem is None and self.first is not None:
            current_elem = self.first
            # if current_elem.value == value:
            #     parent = current_elem
            #     if current_elem.right.left is not None:
            #         current_elem = min_left_in_right(current_elem)
            #         parent.right = current_elem
            #         parent = min_left_in_right_parent(self.first)
            #         parent.left = None
            #         current_elem.right = self.first.right
            #         current_elem.left = self.first.left
            #         return
            #     if current_elem.right.left is None:
            #         parent.right = current_elem.right
            #         parent.right.left = current_elem.left
            #         return
            if current_elem.left is not None:
                if current_elem.left.value == value:
                    parent = current_elem
                    current_elem = current_elem.left
                    if current_elem.left is None and current_elem.right is None:
                        parent.left = None
                        return
                    if current_elem.left is not None and current_elem.right is None:
                        parent.left = current_elem.left
                        return
                    if current_elem.left is None and current_elem.right is not None:
                        parent.left = current_elem.right
                        return
                    if current_elem.left is not None and current_elem.right is not None:
                        if current_elem.right.left is not None:
                            temp_curr = current_elem
                            current_elem = min_left_in_right(current_elem)
                            parent.left = current_elem
                            parent = min_left_in_right_parent(temp_curr)
                            parent.left = None
                            current_elem.right = temp_curr.right
                            current_elem.left = temp_curr.left
                            return
                        if current_elem.right.left is None:
                            if current_elem == parent.right:
                                parent.right = current_elem.right
                                current_elem.right = parent.left
                                return
                            if current_elem == parent.left:
                                parent.left = current_elem.right
                                parent.left.left = current_elem.left
                                return

                else:
                    self.remove(value, current_elem.left)
            if current_elem.right is not None:
                if current_elem.right.value == value:
                    parent = current_elem
                    current_elem = current_elem.right
                    if current_elem.left is None and current_elem.right is None:
                        parent.right = None
                        return
                    if current_elem.left is not None and current_elem.right is None:
                        parent.right = current_elem.left
                        return
                    if current_elem.left is None and current_elem.right is not None:
                        parent.right = current_elem.right
                        return
                    if current_elem.left is not None and current_elem.right is not None:
                        if current_elem.right.left is not None:
                            temp_curr = current_elem
                            current_elem = min_left_in_right(current_elem)
                            parent.right = current_elem
                            parent = min_left_in_right_parent(temp_curr)
                            parent.left = None
                            current_elem.right = temp_curr.right
                            current_elem.left = temp_curr.left
                            return
                        if current_elem.right.left is None:
                            parent.right = current_elem.right
                            parent.right.left = current_elem.left
                            return
                else:
                    self.remove(value, current_elem.right)
            return

tree = Tree()

tree.add(33)
tree.add(35)
tree.add(5)
tree.add(99)
tree.add(1)
tree.add(20)
tree.add(4)
tree.add(17)
tree.add(31)
tree.add(18)
tree.add(19)
tree.add(16)
tree.add(15)
tree.add(34)
tree.add(70)
tree.add(110)
tree.add(105)
tree.add(80)
tree.add(65)

tree.remove(35)


tree.print()
