# TO-DO: complete the help function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    print(f"arrA: {arrA}, arrB: {arrB}")
    elements = int(len( arrA ) + len( arrB ) / 2 - 1)
    print(elements)
    merged_arr = [0] * elements
  
    # TO-DO
    num1 = 0
    num2 = 0

    count = 0
    for i in range(elements-1):
        if arrA[num1] <= arrB[num2]:
            print(f"a: {i} = {arrA[num1]}, a: {i+1} = {arrB[num2]} LESS THAN")
            merged_arr[i] = arrA[num1]
            merged_arr[i+1] = arrB[num2]
            num1 += 1
            count+=1
   
        else:
            print(f"a: {i} = {arrB[num2]}, a: {i+1} = {arrA[num1]} GREATER THAN")
            merged_arr[i] = arrB[num2]
            merged_arr[i+1] = arrA[num2]
            num2 += 1
            count+=1

    
            
        return merge( arrA, arrB )
    return merged_arr
           
# print(merge([1,3,5,7],[6,9,10,12]))
# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    arr_length = len(arr)
    arr_half_length = int(arr_length / 2)
    fh = arr[0:arr_half_length]
    sh = arr[arr_half_length:]
 
    return merge( fh,sh )
    return arr

print(merge_sort([1,5,9,6,7,8]))


# arr = [1,2,3,4,5,6]
# arr_length = len(arr)
# print(arr_length, "length")
# arr_half_length = int(arr_length / 2)
# print(arr_half_length,"half-length")




# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
