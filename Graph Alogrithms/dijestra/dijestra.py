inf = float('inf')

graph = {
    0: {0:0, 1:10, 2:5, 3:inf},
    1: {0:inf, 1:0, 2:3, 4:inf},
    2: {0:inf, 1:4, 2:0, 3:1},
    3: {0:inf, 1:2, 2:inf, 3:0},
}


def relax(u, v ,w ,dp):
    if dp[u] + w < dp[v]:
        dp[v] = dp[u] + w

def dijestra(start_node, graph):
    visitd_nodes = []
    n = len(graph)
    dp = {i:inf for i in range(n)}
    dp[start_node] = 0
    
    while len(visitd_nodes) != len(graph):
        find_node = min(
                    filter(lambda t: t[0] not in visitd_nodes, dp.items())
                    ,key=lambda t:t[1])[0]
        visitd_nodes.append(find_node)
        neighbors = [(v ,w) for v,w in graph[find_node].items() if v != 0 and w != inf and v not in visitd_nodes]

        for v,w in neighbors :
            relax(find_node, v ,w ,dp)

    return dp

print(dijestra(0, graph))