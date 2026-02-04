# Test Case Design Skills

Designing effective test cases is a core QA task. Using AI CLIs can help you brainstorm scenarios, cover edge cases, and ensure comprehensive coverage.

## Core Strategies

### 1. Requirements-to-Test Mapping
Provide the AI with a feature requirement or user story and ask it to generate test cases.

**Prompt Example:**
```text
Based on this requirement: "As a user, I want to be able to reset my password via email," generate a list of functional and non-functional test cases including happy paths, negative scenarios, and edge cases.
```

### 2. Boundary Value Analysis (BVA)
Ask the AI to identify boundary values for specific inputs.

**Prompt Example:**
```text
For a field that accepts an integer between 1 and 100, list all the boundary values and the corresponding test cases (Valid and Invalid).
```

### 3. Equivalence Partitioning
Group inputs into sets and let the AI pick representative values.

### 4. Error Guessing
Leverage the AI's knowledge of common software bugs to suggest where errors might occur in a specific piece of code.

## Using AI CLIs for Design

### Kimi CLI (Long Context)
Best for analyzing large requirement documents or existing codebases to find missing tests.

```bash
# Analyze a file for potential missing test cases
kimi-cli analyze src/auth.js "Suggest 5 critical test cases that are currently missing for this authentication logic."
```

### Claude Code CLI (Reasoning)
Best for complex multi-step scenarios and logic-heavy features.

```bash
# Generate a test plan for a new feature
claude explain docs/new-feature.md "Generate a detailed test plan including integration and end-to-end scenarios."
```

## Best Practices
- **Be Specific**: Include data types, constraints, and expected outcomes in your prompts.
- **Context is King**: Provide relevant code snippets or documentation.
- **Iterate**: Ask the AI to "think step-by-step" or "refine the previous test cases for better coverage".
