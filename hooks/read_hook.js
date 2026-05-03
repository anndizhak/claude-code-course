#!/usr/bin/env node

const chunks = [];
process.stdin.on("data", (chunk) => chunks.push(chunk));
process.stdin.on("end", () => {
  const input = JSON.parse(Buffer.concat(chunks).toString());
  const filePath = input?.tool_input?.file_path ?? "";

  if (filePath.includes(".env")) {
    console.error("Blocked: reading .env files is not allowed.");
    process.exit(2);
  }

  process.exit(0);
});
