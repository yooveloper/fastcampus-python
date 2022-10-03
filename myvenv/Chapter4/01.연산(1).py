# 연산


# 1. 대입연산
# 변수이름 = 데이터

# 2. 산술연산
# - 숫자연산
x = 5
y = 2
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x // y)  # 몫
print(x % y)  # 나머지
print(x ** y)  # 제곱


# - 문자열 연산
tag1 = "#안녕하세요"
tag2 = "#반갑습니다."
tag3 = "bye!"

tag = tag1 + tag2 + tag3
print(tag)

message = "메세지 입니디. \n" * 5
print(message)

# && 연산 파이썬에서는 and
# || 연산 파이썬에사는 or
# not 은 뒤집음

# 3. 멤버십 연산
print("a" in "abc")  # 포함되어 있다면 True
print("a" not in "abc")  # 포함되어 있지 있다면 True
