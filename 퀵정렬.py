def quickSort(ary) :
    n = len(ary)

    if n <= 1 :
        return ary

    pivot = ary[n//2] # 기준값 : 배열의 중간값
    leftAry = []
    rightAry = []
    midAry = []  # 중복이 있을 경우
    for num in ary :
        if num < pivot :
            leftAry.append(num)
        elif num > pivot :
            rightAry.append(num)
        else :
            midAry.append(num) # pivot 및 pivot이랑 같을 경우
    # return quickSort(leftAry) + [pivot] + quickSort(rightAry)
    return quickSort(leftAry) + midAry + quickSort(rightAry)


dataAry = [188, 143, 150, 185, 165, 200, 120, 178, 34]
# dataAry = [188, 143, 150, 185, 165, 150, 185, 165, 200, 150, 185, 165, 120, 178, 34]

print("12-3 퀵 정렬\n", "정렬 전 -->", dataAry)
dataAry = quickSort(dataAry)
print("정렬 후 -->", dataAry)

a = [1, 2]
b = [5]
print(a + b + [10, 11])
