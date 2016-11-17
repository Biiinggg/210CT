class BinTreeNode(object):

    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None

      
def tree_insert( tree, item):
    if tree==None:
        tree=BinTreeNode(item)
    else:
        if(item < tree.value):
            if(tree.left==None):
                tree.left=BinTreeNode(item)
            else:
                tree_insert(tree.left,item)
        else:
            if(tree.right==None):
                tree.right=BinTreeNode(item)
            else:
                tree_insert(tree.right,item)
    return tree

def postorder(tree):
    if(tree.left!=None):
        postorder(tree.left)
    if(tree.right!=None):
        postorder(tree.right)
    print(tree.value)
  

def in_order(tree):
    if(tree.left!=None):
        in_order(tree.left)
    print(tree.value)
    if(tree.right!=None):
        in_order(tree.right)

def in_order_iteratively(tree):
    s=[] ##New stack
    done=False ##End condition
    while(done!=True):
        if(tree!=None):
            s.append(tree)
            tree=tree.left
        else:
            if(len(s)>0):##Something in the Stack
                tree = s.pop()
                print(tree.value)
                tree=tree.right
            else:
                done=True

def tree_sort(A):
    for i in A:
        tree_insert(t,i)
    in_order(t)

if __name__ == '__main__':
    
  t=tree_insert(None,6);
  tree_insert(t,10)
  tree_insert(t,5)
  tree_insert(t,2)
  tree_insert(t,3)
  tree_insert(t,4)
  tree_insert(t,11)
  in_order_iteratively(t)
