#!/usr/bin/env node

const { execSync } = require("child_process");
const path = require("path");

const chunks = [];
process.stdin.on("data", (chunk) => chunks.push(chunk));
process.stdin.on("end", () => {
  const input = JSON.parse(Buffer.concat(chunks).toString());
  const filePath = input?.tool_input?.file_path ?? "";

  if (!filePath.endsWith(".ts") && !filePath.endsWith(".tsx")) {
    process.exit(0);
  }

  try {
    execSync("npx tsc --noEmit", { stdio: "pipe" });
  } catch (err) {
    const output = err.stdout?.toString() || err.stderr?.toString() || "";
    console.error("TypeScript type errors detected:\n" + output);
    process.exit(1);
  }

  process.exit(0);
});
