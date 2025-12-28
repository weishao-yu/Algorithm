def LCS(x, y):
    m = len(x)
    n = len(y)
    # 修正 1: 建立表格
    # 這裡讓列數(Row)跟著 x 的長度 (m)，行數(Col)跟著 y 的長度 (n)
    # 寫法是： [[0 * 行數] for _ in range(列數)]
    mp = [[0 for _ in range(n + 1)]for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # 修正 2: 索引偏移
            # DP 的第 i 個字，在 Python list 裡面的索引是 i-1
            if x[i - 1] == y[j - 1]:
                mp[i][j] = mp[i - 1][j - 1] + 1
            else:
                mp[i][j] = max(mp[i - 1][j], mp[i][j - 1])
    return mp[m][n]

while True:
    try:
        x = list(map(int, input().split()))
        y = list(map(int, input().split()))
        print(LCS(x, y))
    except EOFError:
        break
    
