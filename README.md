[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=18203601&assignment_repo_type=AssignmentRepo)
# GPA Calculation Program

The task of this assignment is to create a program that:

1. Allows a user to enter as many course letter grades as they would like
2. Calculates the GPA based on those letter grades

The formula to average a set of N numbers is 
- `(n1 + n2 + ... + nN) / N`

For grades, GPA (non-weighted) is found with:
- `(number_of_As * 4.0 + number_of_Bs * 3.0 + number_of_Cs * 2.0 + number_of_Ds * 1.0 + number_of_Fs * 0.0) / (number_of_grades)`

Loop until all grades are entered

For example:  
```shell
admin@computer$ python gpa_calculation.py 
Enter a letter grade for a course: A
Enter a letter grade for a course: B
Enter a letter grade for a course: B
Enter a letter grade for a course: A
Enter a letter grade for a course: 
Your GPA is 3.500!
```

## Detailed Program Specifications:

- Instructions to the user should be clear
- Allows the user to enter as many letter grades as they wish
  - Account for uppercase and lowercase letters
- Properly calculate GPA average based on course letter grades and number of courses
  - You can assume that each course is worth equal credit hours for simplicity, although you may implement functionality to account for courses with differing credit hours if you desire
- Display the GPA average to the user with **exactly 3** decimal places
- Code should be well-formatted and properly commented
  - If you cannot look at your code the next day and understand what it does, it needs more comments
- The code must be void of any syntax errors and should run.

## Hints:

- You will need to use at least one looping structure
- Run your code often to catch bugs early. **Iterative development** is a must!
- The programming exercise discussed in lecture 4 will provide many hints on how to structure this assignment

## Think you are finished? Ask yourself these questions:

- [ ] Does my code run?
- [ ] Does my program satisfy the requirements listed above?
- [ ] If I run the program with an A, B, and C, is the GPA 3.0? Is an A and B GPA average calculated to 3.5?
- [ ] Did I account for abnormal user input? (or rather, will my program break if someone enters "}[v'34243inm" as a grade?)
- [ ] Am I using a while loop? (if not, it is likely the program does not satisfy the above requirements)
