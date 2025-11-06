# class Tree_Node():
#     def __init__(self, data=0):
#         self.Data = data
#         self.Lchild = None
#         self.Rchild = None
# class Tree():
#     def __init__(self, tree_list=[]):
#         if len(tree_list) > 0:
#             self.root = Tree.make_a_tree(1, tree_list)
#         else:
#             self.root = None
#     @staticmethod
#     def make_a_tree(idx, L):
#         if idx <= len(L) and L[idx-1] is not None:
#             new_node = Tree_Node(L[idx-1])
#             new_node.Lchild = Tree.make_a_tree(2*idx, L)
#             new_node.Rchild = Tree.make_a_tree(2*idx+1, L)
#             return new_node
#         return None
inp = input().split()
result = []
for i in inp:
    val = i.strip().strip("'").strip('"')
    if val != 'X':
        result.append(val)
count = len(result)
count -= 1
print(count)

