import random

def MakeList():
    list_max = int(input("List Max >>"))
    list = []
    
    for i in range(list_max):
        num = int(input("list[{}] value >>".format(i)))
        
        while num in list:
            print("//ERROR >> Same num is exit in list plz Insert num again")
            num = int(input("list[{}] value >>".format(i)))        
        list.append(num)
        print("list value >> {}".format(list))
                
    print("//Finish Value in List")   
    return list

def QuickSort(result_sort: list):
    int list_middle = random.randint(list)
    int i = 0
    int j =  len(list)
    
    while(j < i) {
        
    }
    
    
