# while 사용법

# for 를 사용할때는 반복할 횟수가 정해졌을때 사용
# while 을 사용할때는 반복할 횟수가 정해지지 않았을때 사용

# while 문의 기본 구조

i = 0
while i < 10:
    print(i)
    i += 1

# 무한루프와 break
# while True: 를 사용하면 무한루프를 만들 수 있음
# break는 가장 가까운 반복문만 탈출

while True:
    # 반복할 명령
    x = input("종료하려면 q를 입력하세요 >>>  ")
    if 조건:
        break
