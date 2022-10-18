import random

def Make_list(list):
    MAX_num = int(input("Insert Max num >>"))
    for i in range(1, MAX_num+1):
        list.append(i)
        
    random.shuffle(list)

    print("//List >> {}".format(list))
    if len(list) == MAX_num:
        return list
    else:
        print("//ERROR >> list error.")
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