def gugudan1():    # 홀수 구구단
    for dan in range(3, 10, 2):    # 홀수 단만 반복
        print(f"{dan}단")
        for mul_num in range(1, 10):    # 구구단 출력
            print(f"{dan} * {mul_num} = {dan*mul_num}")
        print("\n......")

def gugudan2():    # 짝수 구구단
    for dan in range(2, 9, 2):    # 짝수 단만 반복
        print(f"{dan}단")
        for mul_num in range(1, 10):    # 구구단 출력
            print(f"{dan} * {mul_num} = {dan*mul_num}")
        print("\n......")

def exit_program():    # 프로그램 종료
    print("프로그램을 종료 합니다.")
    exit()

# 프로그램 시작
print("구구단 프로그램을 실행합니다.")
print("1. 홀수 구구단")
print("2. 짝수 구구단")
print("3. 종료")

while(True):    # 프로그램 실행 반복문
    print()
    input_num = int(input("숫자를 입력 하세요: "))
    if input_num==1:    # 입력이 1일 경우
        gugudan1()
    elif input_num==2:  # 입력이 2일 경우
        gugudan2()
    elif input_num==3:  # 입력이 3일 경우
        exit_program()
    else:   # 입력이 1,2,3 이외일 경우
        print("잘못 입력 하셨습니다. 1 ~ 3번 숫자를 입력하세요.")