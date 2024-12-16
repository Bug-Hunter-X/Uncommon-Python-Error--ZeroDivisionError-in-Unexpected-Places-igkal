# Uncommon Python Error: ZeroDivisionError

This repository demonstrates a common error, ZeroDivisionError, which can appear in unexpected places in Python code if not managed correctly.  The `bug.py` file contains the flawed function, while `bugSolution.py` provides the correct implementation.

## Bug Description:
The provided function (`function_with_uncommon_error`) fails when the input `x` is 0 due to division by zero. This leads to a `ZeroDivisionError` exception.  The error might not be obvious if the function is called with dynamically-generated values or if the input is derived from an external source.

## Solution:
The solution involves adding error handling, specifically a conditional check before performing division, to avoid the error.