
#Insertion sort

def insertion_sort(arr):
    for i in range(1,len(arr)):
            temp = arr[i]
        # b. Iterate to the left until you find the correct index in the "sorted" part of the list
            compare = i
            while compare > 0 and temp < arr[compare - 1]:
                #shfit items over to the right as you iterate
                arr[compare] = arr[compare-1]
                compare-= 1
                arr[compare] = temp
    return arr
    # c. When the correct indexis found, copy [temp] into this position

 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        if arr[cur_index] <= arr[cur_index + 1]:
            print(f"if {arr[cur_index]} <= {arr[cur_index + 1]}")
 
        elif arr[cur_index] > arr[cur_index + 1]:
            print(f"else {arr[cur_index]} > {arr[cur_index + 1]}")

            smallest_index = arr[cur_index + 1]
            arr[cur_index], arr[cur_index + 1] = arr[cur_index + 1], arr[cur_index]

            return selection_sort(arr)
    return arr


print(selection_sort([2,5,3,8,7]), "selection sort")
print(selection_sort([1,87,45,6,78,9,4,4,14,15,16,18,25,23,22,24]), "selection sort")
# TO-DO:  implement the Bubble Sort function below

# 1. Loop through your array
#     - Compare each element to its neighbor
#     - If elements in wrong position (relative to each other, swap them)
# 2. If no swaps performed, stop. Else, go back to the element at index 0 and repeat step 1. 
# 
import random
test_list = list(range(100))
random.shuffle(test_list)
# print(l)


def bubble_sort( arr ):
    for i in range(1,len(arr)):
            temp = arr[i]
            compare = arr[i - 1]
            stop = len(arr)
   
            while stop > 0 and temp < compare:
                # print(f"Compare: {compare} is greater than temp: {temp}")
                arr[i-1] = temp
                arr[i] = compare
                stop-=1
               
                return bubble_sort(arr)
    return arr

    
test_list_2 = [1,87,45,6,78,9,4,4,14,15,16,18,25,23,22,24]
test_list_3 = [1,87,45,6,78,9,4,4]
arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]

# print(bubble_sort([1, 2, 5, 8, 20, 115, 45]))
# print(bubble_sort(test_list_2))
# print(bubble_sort(test_list_3))
# print(bubble_sort(test_list))

def bubble_sort2( arr ):
    for i in range(1,len(arr)):
            temp = arr[i]
            compare = arr[i - 1]
            while temp < compare:
                # print(f"Compare: {compare} is greater than temp: {temp}")
                arr[i-1] = temp
                arr[i] = compare
               
                return bubble_sort(arr)
    return arr

# print(bubble_sort2([1, 2, 5, 8, 20, 115, 45]))
# print(bubble_sort2(test_list_2))
# print(bubble_sort2(test_list_3))
# print(bubble_sort2(arr1))

# michaels version without recursion and swapping values
def bubble_sort3( arr ):
    swap = True
    while swap == True:
        for i in range(0, len(arr) - 1):
            swap = False
            if arr[i] > arr[i + 1]:
                arr[i],arr[i + 1] = arr[i + 1], arr[i]
                swap = True
    return arr

# print(bubble_sort3([1, 2, 5, 8, 20, 115, 45]))
# print(bubble_sort3(test_list_2))
# print(bubble_sort3(test_list_3))
# print(bubble_sort3(arr1))




# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr