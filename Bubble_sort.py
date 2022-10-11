import random

def bsort(list):
    for i in range(0,len(list)-1):
        for j in range(0,len(list)-1):
            if(list[j] > list[j + 1]):
                list[j], list[j + 1] = list[j + 1], list[j]
    
    return list

def list_random():
    list = []
    
    for i in range(9):
        num = random.randint(1,10)
        
        while num in list:
            num = int(random.randint(1,9))
        list.append(num)

    return list

print("Bubble sort list >> {}".format(bsort(list_random())))