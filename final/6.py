def function(W, X):
    total = W[0]
    num = len(X)
    for i in range(num):
        total += W[i + 1] * X[i]
    return total == 0
while True:
    try:
        W = list(map(int, input().split()))
        X = list(map(int, input().split()))
        print(function(W,X))
    except EOFError:
        break