# claude-code-course
# Claude Code in Action — Course Miniproject

Hands-on practice repository for the [Claude Code in Action](https://claudecertifications.com/courses/claude-code-in-action) course by Claude Certifications. Each folder and file in this repo corresponds to a specific lesson from the course.

## What This Covers

| Lesson | Topic | Files |
|--------|-------|-------|
| 4 | Adding context with CLAUDE.md | `CLAUDE.md` |
| 7 | Building custom slash commands | `.claude/commands/` |
| 8 | Extending Claude Code with MCP servers | `.claude/settings.local.json` |
| 9 | GitHub integration for automated workflows | `.github/workflows/` |
| 12 | Implementing a security hook | `hooks/read_hook.js` |
| 14 | Using the Claude Code SDK | `sdk/` |

## Key Concepts Practiced

**CLAUDE.md** — persistent context file that acts as a system prompt for your project. Generated with `/init` and customized with the `#` memory shortcut.

**Custom Commands** — reusable slash commands stored as markdown files in `.claude/commands/`. Support dynamic arguments via `$ARGUMENTS`.

**MCP Servers** — extend Claude Code with new tools like browser automation (Playwright), database access, and more. Installed with `claude mcp add`.

**GitHub Integration** — automated pull request reviews and `@claude` mentions in issues, set up with `/install-github-app`.

**Hooks** — scripts that run before (`PreToolUse`) or after (`PostToolUse`) Claude uses a tool. Used here to block access to `.env` files.

**Claude Code SDK** — run Claude Code programmatically from TypeScript or Python scripts, CI/CD pipelines, and custom automation tools.

## How to Use This Repo

1. Install Claude Code:
   ```powershell
   # Windows PowerShell
   irm https://claude.ai/install.ps1 | iex
   ```

2. Clone and open the project:
   ```bash
   git clone https://github.com/YOUR_USERNAME/claude-code-course.git
   cd claude-code-course
   claude
   ```

3. Try the custom commands inside Claude Code:
   ```
   /audit
   /write_tests src/utils.ts
   ```

## Course

[Claude Code in Action](https://claudecertifications.com/courses/claude-code-in-action) — Claude Certifications
