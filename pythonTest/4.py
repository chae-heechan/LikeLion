original_num = "010-1234-5678"
new_num = original_num.split("-")    # - 기준으로 슬라이싱
for element in new_num:
    print(element, end="")