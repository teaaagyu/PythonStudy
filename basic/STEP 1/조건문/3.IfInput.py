age = int(input("나이를 입력하세요: "))
is_student = input("학생인가요? (yes/no): ")

if is_student == "yes":
    is_student = True
else:
    is_student = False

if age>=20 and is_student:
    print("대학생 입니다.")
elif age>=20 and is_student == False:
    print("성인 입니다.")
else:
    print("성인이 아닙니다.")

