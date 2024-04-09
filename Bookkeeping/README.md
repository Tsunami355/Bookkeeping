# Project BOOKKEEPING

This repository contains the homework code for the Python Beginning course.

## Contents

- milestone_1
  - equations.py
- milestone_2
  - encrypt.py
  - decrypt.py
- milestone_3
  - triangle.py
- milestone_4
  - trade_offs.py
- milestone_4
  - generate_data.py
  - report.py
  - database.csv

## milestone_1

Here is the code for solving quadratic equations.

### equations.py

#### Usage

1. Run the code.
2. Enter the coefficients a, b, and c.
3. Get the roots of the equation.

##### Example

Enter the equation: 2x^2 + 5x - 3 = 0
The roots of the equation are: x1 = 0.5, x2 = -3

## milestone_2

This is where the code to encrypt and decrypt the data is located.

### encrypt.py

#### Usage

1. Enter a key (an integer) and a message.
2. Receive an encrypted message.

### decrypt.py

#### Usage

1. Run the code file.
2. Enter the key (integer).
3. Enter an encrypted message.
4. Receive the decrypted message.

##### Example

Enter key: 3
Enter an encrypted message: Khoor, Zruog!
Результат: Hello, World!

## milestone_3

Generation of the Pascal triangle

### triangle.py

Этот код генерирует треугольник Паскаля и выводит его на экран.

#### Usage

1. Run the code file.
2. Enter the number of triangle rows (for example, 5).
3. Get Pascal's triangle on the screen.

##### Example

      1
     1 1
    1 2 1

1 3 3 1
1 4 6 4 1

## milestone_4

This file contains two functions for finding a pair of items in a list that add up to a given number.

### trade_offs.py

#### Usage

1. Run the code file.
2. Verify that the functions return the expected results.

##### Example

assert find_sum(5, [1, 2, 3, 4, 5]) in {(0, 3), (1, 2)}
assert find_sum_fast(5, [1, 2, 3, 4, 5]) in {(0, 3), (1, 2)}

## milestone_5

Code to generate an employee report and creates a CSV file with employee data.

### report.py

#### Usage

1. Run the code file.
2. Specify the path to the CSV file with employee data.
3. Enter the month (e.g. "january", "february").
4. Add the -v flag to include employee names in the report.

##### Example

python employee_report.py employees.csv january -v

### generate_data.py

#### Usage

1. Run the code file.
2. Enter a file name (e.g., "database.csv") and the number of entries (e.g., 100).
3. Get a file with employee data.

##### Example

python generate_data.py database.csv 100
