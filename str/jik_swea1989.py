import sys

sys.stdin = open('001.txt')

T = int(input())

for tc in range(T) :
    word = list((input()))
    ans = 0
    if word == word[::-1] :
        ans = 1
    print(f'#{tc} {ans}')