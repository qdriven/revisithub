# Claude QA Skills

Claude (especially via **Claude Code CLI**) is exceptionally strong at **reasoning**, **coding**, and **complex problem-solving**. It is your best partner for advanced QA engineering.

## Advanced QA Workflows with Claude

### 1. Automated Test Script Generation
Claude can write high-quality test scripts in various frameworks (Jest, Playwright, Selenium, etc.).

**Command:**
```bash
claude "Write a Playwright E2E test for the login flow using the elements defined in src/pages/LoginPage.js"
```

### 2. Bug Reproduction & Debugging
If you have a bug report, Claude can help you write a reproduction script.

**Command:**
```bash
claude "Based on this bug report: [report], create a minimal reproduction script using Node.js that demonstrates the issue."
```

### 3. Edge Case Brainstorming
Claude is excellent at thinking "outside the box" for security and performance edge cases.

**Prompt:**
```text
Think about the 'Transfer Funds' feature. List 10 creative ways a malicious user might try to exploit this, and suggest test cases to prevent these exploits.
```

## Using Claude Code Tools
Claude Code CLI allows for direct interaction with your filesystem, making it a powerful tool for:
- Running tests and analyzing failures.
- Automatically fixing minor bugs identified during testing.
- Refactoring tests for better maintainability.

## Best Practices
- **Use System Prompts**: If using the API, define Claude's role as a "Senior QA Engineer".
- **Chain of Thought**: Ask Claude to "think step-by-step" before providing the final test cases.
