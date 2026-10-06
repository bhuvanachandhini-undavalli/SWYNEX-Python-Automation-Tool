students = [
    ["Bhuvana", 85, 90, 78],
    ["Ravi", 72, 68, 80],
    ["Anu", 45, 55, 40],
    ["Kiran", 92, 88, 95]
]

print("===== STUDENT REPORT =====")
print()

for student in students:
    name = student[0]
    mark1 = student[1]
    mark2 = student[2]
    mark3 = student[3]

    total = mark1 + mark2 + mark3
    average = total / 3

    if average >= 40:
        result = "PASS"
    else:
        result = "FAIL"

    print("Name:", name)
    print("Total:", total)
    print("Average:", round(average, 2))
    print("Result:", result)
    print("--------------------------")

print("Report generated automatically!")
