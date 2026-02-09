### 260209 stack1_1

## 4866. [파이썬 S/W 문제해결 기본] 4일차 - 괄호검사

## 코드 방향성 / 구상한 내용

오늘 배운 stack을 연습한다고 생각하고 구현

## 어려웠던 점
근데 사실 중간에 코드들이 기억안나서 보고함

stack 문제를 몇번 풀다보면 반복숙달이 되지 않을까 생각

```python
import sys
sys.stdin = open('4866.txt')

def solve(string):
    """
    문자열에 포함된 괄호들의 짝이 올바른지 검사하는 함수
    반환값: 올바른 괄호 문자열이면 1 아니면 0
    """

    # 여는 괄호를 담아둘 스택
    stack = []

    # 닫는 괄호와 여는 괄호 매핑한 딕셔너리
    matches = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    # 문자열을 한 글자씩 검사
    for char in string:

        # 여는 괄호인 경우 스택에 저장
        # 나중에 닫는 괄호와 비교하기 위함
        if char in matches.values():
            stack.append(char)

        # 닫는 괄호인 경우
        elif char in matches.keys():

            # 스택에 쌓인 게 없으면 실패
            if len(stack) == 0:
                return 0

            # 가장 마지막에 들어간 여는 괄호 꺼내기
            open_char = stack.pop()

            # 닫는 괄호와 꺼낸 여는 괄호가 짝이 안맞으면 실패
            if matches[char] != open_char:
                return 0

    # 문자열을 모두 검사했는데
    # 여는 괄호가 남아있으면 실패
    # 아니면 성공
    if len(stack) == 0:
        return 1
    else:
        return 0

# 테스트 케이스 입력
T = int(input())

# 테스트 케이스 처리
for tc in range(1, T+1):

    # 한 줄 입력
    lst = input().strip()

    ans = solve(lst)
    print(f'#{tc} {ans}')
```

## 4873. [파이썬 S/W 문제해결 기본] 4일차 - 반복문자 지우기

## 코드 방향성 / 구상한 내용

스택을 활용하려고 함

근데 새로운 문자면 다 넣으려고 했는데 그걸 어케 구현해야하는 지 고민을 함 

## 어려웠던 점
no

```python
import sys
sys.stdin = open('4873.txt')

def solve(string):
    """
    문자열에서 서로 인접한 동일한 문자를 반복적으로 제거한 뒤
    최종적으로 남아 있는 문자의 개수를 반환하는 함수
    """
    # 연속 중복 제거를 위한 스택
    stack = []

    # 문자열을 한 글자씩 순차적으로 탐색
    for char in string:

        # 스택이 비어있거나
        # 현재 문자와 이전 문자가 다르면
        # 새로운 문자이므로 스택에 추가
        if len(stack) == 0 or char != stack[-1]:
            stack.append(char)

        # 현재 문자와 스택의 맨 뒤 문자가 같다면
        # 인접한 중복 문자이므로 제거
        else:
            stack.pop()

    # 스택에 남아있는 문자의 개수 반환
    return len(stack)

# 테스트 케이스 입력
T = int(input())

# 테스트 케이스 처리
for tc in range(1, T+1):

    # 문자열 입력
    lst = input().strip()

    ans = solve(lst)
    print(f'#{tc} {ans}')
```

## 1234. [S/W 문제해결 기본] 10일차 - 비밀번호

## 코드 방향성 / 구상한 내용

스택 연습한다는 생각으로 풂


## 어려웠던 점

마지막에 ans를 어떻게 풀어야할 지 고민함

처음엔 *ans로 했는데 띄어쓰기가 포함된 채로 나와서

join 사용함 

```python
import sys
sys.stdin = open('1234.txt')

def solve(string):
    stack = []

    for char in string:
        if len(stack) == 0 or char != stack[-1]:
            stack.append(char)
        else:
            stack.pop()
    return stack

T = 10
for tc in range(1, T+1):
    N, lst = input().split()

    ans = solve(lst)
    print(f'#{tc}', ''.join(ans))
```

## 1218. [S/W 문제해결 기본] 4일차 - 괄호 짝짓기

## 코드 방향성 / 구상한 내용

스택 연습 


## 어려웠던 점

no

```python
import sys
sys.stdin = open('1218.txt')

def solve(string):
    stack = []
    matches = {
        ')': '(',
        ']': '[',
        '}': '{',
        '>': '<'
    }

    for char in string:
        if char in matches.values():
            stack.append(char)
        elif char in matches.keys():
            if len(stack) == 0:
                return 0
            open_char = stack.pop()

            if matches[char] != open_char:
                return 0
    if len(stack) == 0:
        return 1
    else:
        return 0

T = 10
for tc in range(1, T+1):
    l = int(input())
    string = input().strip()

    ans = solve(string)
    print(f'#{tc} {ans}')
```

## 2005. 파스칼의 삼각형

## 코드 방향성 / 구상한 내용

스택으로 어떻게 해야하는 지 모르겠음

그냥 파스칼의 삼각형 하면 생각나는게 (x+1) $^n$ 이거랑 nCr 이거 밖에 없어서

그냥 이걸로 밀고 나감


## 어려웠던 점
스택으로 어케 풂? 진짜 모름

```python
import sys

sys.stdin = open('2005.txt')

def comb(n, r):
    """
    nCr(조합)을 계산하는 함수
    """
    # 5C2 = 5C3인데
    # 5C2가 더 계산하기 수월함
    r = min(r, n-r)

    # 누적 곱 결과
    result = 1

    # 분자: i+1
    # 분모: n-1
    # 한 항씩 곱하고 나누며 조합 값 누적
    # ex) 5C2인 경우
    # result = 1* 5 / 1 = 5
    # result = 5* 4 / 2 = 10
    for i in range(r):
        result = result * (n-i) // (i+1)
    return result

def pascal_triangle(n):
    """
    파스칼의 삼각형 n번째 줄을 생성하는 함수
    파스칼의 삼각형의 n번째 줄의 값은 (n-1)C0, (n-1)C1, ...(n-1)C(n-1)
    """
    # n번째 줄의 값을 저장할 리스트
    lst = []

    # (n-1)Ci 값을 차례대로 계산하여 리스트에 추가
    for i n range(n):
        lst.append(comb(n-1, i))

    return lst

# 테스트 케이스 입력
T = int(input())

# 테스트 케이스 처리
for tc in range(1, T+1):

    # 파스칼 삼각형 크기 입력
    N = int(input())

    print(f'#{tc}')

    # N번까지의 파스칼 삼각형을 전체 출력해야함
    for i in range(1, N+1):

        # i번째 줄 생성 후 출력
        ans = pascal_triangle(i)
        print(*ans)
```