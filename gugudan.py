repeat = 1
try:
    number = int(input("몇 단?:"))
    print(f"{number}단")
except:
    print("잘못된 입력입니다. 정수로 입력하세요")
    quit()

while True:
    if repeat % 2 != 0:
        gugudan = number * repeat
        if gugudan > 50:
            break
        print(f"{number}X{repeat}={gugudan}")
    else:
        repeat+=1
        continue
    repeat+=1