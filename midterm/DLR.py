# Preorder + Inorder -> Postorder
def build_postorder(preorder, inorder):
    if not preorder or not inorder:
        return []
    
    root = preorder[0]                   # 前序第一個為根
    mid = inorder.index(root)            # 根在中序的位置

    left = build_postorder(preorder[1:mid+1], inorder[:mid])
    right = build_postorder(preorder[mid+1:], inorder[mid+1:])
    
    return left + right + [root]         # 後序 = 左右根

preorder = input().split()
inorder = input().split()
postorder = build_postorder(preorder, inorder)
print(' '.join(postorder))
