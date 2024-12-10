a = int(input("Attendance of student: "))
b = int(input("Absent of student: "))

p = (a + b)*100/100

if p <= 75:
    print("Not eligible for exam")
else:
    print("Eligible for exam")