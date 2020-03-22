###LINEAR SEARCH
import time
def search(arr, n, x):
    for i in range(0, n):
        if (arr[i] == x):
            return i;
    return -1;


start_time = time.time()
num = 1000000
arr = []
x = 90
for i in range(num):
    arr.append(i)
print(arr)
n = len(arr);
result = search(arr, n, x)
if (result == -1):
    print("Element is not present in array")
else:
    print("Element is present at index", result)
end_time = time.time()
print("\nRunning time: ", end_time-start_time)







####BINARY SEARCH
import time
def binarySearch(arr, l, r, x):
    if r >= l:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)
        else:
            return binarySearch(arr, mid + 1, r, x)
    else:
        return -1
start_time = time.time()
num = 1000000
arr = []
x = 90
for i in range(num):
    arr.append(i)
print(arr)
result = binarySearch(arr, 0, len(arr) - 1, x)
if result != -1:
    print("Element is present at index % d" % result)
else:
    print("Element is not present in array")
end_time = time.time()
print("\nRunning time: ", end_time-start_time)

