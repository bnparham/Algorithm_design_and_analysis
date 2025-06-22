inf = float('inf')

graph = {
    0: {0: 0, 1: 6, 2: 7, 3: inf, 4: inf},
    1: {0: inf, 1: 0, 2: 8, 3: 5, 4: -4},
    2: {0: inf, 1: inf, 2: 0, 3: -3, 4: 9},
    3: {0: inf, 1: -2, 2: inf, 3: 0, 4: inf},
    4: {0: 2, 1: inf, 2: inf, 3: 7, 4: 0}
}

# graph = {
#     0: {0:0, 1:10, 2:5, 3:inf},
#     1: {0:inf, 1:0, 2:3, 4:inf},
#     2: {0:inf, 1:4, 2:0, 3:1},
#     3: {0:inf, 1:2, 2:inf, 3:0},
# }

def bellman_ford(start_node, graph):
    n = len(graph)
    if start_node not in range(n) : raise ValueError('wrong start node input !')
    dp = {i: inf for i in range(n)}
    dp[start_node] = 0

    edges = [(u, v, graph[u][v]) for u in graph for v in graph[u] if graph[u][v] != inf and u != v]

    for _ in range(n):
        for u, v, w in edges:
            if dp[u] + w < dp[v]:
                dp[v] = dp[u] + w

    # Check for negative-weight cycles
    for u, v, w in edges:
        if dp[u] != inf and dp[u] + w < dp[v]:
            return False  # Negative cycle detected

    return True, dp

ok, distances = bellman_ford(0, graph)
print(ok)
print(distances)
