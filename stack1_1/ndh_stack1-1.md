## stack1-1

### 4866 SWEA 괄호 검사
- 이 문제를 풀면서 개선할 점 : 문제의 난이도 자체는 어렵지 않았지만 열려있는 괄호 하나가 남은 예외상황에 대해서 예외처리를 미리 하지 않았던 점이 아쉽습니다. 
```python
# 4866 SWEA 괄호 검사
# 요구사항 정리 -> []{}() 각 괄호들이 정상적으로 짝을 이루면 1 출력, 아니면 0 출력
# 아이디어 -> 문자열은 제외하고 괄호 종류만 추출한다. 추출된 괄호들에서 짝이 맞는지 검사한다.

T = int(input())

for test in range(T):
    text_list = input()
    stack = []
    num = 1
    for char in text_list:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if len(stack) == 0:
                num = 0
                break
            out_stack = stack.pop()
            if (char == ')' and out_stack != '(') or \
                    (char == ']' and out_stack != '[') or \
                    (char == '}' and out_stack != '{'):
                num = 0
                break
    if len(stack) != 0:
        num = 0
    print(f'#{test+1} {num}')
```

### 4873 SWEA 반복문자 지우기
- 이 문제를 풀면서 개선할 점 : 인덱스 오류에 대한 처리에서 개선할 부분이 있었습니다. 인덱스 오류를 처리하는 방법을 더 공부하려고 합니다. 
```python
# 4873 SWEA 반복문자 지우기
# 요구사항 정리 -> 입력된 문자열에서 연속된 문자들을 지운다.
# 아이디어 -> stack을 이용한다.

T = int(input())

for test in range(T):
    text_before = input()
    stack = []
    for text in text_before:
        if stack and stack[-1] == text:
            stack.pop()
        else:
            stack.append(text)
    print(f'#{test+1}', len(stack))
```

### 1234 SWEA 비밀번호
- 이 문제를 풀면서 어려웠던 점 : 이번 문제는 4873 문제와 사실상 동일한 문제이기 때문에 다르게 풀려고 했지만 역시 stack에서 요소를 제거하는 과정에서 발생하는 인덱스 오류 처리에 미숙한 부분이 있어서 동일한 방법으로 풀었습니다.  
```python
# 1234 SWEA 비밀번호
# 요구사항 정리 -> 연속한 두 번호 소거, 소거 후 숫자에서 또 연속 발생하면 소거 반복
# 아이디어 -> stack 아이디어를 활용해서 문제 풀이

for test in range(10):
    N, M = input().split()
    # Stack으로 풀기
    stack = []  # stack 빈 리스트 설정
    for char in M:
        # 만약 stack이 공백이 아니고
        # stack[-1] == char 이 True라면 stack의 마지막 요소를 제거합니다.
        if stack and stack[-1] == char:
            stack.pop()
        else:
            # 이외의 경우는 전부 stack 리스트에 답습니다.
            stack.append(char)
    print(f'#{test+1}', end=' ')
    print(*stack, sep='')
```

### 2005 SWEA 파스칼의 삼각형
- 이 문제를 풀면서 개선할 점 : 내부 로직 중 개선이 시급한 부분에 대해서 피드백을 받았습니다. 함수로 처리한 내용 중 pascal 리스트를 각각 출력하는 방식은 출력과 생성 로직의 분리를 어렵게 하기 때문에 이 부분의 개선이 가장 시급하다. 또한 pascal[i] 중복 할당에 대한 논리 오류를 개선할 필요가 있습니다.
- [참고 자료: 파스칼의 삼각형](https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif)
```python
# 2005 SWEA 파스칼의 삼각형
# 요구사항 정리 -> 파스칼의 삼각형 만들기
# 아이디어 -> 리스트 만들기(재귀), N번 리스트 인덱스 i의 값은 N-1번째 리스트 인덱스 i-1, i의 합, 스택으로 풀기

T = int(input())

def pascal_triangle(n):
    triangle = []
    for row in range(n):
        pascal = [1] * (row + 1)
        for i in range(1, row):
            # print('i:', i)
            # print(pascal)
            # if row > 1 and 0 < i < n:
            for _ in range(row-1):
                pascal[i] = triangle[row-1][i-1] + triangle[row-1][i]
        # print('row :', row)
        print(* pascal)
        triangle.append(pascal)

for test in range(T):
    N = int(input())

    print(f'#{test+1}')
    pascal_triangle(N)
```