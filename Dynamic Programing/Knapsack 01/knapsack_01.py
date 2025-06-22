
M = 30
W = [5, 10, 20]
P = [50, 60, 140]
n = len(P)

dp = [[0 for _ in range(M + 1)] for _ in range(n + 1)]


for i in range(1, n + 1):
    for w in range(0, M+1):
        if W[i - 1] > w :
            dp[i][w] = dp[i-1][w]
        else:
            dp[i][w] = max(
                P[i-1] + dp[i-1][w - W[i-1]] , dp[i-1][w]
            )


# === best case profit ===
print(dp[-1][-1])


w = M
selected_items = []

for i in range(n, 0, -1):
    if dp[i][w] != dp[i-1][w]:
        selected_items.append(i - 1)  # item index (0-based)
        w -= W[i - 1]

print("Selected item indices:", selected_items)
for idx in selected_items:
    print(f"Item {idx}: weight = {W[idx]}, profit = {P[idx]}")