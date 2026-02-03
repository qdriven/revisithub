# GLM4 CLI

GLM4 CLI provides command-line access to Zhipu AI's GLM4 model, offering AI-powered development assistance in the terminal.

## Features
- Terminal access to GLM4 AI model
- Chinese and English language support
- Code generation and completion
- Technical document generation

## Installation
1. Install the CLI package:
   ```
   npm install -g @zhipu/glm4-cli
   ```
2. Or use npx without installation:
   ```
   npx @zhipu/glm4-cli
   ```

## Configuration
1. Obtain your API key from Zhipu AI platform
2. Set the API key as an environment variable:
   ```
   export ZHIPU_API_KEY='your-api-key-here'
   ```
3. Or configure using:
   ```
   glm4-cli config
   ```

## Usage
Common usage patterns:
```
# Generate code from prompt
glm4-cli generate "create a React component for a todo list"

# Explain complex code
glm4-cli explain <file-path> --language zh

# Create documentation
glm4-cli doc <source-file>

# Convert code between languages
glm4-cli convert <input-file> --from python --to javascript
```

## Integration with Other CLIs
GLM4 CLI works well with other AI CLIs, particularly for tasks involving Chinese language processing. See the main CLI directory documentation for best practices on using multiple AI tools together.