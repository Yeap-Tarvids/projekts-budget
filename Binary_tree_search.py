from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False 
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

    def height(self):
        def _height(node):
            if node is None:
                return 0
            left = _height(node.left)
            right = _height(node.right)
            return 1 + max(left, right)

        return _height(self.root)

    def print_tree(self):
        def _print(node, level=0):
            if node is None:
                return
            print("--" * level + str(node.value))
            _print(node.left, level + 1)
            _print(node.right, level + 1)

        _print(self.root)

    def find_siblings_and_cousins(self):
        if not self.root:
            return

        level_nodes = {}  
        queue = [(self.root, None, 0)] #might have to change to 1 if levels end up being the same as height i guess

        while queue:
            node, parent, level = queue.pop(0)

            if level not in level_nodes:
                level_nodes[level] = []
            level_nodes[level].append((node, parent))

            if node.left:
                queue.append((node.left, node, level + 1))
            if node.right:
                queue.append((node.right, node, level + 1))

        print("\nBrāļi:")
        for level, pairs in level_nodes.items():
            brothers = {}
            for node, parent in pairs:
                if parent not in brothers:
                    brothers[parent] = []
                brothers[parent].append(node)
            for siblings in brothers.values():
                if len(siblings) > 1:
                    print(", ".join(str(n.value) for n in siblings), f"(level {level})")

        print("\nBrālēni:")
        for level, pairs in level_nodes.items():
            if level < 2:
                continue
            cousins = {}
            for node, parent in pairs:
                grandparent = self.find_parent(self.root, parent)
                if grandparent not in cousins:
                    cousins[grandparent] = []
                cousins[grandparent].append(node)
            for group in cousins.values():
                if len(group) > 1:
                    print(", ".join(str(n.value) for n in group), f"(level {level})")

    def find_parent(self, current, target):
        if current is None or target is None:
            return None
        if current.left == target or current.right == target:
            return current
        return self.find_parent(current.left, target) or self.find_parent(current.right, target)

my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(76)
my_tree.insert(52)
my_tree.insert(82)

print("Tree structure:")
my_tree.print_tree()

print("\nTree height:")
print(my_tree.height())

my_tree.find_siblings_and_cousins()