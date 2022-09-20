import numpy

def InsertList(num_list, len_list):
    for i in range(len_list):
        num_list[i] = int(input("Score >>"))
    print("Finish Insert List\n")

def StudentList():
    num = int(input("Insert Student's num >>"))
    list = [0 for i in range(num)]
    print("Finish insert 0 to List")

    InsertList(list, num)
    return list

def CheckList(list):
    print("List value >> {}".format(list))  
    print("List Over")
    
def AverageScore(num_list):
    CheckList(num_list)
    return numpy.mean(num_list)

print("Make Man Student List")
man_student_list = StudentList()
print("Make Woman Student List")
woman_student_list = StudentList()
num_student_list = man_student_list + woman_student_list

print("Man Student Score Average is >> {}".format(AverageScore(man_student_list)))
print("Woman Student Score Average is >> {}".format(AverageScore(woman_student_list)))
print("All Student Score Average is >> {}".format(AverageScore(num_student_list)))