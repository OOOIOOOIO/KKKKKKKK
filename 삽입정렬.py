# 삽입정렬
def findInsertSort(ary, data) :
    idx = -1
    for i in range(len(ary)) :
        if(ary[i] > data) :
            idx = i
            break # 찾으면 바로 작동 중지

    if idx == -1 :
        return len(ary)
    else :
        return idx


    return idx
before = [188, 162, 168, 120, 50, 150, 177, 105]
after = []

print("11-5 삽입 정렬\n", "정렬 전 -->", before)
for i in range(len(before)) :
    data = before[i]
    idx = findInsertSort(after, data)
    after.insert(idx, data)
print("정렬 후 -->", after)
print()

# ==============================================================================

# 개선된 삽입 정렬
def insertionSort(ary) :
    n = len(ary)
    for end in range(1, n) :
        for i in range(end, 0, -1) :
            if(ary[i-1] > ary[i]) :
                ary[i-1], ary[i] = ary[i], ary[i-1]
        # for i in range(n-1) :
        #     if(ary[i] >ary[i+1]) :
        #         ary[i+1], ary[i] = ary[i], ary[i+1]

    return ary


dataAry = [188, 162, 168, 120, 50, 150, 177, 105]

print("11-6 개선된 삽입 정렬\n", "정렬 전 -->", dataAry)
dataAry = insertionSort(dataAry)
print("정렬 후 -->", dataAry)

print()

for i in range(10, 1, -1) :
    print(i, end=" ")
