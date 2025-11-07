class Tree_Node():
    def __init__(self, Data=0):
        self.Data = Data
        self.left = None
        self.right = None
class Tree():
    def __init__(self, tree_list= []):
        if len(tree_list) != 0:
            self.root = Tree.make_a_tree(1, tree_list)
        else:
            self.root = None
    @staticmethod
    def make_a_tree(idx, L):
        if idx <= len(L) and L[idx - 1] is not None:
            node = Tree_Node(L[idx - 1])
            node.left = Tree.make_a_tree(2 * idx, L)
            node.right = Tree.make_a_tree(2 * idx + 1, L)
            return node
        return None
    
def DLR(ptr):
    if ptr is not None:
        print(ptr.Data, end=' ')
        DLR(ptr.left)
        DLR(ptr.right)
def LDR(ptr):
    if ptr is not None:
        LDR(ptr.left)
        print(ptr.Data, end=' ')
        LDR(ptr.right)
def LRD(ptr):
    if ptr is not None:
        LRD(ptr.left)
        LRD(ptr.right)
        print(ptr.Data, end=' ')

inp = input().split()
result = []
for i in inp:
    val = i.strip().strip("'").strip('"')
    if val == 'X':
        result.append(None)
    else:
        result.append(val)
tree = Tree(result)
DLR(tree.root)
print('')
LDR(tree.root)      
print('')
LRD(tree.root)