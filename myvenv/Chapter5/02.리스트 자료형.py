# 리스트 자료형


# 리스트 만들기
a = []

# 리스트에 요소 추가
a.append(1)
a.append(2)
a.append(3)

# 리스트 출력
print(a)

# 리스트의 요소 출력
print(a[0])


# 리스트의 요소 수정
a[0] = 4

print(a[0])

# 리스트의 요소 삭제
del a[0]

print(a[0])

print(a)

# 리스트 길이 구하기
print(len(a))

# 리스트 슬라이싱
print(a[0:1])

# 리스트 정렬
a.sort()
