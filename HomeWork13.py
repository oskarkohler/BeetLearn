###taks1####

def a_func():
    x = 1
    y = 2
    z = 3

    print(x, y, z)


print(a_func.__code__.co_nlocals)





###taks2####
def func():
    def innerFunc():
        print("hello")
    return innerFunc()


the_func = func()




###task3###
def choose_func(numbers, func1, func2):
    is_positive = True
    for num in numbers:
        if num <0:
            is_positive = False
            break

    if is_positive:
        return func1(numbers)
    else:
        return func2(numbers)


def remove_negatives(nums):
    #remove negatives
    return [num for num in nums if num > 0]

def square_nums(nums):
    #square numbers
    return [num ** 2 for num in nums]


nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]

choose_func(nums1, square_nums, remove_negatives)
choose_func(nums2, square_nums, remove_negatives)
