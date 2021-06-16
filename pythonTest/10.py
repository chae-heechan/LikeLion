lines = 6   # 줄 수
while(lines!=0):
    stars = lines   # 별 수를 줄 수로 초기화

    while(stars!=0):
        print("*", end="")
        stars -= 1

    print()     # 개행
    lines -= 1