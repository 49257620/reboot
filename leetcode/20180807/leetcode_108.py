"""
将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

示例:

给定有序数组: [-10,-3,0,5,9],

一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type root: TreeNode
        :rtype: bool
        """

        list_size = len(nums)
        mid_index = list_size // 2
        if list_size>=3:
            result = TreeNode(nums[mid_index])
            nums_left = nums[:mid_index]
            nums_right = nums[mid_index + 1:]

            result.left = self.sortedArrayToBST(nums_left)
            result.right = self.sortedArrayToBST(nums_right)
        elif list_size == 2:
            result = TreeNode(nums[0])
            if nums[0] > nums[1]:
                result.left = TreeNode(nums[1])
            else:
                result.right = TreeNode(nums[1])
        elif list_size == 1:
            result = TreeNode(nums[0])
        else:
            result =None



        """
        mid_index = len(nums)//2
        result = TreeNode(nums[mid_index])
        result.left = TreeNode(nums[mid_index-1])
        result.right = TreeNode(nums[mid_index + 1])
        """





        return result


def treeNodeToString(root):
    if not root:
        return "[]"
    output = ""
    queue = [root]
    current = 0
    while current != len(queue):
        node = queue[current]
        current = current + 1

        if not node:
            output += "null, "
            continue

        output += str(node.val) + ", "
        queue.append(node.left)
        queue.append(node.right)
    return "[" + output[:-2] + "]"


def main():
    line = [-10,-3,0,5,9]

    ret = Solution().sortedArrayToBST(line)

    print(treeNodeToString(ret))


if __name__ == '__main__':
    main()
