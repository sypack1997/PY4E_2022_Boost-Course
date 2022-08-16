def bs31():
    import random
    number = 0
    while True:
        my = list(map(int, input("My turn - 숫자를 입력하세요:").split()))
        if my[0] != number + 1 or len(my) > 3:
            print("숫자를 제대로 입력하세요")
            continue

        if len(my) == 2:
            if (my[1] - my[0]) != 1:
                print("연속된 숫자만 입력하세요")
                continue
        
        if len(my) == 3:
            if (my[2] - my[1]) !=1 or (my[1] - my[0]) != 1:
                print("연속된 숫자만 입력하세요")
                continue
        
        number = my[-1]
        print(f"현재 숫자:{number}")

        if number >=31:
            print("패배")
            break

        computer = []
        computer_turn_num = random.randint(1,3)
        for i in range(computer_turn_num):
            number += 1
            if number >31:
                number = number -1
                continue
            computer.append(number)
            print(f"컴퓨터 : {computer[-1]}")
        print(f"현재 숫자 : {number}")
        print()

        if 31 in computer:
            print("승리!")
            break
    print("게임 종료")

bs31()