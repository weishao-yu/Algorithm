# --- 1. 核心邏輯 ---
def validate_coloring(Mat, Solution):
    N = len(Mat)
    
    # 遍歷每一個點 u
    for u in range(N):
        # 遍歷 u 的所有鄰居 v
        for v in range(N):
            # 條件 1: u 和 v 之間有邊 (Mat[u][v] == 1)
            # 條件 2: u 和 v 的顏色相同 (Solution[u] == Solution[v])
            # 條件 3: 顏色不能是 0 (有些題目定義 0 是未上色，若全是0也算錯)
            if Mat[u][v] == 1 and Solution[u] == Solution[v]:
                return False # 抓到衝突，直接失敗
                
    return True # 全部檢查完都沒事

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

        # 讀取待驗證的解 (例如: 1 2 3 1)
        print("請輸入要驗證的著色結果:") # 提示用，考試可拿掉
        Solution = list(map(int, input().split()))
        
        # 檢查長度是否吻合 (防呆)
        if len(Solution) != N:
            print("Invalid Length")
            continue

        # 呼叫驗證
        if validate_coloring(matrix, Solution):
            print("Valid") # 合法
        else:
            print("Invalid") # 不合法

    except EOFError:
        break