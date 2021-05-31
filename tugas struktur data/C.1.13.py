def myReverse(data):
    # returning a new reversed list
    return [data[i] for i in range(len(data)-1, -1, -1)]

print(myReverse([45, 46, 47, 48, 49, 50]))
