

def quick_sort(array):

    size = len(array)
    if size <= 1:
        return array
    
    pivot = array.pop() # You can also find another way to select pivot based on mid value
    less_than = []
    greater_than = []

    for num in array:
        if num > pivot:
            greater_than.append(num)
        else:
            less_than.append(num)
    
    return quick_sort(less_than) + [pivot] + quick_sort(greater_than)

print(quick_sort([1,24,5,4,5,67,78,3,2]))

# More efficient implementation here: https://www.youtube.com/watch?v=CB_NCoxzQnk&list=PLj8W7XIvO93rJHSYzkk7CgfiLQRUEC2Sq&index=5&ab_channel=OggiAI-ArtificialIntelligenceToday