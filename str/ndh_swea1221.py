# 1221 SWEA GNS
# 요구사항 정리 -> "ZRO" 등 영어 숫자들의 정렬 진행하는 코드 작성
# 아이디어 -> 하드코딩 ... 각 영어별로 뭉치고 순서를 부여한다. 합칠 떄 순서대로 합친다.

numbers = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

T = int(input())

for test in range(T):
    ZRO = []
    ONE = []
    TWO = []
    THR = []
    FOR = []
    FIV = []
    SIX = []
    SVN = []
    EGT = []
    NIN = []
    case_num, case_len = input().split()
    eng_num = list(map(str, input().split()))

    for eng in eng_num:
        if eng == "ZRO":
            ZRO.append(eng)
        elif eng == "ONE":
            ONE.append(eng)
        elif eng == "TWO":
            TWO.append(eng)
        elif eng == "THR":
            THR.append(eng)
        elif eng == "FOR":
            FOR.append(eng)
        elif eng == "FIV":
            FIV.append(eng)
        elif eng == "SIX":
            SIX.append(eng)
        elif eng == "SVN":
            SVN.append(eng)
        elif eng == "EGT":
            EGT.append(eng)
        elif eng == "NIN":
            NIN.append(eng)

    output = ZRO + ONE + TWO + THR + FOR + FIV + SIX + SVN + EGT + NIN
    print(f'{case_num}')
    print(*output)