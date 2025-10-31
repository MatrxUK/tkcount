# Codebase Analysis

**Total Files:** 2
**Total Words:** 2,718
**Total Tokens:** 7,509

## File Types

- Markdown: 1
- Python: 1

## ✅ Security Scan

**No sensitive data detected in the codebase.**

## Source Code

## README.md

```md
# Code Analyzer

A powerful Python tool that analyzes source code repositories and generates comprehensive reports with token counts optimized for Large Language Models (LLMs). It intelligently filters files, scans for security vulnerabilities, provides detailed statistics, and exports everything to a single organized markdown file.

## ✨ Features

- **Smart File Detection**: Automatically identifies and analyzes 40+ programming languages and file types
- **Intelligent Filtering**: Respects `.gitignore`, excludes sensitive files (`.env*`, keys, certificates), and project-specific build outputs
- **Project-Aware**: Detects TypeScript projects and automatically ignores `dist/`, `build/`, and compiled JavaScript files
- **Security Scanning**: Automatically detects API keys, passwords, PII, and other sensitive data with highlighted warnings
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

Analyze source code, scan for security issues, and count tokens for LLM

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

🚨 SECURITY ISSUES FOUND:
   ⚠️  3 potential security issues detected
   • Passwords: 1 issues
   • API Keys: 2 issues
   📋 See detailed report in the markdown file
============================================================
```

### Generated Markdown File
The tool creates a comprehensive `codebase.md` file containing:
- Summary statistics
- File type breakdown
- **Security scan results** with highlighted warnings for sensitive data
- All source code organized by file with syntax highlighting
- **Prominent security warnings** in red-highlighted boxes when issues are found

## 🔒 Security Scanning

The tool automatically scans for sensitive data including:

**Credentials & Keys:**
- API keys (OpenAI, Slack, GitHub, AWS, etc.)
- Passwords and database credentials
- Authentication tokens and bearer tokens
- Private keys and certificates

**Personal Information:**
- Email addresses
- Phone numbers
- Social security numbers
- Credit card numbers

**Security Issues:**
- Hardcoded database connection strings
- URLs with embedded credentials
- IP addresses and network information

**Console Alert:**
```
🚨 SECURITY ISSUES FOUND:
   ⚠️  3 potential security issues detected
   • Passwords: 1 issues
   • API Keys: 2 issues
   📋 See detailed report in the markdown file
```

**Markdown Report:**
Security findings appear in a prominent red-highlighted warning box with:
- File location and line numbers
- Detected sensitive content (truncated for safety)
- Security recommendations

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
- Security patterns based on common industry standards and best practices
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

**Security scanning false positives**
- Some patterns may match legitimate code or test data
- Review findings carefully before taking action
- Consider adding detected patterns to `.gitignore` if they're intentional

**Security scanning misses**
- Only scans text files that pass the file type filter
- Binary files and certain encoded content are not scanned
- Complex obfuscation may bypass pattern matching

### Getting Help

- Open an [issue](https://github.com/yourusername/code-analyzer/issues) on GitHub
- Check the [troubleshooting guide](docs/troubleshooting.md) (if available)

---

**Made with ❤️ for developers working with Large Language Models and prioritizing code security**
```

## code_analyzer.py

```py
#!/usr/bin/env python3
"""
Code Analyzer - Analyzes source code files and generates token counts for LLM usage
"""

import os
import sys
import glob
import fnmatch
import re
import time
import threading
from pathlib import Path
from collections import defaultdict, Counter
import argparse

try:
    import tiktoken
    HAS_TIKTOKEN = True
except ImportError:
    HAS_TIKTOKEN = False


class Spinner:
    """Simple terminal spinner for showing progress"""
    def __init__(self, message="Processing..."):
        self.message = message
        self.spinner_chars = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
        self.stop_event = threading.Event()
        self.thread = None

    def spin(self):
        i = 0
        while not self.stop_event.is_set():
            char = self.spinner_chars[i % len(self.spinner_chars)]
            sys.stdout.write(f'\r{char} {self.message}')
            sys.stdout.flush()
            time.sleep(0.1)
            i += 1

    def start(self):
        self.stop_event.clear()
        self.thread = threading.Thread(target=self.spin, daemon=True)
        self.thread.start()

    def stop(self):
        self.stop_event.set()
        if self.thread:
            self.thread.join()
        sys.stdout.write('\r' + ' ' * (len(self.message) + 2) + '\r')
        sys.stdout.flush()


class CodeAnalyzer:
    def __init__(self, folder_path, output_file="codebase.md"):
        self.folder_path = Path(folder_path)
        self.output_file = output_file
        self.gitignore_patterns = self.load_gitignore()
        self.sensitive_patterns = ['.env*', '*.key', '*.pem', '*.crt', '*.p12']
        self.additional_ignore_patterns = self.get_project_specific_ignores()
        self.file_extensions = {
            '.py': 'Python',
            '.js': 'JavaScript',
            '.ts': 'TypeScript',
            '.jsx': 'React JSX',
            '.tsx': 'React TSX',
            '.java': 'Java',
            '.cpp': 'C++',
            '.c': 'C',
            '.h': 'C/C++ Header',
            '.cs': 'C#',
            '.php': 'PHP',
            '.rb': 'Ruby',
            '.go': 'Go',
            '.rs': 'Rust',
            '.swift': 'Swift',
            '.kt': 'Kotlin',
            '.scala': 'Scala',
            '.html': 'HTML',
            '.css': 'CSS',
            '.scss': 'SCSS',
            '.sass': 'Sass',
            '.less': 'Less',
            '.json': 'JSON',
            '.xml': 'XML',
            '.yaml': 'YAML',
            '.yml': 'YAML',
            '.toml': 'TOML',
            '.md': 'Markdown',
            '.txt': 'Text',
            '.sh': 'Shell Script',
            '.bash': 'Bash Script',
            '.ps1': 'PowerShell',
            '.sql': 'SQL',
            '.r': 'R',
            '.m': 'MATLAB/Objective-C',
            '.pl': 'Perl',
            '.lua': 'Lua',
            '.dart': 'Dart',
            '.elm': 'Elm',
            '.hs': 'Haskell',
            '.ml': 'OCaml',
            '.fs': 'F#',
            '.vb': 'Visual Basic',
            '.clj': 'Clojure',
            '.cljs': 'ClojureScript',
            '.ex': 'Elixir',
            '.exs': 'Elixir Script'
        }

    def load_gitignore(self):
        """Load .gitignore patterns if file exists"""
        gitignore_path = self.folder_path / '.gitignore'
        patterns = []

        if gitignore_path.exists():
            with open(gitignore_path, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#'):
                        # Handle directory patterns - add both with and without trailing slash
                        if line.endswith('/'):
                            patterns.extend([line, line.rstrip('/'), line + '**', line.rstrip('/') + '/**'])
                        else:
                            patterns.extend([line, line + '/', line + '/**'])
                        # Remove duplicates
                        patterns = list(set(patterns))

        return patterns

    def get_project_specific_ignores(self):
        """Get project-specific ignore patterns based on project type"""
        ignores = []

        # Check for TypeScript projects (root level and nested)
        has_typescript = False

        # Check root level
        if (self.folder_path / 'tsconfig.json').exists():
            has_typescript = True
        elif (self.folder_path / 'package.json').exists():
            try:
                import json
                with open(self.folder_path / 'package.json', 'r', encoding='utf-8') as f:
                    package_data = json.load(f)
                    deps = package_data.get('dependencies', {})
                    dev_deps = package_data.get('devDependencies', {})
                    all_deps = {**deps, **dev_deps}
                    if 'typescript' in all_deps:
                        has_typescript = True
            except:
                pass

        # Check for nested TypeScript projects
        if not has_typescript:
            for tsconfig in self.folder_path.rglob('tsconfig.json'):
                has_typescript = True
                break

        if has_typescript:
            # Ignore TypeScript output folders at any nesting level
            ignores.extend([
                'dist/', 'dist/**', '**/dist/', '**/dist/**',
                'build/', 'build/**', '**/build/', '**/build/**',
                'out/', 'out/**', '**/out/', '**/out/**',
                '*.js', '*.d.ts', '**/*.js', '**/*.d.ts'
            ])

        # Check for other common build outputs and package directories
        if (self.folder_path / 'package.json').exists():
            ignores.extend(['node_modules/', 'node_modules/**', '**/node_modules/', '**/node_modules/**'])

        # Language-specific package and build directories (always ignore)
        package_dirs = [
            # JavaScript/Node.js
            'node_modules/', 'node_modules/**', '**/node_modules/', '**/node_modules/**',
            # Python
            '__pycache__/', '__pycache__/**', '**/__pycache__/', '**/__pycache__/**',
            '.venv/', '.venv/**', '**/.venv/', '**/.venv/**',
            'venv/', 'venv/**', '**/venv/', '**/venv/**',
            'env/', 'env/**', '**/env/', '**/env/**',
            '.env/', '.env/**', '**/.env/', '**/.env/**',
            # Rust
            '.cargo/', '.cargo/**', '**/.cargo/', '**/.cargo/**',
            'target/', 'target/**', '**/target/', '**/target/**',
            # Go
            'vendor/', 'vendor/**', '**/vendor/', '**/vendor/**',
            'Godeps/', 'Godeps/**', '**/Godeps/', '**/Godeps/**',
            # PHP
            'vendor/', 'vendor/**', '**/vendor/', '**/vendor/**',  # PHP (duplicate but comprehensive)
            # Ruby
            '.bundle/', '.bundle/**', '**/.bundle/', '**/.bundle/**',
            'vendor/bundle/', 'vendor/bundle/**', '**/vendor/bundle/', '**/vendor/bundle/**',
            # Java
            '.gradle/', '.gradle/**', '**/.gradle/', '**/.gradle/**',
            'build/', 'build/**', '**/build/', '**/build/**',  # Java (duplicate but comprehensive)
            'target/', 'target/**', '**/target/', '**/target/**',  # Java/Maven (duplicate but comprehensive)
            # .NET
            'bin/', 'bin/**', '**/bin/', '**/bin/**',
            'obj/', 'obj/**', '**/obj/', '**/obj/**',
            'packages/', 'packages/**', '**/packages/', '**/packages/**',
            # Swift
            '.build/', '.build/**', '**/.build/', '**/.build/**',
            'Packages/', 'Packages/**', '**/Packages/', '**/Packages/**',
            # Haskell
            'dist/', 'dist/**', '**/dist/', '**/dist/**',  # Haskell (duplicate but comprehensive)
            'dist-newstyle/', 'dist-newstyle/**', '**/dist-newstyle/', '**/dist-newstyle/**',
            # Scala
            'target/', 'target/**', '**/target/', '**/target/**',  # Scala (duplicate but comprehensive)
            'project/target/', 'project/target/**', '**/project/target/', '**/project/target/**',
            # Elixir
            '_build/', '_build/**', '**/_build/', '**/_build/**',
            'deps/', 'deps/**', '**/deps/', '**/deps/**',
            # Dart/Flutter
            '.dart_tool/', '.dart_tool/**', '**/.dart_tool/', '**/.dart_tool/**',
            'build/', 'build/**', '**/build/', '**/build/**',  # Flutter (duplicate but comprehensive)
            # C/C++
            'cmake-build-*/', 'cmake-build-*/**', '**/cmake-build-*/', '**/cmake-build-*/**',
            'CMakeFiles/', 'CMakeFiles/**', '**/CMakeFiles/', '**/CMakeFiles/**',
            # General
            '.DS_Store', '.DS_Store/**', '**/.DS_Store', '**/.DS_Store/**',
            'Thumbs.db', 'Thumbs.db/**', '**/Thumbs.db', '**/Thumbs.db/**',
        ]

        ignores.extend(package_dirs)

        return ignores

    def scan_for_sensitive_data(self):
        """Scan all source files for sensitive data patterns"""
        # Start security scan spinner
        scan_spinner = Spinner("Scanning for sensitive data...")
        scan_spinner.start()

        sensitive_patterns = {
            'API Keys': [
                r'(?i)(api[_-]?key|apikey)\s*[=:]\s*["\']([a-zA-Z0-9_-]{20,})["\']',
                r'(?i)(secret[_-]?key|secretkey)\s*[=:]\s*["\']([a-zA-Z0-9_-]{20,})["\']',
                r'(?i)(access[_-]?token|accesstoken)\s*[=:]\s*["\']([a-zA-Z0-9_-]{20,})["\']',
                r'(?i)(bearer[_-]?token|bearertoken)\s*[=:]\s*["\']([a-zA-Z0-9_-]{20,})["\']',
                r'(?i)(auth[_-]?token|authtoken)\s*[=:]\s*["\']([a-zA-Z0-9_-]{20,})["\']',
                r'sk-[a-zA-Z0-9]{48}',  # OpenAI API keys
                r'xox[baprs]-[0-9]{10,12}-[0-9]{10,12}-[a-zA-Z0-9]*',  # Slack tokens
                r'ghp_[a-zA-Z0-9]{36}',  # GitHub personal access tokens
                r'AKIA[0-9A-Z]{16}',  # AWS access key ID
                r'(?i)aws[_-]?secret[_-]?key\s*[=:]\s*["\']([a-zA-Z0-9/+=]{40})["\']',  # AWS secret keys
            ],
            'Passwords': [
                r'(?i)(password|passwd|pwd)\s*[=:]\s*["\']([^"\']{3,})["\']',
                r'(?i)(db[_-]?password|dbpasswd)\s*[=:]\s*["\']([^"\']{3,})["\']',
                r'(?i)(admin[_-]?password|adminpwd)\s*[=:]\s*["\']([^"\']{3,})["\']',
            ],
            'Database Connections': [
                r'(?i)(mongodb|postgres|mysql|sqlite)://[^"\'\s]+',
                r'(?i)(host|hostname)\s*[=:]\s*["\']([^"\']+)["\']',
                r'(?i)(database|db[_-]?name)\s*[=:]\s*["\']([^"\']+)["\']',
                r'(?i)(username|user)\s*[=:]\s*["\']([^"\']+)["\']',
            ],
            'Private Keys': [
                r'-----BEGIN\s+(RSA\s+)?PRIVATE\s+KEY-----',
                r'-----BEGIN\s+(EC\s+)?PRIVATE\s+KEY-----',
                r'-----BEGIN\s+OPENSSH\s+PRIVATE\s+KEY-----',
            ],
            'PII - Email Addresses': [
                r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
            ],
            'PII - Phone Numbers': [
                r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b',  # US phone numbers
                r'\+\d{1,3}[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,4}',  # International
            ],
            'PII - Social Security Numbers': [
                r'\b\d{3}[-]?\d{2}[-]?\d{4}\b',  # SSN
            ],
            'Credit Card Numbers': [
                r'\b\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}\b',  # Basic CC pattern
            ],
            'IP Addresses': [
                r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b',
            ],
            'URLs with Credentials': [
                r'https?://[^:\s]+:[^@\s]+@[^"\'\s]+',  # URL with user:pass@
            ],
        }

        findings = defaultdict(list)

        for file_path in self.get_source_files():
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    lines = content.split('\n')

                for category, patterns in sensitive_patterns.items():
                    for pattern in patterns:
                        matches = re.findall(pattern, content, re.IGNORECASE | re.MULTILINE)
                        if matches:
                            for match in matches:
                                # Find line number
                                line_num = None
                                for i, line in enumerate(lines, 1):
                                    if re.search(pattern, line, re.IGNORECASE):
                                        line_num = i
                                        break

                                findings[category].append({
                                    'file': str(file_path.relative_to(self.folder_path)),
                                    'line': line_num or 'Unknown',
                                    'match': str(match)[:100] + '...' if len(str(match)) > 100 else str(match)
                                })

            except Exception as e:
                print(f"Warning: Could not scan {file_path} for sensitive data: {e}")

        # Stop security scan spinner
        scan_spinner.stop()
        return dict(findings)

    def should_ignore_file(self, file_path):
        """Check if file should be ignored based on gitignore, sensitive patterns, and project-specific patterns"""
        # Exclude the output file
        if file_path.name == self.output_file or file_path == self.folder_path / self.output_file:
            return True

        # Check sensitive patterns
        for pattern in self.sensitive_patterns:
            if fnmatch.fnmatch(file_path.name, pattern):
                return True

        # Check gitignore patterns
        for pattern in self.gitignore_patterns:
            if fnmatch.fnmatch(str(file_path), pattern) or fnmatch.fnmatch(file_path.name, pattern):
                return True

        # Check project-specific ignore patterns
        for pattern in self.additional_ignore_patterns:
            if fnmatch.fnmatch(str(file_path), pattern) or fnmatch.fnmatch(file_path.name, pattern):
                return True

        return False

    def get_source_files(self):
        """Get all relevant source code files"""
        source_files = []

        # Common source file patterns
        patterns = [
            '**/*.py', '**/*.js', '**/*.ts', '**/*.jsx', '**/*.tsx',
            '**/*.java', '**/*.cpp', '**/*.c', '**/*.h', '**/*.cs',
            '**/*.php', '**/*.rb', '**/*.go', '**/*.rs', '**/*.swift',
            '**/*.kt', '**/*.scala', '**/*.html', '**/*.css', '**/*.scss',
            '**/*.sass', '**/*.less', '**/*.json', '**/*.xml', '**/*.yaml',
            '**/*.yml', '**/*.toml', '**/*.md', '**/*.txt', '**/*.sh',
            '**/*.bash', '**/*.ps1', '**/*.sql', '**/*.r', '**/*.m',
            '**/*.pl', '**/*.lua', '**/*.dart', '**/*.elm', '**/*.hs',
            '**/*.ml', '**/*.fs', '**/*.vb', '**/*.clj', '**/*.cljs',
            '**/*.ex', '**/*.exs'
        ]

        for pattern in patterns:
            for file_path in glob.glob(str(self.folder_path / pattern), recursive=True):
                path_obj = Path(file_path)
                if not self.should_ignore_file(path_obj):
                    source_files.append(path_obj)

        return sorted(source_files)

    def count_tokens(self, text):
        """Count tokens using tiktoken (GPT-4 tokenizer) or fallback"""
        if HAS_TIKTOKEN:
            try:
                encoding = tiktoken.get_encoding("cl100k_base")  # GPT-4 tokenizer
                return len(encoding.encode(text))
            except:
                pass

        # Fallback: rough estimate of 4 characters per token
        return len(text) // 4

    def analyze_files(self):
        """Analyze all source files and return statistics"""
        files = self.get_source_files()
        file_types = Counter()
        total_words = 0
        total_tokens = 0
        all_content = []

        # Start progress spinner
        spinner = Spinner(f"Analyzing {len(files)} files...")
        spinner.start()

        # Scan for sensitive data
        security_findings = self.scan_for_sensitive_data()

        # Stop spinner
        spinner.stop()
        print(f"✅ Analyzed {len(files)} files")

        for file_path in files:
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()

                # Count words
                words = len(content.split())
                total_words += words

                # Count tokens
                tokens = self.count_tokens(content)
                total_tokens += tokens

                # Track file types
                ext = file_path.suffix.lower()
                file_type = self.file_extensions.get(ext, f'Other ({ext})')
                file_types[file_type] += 1

                # Store content for markdown
                relative_path = file_path.relative_to(self.folder_path)
                all_content.append(f"## {relative_path}\n\n```{ext[1:] if ext else ''}\n{content}\n```\n\n")

            except Exception as e:
                print(f"Warning: Could not read {file_path}: {e}")

        return {
            'total_files': len(files),
            'file_types': dict(file_types.most_common()),
            'total_words': total_words,
            'total_tokens': total_tokens,
            'content': all_content,
            'security_findings': security_findings
        }

    def generate_report(self, stats):
        """Generate console report"""
        print("\n" + "="*60)
        print("📊 CODE ANALYSIS REPORT")
        print("="*60)
        print(f"📁 Total Files: {stats['total_files']}")
        print(f"📝 Total Words: {stats['total_words']:,}")
        print(f"🤖 Total Tokens: {stats['total_tokens']:,}")
        print("\n📂 Files by Type:")
        for file_type, count in stats['file_types'].items():
            print(f"  • {file_type}: {count}")

        # Security findings
        security_findings = stats.get('security_findings', {})
        if security_findings:
            print("\n🚨 SECURITY ISSUES FOUND:")
            total_findings = sum(len(findings) for findings in security_findings.values())
            print(f"   ⚠️  {total_findings} potential security issues detected")
            for category, findings in security_findings.items():
                print(f"   • {category}: {len(findings)} issues")
            print("   📋 See detailed report in the markdown file")
        else:
            print("\n✅ No sensitive data detected")

        print("="*60)

    def save_markdown(self, stats, output_file="codebase.md"):
        """Save all content to markdown file"""
        output_path = self.folder_path / output_file

        # Start save spinner
        save_spinner = Spinner(f"Saving to {output_path.name}...")
        save_spinner.start()

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write("# Codebase Analysis\n\n")
            f.write(f"**Total Files:** {stats['total_files']}\n")
            f.write(f"**Total Words:** {stats['total_words']:,}\n")
            f.write(f"**Total Tokens:** {stats['total_tokens']:,}\n\n")

            f.write("## File Types\n\n")
            for file_type, count in stats['file_types'].items():
                f.write(f"- {file_type}: {count}\n")
            f.write("\n")

            # Security findings
            security_findings = stats.get('security_findings', {})
            if security_findings:
                f.write("## 🚨 SECURITY ISSUES FOUND\n\n")
                f.write("<div style='background-color: #ffebee; border: 2px solid #f44336; border-radius: 5px; padding: 15px; margin: 10px 0;'>\n\n")
                f.write("**⚠️ WARNING: Potential sensitive data detected in the codebase!**\n\n")
                total_findings = sum(len(findings) for findings in security_findings.values())
                f.write(f"**Total Issues Found:** {total_findings}\n\n")

                for category, findings in security_findings.items():
                    f.write(f"### {category} ({len(findings)} issues)\n\n")
                    for finding in findings:
                        f.write(f"- **File:** `{finding['file']}` (Line: {finding['line']})\n")
                        f.write(f"  - **Detected:** `{finding['match']}`\n")
                    f.write("\n")

                f.write("**🔒 Security Recommendations:**\n")
                f.write("- Review and remove any hardcoded credentials\n")
                f.write("- Use environment variables for sensitive data\n")
                f.write("- Consider using secret management services\n")
                f.write("- Audit your .gitignore to ensure sensitive files are excluded\n\n")
                f.write("</div>\n\n")
            else:
                f.write("## ✅ Security Scan\n\n")
                f.write("**No sensitive data detected in the codebase.**\n\n")

            f.write("## Source Code\n\n")
            f.write("".join(stats['content']))

        # Stop save spinner
        save_spinner.stop()
        print(f"✅ Saved {len(stats['content'])} files to {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Analyze source code and count tokens for LLM")
    parser.add_argument("folder", nargs="?", help="Folder path to analyze")
    parser.add_argument("-o", "--output", default="codebase.md", help="Output markdown file")

    args = parser.parse_args()

    if not args.folder:
        args.folder = input("Enter folder path to analyze: ").strip()

    if not args.folder:
        print("❌ No folder specified")
        sys.exit(1)

    folder_path = Path(args.folder)
    if not folder_path.exists() or not folder_path.is_dir():
        print(f"❌ Folder does not exist: {folder_path}")
        sys.exit(1)

    analyzer = CodeAnalyzer(folder_path, args.output)
    stats = analyzer.analyze_files()
    analyzer.generate_report(stats)
    analyzer.save_markdown(stats, args.output)


if __name__ == "__main__":
    main()
```

