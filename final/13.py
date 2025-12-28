def check_stack_permutation(target):
    original = sorted(target)
    list = []
    target_index = 0
    n = len(target)
    for i in target:
        while (len(list) == 0 or list[-1] != i) and target_index < n:
            list.append(original[target_index])
            target_index += 1
        if len(list) > 0 and list[-1] == i:
            list.pop()
        else:
            return False
    return True
    

while True:
    try:
        target = input().split()
        result = check_stack_permutation(target)
        print(result)
    except EOFError:
        break