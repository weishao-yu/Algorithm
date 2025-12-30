# 設計一函式 LCS_practice()，其功能為計算輸入的兩個序列其最大共同子序列 (Longest Common Subsequence) 的長度，並輸出。
# Input format 輸入兩行序列，每行包含數個數字，數字間以空格隔開。
# Output format 輸出最大共同子序列的長度。
# input
# 2 5 7 9 3 1 2
# 3 5 3 2 8
# output
# 3
def LCS(x, y):
    nX = len(x)
    nY = len(y)
    table = [[0  for i in range(nY + 1)] for j in range(nX + 1)]
    for i in range(1, nX + 1):
        for j in range(1, nY + 1):
            if x[i - 1] == y[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])
    return table[nX][nY]
while True:
    try:
        x = list(map(int, input().split()))
        y = list(map(int, input().split()))    
        print(LCS(x, y))
    except EOFError:
        break
