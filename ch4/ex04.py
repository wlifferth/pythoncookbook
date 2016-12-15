# Problem: You are building a custom class on which you would like to support iteration, but would like an easy way to implement an iterator protocol

class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()

root = Node(0)
c1 = Node(1)
c2 = Node(2)
root.add_child(c1)
root.add_child(c2)
c1.add_child(Node(3))
c1.add_child(Node(4))
c2.add_child(Node(5))

for ch in root.depth_first():
    print(ch)
