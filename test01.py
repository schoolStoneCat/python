import math
import time

def MakeList():
    MAX_SIZE = int(input("Max SIze of List >>"))
    list = []
        
    for i in range(MAX_SIZE):
        list_num = int(input("List[{}] num >>".format(i)))
        list.insert(i, list_num)
        
    ListAnaly(list)

def ListAnaly(list):
    start_time = time.process_time()
    print("Start time is {}".format(start_time))

    MIN_num = len(list)
    result = 0
        
    for i in range(len(list)):
        MIN_num = min(MIN_num, list[i])
        result = max(result, list[i] - MIN_num)
    
    MAX_num = result + MIN_num
    element_min = list.index(MIN_num)
    element_max = list.index(MAX_num, element_min, len(list))
    end_time = time.process_time()
    
    print("you must buy in {} and sell in {}".format(element_min, element_max))
    print("then you can buy best price {}".format(result))
    
    print("Lastly time is {}".format(end_time))
    print("Analysis Time is {}".format(end_time - start_time))

MakeList()