# 設計一函式 LCString_compute()，其功能為計算輸入的兩個字串其 最長共同子字串 (Longest Common Substring) 的長度，並輸出。
# Input format 輸入兩行字串 (String)，可能包含英文大小寫或數字。
# Output format 輸出最長共同子字串的長度。
# Sample input
# BANANA
# BANDANA
# Sample output
# 3
def LCString_compute(str1, str2):
    nX = len(str1)
    nY = len(str2)
    table = [[0 for i in range(nY + 1)]for j in range(nX + 1)]
    num = 0
    for i in range(1, nX + 1):
        for j in range(1, nY + 1):
            if str1[i - 1] == str2[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
                if num < table[i][j]:
                    num = table[i][j]
            else:
                table[i][j] = 0
    return num
while True:
    try:
        str1 = input().strip()
        str2 = input().strip()
        print(LCString_compute(str1, str2))
    except EOFError:
        break
# 錯誤:
# 回傳最大值 (Return Error)
# 你的寫法： return max(table)
# 後果： table 是一個二維陣列 (List of Lists)。max(table) 會回傳「總和最大」或「字典序最大」的那一列 (Row)（例如回傳 [0, 1, 2, 0]），而不是你要的單一數字 3。
# 修正： 我們需要在迴圈中用一個變數 max_len 來隨時記錄最大值，或者用雙層迴圈找最大值。
# 輸入處理 (Input Error)
# 你的寫法： input().split()
# 後果： 如果輸入是 BANANA，split() 會把它變成列表 ['BANANA']。那麼 len(str1) 變成 1，你的程式根本沒在比對字元。
# 修正： 直接用 input().strip() 讀取字串即可。


