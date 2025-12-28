def stack_permutation(data, char):
    if char not in data:
        return 0
    n = len(data)
    # L 是用來存放操作序列的陣列 (0:Push, 1:Pop)
    # 長度為 2n (因為進 n 次也要出 n 次)
    L = [0] * (2 * n)
    cnt_info = [0] # 用 list 傳遞引用，計算總共有幾種解
    
    # 開始遞迴生成操作序列
    brute_force(data, L, 0, char, cnt_info)
    return cnt_info[0]

def brute_force(Linp, L, i ,char, cnt):
    N = len(L) # N 為操作序列總長度 (2n)
    
    # Base Case: 操作序列填滿了
    if i == N:
        n = N // 2
        # 再次確認 0 和 1 的數量是否各半 (其實剪枝做好的話，這裡一定成立)
        if sum(L) == n: 
            
            # --- 開始模擬 Stack 運作以印出字母 ---
            stack1 = Linp[::-1] # Input 區 (反轉以方便 pop)
            stack2 = []         # 實際的 Stack
            first_char = None
            for a in L:
                if a == 0: # Push
                    stack2.append(stack1.pop())
                else:      # Pop
                    data = stack2.pop()
                    first_char = data
                    break
            if first_char == char:
                cnt[0] += 1
    else:
        # 嘗試填入 0 (Push) 或 1 (Pop)
        for j in [0, 1]:
            L[i] = j
            
            # --- 關鍵剪枝 logic ---
            # 檢查在目前為止的序列中，Pop 次數是否超過 Push 次數
            flag = True
            for k in range(i + 1):
                n1 = sum(L[:k+1]) # 目前累積的 1 (Pop)
                n0 = (k + 1) - n1 # 目前累積的 0 (Push)
                if n1 > n0: # 非法狀態：想從空堆疊 Pop
                    flag = False
                    break
            
            # 只有在合法狀態下，才繼續往下遞迴
            if flag == True:
                brute_force(Linp, L, i + 1, char, cnt)
while True:
    try:
        data = input().split()
        char = input()
        result = stack_permutation(data, char)
        print(result)
    except EOFError:
        break
