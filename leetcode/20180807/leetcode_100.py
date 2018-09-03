"""
给定两个二叉树，编写一个函数来检验它们是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # print("--------------------", p.val, p.left.val, p.right.val)
        return Solution.compareNode(p, q)

    @staticmethod
    def compareNode(p, q):
        if p and q:
            if p.val == q.val:
                return Solution.compareNode(p.left, q.left) and Solution.compareNode(p.right, q.right)
            else:
                return False
        elif not p and not q:
            return True
        else:
            return False


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
    line = "[1,2,3]"
    p = stringToTreeNode(line)
    line = "[1,2,3]"
    q = stringToTreeNode(line)

    ret = Solution().isSameTree(p, q)

    print(ret)


if __name__ == '__main__':
    main()
