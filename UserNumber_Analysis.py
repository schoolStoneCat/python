import pickle
import re
import os.path

def MK_file(dic):
    #바이너리 파일 생성 함수
    with open('SSN.p', 'wb') as f:
        pickle.dump(dic, f)
        
    print("finish file save.")
    
def GD_file():
    #바이너리 파일 불러오기 함수
    with open('SSN.p', 'rb') as f:
        data = pickle.load(f)

    print("finish load file data.")
    return data

def User_Save(dic):
    #사용자가 이름과 주민번호를 만들고 그에 따른 딕셔너리 생성
    repeat_num = int(input("How much are you putting in? >>"))
    
    for i in range(repeat_num):
        name = input("Input name >>")
        num = input("Input Social Security Number (Input 000000-0000000) >>")
        dic[name] = num
    
    print("finish input info.")
    
def Ch_SSN(result_dic, dic):
    #딕셔너리의 밸류값(주민번호)를 불러와서 변형하는 함수
    pat = re.compile("(\d{6})[-]\d{7}")
    for key in dic:
        result_dic[key] = pat.sub("\g<1>-"+"*"*7, str(dic[key]))
    
    print("finish Change SSN")
    
def Save_txtfile(dic):
    #출력파일(txt) 파일을 열고 딕셔너리의 키와 밸류를 저장하는 함수.
    with open('SSN.txt', 'w+', encoding='utf8') as f:
        for name,SSN in dic.items():
            f.write(f'{name} : {SSN}\n')
            
    print("Success to make Output txt file.")

def main():
    #메인함수
    SSN_dic = {}
    Ch_SSN_dic = {}

    if os.path.isfile("SSN.p"):
        print("SSN.p file is exist.")
        print("1.Make New file.")
        print("2.Don't Make New file.")
        num = int(input(">> "))
        if num == 1:
            User_Save(SSN_dic)
        else:
            SSN_dic = GD_file()
    else:
        print("SSN.p file is not exist.")
        User_Save(SSN_dic)
        MK_file(SSN_dic)
        
    print(SSN_dic)
        
    print("1.Change Social Security Number.")
    print("2.Don't Change Social Security Number")
    num = int(input(">> "))

    if num == 1:
        Ch_SSN(Ch_SSN_dic, SSN_dic)
        Save_txtfile(Ch_SSN_dic)
    else:
        Save_txtfile(SSN_dic)

    MK_file(SSN_dic)
    
if __name__ == "__main__":
    main()

