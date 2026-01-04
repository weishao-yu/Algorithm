# --- 1. 核心邏輯 ---
def is_safe(Mat, VC, v, c):
    """ 檢查點 v 塗上顏色 c 是否安全 """
    for i in range(len(Mat)):
        # 如果 i 是鄰居 (有邊) 且 i 的顏色也是 c -> 衝突
        if Mat[i][v] == 1 and VC[i] == c:
            return False
    return True

def m_coloring_prefilled(Mat, VC, v, m):
    N = len(Mat)
    
    # Base Case: 所有點都處理完
    if v == N:
        return True

    # 【關鍵差異點】
    # 如果這個點 v 在輸入時就已經有顏色了 (不是 0)
    if VC[v] != 0:
        # 1. 先檢查這個預填的顏色是否合法 (防止題目給錯)
        if not is_safe(Mat, VC, v, VC[v]):
            return False
        
        # 2. 合法就跳過這個點，直接處理下一個 (v+1)
        # 注意：這裡不能回傳 True，要看下一層的結果
        return m_coloring_prefilled(Mat, VC, v + 1, m)

    # 如果是 0 (空點)，就照常嘗試顏色 1~m
    for c in range(1, m + 1):
        if is_safe(Mat, VC, v, c):
            VC[v] = c
            
            if m_coloring_prefilled(Mat, VC, v + 1, m):
                return True
            
            VC[v] = 0 # Backtrack
            
    return False

# --- 2. 主程式輸入 ---
while True:
    try:
        # 讀取點數 N
        line = input().split()
        if not line: break
        N = int(line[0])

        # 讀取鄰接矩陣
        matrix = []
        for i in range(N):
            row = list(map(int, input().split()))
            matrix.append(row)

        # 讀取預填色陣列 (例如: 0 1 0 2 -> 代表點1已塗色1, 點3已塗色2)
        # 題目通常會給這一行
        print("請輸入預填色陣列 (0代表未填):") # 提示用，考試可拿掉
        VC = list(map(int, input().split()))
        
        # 設定顏色總數 m (看題目規定，這裡假設 m=3)
        m = 3 
        
        if m_coloring_prefilled(matrix, VC, 0, m):
            print("Solution found:")
            print(VC)
        else:
            print("No solution")

    except EOFError:
        break