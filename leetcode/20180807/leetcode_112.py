"""

给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。

说明: 叶子节点是指没有子节点的节点。

示例:
给定如下二叉树，以及目标和 sum = 22，
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root, sum1):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        ll_list = []
        if not root:
            return False
        ll_tmp = []

        self.deepPath(root,ll_list,ll_tmp)
        print(ll_list)
        flag = False
        for x in ll_list:
            if sum(x) == sum1:
                flag = True

        return flag

    def deepPath(self,root,ll_list,ll_tmp):
        if not root:
            ll_list.append(ll_tmp)
            return
        ll_tmp.append(root.val)
        if not root.left and not root.right:
            ll_list.append(ll_tmp)
        if root.left:
            self.deepPath(root.left,ll_list,ll_tmp[:])
        if root.right:
            self.deepPath(root.right, ll_list, ll_tmp[:])




def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()

    line = "[1,2]"
    root = stringToTreeNode(line);
    line = "1"
    sum = int(line);

    ret = Solution().hasPathSum(root, sum)

    out = (ret);
    print(out)


if __name__ == '__main__':
    main()
