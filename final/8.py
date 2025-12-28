def Hamilton(n, graph):
    path = [0]
    visited = {0}
    

while True:
    try:
        n = int(input())
        graph = []
        for i in range(n):
            row = input().split()
            row1 = []
            for i in row:
                if i == 'x':
                    row.append(0)
                else:
                    row.append(int(i))
            graph.append(row1)
        print(Hamilton(n, graph))