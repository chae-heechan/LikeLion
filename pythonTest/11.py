input_num = int(input())
line_count = 1    # 현재 줄 카운트 변수

for lines in range(input_num):    # input_num번 반복된다
    if line_count%2!=0:    #홀수줄일 경우
        print(" ", end="")
        for element in range(1, input_num+1, 2):
            print(f"{element}    ", end="")
    else:    # 짝수줄일 경우
        for element in range(2, input_num+1, 2):
            print(f"    {element}", end="")
    print()
    line_count += 1
