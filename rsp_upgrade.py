import random
def computer_Korean (computer):
    if computer == 0:
        return "가위"
    elif computer == 1:
        return "바위"
    elif computer == 2:
        return "보"

games= int(input("몇 판을 진행하시겠습니까?"))
my_rsp = ["가위", "바위", "보"]
ComWin = 0
Draw = 0
MeWin = 0
for count in range(1,games+1):
    computer = random.randint(0,2)
    while True:
        my = input("가위 바위 보 중 하나를 선택하세요:")
        if my in my_rsp:
            break
        print("잘못된 입력입니다. 다시 입력하세요.")
    print("나:", my)
    print("컴퓨터:", computer_Korean(computer))

    if my == "가위" and computer_Korean(computer) == "보" or \
    my == "바위" and computer_Korean(computer) == "가위" or \
    my == "보" and computer_Korean(computer) == "바위" :
        MeWin+=1
        print(f"{count}번째 판 나의 승리!\n")
    elif my == computer_Korean(computer) :
        Draw+=1
        print(f"{count}번째 판 무승부!\n")
    else :
        ComWin+=1
        print(f"{count}번째 판 컴퓨터의 승리!\n")

print(f"나의 전적: {MeWin}승 {Draw}무 {ComWin}패")
print(f"컴퓨터의 전적: {ComWin}승 {Draw}무 {MeWin}패")