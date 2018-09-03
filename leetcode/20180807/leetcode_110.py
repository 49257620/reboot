"""
给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：

一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。

示例 1:

给定二叉树 [3,9,20,null,null,15,7]

    3
   / \
  9  20
    /  \
   15   7
返回 true 。

示例 2:

给定二叉树 [1,2,2,3,3,null,null,4,4]

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
返回 false 。
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if not root:
            return True
        tmp = root
        if abs(self.maxDepth(tmp.left) - self.maxDepth(tmp.right)) > 1:
            return False
        else:
            return self.isBalanced(tmp.left) and self.isBalanced(tmp.right)

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        lvl = 0
        if not root:
            return 0
        ll = [root]

        while ll:
            lvl += 1
            ll = [kid for item in ll for kid in (item.left, item.right) if kid]

        return lvl


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
    line = "[1,2,2,3,3,null,null,4,4]"
    p = stringToTreeNode(line)

    ret = Solution().isBalanced(p)

    print(ret)


if __name__ == '__main__':
    main()
