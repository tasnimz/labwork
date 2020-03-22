from heapq import nlargest

with open("Lucky_ids.txt", "r") as f:
    three_largest = nlargest(3, f)
    print(three_largest)
