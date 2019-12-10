
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

# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
             



        # TO-DO: swap




    return arr


# TO-DO:  implement the Bubble Sort function below

# 1. Loop through your array
#     - Compare each element to its neighbor
#     - If elements in wrong position (relative to each other, swap them)
# 2. If no swaps performed, stop. Else, go back to the element at index 0 and repeat step 1. 
# 
import random
l = list(range(100))
random.shuffle(l)
# print(l)


def bubble_sort( arr ):
    for i in range(1,len(arr)):
            temp = arr[i]
            compare = arr[i - 1]
            arr_length = len(arr)
            while arr_length > 0 and temp < compare:
                # print(f"Compare: {compare} is greater than temp: {temp}")
                arr[i-1] = temp
                arr[i] = compare
                arr_length -= 1
    return arr

    

print(bubble_sort([1,2,5,8,115,20]))






# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr