def  input_student(MAX_num):
##학생 딕셔너리를 만드는 함수
    dic = {}

    for i in range(MAX_num):
        input_student_name = str(input("Student name >>"))
        ##학생 딕셔너리를 만들고 값을 입력받음
  
        while input_student_name in dic.keys():
            print("//ERROR >> this name is already in dic.")
            input_student_name = str(input("Student name >>"))
        ##학생 이름의 딕셔너리의 값의 중복을 확인함.

        input_student_score = int(input("Student score >>"))
        ##학생 딕셔너리의 점수값을 입력 받음

        dic[input_student_name] = input_student_score
        ##딕셔너리에 input

    print("{}".format(dic.items()))
    print_grade(dic)

def print_grade(dic_student):
##학생 딕셔너리를 이용하여 그래프 그리는 함수
    for i in range(0 ,len(dic_student.keys())):
    ##학생의 키값에 따라서 반복
        temp = list(dic_student.values())[i]
        ##학생의 벨류의 값을 리스트화 하여, 값을 temp에 저장.

        score_chart = int(round(temp / 5, 0))
        ##학생의 점수값을 반올림하여, 값을 저장.
  
        print("{}'s score >>".format(list(dic_student.keys())[i]), end = " ")
        for i in range(score_chart):
            print("*", end ="")
        ##학생의 점수값을 반환하여 반올림 한 값에 따라서 그래프를 그림.

##main 함수
MAX_num = int(input("Student Max num >> "))
input_student(MAX_num)
