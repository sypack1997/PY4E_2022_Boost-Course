monthly_payment = input("월급을 입력하세요:")
try:
    mp = int(monthly_payment)
except:
    print("잘못된 입력입니다. 다시 입력하세요.")
    quit()

yearly_payment = (12 * mp)

if yearly_payment <= 1200:
    yp = yearly_payment * 0.94
elif yearly_payment <= 4600:
    yp = yearly_payment * 0.85
elif yearly_payment <= 8800:
    yp = yearly_payment * 0.76
elif yearly_payment <= 15000:
    yp = yearly_payment * 0.65
elif yearly_payment <= 30000:
    yp = yearly_payment * 0.62
elif yearly_payment <= 50000:
    yp = yearly_payment * 0.60
elif yearly_payment > 50000:
    yp = yearly_payment * 0.58

print("세전 연봉: %s만원" % yearly_payment)
print("세후 연봉: %s만원" % int(yp))
