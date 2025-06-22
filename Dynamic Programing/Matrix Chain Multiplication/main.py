import math
MATRIX_DEMENTIONS = [
    (5,6), (6,4), (4,2), (2,3)
]

# MATRIX_DEMENTIONS = [
#     (20,2), (2,30), (30,12), (12,8)
# ]

# MATRIX_DEMENTIONS = [
#     (10,20), (20,50), (50,1), (1,100)
# ]

P = [MATRIX_DEMENTIONS[0][0], MATRIX_DEMENTIONS[0][1]]
P.extend(j for _,j in MATRIX_DEMENTIONS[1:])

dp = [[0 for _ in range(len(MATRIX_DEMENTIONS))] for _ in range(len(MATRIX_DEMENTIONS))]

k_table = [[0 for _ in range(len(MATRIX_DEMENTIONS))] for _ in range(len(MATRIX_DEMENTIONS))]

find_sutuble_calc = []
for i in range(1, len(MATRIX_DEMENTIONS) + 1):
    for j in range(1, len(MATRIX_DEMENTIONS) + 1):
        if j <= i: continue
        find_sutuble_calc.append((i,j))

find_sutuble_calc.sort(key=lambda t: t[1] - t[0])

for t in find_sutuble_calc:
    i,j = t
    K = [_ for _ in range(i, j)]
    results = {
        'value': math.inf,        
    }
    for k in K :
        calc = dp[i-1][k-1] + dp[k][j-1] + P[i-1]*P[k]*P[j]
        if calc < results['value']:
            results.update(
                {
                'value': dp[i-1][k-1] + dp[k][j-1] + P[i-1]*P[k]*P[j],
                'k' : k
                }
            )
    dp[i-1][j-1] = results['value']
    k_table[i-1][j-1] = results['k']


a,b = [int(i) for i in input("Enter Matrix A * Matrix B / input example : 1 4 means M1 * M2 * M3 * M4 : \n").split()]

ask_matrix_range = [_ for _ in range(a,b+1)]
ask_matrix_range_text = " * ".join([f'M{_}' for _ in ask_matrix_range])
find_input_matrix_demenstions_text = " * ".join(
    str(t) for t in [MATRIX_DEMENTIONS[i-1] for i in ask_matrix_range]
)


print(f"""minum multipication for {ask_matrix_range_text} with dementions of {find_input_matrix_demenstions_text} is : {dp[a-1][b-1]}
""")

# ================================================
# 
# ================================================

def split_matrix(start, end):

    if start == end :
        return MATRIX_DEMENTIONS[start]
    
    k = k_table[start][end]

    left = split_matrix(start,k-1)
    right = split_matrix(k, end)

    return [left,right]


print("find matrix position for how to calc : " , split_matrix(a-1, b-1))

print('\n')

print('dp :')
for row in dp:
    print(row)

print('\n')

print('k table :')
for row in k_table:
    print(row)