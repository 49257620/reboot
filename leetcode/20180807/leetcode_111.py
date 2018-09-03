"""

给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明: 叶子节点是指没有子节点的节点。

示例:

给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回它的最小深度  2.
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        lvl_list = []
        lvl = 0
        self.minLvl(root, lvl_list, lvl)
        if len(lvl_list)>0:
            return min(lvl_list)
        else:
            return 0

    def minLvl(self, root, lvl_list, lvl):
        if not root:
            return
        lvl += 1
        if not root.left and not root.right:
            lvl_list.append(lvl)
        self.minLvl(root.left, lvl_list, lvl)
        self.minLvl(root.right, lvl_list, lvl)


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
    line = "[3,9,20,null,null,15,7]"
    p = stringToTreeNode(line)

    ret = Solution().minDepth(p)

    print(ret)


if __name__ == '__main__':
    main()
