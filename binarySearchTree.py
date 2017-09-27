# -*- coding:utf-8 -*-


class BinarySearchTree(object):

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


if __name__ == '__main__':
    bst = BinarySearchTree()

    array = [1,2,3,4]
    index = bst.binarySearch(array, 5)
    print('index is %d' %index)
