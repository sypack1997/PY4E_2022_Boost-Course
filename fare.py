def buspay(age, fare):
    if age < 8:
        pay = "무료"
    elif age < 14:
        pay = "450원"
    elif age < 20 and fare == "카드":
        pay = "720원"
    elif age < 20 and fare == "현금":
        pay = "1000원"
    elif age >= 75:
        pay = "무료"
    elif age >= 20 and fare == "카드":
        pay = "1200원"
    elif age >= 20 and fare == "현금":
        pay = "1300원"
    return pay

aa =  input("나이를 입력하세요:")
aa = int(aa)
fare_choice = ["카드", "현금"]
while True:
    ff = input("지불유형을 선택하세요. 카드 or 현금:")
    if ff in fare_choice:
        break
    print("잘못된 입력입니다. 다시 입력하세요.")

bb = buspay (aa, ff)


print("나이: %s세" %aa)
print("지불유형:", ff)
print("버스요금:", bb)
