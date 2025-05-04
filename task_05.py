import time
from collections import deque
import uuid
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    # Add the node and its children to the graph
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2**layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2**layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root):
    # Draw the tree
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(
        tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors
    )
    plt.show()


def build_heap_tree(arr):
    # Build a binary tree from the array
    if not arr:
        return None
    nodes = [Node(val) for val in arr]
    for i in range(len(arr)):
        left_index = 2 * i + 1
        right_index = 2 * i + 2
        if left_index < len(arr):
            nodes[i].left = nodes[left_index]
        if right_index < len(arr):
            nodes[i].right = nodes[right_index]
    return nodes[0]


# Generate colors from dark to light
def generate_colors(n):
    colors = []
    for i in range(n):
        shade = int(255 * (i / (n - 1)))
        colors.append(f"#{shade:02x}{shade:02x}{255:02x}")  # RGB format
    return colors


# Depth-First Search traversal using a stack
def dfs_traversal(root):
    stack = [root]
    visited = set()
    nodes_in_order = []

    while stack:
        node = stack.pop()
        if node and node.id not in visited:
            visited.add(node.id)
            nodes_in_order.append(node)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
    return nodes_in_order


# Breadth-First Search traversal using a queue
def bfs_traversal(root):
    queue = deque([root])
    visited = set()
    nodes_in_order = []

    while queue:
        node = queue.popleft()
        if node and node.id not in visited:
            visited.add(node.id)
            nodes_in_order.append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return nodes_in_order


# Animate the tree traversal
def animate_traversal(root, traversal_func, title):
    nodes = traversal_func(root)
    colors = generate_colors(len(nodes))

    print(f"Traversal Order ({title}): {[node.val for node in nodes]}")

    for i, node in enumerate(nodes):
        node.color = colors[i]
        draw_tree(root)
        time.sleep(0.5)  # Pause between steps


# Modified array for building the tree
heap_array = [20, 15, 10, 5, 8, 12, 25, 1, 2, 6]

heap_root = build_heap_tree(heap_array)

# DFS animation
animate_traversal(heap_root, dfs_traversal, "DFS")

# Reset colors for BFS
for node in dfs_traversal(heap_root):
    node.color = "skyblue"

# BFS animation
animate_traversal(heap_root, bfs_traversal, "BFS")
