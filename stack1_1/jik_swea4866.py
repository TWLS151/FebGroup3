import sys
sys.stdin = open("01.txt")
#테스트 케이스 입력
T = int(input())

#테스트 수만큼 순환
for tc in range(1, T+1) :
    #문자열 입력
    chars = list(input())
    #짝 맞는지 검사 위한 새로운 list 생성
    stack = []
    #짝 별로 딕셔너리 생성
    matches = {
        ')': '(',
        ']': '[',
        '}': '{',
    }
    #각 문자열 순환
    for char in chars:
        #문자열이 값에 해당하면
        if char in matches.values() :
            #stack list 에 포함
            stack.append(char)
        elif char in matches.keys():
            if len(stack) == 0:
                ans = False
            open_char = stack.pop()

            if matches[char] != open_char:
                ans = False

    if len(stack) == 0:
        ans = True
    else :
        ans = False

    if ans :
        print(f'#{tc} 1')
    else :
        print(f'#{tc} 0')




