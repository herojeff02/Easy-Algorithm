class Priority_Queue:
    def __init__(self):
        self.pqueue = []
        self.length = 0

    def push(self, node):
        for i in self.pqueue:
            get_bound(i)
        i = 0
        while i < len(self.pqueue):
            if self.pqueue[i].bound > node.bound:
                break
            i += 1
        self.pqueue.insert(i, node)
        self.length += 1

    def pop(self):
        try:
            result = self.pqueue.pop()
            self.length -= 1
        except:
            print("Priority queue is empty, cannot pop from empty list.")
        else:
            return result


class Node:
    def __init__(self, level, profit, weight):
        self.level, self.profit, self.weight = level, profit, weight
        self.items = []


def get_bound(node):
    if node.weight >= W:
        return 0
    else:
        result = node.profit
        j = node.level + 1
        total_weight = node.weight
        while j <= n - 1 and total_weight + w[j] <= W:
            total_weight = total_weight + w[j]
            result = result + p[j]
            j += 1
        if j <= n - 1:
            result = result + (W - total_weight) * p_per_weight[j]
        return result


p = [60, 100, 120]
n = len(p)
w = [10, 20, 30]
p_per_weight = [6, 5, 4]
W = 50

queue = Priority_Queue()

parent = Node(-1, 0, 0)
max = 0
parent.bound = get_bound(parent)

queue.push(parent)

while queue.length != 0:
    parent = queue.pop()
    if parent.bound > max:
        lvl = parent.level + 1
        left = Node(lvl, parent.profit + p[lvl], parent.weight + w[lvl])
        left.items = parent.items.copy()
        left.items.append(left.level)
        if left.weight <= W and left.profit > max:
            max = left.profit
            bestitems = left.items
        left.bound = get_bound(left)
        if left.bound > max:
            queue.push(left)

        right = Node(left.level, parent.profit, parent.weight)
        right.bound = get_bound(right)
        right.items = parent.items.copy()
        if right.bound > max:
            queue.push(right)

print("\nEND maxprofit = ", max)
print("bestitems = ", bestitems)