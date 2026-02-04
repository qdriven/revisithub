# Skill: Test Case Design

## Description
Generate comprehensive functional and non-functional test cases based on requirements or code.

## How to Run

### Using Kimi CLI
```bash
kimi-cli analyze <requirement_file> "$(cat prompts/test-case-gen.txt)"
```

### Using Claude CLI
```bash
claude "Design test cases for the following feature using the standard template: [Feature Description]"
```

## Template
Located in `prompts/test-case-gen.txt`
