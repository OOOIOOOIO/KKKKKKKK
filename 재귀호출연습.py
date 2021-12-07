# 카운트다운
def count(num) :
    if num == 0 :
        return print("발사아")
    else :
        print(num)
        count(num - 1)

count(5)
print()

# 별 찍기
def star(num) :
    if num > 0 :
        star(num-1)
        print("★" * num)
star(5)
print()

#구구단
def gugu(dan, num) :
    print("%d x %d = %d" %(dan, num, dan*num))
    if num < 9 :
        gugu(dan, num+1)
print("##2단##")
# for i in range(2, 10) :
gugu(2, 1)
print()

# 배열의 합
import random
def arySum(ary, n) :
    if n <= 0 :
        return ary[0]
    return ary[n] + arySum(ary, n-1)
ary = [random.randint(0, 255) for _ in range(random.randint(10, 20))]
# ary = [1, 1, 1]
print(ary)
print(arySum(ary, len(ary)-1))


# 피보나치
def fibo(n) :
    if n == 0 :
        return 0
    elif n == 1 :
        return 1
    return fibo(n-1) + fibo(n-2)
for i in range(20) :
    print(fibo(i), end = " ")

print()

# 진수변환하기
def notation(base, n) :
    return

numberChar = ['']
