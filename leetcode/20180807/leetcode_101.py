"""
给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        flag = True
        if not root:
            return True
        ll = [root]

        while flag:
            ll = [kid for item in ll for kid in (item.left if item else None, item.right if item else None)]
            if ll.count(None) == len(ll):
                break
            for x in range(len(ll)//2):
                val1 = ll[x].val if ll[x] else None
                val2 = ll[-x - 1].val if ll[-x - 1] else None
                if val1 != val2:
                    flag = False
                    break

        """
        while flag:
            flag2 = False
            temp = []
            for x in range(len(ll)):
                val1 = ll[x].val if ll[x] else None
                val2 = ll[-x - 1].val if ll[-x - 1] else None
                left = ll[x].left if ll[x] else None
                right = ll[x].right if ll[x] else None
                if val1 != val2:
                    flag = False
                    break
                if left or right:
                    flag2 = True
                temp.append(left)
                temp.append(right)

            ll = temp
            if not flag2:
                break
        """

        """
        while flag:
            flag2 = False
            for x in range(len(ll) // 2):
                if (ll[x].val if ll[x] else None) != (ll[-x - 1].val if ll[-x - 1] else None):
                    flag = False
                    break
                if ll[x]:
                    flag2 = True
            if not flag2:
                break
            if flag:
                ll = [kid for item in ll for kid in (item.left if item else None, item.right if item else None)]
        """
        return flag


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
    line = "[6,82,82,null,53,53,null,-58,null,null,-58,null,-85,-85,null,-9,null,null,-9,null,48,48,null,33,null,null,33,81,null,null,81,5,null,null,5,61,null,null,61,null,9,9,null,91,null,null,91,72,7,7,72,89,null,94,null,null,94,null,89,-27,null,-30,36,36,-30,null,-27,50,36,null,-80,34,null,null,34,-80,null,36,50,18,null,null,91,77,null,null,95,95,null,null,77,91,null,null,18,-19,65,null,94,null,-53,null,-29,-29,null,-53,null,94,null,65,-19,-62,-15,-35,null,null,-19,43,null,-21,null,null,-21,null,43,-19,null,null,-35,-15,-62,86,null,null,-70,null,19,null,55,-79,null,null,-96,-96,null,null,-79,55,null,19,null,-70,null,null,86,49,null,25,null,-19,null,null,8,30,null,82,-47,-47,82,null,30,8,null,null,-19,null,25,null,49]"
    p = stringToTreeNode(line)

    ret = Solution().isSymmetric(p)

    print(ret)


if __name__ == '__main__':
    main()
