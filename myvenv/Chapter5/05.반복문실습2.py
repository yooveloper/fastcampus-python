# 구구단 출력하기

x = int(input("몇 단을 출력할까요? >>>  "))

for i in range(1, 10):
    print(x, "*", i, "=", x * i)


# 문제2
# 숫자 1 입력 : "게임을 시작합니다" 출력
# 숫자 2 입력 : "실시간 랭킹" 출력
# 숫자 3 입력 : "게임을 종료합니다" 출력
# 그 외 숫자 입력 : 다른 숫자를 입력해주세요
#

while True:
    x = int(input("숫자를 입력하세요 >>>  "))
    if x == 1:
        print("게임을 시작합니다.")
    elif x == 2:
        print("실시간 랭킹")
    elif x == 3:
        print("게임을 종료합니다.")
        break
    else:
        print("다른 숫자를 입력해주세요.")
