"""
Suggest refactoring improvements for utility functions in a Python file using Claude.

Usage:
    python refactor_utils.py <file.py>           # print suggestions
    python refactor_utils.py <file.py> --write   # also save <file>_refactored.py

Features:
    - Streams Claude's refactored output in real time
    - Caches the system prompt to save tokens on repeated runs
    - Optionally extracts and writes the refactored code to a new file
"""

import re
import sys
import os
import anthropic


def refactor_utils(file_path: str, write_output: bool = False) -> None:
    if not os.path.isfile(file_path):
        print(f"Error: File not found: {file_path}")
        sys.exit(1)

    with open(file_path, encoding="utf-8") as f:
        source_code = f.read()

    client = anthropic.Anthropic()
    print(f"Refactoring suggestions for: {file_path}\n")
    print("=" * 60)

    response_parts: list[str] = []

    with client.messages.stream(
        model="claude-opus-4-7",
        max_tokens=16000,
        thinking={"type": "adaptive"},
        system=[
            {
                "type": "text",
                "text": (
                    "You are an expert Python developer focused on clean code and refactoring.\n\n"
                    "When given a Python source file, you:\n"
                    "1. Add or improve type hints throughout\n"
                    "2. Write concise one-line docstrings where missing\n"
                    "3. Apply Pythonic patterns (list comprehensions, context managers, etc.)\n"
                    "4. Split functions that violate single-responsibility into focused helpers\n"
                    "5. Remove unnecessary complexity and improve naming\n\n"
                    "Output format:\n"
                    "- The complete refactored file wrapped in ```python ... ``` fences\n"
                    "- A short bullet-point summary of the changes made\n\n"
                    "Preserve all existing functionality — only improve structure and clarity."
                ),
                "cache_control": {"type": "ephemeral"},
            }
        ],
        messages=[
            {
                "role": "user",
                "content": f"Refactor this Python file:\n\n```python\n{source_code}\n```",
            }
        ],
    ) as stream:
        for text in stream.text_stream:
            print(text, end="", flush=True)
            response_parts.append(text)

        final = stream.get_final_message()

    full_response = "".join(response_parts)

    print("\n\n" + "=" * 60)
    print(f"Tokens  — input: {final.usage.input_tokens}, output: {final.usage.output_tokens}")
    if final.usage.cache_read_input_tokens:
        print(f"Cache   — {final.usage.cache_read_input_tokens} tokens served from cache")
    if final.usage.cache_creation_input_tokens:
        print(f"Written — {final.usage.cache_creation_input_tokens} tokens written to cache")

    if write_output:
        match = re.search(r"```python\n(.*?)```", full_response, re.DOTALL)
        if match:
            refactored_code = match.group(1)
            out_path = file_path.replace(".py", "_refactored.py")
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(refactored_code)
            print(f"\nRefactored file written to: {out_path}")
        else:
            print("\nCould not extract a ```python``` block from the response.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python refactor_utils.py <file.py> [--write]")
        sys.exit(1)

    try:
        refactor_utils(sys.argv[1], write_output="--write" in sys.argv)
    except anthropic.APIError as e:
        print(f"API error ({e.status_code}): {e.message}")
        sys.exit(1)
