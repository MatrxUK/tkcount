# Code Analyzer

A powerful Python tool that analyzes source code repositories and generates comprehensive reports with token counts optimized for Large Language Models (LLMs). It intelligently filters files, provides detailed statistics, and exports everything to a single organized markdown file.

## ✨ Features

- **Smart File Detection**: Automatically identifies and analyzes 40+ programming languages and file types
- **Intelligent Filtering**: Respects `.gitignore`, excludes sensitive files (`.env*`, keys, certificates), and project-specific build outputs
- **Project-Aware**: Detects TypeScript projects and automatically ignores `dist/`, `build/`, and compiled JavaScript files
- **Accurate Token Counting**: Uses OpenAI's tiktoken library for precise GPT tokenization (with fallback estimation)
- **Beautiful Reports**: Generates console reports with emojis and detailed breakdowns
- **Organized Export**: Saves all source code to a single markdown file with syntax highlighting
- **Cross-Platform**: Works on macOS, Linux, and Windows
- **Zero Dependencies**: Optional tiktoken dependency, works without it

## 🚀 Installation

### Option 1: Direct Download
```bash
# Clone or download the script
curl -O https://example.com/code_analyzer.py
chmod +x code_analyzer.py
```

### Option 2: With Token Counting (Recommended)
```bash
# Install tiktoken for accurate token counting
pip install tiktoken

# Download the script
curl -O https://example.com/code_analyzer.py
chmod +x code_analyzer.py
```

## 📖 Usage

### Basic Usage
```bash
# Interactive mode - will prompt for folder path
python3 code_analyzer.py

# Analyze a specific folder
python3 code_analyzer.py /path/to/your/project

# Custom output file
python3 code_analyzer.py /path/to/project -o my_analysis.md
```

### Command Line Options
```
usage: code_analyzer.py [-h] [-o OUTPUT] [folder]

Analyze source code and count tokens for LLM

positional arguments:
  folder                Folder path to analyze

options:
  -h, --help            Show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Output markdown file (default: codebase.md)
```

## 📊 Example Output

### Console Report
```
============================================================
📊 CODE ANALYSIS REPORT
============================================================
📁 Total Files: 42
📝 Total Words: 15,234
🤖 Total Tokens: 38,491

📂 Files by Type:
  • TypeScript: 12
  • Python: 8
  • JavaScript: 6
  • Markdown: 5
  • JSON: 4
  • Other (.css): 3
  • Other (.html): 2
  • Other (.yaml): 2
============================================================
```

### Generated Markdown File
The tool creates a comprehensive `codebase.md` file containing:
- Summary statistics
- File type breakdown
- All source code organized by file with syntax highlighting

## 🎯 Supported File Types

The analyzer recognizes and processes 40+ file types including:

**Programming Languages:**
- Python (.py), JavaScript (.js), TypeScript (.ts, .tsx)
- Java (.java), C/C++ (.c, .cpp, .h), C# (.cs)
- Go (.go), Rust (.rs), Swift (.swift), Kotlin (.kt)
- PHP (.php), Ruby (.rb), Scala (.scala)
- And many more...

**Web Technologies:**
- HTML (.html), CSS (.css), SCSS/Sass (.scss, .sass)
- JSON (.json), XML (.xml), YAML (.yaml, .yml)

**Documentation & Config:**
- Markdown (.md), Text (.txt), TOML (.toml)
- Shell scripts (.sh, .bash), PowerShell (.ps1)

## 🧠 Smart Filtering

### Always Ignored
- Sensitive files: `.env*`, `*.key`, `*.pem`, `*.crt`, `*.p12`
- The output file itself (to prevent double-counting)

### Project-Specific Rules
- **TypeScript Projects**: Automatically ignores `dist/`, `build/`, `*.js`, `*.d.ts`
- **Node.js Projects**: Ignores `node_modules/`
- **Git Projects**: Respects all `.gitignore` patterns

### Detection Logic
- **TypeScript**: Checks for `tsconfig.json` or `typescript` in `package.json` dependencies
- **Node.js**: Checks for `package.json` presence

## 🔧 Requirements

- **Python**: 3.6+
- **Optional**: tiktoken (for accurate token counting)
  ```bash
  pip install tiktoken
  ```

Without tiktoken, the tool uses a fallback estimation of ~4 characters per token.

## 📈 Token Counting

The tool provides accurate token counts using:
- **Primary**: OpenAI's tiktoken library (GPT-4/cl100k_base encoding)
- **Fallback**: Character-based estimation (1 token ≈ 4 characters)

Token counts are essential for:
- Estimating LLM API costs
- Ensuring code fits within model context windows
- Planning prompt engineering strategies

## 🤝 Contributing

We welcome contributions! Please:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

### Development Setup
```bash
git clone https://github.com/yourusername/code-analyzer.git
cd code-analyzer
pip install tiktoken  # For development
python3 code_analyzer.py .  # Test on itself
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Uses [tiktoken](https://github.com/openai/tiktoken) for accurate tokenization
- Inspired by the need for better codebase analysis tools for LLM workflows

## 🐛 Troubleshooting

### Common Issues

**"tiktoken could not be resolved"**
- This is normal if tiktoken isn't installed
- The tool works with fallback token counting
- Install with: `pip install tiktoken`

**High token counts**
- Check if output file is being included in analysis
- Ensure `.gitignore` is properly configured
- For TypeScript projects, verify `dist/` is being ignored

**Missing files**
- Check file permissions
- Ensure folder path is correct
- Verify files aren't in `.gitignore`

### Getting Help

- Open an [issue](https://github.com/yourusername/code-analyzer/issues) on GitHub
- Check the [troubleshooting guide](docs/troubleshooting.md) (if available)

---

**Made with ❤️ for developers working with Large Language Models**