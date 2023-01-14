# insertion sort coading approach 2

def insertionSort(list):
    for i in range(1,len(list)):
        value = list[i]

        while list[i-1] > value and i>0:
            list[i],list[i-1] = list[i-1],list[i]
            i = i-1
    return list

list= [9,4,6,3,2,7,1]
print(insertionSort(list))
