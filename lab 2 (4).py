ID = input("what is your Id?")
f = open("lucky_ids.txt", "r")
for bannerId in f:
    if ID in bannerId:
        print("yes")
    else:
        print("no")
