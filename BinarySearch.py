##task 1###
def binary_search(list, low, high, x):

    if high >= low:

        mid = (high + low) // 2

        #
        if list[mid] == x:
            return mid


        elif list[mid] > x:
            return binary_search(list, low, mid - 1, x)

        else:
            return binary_search(list, mid + 1, high, x)

    else:
        return -1


# Test array
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x = 2

result = binary_search(list, 0, len(list) - 1, x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")

##task 2####

def fibonacci_search(lst, target):
    size = len(lst)

    start = -1

 #   f0 = 0
 #   f1 = 1
 #   f2 = 1
 #   while (f2 < size):
 #       f0 = f1
 #       f1 = f2
#        f2 = f1 + f0

#    while (f2 > 1):
#        index = min(start + f0, size - 1)
#        if lst[index] < target:
#            f2 = f1
#            f1 = f0

  #          f0 = f2 - f1
  #          start = index
 #       elif lst[index] > target:
 #           f2 = f0
 #           f1 = f1 - f0
 #           f0 = f2 - f1
#        else:
#            return index
#    if (f1) and (lst[size - 1] == target):
#        return size - 1
#    return None








