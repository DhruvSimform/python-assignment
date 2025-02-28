# Python Practical Assignment

This repository contains solutions to three Python programming tasks designed to assess problem-solving skills and proficiency in Python. Each task includes a problem statement, constraints, example inputs and outputs, and a detailed explanation of the solution approach.

## Table of Contents

1. [Task 1: Compute GCD of Two Numbers](#task-1-compute-gcd-of-two-numbers)
2. [Task 2: Generate Well-Formed Parentheses](#task-2-generate-well-formed-parentheses)
3. [Task 3: Group Anagrams](#task-3-group-anagrams)
4. [How to Run the Code](#how-to-run-the-code)

## Task 1: Compute GCD of Two Numbers

### Problem Statement

Write a program to compute the Greatest Common Divisor (GCD) of two numbers.

### Constraints

- Use optimal data structures and ensure the solution is time-efficient.
- The program should accept input from the console or command-line arguments and handle unexpected inputs gracefully.
- **For loops are not allowed.**
- Inputs will be provided as words representing numbers (e.g., `onetwo` for `12`, `sixone` for `61`).
- Only numbers from `zero` to `nine` will be used.
- Do **not** use built-in functions like `max`, `min`, or any math-related functions.

### Example

#### Input
```plaintext
Input 1: onezero
Input 2: twozero
```

#### Output
```plaintext
Output: onezero
```

### Solution Approach

1. **Convert Word Representation to Integer**
   - Create a mapping of word representations to their corresponding digits.
   - Parse the input strings to construct numerical values.

2. **Implement the Euclidean Algorithm Recursively**
   - Use the Euclidean algorithm to compute the GCD recursively without loops or built-in math functions.

3. **Convert the GCD Back to Word Representation**
   - Convert the numerical result back to its word representation for the output.

This approach ensures that the solution is efficient and meets all the specified constraints.

---

## Task 2: Generate Well-Formed Parentheses

### Problem Statement

Given `n` pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

### Constraints

- `1 ≤ n ≤ 8`

### Example

#### Input
```plaintext
n = 3
```

#### Output
```plaintext
["((()))", "(()())", "(())()", "()(())", "()()()"]
```

### Solution Approach

1. **Recursive Backtracking**
   - Define a recursive function that builds valid parentheses combinations by adding `(` or `)` at each step.
   - Maintain counters for the number of open and close parentheses used.
   - Ensure that at any point, the number of close parentheses does not exceed the number of open ones.

2. **Base Case**
   - When the combination reaches the maximum length (`2 * n`), add it to the result list.

This method efficiently explores all possible combinations and collects those that form valid parentheses sequences.

---

## Task 3: Group Anagrams

### Problem Statement

Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

### Constraints

- `1 ≤ strs.length ≤ 10^4`
- `0 ≤ strs[i].length ≤ 100`
- `strs[i]` consists of lowercase English letters.

### Example

#### Input
```plaintext
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
```

#### Output
```plaintext
[["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
```

### Solution Approach

1. **Sorting Each Word**
   - For each word in the input list, sort its characters alphabetically.
   - This sorted version serves as a key because all anagrams, when sorted, will produce the same string.

2. **Using a Dictionary to Group Words**
   - Utilize a dictionary where the keys are the sorted character strings, and the values are lists of words (anagrams) that correspond to those keys.

3. **Collecting the Results**
   - Iterate through the dictionary and collect all the grouped anagrams into a list.

This approach ensures that words that are anagrams of each other are grouped together efficiently.

---

## How to Run the Code

To execute the solutions for each task:

### 1. Clone the Repository

```bash
git clone https://github.com/DhruvSimform/python-assignment.git
cd python-assignment
```

### 2. Navigate to the Task Directory

Each task is located in its respective directory:

- Task 1: `task1_gcd/`
- Task 2: `task2_parentheses/`
- Task 3: `task3_anagrams/`

### 3. Run the Python Script

For example, to run Task 1:

```bash
python task1_gcd/gcd.py
```

For Task 2:

```bash
python task2_parentheses/generate_parentheses.py
```

For Task 3:

```bash
python task3_anagrams/group_anagrams.py
