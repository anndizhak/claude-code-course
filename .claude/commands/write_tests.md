Write comprehensive tests for the file: $ARGUMENTS

Follow these steps:

1. Read the target file and understand its exports, functions, and classes.
2. Identify the testing framework already used in this project (Jest, Vitest, pytest, unittest, etc.). Match that framework — do not introduce a new one.
3. For each exported function or class method, write tests that cover:
   - The happy path with typical valid input
   - Edge cases (empty input, zero, null/None, boundary values)
   - Error cases (invalid input, expected exceptions/rejections)
4. Place the test file next to the source file using the project's existing naming convention (e.g., `utils.test.ts`, `test_utils.py`).
5. If mocks or fixtures are needed, use the patterns already present in the codebase.

Do not modify the source file. Only create or update the test file.
