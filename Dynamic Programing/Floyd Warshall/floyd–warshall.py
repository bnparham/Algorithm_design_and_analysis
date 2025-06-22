inf = float('inf')

# graph = {
#     0: {0:0, 1:5, 2:inf, 3:inf},
#     1: {0:50, 1:0, 2:15, 3:5},
#     2: {0:30, 1:inf, 2:0, 3:15},
#     3: {0:15, 1:inf, 2:5, 3:0}
# }

graph = {
    0: {0:0, 1:3, 2:8, 3:inf, 4:-4},
    1: {0:inf ,1:0, 2:inf, 3:1, 4:7},
    2: {0:inf, 1:4, 2:0, 3:inf, 4:inf},
    3: {0:2, 1:inf, 2:-5, 3:0, 4:inf},
    4: {0:inf, 1:inf, 2:inf ,3:6, 4:0},
}

def floyd(graph):
    for k in range(len(graph)):
        for i in range(len(graph)):
            if k!=i:
                for j in range(len(graph)):
                    if i!=j and k!=j:
                        a = graph[i][k]
                        b = graph[k][j]
                        if a == inf or b == inf:
                            continue
                        if a + b < graph[i][j]:
                            graph[i][j] = a+b
                    continue
            continue
    return graph



def print_floyd(floyd):
    for v,p in floyd.items():
        for u,w in p.items():
            print(f"{v} to {u} => {w}", end=" | ")
        print('\n')

print_floyd(floyd(graph))

# ======
# all path examples for A1 :

# 2 -> 1 -> 3
# 2 -> 1 -> 4

# 3 -> 1 -> 2
# 3 -> 1 -> 4

# 4 -> 1 -> 2
# 4 -> 1 -> 3
# ======