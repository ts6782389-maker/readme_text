#sorting algortihms are bsaed one recursion and a spiece of sorting 
#bubble sort repeatdely go through the list, comparing pairs of neighboring elemnets,and swap them if they are in the wrong ordeer.keep doing until nothing needs swapping anymore - this list is sorted.
list = [5,2,4,1]

#arr[1] = 2 and arr[0] = 5 so arr[i] =5 and arr[i+1] = 0

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0 , n-1-i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped = True
        if not swapped:
            break
    return arr

arr = [3,7,8,2,1]
print(bubble_sort([3,7,8,2,1]))


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i],arr[min_index] = arr[min_index],arr[i]
    return arr

list = [5,2,4,1]
print(selection_sort(list))

#in selection sort we sort like that the smallest number on the unsorted part gets the upfront means it is swapped to the first index and so in till it is sorted


#insert sort
#insert bulid up sorted section at the front of the list,one element at a time,shifts larger elments right to make room for the smallest one.
#the inesert build can be explained by the pile of cards when pick one its already sorted then u pick another one sort it in the realtive to the first one and then third and fourth and so on....

def insertion_sort(arr):
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        j = i-1
        while j >=0 and arr[j] > key:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = key 
    return arr

#bascially the arr[j+1] = key is only for when we just do one thing the shifting process that can also do one thing for sure that is the loop is [2,2,4,5] so to append the value which is missing we use key to append it so that remains safe.
#also while job is only to shift bigger values out of the way,it never actually places key back into the list. the line after the loop is the only place key actually gets written back into the list whatever gap was left behid.
#without it the list would stay stuck at[2,2,4,5] with 1 silently lost and duplicate 2 sitting there instead so we use key in the last phase 

list = [5,2,4,1]
print(insertion_sort(list))