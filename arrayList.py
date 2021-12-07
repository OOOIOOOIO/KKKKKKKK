
# 생성(추가)하기
def add_data(data) :
    # global katok
    katok.append(None)
    katok[len(katok) - 1] = data


# 삽입하기
def insert_data(index, data) :
    # global katok
    if index < 0 or index > len(katok) :
        print("범위를 벗어났습니다.")

    katok.append(None)

    maxLen = len(katok)

    for i in range(maxLen-1, index, -1) :
        katok[i] = katok[i-1]

    katok[index] = data


def delete_data(index) :
    # global katok
    if index < 0 or index > len(katok) :
        print("범위를 벗어났습니다.")

    maxLen = len(katok)

    for i in range(index, maxLen-1) :
        katok[i] = katok[i+1]

    del(katok[maxLen-1])




katok = ["다현", "정연", "쯔위", "사나", "지효"]


if __name__ == "__main__" :

    add_data("성호")
    print(katok)

    insert_data(2, "김성호")
    print(katok)

    delete_data(4)
    print(katok)
