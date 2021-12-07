# p105 : ArrayList 구현

def add(data) :
    List.append(None)
    maxLen = len(List)
    List[maxLen -1] = data

def insert(idx, data) :
    if idx < 0 and idx > len(List) :
        print("삽입할 공간이 없습니다.")


    List.append(None)
    maxLen = len(List)

    for i in range(maxLen -1, idx, -1) :
        List[i] = List[i-1]
        List[i-1] = None

    List[idx] = data


def delete(idx) :
    if idx < 0 and idx > len(List) :
        print("삭제할 데이터가 없습니다.")

    maxLen = len(List)
    List[idx] = None

    for i in range(idx, maxLen - 1) :
        List[i] = List[i+1]
        List[i+1] = None

    del(List[maxLen-1])


def printData() :

    return print("Data :", List, "\nLength :", len(List))



List = []



add("성호")

for i in range(1, 6) :
    insert(i, i) # 삽입

# print(List)
# print(len(List))

delete(2) # 인덱스 번호로 지우기

# print(List)
# print(len(List))

printData()



# p107~ : ArrayList 응용 (다항식 표현)


# 출력형태 : P(x) = + 7x^3 -4x^2 + 0x^1 + 5x^0

def printPoly(px) :
    term = len(px) - 1 # 차수 (최고차항 4 - 1 = 3)

    result = "P(x) = "

    for i in range(term + 1) :
        # if p x[i] == 0 : # 계수가 0이면 출력 X
        #     continue

        if px[i] >= 0 :
            result += "+ "
        result += str(px[i]) + "x^" + str(term) + " "

        term -= 1

    return result

def calPoly(n, px) :
    term = len(px) - 1
    result = 0
    for i in range(term + 1) :
        result += px[i] * n ** term

        term -= 1

    return result


px = [7, -4, 0, 5] # 계수


print("출력 형태 :", printPoly(px))

print("계산 : ", calPoly(1, px))
