# TO-DO: complete the help function below to merge 2 sorted arrays
def merge( arr, arrA, arrB ):
    print(f"arrA: {arrA}, arrB: {arrB}")
    elements = int(len( arrA ) + len( arrB ) / 2 - 1)
    element = int(len( arrA ) + len( arrB ))
    merged_arr = [0] * elements

    if element == 0:
        return merged_arr

    if element == 1:
        concat_arr = arrA + arrB
        merged_arr.insert(0,concat_arr[0])
        return merged_arr

    num1 = 0
    num2 = 0
    index = 0
    while num1 < len(arrA) and num2 < len(arrB):
        if arrA[num1] < arrB[num2]:
            arr[index] = arrA[num1]
            num1+=1
            index+=1
        else:
            arr[index] = arrB[num2]
            num2+=1
            index+=1
    print(arr, "this is the arr")
    
           
# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    if len(arr) > 1:
        arr_length = len(arr)
        arr_half_length = int(arr_length / 2)
        fh = arr[:arr_half_length]
        sh = arr[arr_half_length:]
     
        merge_sort( fh )
        merge_sort( sh )

        num1 = 0
        num2 = 0
        index = 0
        while num1 < len(fh) and num2 < len(sh):
            if fh[num1] < sh[num2]:
                arr[index] = fh[num1]
                num1+=1
            else:
                arr[index] = sh[num2]
                num2+=1
            index+=1

        while num1 < len(fh):
            arr[index] = fh[num1]
            num1+=1
            index+=1

        while num2 < len(sh):
            arr[index] = sh[num2]
            num2+=1
            index+=1
        
    return arr
   
arr = [12, 11, 13, 5, 6, 7]
print(merge_sort([1,5,4,20,2,3]))
print(merge_sort(arr))


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
