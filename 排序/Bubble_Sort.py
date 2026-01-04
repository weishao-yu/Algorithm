def Bubble_sort(M):
    n = len(M)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if M[j] > M[j + 1]:
                M[j] , M[j + 1] = M[j + 1], M[j]
    return M

while True:
    try:
        M = list(map(int, input().split()))
        result = Bubble_sort(M)
        print(*result)
    except EOFError:
        break