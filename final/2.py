def LCS(x, y):
    m = len(x)
    n = len(y)
    mp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                mp[i][j] = mp[i - 1][j - 1]+ 1
            else:
                mp[i][j] = max(mp[i - 1][j], mp[i][j - 1])
    return mp

def get_content (x, y, mp):
    i = len(x)
    j = len(y)
    result = []
    while i > 0 and j > 0:
        if x[i - 1] == y[j - 1]:
            result.append(x[i - 1])
            i -= 1
            j -= 1
        elif mp[i - 1][j] > mp[i][j - 1]: 
            i -= 1
        else:
            j -= 1
    result.reverse()
    return result
def check(result, z):
    if result == z:
        return True
    else:
        return False    

while True:
    try:
        x = list(map(int, input().split()))
        y = list(map(int, input().split()))
        z = list(map(int, input().split()))
        table = LCS(x, y)
        calculate = get_content(x, y, table)
        if check(calculate, z):
            print("True")
        else:
            print("False")
    except EOFError:
        break