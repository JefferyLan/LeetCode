
class BinTreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BinTreeTraverse:

    def __init__(self):
        pass

    @staticmethod
    def NLRDeepFirstTraverseWithCur(root, qu):
        if root is None:
            return None
        qu.append(root)
        BinTreeTraverse.NLRDeepFirstTraverseWithCur(root.left, qu)
        BinTreeTraverse.NLRDeepFirstTraverseWithCur(root.right, qu)

    @staticmethod
    def LNRDeepFirstTraverseWithCur(root, qu):
        if root is None:
            return None
        BinTreeTraverse.LNRDeepFirstTraverseWithCur(root.left, qu)
        qu.append(root)
        BinTreeTraverse.LNRDeepFirstTraverseWithCur(root.right, qu)

    @staticmethod
    def LRNDeepFirstTraverseWithCur(root, qu):

        if root is None:
            return None
        BinTreeTraverse.LRNDeepFirstTraverseWithCur(root.left, qu)
        BinTreeTraverse.LRNDeepFirstTraverseWithCur(root.right, qu)
        qu.append(root)

    @staticmethod
    def NLRDeepFirstTraverseWithLoop(root, qu):
        if root is None:
            return
        stack = []
        cur_node = root
        while len(stack) > 0 or cur_node is not None:
            if cur_node is not None:
                qu.append(cur_node)
                stack.append(cur_node)
                cur_node = cur_node.left
            else:
                cur_node = stack.pop()
                cur_node = cur_node.right

    @staticmethod
    def LNRDeepFirstTraverseWithLoop(root, qu):
        if root is None:
            return
        stack = []
        cur_node = root
        while len(stack) > 0 or cur_node is not None:
            # 先遍历到最左边节点
            if cur_node is not None:
                stack.append(cur_node)
                cur_node = cur_node.left
            # 取出左边元素
            else:
                cur_node = stack.pop()
                qu.append(cur_node)
                cur_node = cur_node.right

    @staticmethod
    def LRNDeepFirstTraverseWithLoop(root, qu):
        if root is None:
            return
        stack = [root]
        # 显示实现 NRL
        while len(stack) > 0:
            cur_node = stack.pop()
            qu.append(cur_node)
            if cur_node.left:
                stack.append(cur_node.left)
            if cur_node.right:
                stack.append(cur_node.right)
        # NRL  镜像为 LRN
        qu.reverse()

    @staticmethod
    def BroadFirstTraverseWithCur(root, qu):
        if root is None:
            return
        qu.append(root)
        BinTreeTraverse.BroadFirstTraverseWithCur(root.left, qu)
        BinTreeTraverse.BroadFirstTraverseWithCur(root.right, qu)


    @staticmethod
    def BroadFirstTraverseWithLoop(root, qu):
        if root is None:
            return
        # 队列， FIFO
        q = []
        q.append(root)
        while len(q) > 0:
            cur_node = q.pop()
            qu.append(cur_node)
            if cur_node.left:
                q.insert(0, cur_node.left)
            if cur_node.right:
                q.insert(0, cur_node.right)

    @staticmethod
    def Print(treeNode):
        q = []
        if treeNode:
            q.append(treeNode)
        while len(q) > 0:
            curNode = q.pop()
            print(curNode.val)
            if curNode.left:
                q.insert(0, curNode.left)
            if curNode.right:
                q.insert(0, curNode.right)

    @staticmethod
    def PrintQueue(listTree):
        str_out = ""
        for val in listTree:
            str_out += str(val.val)
            str_out += " "
        return str_out


class TestDataMaker:
    '''
            4
          / \
         9   0
        / \   \
       5   1   6
          / \
         8  7
   :return:
   '''

    __NLR__ = "4 9 5 1 8 7 0 6"
    __LNR__ = "5 9 8 1 7 4 0 6"
    __LRN__ = "5 8 7 1 9 6 0 4"
    __BFS__ = "4 9 0 5 1 6 8 7"

    @staticmethod
    def TestData():

        root = BinTreeNode(4)
        cur = root

        cur.left = BinTreeNode(9)

        cur = cur.left
        cur.left = BinTreeNode(5)
        cur.right = BinTreeNode(1)

        cur = cur.right
        cur.left = BinTreeNode(8)
        cur.right = BinTreeNode(7)

        cur = root
        cur.right = BinTreeNode(0)
        cur = cur.right
        cur.right = BinTreeNode(6)

        return root


if __name__ == '__main__':

    treeNode = TestDataMaker.TestData()

    listTree = []
    BinTreeTraverse.NLRDeepFirstTraverseWithCur(treeNode, listTree)
    footprint = BinTreeTraverse.PrintQueue(listTree)
    if footprint.strip() == TestDataMaker.__NLR__.strip():
        print("NLR_CUR OK")
    else:
        print("NLR_CUR: {0}  |||  {1}".format(TestDataMaker.__NLR__, footprint))

    listTree = []
    BinTreeTraverse.LNRDeepFirstTraverseWithCur(treeNode, listTree)
    footprint = BinTreeTraverse.PrintQueue(listTree)
    if footprint.strip() == TestDataMaker.__LNR__.strip():
        print("LNR_CUR OK")
    else:
        print("LNR_CUR: {0}  |||  {1}".format(TestDataMaker.__LNR__, footprint))

    listTree = []
    BinTreeTraverse.LRNDeepFirstTraverseWithCur(treeNode, listTree)
    footprint = BinTreeTraverse.PrintQueue(listTree)
    if footprint.strip() == TestDataMaker.__LRN__.strip():
        print("LRN_CUR OK")
    else:
        print("LRN_CUR:  {0}  |||  {1}".format(TestDataMaker.__NLR__,  footprint))

    listTree = []
    BinTreeTraverse.NLRDeepFirstTraverseWithLoop(treeNode, listTree)
    footprint = BinTreeTraverse.PrintQueue(listTree)
    if footprint.strip() == TestDataMaker.__NLR__.strip():
        print("NLR_LOOP OK")
    else:
        print("NLR_LOOP: {0}  |||  {1}".format(TestDataMaker.__NLR__, footprint))

    listTree = []
    BinTreeTraverse.LNRDeepFirstTraverseWithLoop(treeNode, listTree)
    footprint = BinTreeTraverse.PrintQueue(listTree)
    if footprint.strip() == TestDataMaker.__LNR__.strip():
        print("LNR_LOOP OK")
    else:
        print("LNR_LOOP:  {0}  |||  {1}".format(TestDataMaker.__LNR__, footprint))

    listTree = []
    BinTreeTraverse.LRNDeepFirstTraverseWithLoop(treeNode, listTree)
    footprint = BinTreeTraverse.PrintQueue(listTree)
    if footprint.strip() == TestDataMaker.__LRN__.strip():
        print("LRN_LOOP OK")
    else:
        print("LRN_LOOP:  {0}  |||  {1}".format(TestDataMaker.__LRN__,  footprint))

    listTree = []
    BinTreeTraverse.BroadFirstTraverseWithCur(treeNode, listTree)
    footprint = BinTreeTraverse.PrintQueue(listTree)
    if footprint.strip() == TestDataMaker.__BFS__.strip():
        print("BFS_CUR OK")
    else:
        print("BFS_CUR:  {0}  |||  {1}".format(TestDataMaker.__BFS__, footprint))

    listTree = []
    BinTreeTraverse.BroadFirstTraverseWithLoop(treeNode, listTree)
    footprint = BinTreeTraverse.PrintQueue(listTree)
    if footprint.strip() == TestDataMaker.__BFS__.strip():
        print("BFS_LOOP OK")
    else:
        print("BFS_LOOP:  {0}  |||  {1}".format(TestDataMaker.__BFS__, footprint ))


