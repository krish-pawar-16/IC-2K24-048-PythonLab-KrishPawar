# Lab 2 – Star Patterns in Python

## Aim
To write Python programs to print different star patterns using loops and nested loops.

## Logic
- Take the number of rows as input from the user.
- Use nested `for` loops to control rows, spaces, and stars.
- Use the `print()` function with the `end` parameter to print stars in the same line.
- Apply different loop conditions to generate different star patterns.

## 1. Right-Angle Triangle Pattern

### Aim
To print a right-angle triangle star pattern using nested loops.

### Logic
- Take the number of rows as input.
- Use an outer `for` loop to control the rows.
- Use an inner `for` loop to print stars according to the current row number.

### Sample Input / Output

**Input:**
```text
Enter value: 4
```

**Output:**
```text
*
* *
* * *
* * * *
```

## 2. Pyramid Triangle Pattern

### Aim
To print a pyramid-shaped star pattern using nested loops.

### Logic
- Take the number of rows as input.
- Use the first inner loop to print spaces.
- Use the second inner loop to print stars.
- Repeat the process for each row to create a pyramid shape.

### Sample Input / Output

**Input:**
```text
Enter value: 4
```

**Output:**
```text
   *
  * *
 * * *
* * * *
```

## 3. Inverted Triangle Pattern

### Aim
To print an inverted right-angle triangle star pattern.

### Logic
- Take the number of rows as input.
- Use the outer loop to control the rows.
- Print spaces at the beginning of each row.
- Print decreasing numbers of stars in each successive row.

### Sample Input / Output

**Input:**
```text
Enter value: 4
```

**Output:**
```text
* * * *
 * * *
  * *
   *
```

## 4. Square Pattern

### Aim
To print a hollow square star pattern using loops and conditional statements.

### Logic
- Take the size of the square as input.
- Use nested `for` loops to control rows and columns.
- Use an `if-else` condition to print stars on the boundary and spaces inside the square.

### Sample Input / Output

**Input:**
```text
Enter value: 4
```

**Output:**
```text
****
*  *
*  *
****
```

## 5. Rhombus Pattern

### Aim
To print a rhombus-shaped star pattern using nested loops.

### Logic
- Take the number of rows as input.
- Use the first inner loop to print decreasing spaces.
- Use the second inner loop to print stars.
- Repeat the process to create a rhombus shape.

### Sample Input / Output

**Input:**
```text
Enter value: 4
```

**Output:**
```text
   ****
  ****
 ****
****
```

## Conclusion
Thus, different star patterns were successfully created using Python programming concepts such as `for` loops, nested loops, conditional statements, and the `print()` function.