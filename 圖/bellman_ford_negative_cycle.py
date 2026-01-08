def bellman_ford_negative_cycle(num, matrix, start): # 參數拿掉 end

    # 【特例處理】如果只有 1 個點，直接看自己連自己的邊
    if num == 1:
        # matrix[0][0] 就是自己連自己的權重
        if matrix[0][0] < 0:
            return "Negative Loop"
        else:
            return "No Negative Loop"
    # 1. 為了跑第 N 輪 (偵測用)，列數開 num + 1
    #    優化：內層行數維持 num 即可
    Dk = [[float('inf') for b in range(num)] for a in range(num + 1)]

    Dk[0][start] = 0 
    
    # 初始化 k=1
    for j in range(num):
        Dk[1][j] = matrix[start][j]

    # 2. 跑 k = 2 到 num (也就是 N 輪)
    for k in range(2, num + 1):
        changed = False 
        
        # 這一層是在複製上一輪的結果 (繼承遺志)
        for v in range(num):
            Dk[k][v] = Dk[k-1][v] 

            # 這一層是在找有沒有更短的路 (鬆弛)
            for u in range(num):
                if u != v and matrix[u][v] < float('inf'):
                    d = Dk[k-1][u] + matrix[u][v]
                    if d < Dk[k][v]:
                        Dk[k][v] = d
                        changed = True
        
        # 3. 每一輪跑完所有點後，檢查是否為第 N 輪且有變動
        # (這裡縮排要注意，建議放在外層迴圈最後)
        if k == num and changed:
            return "Negative Loop"

    # 如果跑完都沒有負環，回傳 "OK" 或是最後一列的距離表
    return "No Negative Loop"
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
        start = int(input())
        result = bellman_ford_negative_cycle(num, matrix, start)        
        print(result)
    except EOFError:
        break