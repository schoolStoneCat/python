def MakeList():
    list_max = int(input("List Max >>"))
    list = [0 for i in range(list_max)]
    print("//Finish 0 in List\n")
    
    for i in range(list_max):
        num = int(input("list[{}] value >>".format(i)))
        
        while num in list:
            print("//ERROR >> Same num is exit in list plz Insert num again")
            num = int(input("list[{}] value >>".format(i)))        
        list[i] = num
        print("list value >> {}".format(list))
                
    print("//Finish Value in List")   
    return list

def EvenList(list):
    result_list = []
    
    for i in range(0, len(list)):
        if(list[i] % 2 == 0):
            result_list.append(list[i])
    print("//Finish Analysis Even value")
    return result_list

def OddList(list):
    result_list = []
    
    for i in range(0, len(list)):
        if(list[i] % 2 != 0):
            result_list.append(list[i])
    
    print("//Finish Analysis Odd value")  
    return result_list

def AscendingList(result_list: list):
    for i in range(len(result_list)):
        for j in range(i ,len(result_list)):
            if(result_list[i] > result_list[j]):
                result_list[i], result_list[j] = result_list[j], result_list[i]
                
    print("//Finish Ascentding List")
    return result_list

def DescendingList(result_list: list):
    for i in range(len(result_list)):
        for j in range(i ,len(result_list)):
            if(result_list[i] < result_list[j]):
                result_list[i], result_list[j] = result_list[j], result_list[i]
                
    print("//Finish Descentding List")
    return result_list
    
main_list = MakeList()

print("Main List >> {}".format(main_list))
print("Even value List >> {}".format(EvenList(main_list)))
print("Odd value List >> {}".format(OddList(main_list)))
print("Ascending List >> {}".format(AscendingList(main_list)))
print("Descending List >> {}".format(DescendingList(main_list)))