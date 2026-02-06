### 260206 str

## 1989. 초심자의 회문 검사

## 코드 방향성 / 구상한 내용

오늘 배운 회문 연습하는 느낌으로 리스트 정렬 안쓰고 풀어봄

## 어려웠던 점
없음

```python
import sys

sys.stdin = open('1989.txt')

def is_palindrome(word):
		"""
		문자열 word가 회문이면 1, 
		아니면 0을 반환하는 함수
		"""
		
		# 회문 여부를 저장할 플래그
    palindrome = True
    
    # 문자열 길이
    N = len(word)
	
		# 문자열의 앞쪽 절반만 순회
		# i와 대응되는 뒤쪽 인덱스 j를 비교
    for i in range(N//2):
    
		    # 대응 되는 위치 j
        j = (N-1) - i
        
        # 서로 다른 문자가 나오면 회문이 아님
        if word[i] != word[j]:
            palindrome = False
            
            # 반복 종료
            break 
            
    # 회문이면 1, 아니면 0 반환        
    if palindrome:
        return 1
    else:
        return 0

T = int(input())
for tc in range(1, T+1):
    words = input()

    answer = is_palindrome(words)

    print(f'#{tc} {answer}')
```

## 4861. [파이썬 S/W 문제해결 기본] 3일차 - 회문

## 코드 방향성 / 구상한 내용

가로 방향, 세로 방향 따로 해서 함수로 만들긴 했는데 너무 비효율적임

1. 회문 판별 함수
2. 회문 찾는 함수

이렇게 2개 함수로 만

## 어려웠던 점
함수를 다시 배워야할 듯…

이게 프린트를 하면 답이 나오는데 프린트 자리에 리턴을 넣으면 아무것도 반환되지 않는 상황이 계속 나옴

이건 주말에 다시 풀어볼 예정

함수 부분만

```python
import sys

sys.stdin = open('4861.txt')

def is_palindrome(word):
    """
    문자열 word의 회문 판별 함수
    """
    palindrome = True
    N = len(word)
    
    for i in range(N//2):
        j = (N-1) - i
        if word[i] != word[j]:
            palindrome = False
            break
    if palindrome:
        return True
    else:
        return False


def find_palindrome(arr):
    """
    가로 -> 세로 순서로 회문 탐색
    발견하면 회문 문자열 반환
    """
    
    # 가로 탐색
    # i: 행 인덱스
    # j: 시작 열 인덱스
    for i in range(N):
        for j in range(N-M+1):
            is_p = arr[i][j:j+M]
            if is_palindrome(is_p):
                return is_p
    
    # 세로 문자열 생성
    vertical = []
    for c in range(N):
        result = ""
        for r in range(N):
            result += arr[r][c]
        vertical.append(result)
    
    # 세로 탐색
    # 세로도 가로와 동일한 방식으로 탐색
    for c in range(N):
        for r in range(N-M+1):
            is_p = vertical[c][r:r+M]
            if is_palindrome(is_p):
                return is_p

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(input() for _ in range(N))

    answer = find_palindrome(arr)
    print(f'#{tc} {answer}')
```

## 1221. [S/W 문제해결 기본] 5일차 - GNS

## 코드 방향성 / 구상한 내용

외계인 문자와 숫자가 대응되는 딕셔너리를 만들고 딕셔너리 키와 벨류 값으로 재정렬하는 걸 생각함

근데 지금 생각해보니까 어차피 0 ~ 9는 인덱스라서 그냥 딕셔너리 말고 리스트로 해도 될 듯;


## 어려웠던 점

NO

```python
import sys

sys.stdin = open('1221.txt')

# 테스트 케이스 입력
T = int(input())
for _ in range(1, T+1):

    # tc: 테스트 케이스 번호 문자열
    # l: 입력으로 주어지는 문자열 개수
    tc, l = input().split()

    # 숫자 문자열 입력
    lst = list(input().split())

    # 문자 -> 숫자 변환을 위한 딕셔너리
    trans_dict = {
        'ZRO': 0,
        'ONE': 1,
        'TWO': 2,
        'THR': 3,
        'FOR': 4,
        'FIV': 5,
        'SIX': 6,
        'SVN': 7,
        'EGT': 8,
        'NIN': 9
    }

    # 문자열 숫자를 실제 숫자로 변환
    new_lst = []
    for i in range(int(l)):
        new_lst.append(trans_dict[lst[i]])

    # 숫자 기준으로 정렬
    new_lst.sort()

    # 숫자를 문자열로 역변환
    answer = []
    for j in range(int(l)):
        for k, v in trans_dict.items():
            if v == new_lst[j]:
                answer.append(k)
        # [answer.append(k) for k, v in trans_dict.items() if v == new_lst[j]]


    print(f'{tc}')
    print(* answer)
```

## 5356. 의석이의 세로로 말해요

## 코드 방향성 / 구상한 내용

아까 배운 세로로 읽기 그대로 사용함 근데 몇번 틀려서 다시 풀어봐야할듯


## 어려웠던 점

그냥 처음 생각한 가장 높은 수 오른쪽에 있는 걸로 할껄;

```python
import sys

sys.stdin = open('5356.txt')

T = int(input())
for tc in range(1, T+1):
    arr = list(input() for _ in range(5))

    max_val = 0
    for i in range(len(arr)):
        if len(arr[i]) > max_val:
            max_val = len(arr[i])

    result = ""
    for c in range(max_val):
        for r in range(5):
            if c < len(arr[r]):
                result += arr[r][c]

    print(f'#{tc} {result}')
```

## 5432. 쇠막대기 자르기

## 코드 방향성 / 구상한 내용

2차원 행렬로 진짜 구현하고 싶었는데 그건 힘들 것 같았음

‘(’로 막대 시작하면 층 증가

‘()’로 레이저 나오면 현재 있는 층 만큼 막대가 늘어날 것

‘)’면 막대 끝이고 층 하나 내려감

그리고 막대도 하나 증가

이렇게 전체를 도는 방향


## 어려웠던 점
반복문은 어려움

```python
import sys

sys.stdin = open('5356.txt')

T = int(input())
for tc in range(1, T+1):
    arr = list(input() for _ in range(5))

    max_val = 0
    for i in range(len(arr)):
        if len(arr[i]) > max_val:
            max_val = len(arr[i])

    result = ""
    for c in range(max_val):
        for r in range(5):
            if c < len(arr[r]):
                result += arr[r][c]

    print(f'#{tc} {result}')
```