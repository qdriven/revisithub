# Kimi QA Skills

Kimi's strength lies in its **long-context window**, making it ideal for QA tasks that involve reading large files, multiple modules, or extensive documentation.

## Specialized QA Tasks for Kimi

### 1. Deep Code Analysis for QA
Kimi can read through entire modules to find logical flaws that might lead to bugs.

**Command:**
```bash
kimi-cli analyze <file_path> "Review this code for potential race conditions or memory leaks that should be tested."
```

### 2. Regression Test Identification
When code changes, Kimi can help identify which existing tests might be affected.

**Prompt:**
```text
Given these changes in auth.js: [paste diff], which existing test cases in tests/auth.test.js should I prioritize for regression testing?
```

### 3. Documentation Consistency Check
Verify if the implementation matches the documentation.

**Command:**
```bash
kimi-cli create "Compare the implementation in src/api.js with the documentation in docs/api.md. List any discrepancies as potential bugs."
```

## Tips for Kimi QA
- **Upload Context**: If using a web-based Kimi or a CLI that supports file attachments, provide as much context as possible.
- **Focus on Logic**: Use Kimi to trace complex logic paths that are hard for humans to follow.
