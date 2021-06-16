tuple1 = (1,2,3,4)
lst_tuple1 = list(tuple1)    # 리스트로 변환

lst_tuple1.append(5)    # 5 추가
tuple1 = tuple(lst_tuple1)    # 튜플로 변환

print(tuple1)