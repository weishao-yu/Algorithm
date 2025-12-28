# Inorder + Postorder -> Preorder
def build_preorder(inorder, postorder):
    if not inorder or not postorder:
        return []
    
    root = postorder[-1]                 # 後序最後為根
    mid = inorder.index(root)

    left = build_preorder(inorder[:mid], postorder[:mid])
    right = build_preorder(inorder[mid+1:], postorder[mid:-1])
    
    return [root] + left + right         # 前序 = 根左右

inorder = input().split()
postorder = input().split()
preorder = build_preorder(inorder, postorder)
print(' '.join(preorder))
