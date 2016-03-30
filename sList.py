class Node:
    def __init__(self, data, next_node):
        self.data = data
        self.next = next_node


class sList:
    def __init__(self):
        self.head_node = None
        self.size = 0

    def __str__(self):
        output = []
        curr = self.head_node
        while curr is not None:
            output.append(str(curr.data, ))
            curr = curr.next
        return ' ,'.join(output)

    def add_Front(self, data):
        self.head_node = Node(data, self.head_node)
        self.size += 1

    def remove(self, data):
        if self.size == 0:
            return False
        elif self.head_node.data == data:
            self.head_node = self.head_node.next
            self.size -= 1
            return True
        else:
            curr = self.head_node
            while curr.next is not None and curr.next.data != data:
                curr = curr.next
            if curr.next is None:
                return False
            else:
                curr.next = curr.next.next
                self.size -= 1
                return True

    def return_node(self, index):
        if index < 0 or self.head_node is None:
            return None
        elif index == 0:
            return self.head_node
        else:
            self.head_node = self.head_node.next
            return self.return_node(index - 1)
