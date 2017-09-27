# -*- coding:utf-8 -*-


import random
import time

class Node(object):
    def __init__(self, key, value, l_node=None, r_node=None):
        self.key = key
        self.value = value
        self.l_node = l_node
        self.r_node = r_node

class BinarySearchTree(object):

    def __init__(self, rootNode=None):
        self.count = 0
        self.rootNode = rootNode


    def size(self):
        """返回搜索树的节点数"""

        return self.count

    def isEmpty(self):
        """搜索树为空则返回True"""

        return self.count is 0

    def insert_node(self, node):
        """插入一个节点"""

        if self.rootNode is None:
            self.rootNode = node
            self.count = 1
        else:
            cur_node = self.rootNode
            while True:
                # 如果已存在相同键的节点，用新的value替换旧的value
                if node.key is cur_node.key:
                    cur_node.value = node.value
                    return
                elif node.key < cur_node.key:
                    if cur_node.l_node is None:
                        cur_node.l_node = node
                        self.count += 1
                        return
                    cur_node = cur_node.l_node
                else:
                    if cur_node.r_node is None:
                        cur_node.r_node = node
                        self.count += 1
                        return
                    cur_node = cur_node.r_node


    def search_node(self, key):
        cur_node = self.rootNode
        while cur_node is not None:
            if key is cur_node.key:
                return cur_node.value
            elif key < cur_node.key:
                cur_node = cur_node.l_node
            else:
                cur_node = cur_node.r_node
        return


    def binarySearch(self, array, target, l=0, r=0):
        # 在arr[l, r]中查找target

        if r is 0:
            r = len(array)-1
        while l <= r:
            # mid = (l+r) // 2, 当l和r很大时，有可能会溢出
            mid = l + (r-l)//2
            if array[mid] is target:
                return mid
            elif array[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1

    def binarySearch2(self, array, target, l=0, r=-2):
        # 使用递归的方法查找target

        if r is -2:
            r = len(array)-1
        if l > r:
            return -1
        # mid = (l+r) // 2, 当l和r很大时，有可能会溢出
        mid = l + (r-l)//2
        if array[mid] is target:
            return mid
        elif array[mid] < target:
            l = mid + 1
            return self.binarySearch(array, target, l, r)
        else:
            r = mid - 1
            return self.binarySearch(array, target, l, r)


if __name__ == '__main__':
    bst = BinarySearchTree()

    # n = 1000
    # array = range(n)
    # index = bst.binarySearch2(array, 100)
    # print('index is %d' %index)

    root = Node('root', 0)
    node1 = Node('node1', 1)
    bst.insert_node(root)
    bst.insert_node(node1)
    print(bst.size(),bst.isEmpty())
    value = bst.search_node('root')
    print(value)