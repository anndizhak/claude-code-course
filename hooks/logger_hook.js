#!/usr/bin/env node

const fs = require("fs");
const path = require("path");

const LOG_FILE = path.join(__dirname, "..", "claude-activity.log");

const chunks = [];
process.stdin.on("data", (chunk) => chunks.push(chunk));
process.stdin.on("end", () => {
  const input = JSON.parse(Buffer.concat(chunks).toString());

  const toolName = input?.tool_name ?? "unknown";
  const toolInput = input?.tool_input ?? {};

  // Extract the most relevant identifier depending on the tool
  const detail =
    toolInput.file_path ??
    toolInput.path ??
    toolInput.command ??
    toolInput.pattern ??
    toolInput.prompt ??
    JSON.stringify(toolInput).slice(0, 120);

  const timestamp = new Date().toISOString();
  const line = `[${timestamp}] tool=${toolName} detail=${detail}\n`;

  fs.appendFileSync(LOG_FILE, line);

  process.exit(0);
});
