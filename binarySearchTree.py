# -*- coding:utf-8 -*-


import random
import re
import time

class Node(object):
    def __init__(self, key, value, l_node=None, r_node=None):
        self.key = key
        self.value = value
        self.l_node = l_node
        self.r_node = r_node

class BinarySearchTree(object):

    def __init__(self, rootNode=None):
        self.size = 0
        self.rootNode = rootNode


    def isEmpty(self):
        """搜索树为空则返回True"""

        return self.size is 0

    def insert_node(self, key, value=None):
        """插入一个节点

        需要传入key和value
        """

        node = Node(key, value)
        if self.rootNode is None:
            self.rootNode = node
            self.size = 1
        else:
            cur_node = self.rootNode
            while True:
                # 如果已存在相同键的节点，用新的value替换旧的value
                if node.key == cur_node.key:
                    cur_node.value = node.value
                    return
                elif node.key < cur_node.key:
                    if cur_node.l_node is None:
                        cur_node.l_node = node
                        self.size += 1
                        return
                    cur_node = cur_node.l_node
                else:
                    if cur_node.r_node is None:
                        cur_node.r_node = node
                        self.size += 1
                        return
                    cur_node = cur_node.r_node

    def search_node(self, key):
        """查找是否存在键为key的节点，存在则返回该节点，不存在则返回None

        因为返回的是节点，所以外部可以操作节点的key和value，
        能否像C++一样返回value指针？
        """

        cur_node = self.rootNode
        while cur_node is not None:
            if key == cur_node.key: # ‘==’不能用‘is’代替
                return cur_node
            elif key < cur_node.key:
                cur_node = cur_node.l_node
            else:
                cur_node = cur_node.r_node
        return

    def preorder(self):
        self._preorder(self.rootNode)

    def _preorder(self, node):
        """前序遍历"""

        if node is None:
            return
        print('%s: %s'%(node.key, node.value))
        self._preorder(node.l_node)
        self._preorder(node.r_node)

    def inorder(self):
        self._inorder(self.rootNode)

    def _inorder(self, node):
        """中序遍历"""

        if node is None:
            return
        self._inorder(node.l_node)
        print('%s: %s'%(node.key, node.value))
        self._inorder(node.r_node)

    def postorder(self):
        self._postorder(self.rootNode)

    def _postorder(self, node):
        """后序遍历"""

        if node is None:
            return
        self._postorder(node.l_node)
        self._postorder(node.r_node)
        print('%s: %s'%(node.key, node.value))

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

    words = []
    with open('text.txt', 'rb') as f:
        text = f.read()
        _, *words = re.findall(r'\w+\b', str(text))  # \b 表示单词边界
    for word in words:
        result = bst.search_node(word)
        if result:
            result.value += 1
        else:
            bst.insert_node(word, 1)

    bst.preorder()
    print(bst.size)