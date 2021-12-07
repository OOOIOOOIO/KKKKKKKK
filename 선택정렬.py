# SELF STUDY 11-1
def findMaxIdx(ary) :
    maxIdx = 0;
    for i in range(1, len(ary)) :
        if(ary[i] > ary[maxIdx]) :
            maxIdx = i
    return maxIdx

testAry = [55, 88, 33, 77]
maxPos = findMaxIdx(testAry)
print("11-1 \n", "최댓값 -->", testAry[maxPos])
print()


#선택정렬 구현 11-2
def findMinIdx(ary) :
    minIdx = 0;
    for i in range(1, len(ary)) :
        if(ary[minIdx] > ary[i]) :
            minIdx = i
    return minIdx

before = [188, 162, 168, 120, 50, 150, 177, 105]
after = []

print("11-2 \n","정렬 전 -->", before)
for _ in range(len(before)) :
    minPos = findMinIdx(before)
    after.append(before[minPos])
    del(before[minPos])
print(" 정렬 후 -->", after)
print(before + "before 다 삭제됨")
print()
# print(before)

# ==============================================================================

#개선된 선택 정렬 11-3
def selectionSort(ary) :
    n = len(ary)
    for i in range(0, n-1) :
        minIdx = i
        for k in range(i+1, n) :
            if (ary[minIdx] > ary[k]) :
                minIdx = k
        temp = ary[i]
        ary[i] = ary[minIdx]
        ary[minIdx] = temp

    return ary

dataAry = [188, 162, 168, 120, 50, 150, 177, 105]

print("11-3 선택정렬 \n","정렬 전 -->", dataAry)
dataAry = selectionSort(dataAry)
print(" 정렬 후 -->", dataAry)
