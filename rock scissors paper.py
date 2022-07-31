import random
computer = random.randint(0,2)
def computer_Korean (computer):
    if computer == 0:
        return "가위"
    elif computer == 1:
        return "바위"
    elif computer == 2:
        return "보"

my_rsp = ["가위", "바위", "보"]
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
    print("나 승리")
elif my == computer_Korean(computer) :
    print("무승부")
else :
    print("컴퓨터 승리")
