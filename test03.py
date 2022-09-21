def MakeList():
    list_max = int(input("List Max >>"))
    list = [0 for i in range(list_max)]
    print("Finish 0 in List\n")
    
    for i in range(list_max):
        list[i] = int(input("list[{}] value >>".format(i)))
        
        for j in range(list_max):
            while(list[j] != 0 & list[j] == list[i]):
                print("ERROR >> Same num is exit plz Insert num again")
                list[i] = int(input("list{} value >>".format(i)))
                
    print("Finish Value in List")
    
    return list

def EvenList(list):
    result_list = []
    
    for i in range(len(list)):
        if(list[i] % 2 == 0):
            result_list.append(list[i])
    
    return result_list

def OddList(list):
    result_list = []
    
    for i in range(len(list)):
        if(list[i] % 2 != 0):
            result_list.append(list[i])
            
    return result_list

def AscendingList(result_list: list):
    for i in range(len(result_list)):
        for j in range(i ,len(result_list)):
            if(result_list[i] > result_list[j]):
                result_list[i], result_list[j] = result_list[j], result_list[i]
                
    print("Finish Ascentding List")
    return result_list

def DescendingList(result_list: list):
    for i in range(len(result_list)):
        for j in range(i ,len(result_list)):
            if(result_list[i] < result_list[j]):
                result_list[i], result_list[j] = result_list[j], result_list[i]
                
    print("Finish Descentding List")
    return result_list
    
main_list = MakeList()

print("Main List >> {}".format(main_list))
print("{} List had only Even value".format(EvenList(main_list)))
print("{} List had only odd value".format(OddList(main_list)))
print("{} List is Ascending List".format(AscendingList(main_list)))
print("{} List is Descending List".format(DescendingList(main_list)))