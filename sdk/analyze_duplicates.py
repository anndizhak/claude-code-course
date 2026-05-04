"""
Analyze a Python file or directory for duplicate code patterns using Claude.

Usage:
    python analyze_duplicates.py <file_or_directory>

Features:
    - Streams Claude's analysis in real time
    - Caches the system prompt across repeated runs
    - Reports token usage and cache hits
"""

import sys
import os
import glob
import anthropic


def read_python_files(path: str) -> dict[str, str]:
    """Read Python file(s) from path, returning {filename: source} pairs."""
    files: dict[str, str] = {}
    if os.path.isfile(path):
        with open(path, encoding="utf-8") as f:
            files[path] = f.read()
    elif os.path.isdir(path):
        for py_file in glob.glob(os.path.join(path, "**/*.py"), recursive=True):
            with open(py_file, encoding="utf-8") as f:
                files[py_file] = f.read()
    else:
        raise FileNotFoundError(f"Path not found: {path}")
    return files


def analyze_duplicates(path: str) -> None:
    files = read_python_files(path)
    if not files:
        print("No Python files found.")
        return

    code_context = "\n\n".join(
        f"# === {fname} ===\n{content}" for fname, content in files.items()
    )

    client = anthropic.Anthropic()
    print(f"Analyzing {len(files)} file(s) for duplicate code patterns...\n")
    print("=" * 60)

    with client.messages.stream(
        model="claude-opus-4-7",
        max_tokens=8192,
        thinking={"type": "adaptive"},
        system=[
            {
                "type": "text",
                "text": (
                    "You are an expert Python code reviewer specializing in identifying "
                    "duplication and refactoring opportunities.\n\n"
                    "When analyzing code, identify:\n"
                    "1. Duplicate or near-duplicate functions\n"
                    "2. Repeated logic blocks that could be extracted into helpers\n"
                    "3. Similar patterns that violate the DRY principle\n"
                    "4. Copy-pasted code with only minor variations\n\n"
                    "For each duplicate found, state:\n"
                    "- Location (file + function or line range)\n"
                    "- What is duplicated and why it matters\n"
                    "- A concrete refactoring suggestion with a short code example\n\n"
                    "Prioritize findings by impact. Be specific and actionable."
                ),
                "cache_control": {"type": "ephemeral"},
            }
        ],
        messages=[
            {
                "role": "user",
                "content": f"Analyze this Python code for duplicate patterns:\n\n{code_context}",
            }
        ],
    ) as stream:
        for text in stream.text_stream:
            print(text, end="", flush=True)

        final = stream.get_final_message()

    print("\n\n" + "=" * 60)
    print(f"Tokens  — input: {final.usage.input_tokens}, output: {final.usage.output_tokens}")
    if final.usage.cache_read_input_tokens:
        print(f"Cache   — {final.usage.cache_read_input_tokens} tokens served from cache")
    if final.usage.cache_creation_input_tokens:
        print(f"Written — {final.usage.cache_creation_input_tokens} tokens written to cache")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python analyze_duplicates.py <file_or_directory>")
        sys.exit(1)

    try:
        analyze_duplicates(sys.argv[1])
    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except anthropic.APIError as e:
        print(f"API error ({e.status_code}): {e.message}")
        sys.exit(1)
