from collections import defaultdict
def build_tree(edges):
    tree = defaultdict(list)
    for edge in edges:
        a, b = edge
        tree[a].append(b)
        tree[b].append(a)
    return tree

queue = []
visited = []
def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)
    while queue:
        s = queue.pop(0)
        print(s, end=" ")
        for neighbor in graph[s]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

edges = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (6, 7)]
x = build_tree(edges)
d = (visited, x, '1')
# print(d)