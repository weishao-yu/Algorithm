# m_coloring_all
# solutions:用來存所有找到的解 (List of Lists)
def m_coloring_all(Mat, VC, v, m, solutions):
    N = len(Mat)
    
    # 1. Base Case: 填滿所有節點
    if v == N:
        # 找到一組解了！
        # 【重要】要用 list(VC)或是 VC[:] 複製一份
        # 不然 VC 後面被改回 0，你存的東西也會變全是 0
        solutions.append(list(VC)) 
        return 

    # 2. 嘗試顏色 1 到 m
    for c in range(1, m + 1):
        flag = True
        
        # 檢查衝突
        for i in range(v):
            if Mat[i][v] == 1 and VC[i] == c:
                flag = False
                break
        
        if flag == True:
            VC[v] = c
            
            # 【修改點】: 這裡不用 check True/False 了
            # 直接遞迴下去找，讓它跑完所有可能性
            m_coloring_all(Mat, VC, v + 1, m, solutions)
            
            # Backtrack: 這一層試完（包含下面所有可能性都跑完），歸零換下個顏色
            VC[v] = 0

# --- 主程式呼叫方式 ---
while True:
    try:
        N = int(input())
        
        matrix = []
        for i in range(N):
            row = list(map(int, input().split()))
            matrix.append(row)
            
        # 題目給定的顏色數 m (例如 m=3)
        m = 3 
        
        VC = [0] * N
        all_solutions = [] # 用來存答案的容器
        
        # 呼叫函式
        m_coloring_all(matrix, VC, 0, m, all_solutions)
        
        # 輸出結果
        if len(all_solutions) > 0:
            print(f"Total solutions: {len(all_solutions)}")
            for sol in all_solutions:
                print(sol)
        else:
            print("No solution")

    except EOFError:
        break