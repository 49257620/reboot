"""
155. 最小栈

设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。

push(x) -- 将元素 x 推入栈中。
pop() -- 删除栈顶的元素。
top() -- 获取栈顶元素。
getMin() -- 检索栈中的最小元素。
示例:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.

"""


class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.__data__ = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.__data__.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if len(self.__data__)>0:
            self.__data__.pop()

    def top(self):
        """
        :rtype: int
        """

        return self.__data__[0] if len(self.__data__)>0 else None

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.__data__)

if __name__ == '__main__':
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    print(obj.top())
    print(obj.getMin())
    obj.pop()
    print(obj.__data__)
    obj.pop()
    obj.pop()
    obj.pop()

