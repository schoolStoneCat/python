def numAnaly(x):
    for number in range(2 , (x-1)):
        if (x % number) == 0:
            print(x, " 는 소수가 아닙니다.")
            return 0
    print(x, " 는 소수가 맞습니다.")

x = int(input("num >>"))
numAnaly(x)