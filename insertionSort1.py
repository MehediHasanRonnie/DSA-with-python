# insertion Sort Algoritham

def insertionSort(arr):
    for i in range(1,len(arr)): # we consider 1st element is sorted so we start from the index[1]
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]: # while the value of j is positive and key is less then the last number of array.
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = key    

if __name__ == '__main__':
    arr = [11,12,9,8,4,5,7,6]
    insertionSort(arr)
    print(arr)


