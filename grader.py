name = input("이름을 입력하세요:")
grade = input("점수를 입력하세요:")
try:
    grade = int(grade)
except:
    print("잘못된 입력입니다. 숫자로 입력해주세요.")
    quit()

if grade >= 95:
    grader = "A+"
elif grade >= 90:
    grader = "A"
elif grade >= 85:
    grader = "B+"
elif grade >= 80:
    grader = "B"
elif grade >= 75:
    grader = "C+"
elif grade >= 70:
    grader = "C"
elif grade >= 65:
    grader = "D+"
elif grade >= 60:
    grader = "D"
else:
    grader = "F"

print("학생이름:", name)
print("점수: %s점" %grade)
print("학점:", grader)
