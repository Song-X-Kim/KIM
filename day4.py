# JadenCase 문자열 만들기
# 제출 내역
# 문제 설명
# JadenCase란 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열입니다. 단, 첫 문자가 알파벳이 아닐 때에는 이어지는 알파벳은 소문자로 쓰면 됩니다. (첫 번째 입출력 예 참고)
# 문자열 s가 주어졌을 때, s를 JadenCase로 바꾼 문자열을 리턴하는 함수, solution을 완성해주세요.

# 제한 조건
# s는 길이 1 이상 200 이하인 문자열입니다.
# s는 알파벳과 숫자, 공백문자(" ")로 이루어져 있습니다.
# 숫자는 단어의 첫 문자로만 나옵니다.
# 숫자로만 이루어진 단어는 없습니다.
# 공백문자가 연속해서 나올 수 있습니다.
# 입출력 예
# s	return
# "3people unFollowed me"	"3people Unfollowed Me"
# "for the last week"	"For The Last Week"
def solution(s):
    words = s.split(' ')

    first_Upper = [w.title() for w in words]

    # .join()은 stringBuilder랑 같음
    return ' '.join(first_Upper)

# 테스트 1
# 입력값 〉	"3people unFollowed me"
# 기댓값 〉	"3people Unfollowed Me"
# 실행 결과 〉	실행한 결괏값 "3People Unfollowed Me"이 기댓값 "3people Unfollowed Me"과 다릅니다.
# 테스트 2
# 입력값 〉	"for the last week"
# 기댓값 〉	"For The Last Week"
# 실행 결과 〉	테스트를 통과하였습니다.

# ㅅㅂ ㅋㅋ .title은 첫글자 알파벳아니면 그 다음글자를 대문자로 반환하네

def solution(s):
    words = s.split(' ')

    # .capitalize()는 첫글자가 알파벳이든 아니든 무조건 첫글자만 대문자로 바꿔버림 나머지는 소문자로
    first_Upper = [w.capitalize() for w in words]

    return ' '.join(first_Upper)