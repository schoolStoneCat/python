def bsort(list):
    for i in range(0,len(list)-1):
        for j in range(0,len(list)-1):
            if(list[j] > list[j + 1]):
                list[j], list[j + 1] = list[j + 1], list[j]

list = [2, 5, 1, 9, 8, 4, 3, 7, 6]

bsort(list)
print("{}".format(list))