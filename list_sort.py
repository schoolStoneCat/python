def MakeList():
    list_max = int(input("List Max >>"))
    list = []
    
    for i in range(list_max):
        num = int(input("list[{}] value >>".format(i)))
        
        ##FIXME: 중복되는 값을 간별하는 코드를 추가하라. 
        list.append(num)
        print("list value >> {}".format(list))
                
    print("//Finish Value in List")   
    return list

def EvenList(list):
    print("//Finish Analysis Even value")
    return [ x for x in list if x%2 == 0 ]

def OddList(list):
    print("//Finish Analysis Odd value")  
    return [ x for x in list if x%2 == 1 ]

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