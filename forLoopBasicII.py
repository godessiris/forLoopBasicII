# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]
# def biggie_size(lst):
#     for i in range (0, len(lst), 1):
#         if (lst[i] > 0):
#             lst[i] = "big"
#     print(lst)
#     return lst
# biggie_size([2,3,-8,5,-1])

# Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it

# def count_positives(lst):
#     newCount = 0
#     for i in range (0, len(lst), 1):
#         if (lst[i] >= 1):
#             newCount = newCount + lst[i]
#         print(i)
#     return lst
# count_positives([1,6,-4,-2,-7,-2])

# Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7

# def sum_total(arr):
#     sum = 0
#     for i in range (0, len(arr),1):
#         sum = sum + arr[i]
#     print(sum)
#     return arr
# sum_total([6,3,-2,])
# Average - Create a function that takes a list and returns the average of all the values.
# Example: average([1,2,3,4]) should return 2.5
# def average(list):
#     sum = 0
#     avg = []
#     for i in range(len(list)):
#         sum = sum + list[i]
#         avg = sum / len(list)
#     print(avg)
#     return list
# average([1,2,1,4])

# Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0
# def listLen(list):
#     for i in range(len(list)):
#         print(len(list[i]))
# listLen([2,3,4,5])


# Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False
# def min(list):
#     min = list[0]
#     for x in range (len(list)):
#         if (min > list[x]):
#             min = list[x]
#     new_list = [min]
#     print(new_list)
# min([37,2,1,9])

# Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False
# def max(list):
#     max = list[0]
#     for x in range (len(list)):
#         if (max < list[x]):
#             max = list[x]
#     new_list = [max]
#     print(new_list)
# max([37,2,1,9])

# Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }


# Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]