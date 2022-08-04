try:
    n = int(input("첫 번쨰 수 입력:"))
    m = int(input("두 번째 수 입력:"))
except:
    print("잘못된 입력입니다. 정수로 입력하세요.")
    quit()
l = int((n+m)/2)

numbers = [i for i in range(n,m+1)]
for even in numbers:
    if even %2 ==0:
        print(even, "짝수")
        if l == even:
            print(l, "중앙값")