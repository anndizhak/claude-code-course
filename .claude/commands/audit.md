Perform a security audit of this codebase.

Check for the following vulnerabilities and issues:

1. **Secrets & credentials** — hardcoded API keys, tokens, passwords, or private keys in source files or config. Flag any `.env` files committed to the repo.
2. **Injection risks** — SQL injection, command injection, and XSS vulnerabilities. Look for unsanitized user input passed to queries, shell commands, or HTML output.
3. **Dependency vulnerabilities** — outdated or known-vulnerable packages in `package.json`, `requirements.txt`, `pyproject.toml`, or similar manifests.
4. **Insecure defaults** — debug modes enabled in production config, overly permissive CORS, missing authentication on sensitive endpoints.
5. **Path traversal** — user-controlled input used in file path construction without validation.
6. **Sensitive data exposure** — PII or secrets logged to console or written to unprotected files.

For each finding report:
- File and line number
- Severity (Critical / High / Medium / Low)
- A one-sentence description of the risk
- A concrete fix or remediation step

If no issues are found in a category, state that explicitly. End with a summary table of all findings.
