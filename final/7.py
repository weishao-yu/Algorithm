def function(X):
    A = X.pop(0)
    target = -A
    possible_sum ={0}
    for i in X:
        current_sum = set()
        for s in possible_sum:
            current_sum.add(i + s)
        possible_sum.update(current_sum)

    return target in possible_sum

while True:
    try:
        X = list(map(int, input().split()))
        print(function(X))
    except EOFError:
        break