def knapsack_01(Vi, Wi, Total_Weight):
    n = len(Vi)
    
    # --- Padding 補 0 ---
    # 為了讓程式碼中的 index i 對應到第 i 個物品 (1-based)
    # 我們在 list 最前面補一個 0
    Vi = [0] + Vi 
    Wi = [0] + Wi
    
    # 初始化 DP 表格
    # 大小為 (n+1) x (Total_Weight+1)，全部填 0
    table = [[0 for k in range(Total_Weight + 1)] for i in range(n + 1)]
    
    # --- 開始填表 ---
    # i 代表目前考慮第幾個物品 (從 1 到 n)
    for i in range(1, n + 1):
        # k 代表目前的背包耐重限制 (從 1 到 Total_Weight)
        for k in range(1, Total_Weight + 1):
            
            # 情況 1: 物品太重了，裝不下
            if Wi[i] > k:
                # 只能選擇「不取」，繼承上一列的結果
                table[i][k] = table[i-1][k]
                
            # 情況 2: 物品裝得下，需決策 (Take or Not Take)
            else:
                # 不取: table[i-1][k]
                # 取:   Vi[i] + table[i-1][k - Wi[i]]
                not_take = table[i-1][k]
                take = Vi[i] + table[i-1][k - Wi[i]]
                
                table[i][k] = max(not_take, take)
    
    # 印出最後一列 (除錯/觀察用)
    #
    # print(table[n]) 
    
    # 回傳表格右下角的值 (最大價值)
    return table[n][Total_Weight]
while True:
    try:
        Vi = list(map(int, input().split()))
        Wi = list(map(int, input().split()))
        Total_Weight = int(input())
        result = knapsack_01(Vi, Wi, Total_Weight)
        print(result)
    except EOFError:
        break