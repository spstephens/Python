class ArrayList:
    __length = None
    __list = None

    def __init__(self, list):
        self.__length = 0
        self.__list = []
        if(list != None):
            self.__length = len(list)
            for i in range (len(list)):
                self.__list.append(list[i])
    def getLength(self):
        return len(self.__list)
    def findIndexOf(self, n):
        for i in range (self.__length):
            if(self.__list[i] == n):
                return i

        return -1

    def addToList(self, n):
        if isinstance(n, int):
            self.__list.append(n)
            self.__length += 1
        else:
            return

    def removeFromList(self, n):
        index = self.findIndexOf(n)
        if(index != -1):
            self.__length -= 1
            self.__list.remove(n)
        else:
            print(n, " not found")

    def quickSort(self, start, end):
        if(start < end):
            pivot = self.partition(start, end)
            self.quickSort(start, pivot-1)
            self.quickSort(pivot+1, end)


    def partition(self, start, end):
        pivot = self.__list[end]
        i = (start-1)
        for j in range (start, (end)):
            if(self.__list[j] <= pivot):
                i += 1
                self.swap(i,j)

        self.swap(i+1, end)
        return i+1

    def swap(self, i, j):
        if(i==j):
            return
        else:
            temp_i = self.__list[i]
            self.__list[i] = self.__list[j]
            self.__list[j] = temp_i
            return


    def toString(self):
        if (self.__length != 0):
            for i in range(len(self.__list)):
                print(self.__list[i], end = " ")
            print(" List length = ", self.__length)
        else:
            print("Empty list")
        return


arr = ArrayList([])
arr.toString()
arr.addToList(1)
arr.toString()
arr2 = ArrayList([1,2,3,4])
arr2.toString()
arr2.removeFromList(5)
arr2.toString()
arrSort = ArrayList([1,3,4,2,90,107,42,36,54,21,100,99,45,34,78,94,106,200,76,54,47,87,90])
arrSort.toString()
arrSort.quickSort(0, (arrSort.getLength()-1))
arrSort.toString()

