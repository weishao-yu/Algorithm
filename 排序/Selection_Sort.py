def selection_sort(L):
    n = len(L)
    for i in range(n-1):
        selection = i 
        for j in range(i+1, n):
            if L[j] < L[selection]:
                selection = j 
        
        L[i], L[selection] = L[selection], L[i]
    return L
        
while True:
    try:
        L = list(map(int, input().split()))
        result = selection_sort(L)
        print(*L)
    except EOFError:
        break