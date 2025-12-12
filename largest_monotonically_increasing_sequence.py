class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.seq = [value]


class Tree:
    def __init__(self):
        self.root = None
        self.best = []

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
            self.best = [value]
            return

        self.insertNode(self.root, value)

    def insertNode(self, node, value):
        if value < node.value:
            if node.left:
                self.insertNode(node.left, value)
            else:
                new_node = Node(value)
                node.left = new_node
                new_node.seq = self.checkSequence(self.root, value) + [value]
                self.update(new_node.seq)

        else:
            if node.right:
                self.insertNode(node.right, value)
            else:
                new_node = Node(value)
                node.right = new_node
                new_node.seq = self.checkSequence(self.root, value) + [value]
                self.update(new_node.seq)

    
    def checkSequence(self, node, target):
        if not node:
            return []

        best = []
        if node.value < target:
            best = node.seq
            right_best = self.checkSequence(node.right, target)
            if len(right_best) > len(best):
                best = right_best

        left_best = self.checkSequence(node.left, target)
        if len(left_best) > len(best):
            best = left_best

        return best

    def update(self, seq):
        if len(seq) > len(self.best):
            self.best = seq


tree = Tree()
numbers = []

print("Masukan sebuah sequence bilangan (tekan enter untuk berhenti):")
numbers = list(map(int, input().split()))

for num in numbers:
    tree.insert(num)

print("Input:", numbers)
print("Largest Monotonically Increasing Subsequence:", tree.best)
