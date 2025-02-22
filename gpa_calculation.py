def calc_gpa(grades):
    points = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'F': 0.0}
    total = 0
    num = sum(grades.values())

    for g, count in grades.items():
        total += points[g] * count

    if num == 0:
        return 0
    else:
        return total / num

def main():
    g = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}

    print("Welcome to the GPA calculator.")
    print("Please enter letter grades one at a time. Enter a blank line to finish.")

    while True:
        grade = input("Enter a letter grade for a course: ").strip().upper()
        if grade == "":
            break
        elif grade in g:
            g[grade] += 1
        else:
            print("Invalid grade. Please enter a valid grade (A, B, C, D, F).")

    gpa = calc_gpa(g)
    print(f"Your GPA is {gpa:.3f}!")

if __name__ == "__main__":
    main()
