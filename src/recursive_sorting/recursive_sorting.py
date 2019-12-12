# TO-DO: complete the help function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    print(f"arrA: {arrA}, arrB: {arrB}")
    elements = int(len( arrA ) + len( arrB ) / 2 - 1)
    element = int(len( arrA ) + len( arrB ))
    merged_arr = [0] * elements

    if element == 0:
        print(element)
        return merged_arr

    if element == 1:
        print(element)
        concat_arr = arrA + arrB
        merged_arr.insert(0,concat_arr[0])
        return merged_arr
    
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

    return merged_arr
           
# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    arr_length = len(arr)
    arr_half_length = int(arr_length / 2)
    fh = arr[0:arr_half_length]
    sh = arr[arr_half_length:]
 
    return merge( fh,sh )
    return arr

print(merge_sort([]))


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
