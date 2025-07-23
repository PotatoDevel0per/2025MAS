print("=== 변수와 데이터 타입 ===")
name = "김철수"
age = 25
height = 175.5
is_student = True

print(f"이름: {name}")
print(f"나이: {age}세")
print(f"키: {height}cm")
print(f"학생 여부: {is_student}")

print("\n=== 조건문 ===")
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print(f"점수: {score}점, 등급: {grade}")
