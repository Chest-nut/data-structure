# -*- coding:utf-8 -*-

"""
基础排序算法
"""

import random
from copy import copy

from sorthelper import SortHelper


class BasicSort(SortHelper):
    """基础排序

    包括：插入排序、选择排序、冒泡排序
    """

    def insertion_sort(self, array):
        """未优化插入排序"""

        for i in range(1, len(array)):
            for j in range(i, 0, -1):
                if array[j-1] > array[j]:
                    array[j], array[j-1] = array[j-1], array[j]
                else:
                    break


    def insertion_sort1(self, array, left=0, right=0):
        """经过优化的插入排序

        可以指定需要排序的范围，默认是0到length-1
        """

        if right is 0:
            right = len(array) - 1

        for i in range(left+1, right+1):
            tmp = array[i]
            index = left
            for j in range(i, left, -1):
                if array[j-1] > tmp:
                    array[j] = array[j-1]
                else:
                    index = j
                    break
            array[index] = tmp


    def insertion_sort_py(self, array):
        """python动态语言特性实现的插入排序：

        n从2开始，取第n个数，将其依次与第1到第n-1个数进行比较，
        当遇见一个数比它大时，说明它就应该插入到比它大这个数之前，
        只需将其pop出，然后insert到那个比它大的数的位置。
        """

        for i in range(1, len(array)):
            for j in range(i):
                if array[i] <= array[j]:
                    tmp = array.pop(i)
                    array.insert(j, tmp)
                    break


    def selection_sort(self, array):
        """选择排序"""

        n = len(array)
        for i in range(n-1):
            minIndex = i
            for j in range(i+1, n):
                if array[minIndex]  > array[j]:
                    minIndex = j
            if minIndex is not i:
                array[minIndex], array[i] = array[i], array[minIndex]


    def bubble_sort(self, array):
        """冒泡排序"""

        n = len(array)
        flag = True     # flag 用于优化当后面的数列已经有序的情况
        for i in range(n):
            if flag:
                flag = False    # 如果本次循环结束flag仍为False，说明后续数列已经有序，下次循环不再进行
                for j in range(n-1, i, -1):
                    if array[j-1] > array[j]:
                        array[j-1], array[j] = array[j], array[j-1]
                        flag = True
            else:
                break


if __name__ == '__main__':

    basic_sort = BasicSort()

    n = 10000
    array = random.sample(range(n),n)
    array_copy1 = copy(array)
    array_copy2 = copy(array)
    array_copy3 = copy(array)
    array_copy4 = copy(array)

    basic_sort.test_sort(array, basic_sort.insertion_sort, '未优化的插入排序')
    basic_sort.test_sort(array_copy1, basic_sort.insertion_sort1, '已优化的插入排序')
    basic_sort.test_sort(array_copy2, basic_sort.insertion_sort_py, 'py风格的插入排序')
    basic_sort.test_sort(array_copy3, basic_sort.selection_sort, '选择排序')
    basic_sort.test_sort(array_copy4, basic_sort.bubble_sort, '冒泡排序')