# 반복문
# : 반복해서 명령을 사용하고 싶을 떄

# 시퀀스 자료형
# 순서가 있는 자료형
# 1. 문자열
# 2. 리스트
# 3. range 객체
# 4. 튜플, 딕셔너리

# for 변수 in 시퀀스자료:
#     반복할 코드


# for 문
# - 리스트 사용
champions = ["티모", "이즈리얼", "리신", "아리"]

for champion in champions:
    print("선택한 챔피언은 : ", champion, "입니다.")


# 문자열 사용
fighting_message = "티모가 이즈리얼을 공격합니다."

for word in fighting_message:
    print(word)


# 예제 1
for a in [1, 2, 3, 4, 5]:
    print(a)


# range
# range(10) 0~9 까지 숫자를 포함하는 range 객체를 만들어준다.
# range(시작, 끝+1, 단계)
for i in range(1, 10, 2):
    print(i)
