# linearly search x in arr[]
# if x is present then return its location
# otherwise return -1
# linear Search algorithm iterative approach code.

# function

def search(arr, n, x):
    for i in range(0, n):
        if arr[i] == x:
            return i
    return -1


# driven code
if __name__ == "__main__":
    arr = [2, 3, 4, 5, 6, 7, 8, 9]
    x = 8
    n = len(arr)

    # function call
    result = search(arr, n, x)
    if result == -1:
        print("Element is not present in the array")
    else:
        print("Element is present. index:", result)



