from collections import defaultdict

def build_tree(edges):
    tree = defaultdict(list)
    for edge in edges:
        a, b = edge
        tree[a].append(b)
        tree[b].append(a)
    return tree

def dfs(tree, node, visited):
    visited[node] = True
    max_length = 0
    for neighbor in tree[node]:
        if not visited[neighbor]:
            max_length = max(max_length, dfs(tree, neighbor, visited))
    return max_length

# def find_longest_path(edges):
#     tree = build_tree(edges)
#     n = len(tree)
#     visited = [False] * (n + 1)
#     print(n)
#     return tree, n, visited
#     # return dfs(tree, 1, visited, 0)


edges = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (6, 7),(4, 8),(8, 9)]


# max_length = find_longest_path(edges)
# print( max_length)
tree = build_tree(edges)
x = dfs(tree, 1,False)
print(x)