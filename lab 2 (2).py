import time
def minmax(data):
    largest = data[0]
    smallest = data[0]
    for value in data:
        if value > largest:
            largest = value
        elif value < smallest:
            smallest = value
    return smallest, largest

number = [1,2,3,45,6,7,8,10]

start_time = time.time()
def(minmax)
end_time = time.time()

print(minmax(number))

print("\nRunning time: ", end_time-start_time)

