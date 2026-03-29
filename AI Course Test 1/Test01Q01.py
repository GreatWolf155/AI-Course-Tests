valid_grades = []

while True:
    try:
        grade = int(input("Enter a grade: "))
        if grade == -999:
            if len(valid_grades) != 10:
                print("Need at least 10 valid grades. Keep entering.")
                continue
            break
        if grade > 100 or grade < 0:
            print("Not in range, skip")
            continue
        valid_grades.append(grade)

    except:
        print("Invalid input")

print(f"Number of valid grades: {len(valid_grades)}")
print(f"Class average: {(sum(valid_grades) / len(valid_grades)):.2f}")
print(f"Highest grade: {max(valid_grades)}")