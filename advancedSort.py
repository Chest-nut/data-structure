# -*- coding:utf-8 -*-

"""高级排序算法"""


from sorthelper import SortHelper
from basicSort import BasicSort

class AdvancedSort(SortHelper):
    """高级排序

    包括：两种归并排序、希尔排序、快速排序
    """

    def __init__(self):
        self.basic_sort = BasicSort()

    def shellSort(self, array, n=3):
        """希尔排序"""

        length = len(array)
        increment = length // n
        while increment >= 1:
            for i in range(increment):  # 分组数为increment
                # 每组内部进行插入排序
                for j in range(i+increment, length, increment):
                    tmp = array[j]
                    index = i   # 当前组的第一个数的索引
                    for k in range(j, increment-1, -increment):
                        if array[k-increment] > tmp:
                            array[k] = array[k-increment]
                        else:
                            index = k
                            break
                    array[index] = tmp
            increment = increment // n


    def mergeSort1(self,array):
        """自顶向下的归并排序"""

        right = len(array)-1
        self.__mergeSort(array, 0, right)

    def mergeSort2(self,array):
        """自底而上的归并排序"""

        n = len(array)
        increment = 2
        while increment/2 < n:
            for i in range(0, n, increment):
                left = i; right = min(left+increment-1, n-1); mid = left + increment//2 -1
                if left is right:
                    break
                if mid >= right:
                    mid = (left+right) // 2
                if array[mid] >= array[mid+1]:
                    self.__merge(array, left, mid, right)
            increment *= 2

    def __merge(self, array, left, mid, right):
        """将数组的 [left,mid] 和 [mid+1,right] 两部分进行归并"""

        tmp = array[left:right+1]
        i = left
        j = mid + 1
        for k in range(left,right+1):
            if i > mid:
                array[k] = tmp[j-left]
                j += 1
            elif j > right:
                array[k] = tmp[i-left]
                i += 1
            elif tmp[i-left] < tmp[j-left]:
                array[k] = tmp[i-left]
                i += 1
            else:
                array[k] = tmp[j-left]
                j += 1

    def __mergeSort(self, array, left, right):
        """用自顶向下的归并排序算法
        对 [left,right] 范围进行归并排序
        """

        # 数组只有一个元素则不用进行排序
        # if left >= right:
        #     return

        # 优化
        if right-left < 16:
            self.basic_sort.insertion_sort1(array, left, right)
            return

        # 将数组分成前后两部分，各自进行归并排序后，再将两部分归并
        mid = (right+left) // 2
        self.__mergeSort(array, left, mid)
        self.__mergeSort(array, mid+1, right)
        if array[mid] >= array[mid+1]:  # 优化
            self.__merge(array, left, mid, right)


    def quickSort(self, array):
        """快速排序对外接口"""

        right = len(array) - 1
        self.__quickSort(array, 0, right)

    def __quickSort(self, array, left, right):
        """对 [left, right] 范围进行快速排序"""

        if left >= right:
            return
        p = self.__partition(array, left, right)
        self.__quickSort(array, left, p-1)
        self.__quickSort(array, p+1, right)

    def __partition(self, array, left, right):
        """将 [left, right] 范围的数进行partition操作，
        使得 array[left, p-1] < array[p] < array[p+1, right],
        并返回p的值
        """

        v = array[left]   # 选定第一个数位基准数
        i = 0             # i用于存放第一个比v大的数的索引，也就是索引大于i的数都比v大
        # 找出第一个比v大的数，索引值赋给i
        for j in range(left+1, right+1):
            if array[j] > v:
                i = j
                break
        # 如果i为0，说明没有数比v大
        if i is 0 :
            array[left], array[right] = array[right], array[left]
            return right
        # 如果i等于right，说明只有最后一个数比v大
        elif i is right:
            array[left], array[right-1] = array[right-1], array[left]
            return right-1

        # 找到有大于v的数之后，遍历之后的每个数，分成大于v和小于v两部分
        for e in range(i+1, right+1):
            if array[e] < v:
                array[e], array[i] = array[i], array[e]
                i += 1
        array[left], array[i-1] = array[i-1], array[left]
        return i-1