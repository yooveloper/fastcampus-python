
# 1. 연습할 한국어가 담긴 리스트를 만든다.
# 2. 리스트에서 순서대로 단어를 가져와 화면에 출력한다.
# 3. 프로그램 사용자는 단어를 그대로 입력하고
# 4. 맞추면 다음 단어를 가져온다. 틀리면 프로그램 종료

# 한국어 리스트
word_list = ["사랑해", "귀엽다", "고마워", "행복해"]

print("시작")

for word in word_list:
    print(word)
    data = input("단어를 입력하세요 >>>  ")
    if data != word:
        print("틀렸습니다.")
        break
