# -*- coding:utf-8 -*-

"""
排序算法
"""


class Sort(object):

    def __init__(self):
        self.array = []

    def insertion_sort1(self, array):
        """
        利用python动态语言特性实现的插入排序：
        n从2开始，取第n个数，将其依次与第1到第n-1个数进行比较，
        当遇见有一个数比这个数大时，将这个数pop出，
        并insert到那个比它大的数的位置。
        """

        self.array = array
        count = 0
        for i in range(1, len(self.array)):
            for j in range(i):
                # count += 1
                if self.array[i] <= self.array[j]:
                    count += 1
                    tmp = self.array.pop(i)
                    self.array.insert(j, tmp)
                    break
        print('第一种方法进行了 %d 次数据交换：'%count)


    def insertion_sort2(self, array):
        """
        n从2开始，取第n个数，将其和前一个数比较，
        如果比前一个数小，则互换位置，然后再和前一个数比较，以此类推，
        直到比前一个数大为止
        """

        self.array = array
        count = 0
        for i in range(1, len(self.array)):
            for j in range(i, 0, -1):
                # count += 1
                if self.array[j] < self.array[j-1]:
                    count += 1
                    self.array[j], self.array[j-1] = self.array[j-1], self.array[j]
                else:
                    break
        print('第二种方法进行了 %d 次数据交换：'%count)


    def selection_sort(self, array):
        n = len(array)
        count = 0
        for i in range(n-1):
            minIndex = i
            for j in range(i+1, n):
                if array[minIndex]  > array[j]:
                    count += 1
                    minIndex, j = j, minIndex
            array[minIndex], array[i] = array[i], array[minIndex]
        print(count)
        return array


    def view(self):
        print(self.array)

