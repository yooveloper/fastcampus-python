# 조건문
# : 조건에 따라 실행할 명령이 달라 지는 것

origin_pass = "1234"
input_pass = input("비밀번호를 입력하세요 : ")


if input_pass == origin_pass:
    # 조건 : input_pass와 origin_pass가 같으면
    print("비밀번호가 일치합니다.")
elif input_pass == "":
    # 조건 : input_pass가 공백이면
    print("비밀번호를 입력해주세요.")
else:
    # 조건 : input_pass와 origin_pass가 다르면
    print("비밀번호가 일치하지 않습니다.")
