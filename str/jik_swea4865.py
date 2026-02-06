import sys

sys.stdin = open('005.txt')
#테스트 케이스 입력
T = int(input())

#테스트 케이스만큼 순환
for tc in range(1,T+1) :
    #str1, str2 입력
    str1 = list(input())
    str2 = list(input())
    #str1 의 각 항목의 개수 담을 딕셔너리 생성
    c_dic = {}
    #str1 순환
    for w in str1 :
        c_dic.setdefault(w, str2.count(w))
    #최댓값 출력
    print(f'#{tc} {max(c_dic.values())}')

