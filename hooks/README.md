# Hooks

Claude Code hooks are scripts that run automatically before or after Claude uses a tool.

## Hook Types (Lesson 10)

- **PreToolUse** — runs before a tool call, can block it (exit code 2)
- **PostToolUse** — runs after a tool call, cannot block but can react

## Hook Events (Lesson 13)

- `PreToolUse` / `PostToolUse` — tool lifecycle
- `Notification` — permission requests or 60s idle
- `Stop` / `SubagentStop` — when Claude finishes
- `PreCompact` — before conversation compaction
- `UserPromptSubmit` — before Claude processes your message
- `SessionStart` / `SessionEnd` — session lifecycle

## Files

- `read_hook.js` — security hook that blocks access to .env files (lesson 12)