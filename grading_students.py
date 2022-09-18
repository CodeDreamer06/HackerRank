grades = [73, 67, 38, 33]

final_grades = []
for grade in grades:
    r = grade % 5
    final_grades.append(grade if grade < 38 else grade +
                        5 - r if 5 - r < 3 else grade)

print(final_grades)
