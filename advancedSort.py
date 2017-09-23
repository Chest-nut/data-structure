# -*- coding:utf-8 -*-

"""高级排序算法"""


from sorthelper import SortHelper


class AdvancedSort(SortHelper):
    """高级排序"""

    def mergeSort(self,array):
        """归并排序"""

        right = len(array)-1
        self.__mergeSort(array, 0, right)


    def __mergeSort(self, array, left, right):
        """对 [left,right] 范围的数组进行归并排序"""

        # 数组只有一个元素则不用进行排序
        if left >= right:
            return

        # 将数组分成前后两部分，各自进行归并排序后，再将两部分归并
        mid = (right+left) // 2
        self.__mergeSort(array, left, mid)
        self.__mergeSort(array, mid+1, right)
        self.__merge(array, left, mid, right)


    def __merge(self, array, left, mid, right):
        """对数组 array 进行归并"""

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
