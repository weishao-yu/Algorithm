def bellman_ford_negative_cycle(num, matrix, start, end):

    # 1. 表格多開一格 (num + 1)，為了跑第 N 輪
    Dk = [[float('inf') for b in range(num + 1)] for a in range(num + 1)]

    Dk[0][start] = 0   # 出發點自己到自己走 0 個邊的成本是 0

    # 當 k = 1 (初始化) --> 在最多走 1 個邊下，為 cost matrix
    for j in range(num):
        Dk[1][j] = matrix[start][j]
    # 2. 迴圈範圍改成 num + 1 (也就是跑到 k = num)
    for k in range(2, num + 1):     # 最多 k 個邊
        changed = False # 【修正 1】每一輪開始前，先假設沒變
        for v in range(num):    # 從節點 i 出發到節點 v 的最低成本
            Dk[k][v] = min(Dk[k-1][v], Dk[k][v])  # 最多走 k 個邊的成本不高過 k-1 邊

            for u in range(num):  # 從節點 i 出發經過節點 u
                if (u != v and matrix[u][v] < float('inf')):   # 如果 u→v 有路
                    d = Dk[k-1][u] + matrix[u][v]              # 若 i→…→u→v 的成本更好
                    if d < Dk[k][v]:
                        Dk[k][v] = d
                        changed = True # 【修正 2】標記發生改變了！
            # 3. 關鍵判定：如果是第 N 輪 (k == num) 且還有變好
            if k == num and changed:
                return "Negative Loop"
    return Dk[-1]   # 回傳表格中最後一列：最多走 n-1 個邊下的最低成本
while True:
    try:
        num = int(input())
        matrix = []
        for i in range(num):
            row_input = input().split()
            row = []
            for j in row_input:
                if j == 'x':
                    row.append(float('inf'))
                else:
                    row.append(int(j))
            matrix.append(row)
        start, end = map(int, input().split())
        result = bellman_ford_negative_cycle(num, matrix, start, end)
        print(result)
    except EOFError:
        break