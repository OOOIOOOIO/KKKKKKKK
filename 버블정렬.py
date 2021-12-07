def bubbleSort(ary) :
    n = len(ary)
    for end in range(n-1, 0, -1) : # 맨 두에 있는 애는 어차피 제일 큰 애니까 맨 뒤를 빼고 다시 정렬 돌림
        flag = False
        print("#사이클 -->", ary)
        for i in range(0, end) : # 제일 큰 게 맨 뒤로 감
            if(ary[i] > ary[i+1]) :
                ary[i], ary[i+1] = ary[i+1], ary[i]
                flag = True
        if not flag : # 정렬할 요소가 더이상 없는 경우 종료한다.
            break
    return ary
    # n = len(ary)
    # for i in range(n-1) :
    #     if(ary[i] > ary[i+1])

dataAry = [50, 105, 120, 1888, 152, 169, 198, 43]

print("12-2 버블 정렬\n", "정렬 전 -->", dataAry)
dataAry = bubbleSort(dataAry)
print("정렬 후 -->", dataAry)
