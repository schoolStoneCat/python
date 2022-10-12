from unittest import result

def testdef(num):
    print("//{} start".format(num))
    
    for i in range(1,10):
        result = num * i
        print("{} x {} = {}".format(num, i, result))

        
for i in range(1,10):
    testdef(i)