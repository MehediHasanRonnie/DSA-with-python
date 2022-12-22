# if not found return -1
# if found the key is arr[size-1]=key

# function
def linear_Search(arr, key, size):
    if size == 0:
        return -1
    elif arr[size-1] == key:
        return size-1
    else:
        return linear_Search(arr, key, size-1)


if __name__ == "__main__": # driven code
    arr = [1,2,3,4,5,6,7,8,9]
    key = 10
    size = len(arr)

    answer = linear_Search(arr, key, size) # function call
    if answer != -1:
        print("The element", key, "is found at", answer, "index of given array")
    else:
        print("the element", key, "is not found")
