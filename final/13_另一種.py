def stack_permutation(target):
    origin = sorted(target)
    list1 = []
    n = len(origin)
    index = 0
    for i in target:
        while (len(list1) == 0 or list1[-1] != i) and n > index:
            list1.append(origin[index])
            index += 1
        if len(list1) > 0 and list1[-1] == i:
            list1.pop()
        else:
            return False
    return True
while True:
    try:
        target = input().split()
        result = stack_permutation(target) 
        print(result)
    except EOFError:
        break
