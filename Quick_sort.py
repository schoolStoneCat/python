import random

def Make_list(list):
    MAX_num = int(input("Insert Max num >>"))
    for i in range(1, MAX_num+1):
        list.append(i)

##Change Code Error
#def MakeList():
    #list_max = int(input("List Max >>"))
    #list = []
    
    #for i in range(list_max):
    #    num = int(input("list[{}] value >>".format(i)))
        
    random.shuffle(list)

    print("//List >> {}".format(list))
    if len(list) == MAX_num:
        return list
    else:
        print("//ERROR >> list MAX size error.")
        return 0
        
def list_Quicksort(list):
    if list != 0:
        if len(list) <= 1:
            print("//Success sort List.")
            return list
        pivot = random.choice(list)
        front_list, pivot_list, lastly_list = [], [], []
        
        for num in list:
            if(num < pivot):
                front_list.append(num)
            elif(num > pivot):
                lastly_list.append(num)
            else:
                pivot_list.append(num)
                
        return list_Quicksort(front_list) + pivot_list + list_Quicksort(lastly_list)
    else:
        print("//ERROR >> list Make error.")
        return 0

list = []
list = list_Quicksort(Make_list(list))

print("List >> {}".format(list))

def QuickSort_O(result_sort: list):
    list_middle = int(random.randint(list))
    i = 0
    j = len(list) - 1
    front_num = list[i]
    last_num = list[j]
    
    while(last_num < front_num):
        if(front_num > list_middle and last_num > list_middle):
            j -= j
        elif (front_num > list_middle and last_num < list_middle):
            list[i], list[j] = list[j], list[i]
            i += i
            j -= j
        elif (front_num < list_middle and last_num < list_middle):
            i += i
        elif (front_num < list_middle and last_num > list_middle):
            i += i
            j -= j
    
    middle_num = list.find(list_middle)
    
    for i in range(len(list)):
        if(list[i] > list_middle):
            list.remove(list_middle)
            list.insert(i - 1, list_middle)

