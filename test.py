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

print("\n=== 함수 ===")
def calculate_circle_area(radius):
    """원의 넓이를 계산하는 함수"""
    import math
    return math.pi * radius ** 2

def greet(name, language="ko"):
    """다국어 인사 함수"""
    greetings = {
        "ko": f"안녕하세요, {name}님!",
        "en": f"Hello, {name}!",
        "jp": f"こんにちは、{name}さん！"
    }
    return greetings.get(language, f"Hello, {name}!")

radius = 5
area = calculate_circle_area(radius)
print(f"반지름 {radius}인 원의 넓이: {area:.2f}")

print(greet("Alice", "en"))
print(greet("태희", "ko"))
