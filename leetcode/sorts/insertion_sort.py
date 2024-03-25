def insertion_sort(array):
    for i in range(l, len(array)):
        curNum = array[i]
        for j in range(i-1, 0, -1): # Start at left of i and go in reverse
            if array[j] > curNum:
                array[j+1] = array[j]
            else:
                array[j+1] = curNum
                break