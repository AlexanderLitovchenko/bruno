import unittest

def mergeSort(alist):
    if len(alist) < 2:
        return alist
    else:
        mid = len(alist)//2
        left = alist[:mid]
        right = alist[mid:]

        mergeSort(left)
        mergeSort(right)

        i=0
        j=0
        k=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                alist[k]=left[i]
                i+=1
            else:
                alist[k]=right[j]
                j+=1
            k+=1

        while i<len(left):
            alist[k]=left[i]
            i+=1
            k+=1

        while j<len(right):
            alist[k]=right[j]
            j+=1
            k+=1
        return alist

a = [54,26,93,17,77,31,44,55,20]
b = [5,8,2,8,5,19,2,984,6,1,9,5,9,4]
c = [489,984,561,984,1,68,49856,15,65]
m = c
c.sort()


class TestMergeSort(unittest.TestCase):

    def test1(self):
        self.assertEqual(mergeSort(a), [17, 20, 26, 31, 44, 54, 55, 77, 93])

    def test2(self):
        self.assertEqual(mergeSort(b), sorted(b))

    def test3(self):
          self.assertEqual(mergeSort(m), c)

unittest.main()

