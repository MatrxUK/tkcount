#!/usr/bin/env python3
"""
Code Analyzer - Analyzes source code files and generates token counts for LLM usage
"""

import os
import sys
import glob
import fnmatch
from pathlib import Path
from collections import defaultdict, Counter
import argparse

try:
    import tiktoken
    HAS_TIKTOKEN = True
except ImportError:
    HAS_TIKTOKEN = False


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
                        patterns.append(line)

        return patterns

    def get_project_specific_ignores(self):
        """Get project-specific ignore patterns based on project type"""
        ignores = []

        # Check for TypeScript project
        tsconfig_path = self.folder_path / 'tsconfig.json'
        package_json_path = self.folder_path / 'package.json'

        is_typescript = tsconfig_path.exists()

        if not is_typescript and package_json_path.exists():
            try:
                import json
                with open(package_json_path, 'r', encoding='utf-8') as f:
                    package_data = json.load(f)
                    deps = package_data.get('dependencies', {})
                    dev_deps = package_data.get('devDependencies', {})
                    all_deps = {**deps, **dev_deps}
                    is_typescript = 'typescript' in all_deps
            except:
                pass

        if is_typescript:
            ignores.extend(['dist/', 'dist/**', 'build/', 'build/**', '*.js', '*.d.ts'])

        # Check for other common build outputs
        if (self.folder_path / 'package.json').exists():
            ignores.extend(['node_modules/', 'node_modules/**'])

        return ignores

    def should_ignore_file(self, file_path):
        """Check if file should be ignored based on gitignore, sensitive patterns, and project-specific patterns"""
        # Exclude the output file
        if file_path.name == self.output_file:
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

        print(f"Analyzing {len(files)} files...")

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
            'content': all_content
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
        print("="*60)

    def save_markdown(self, stats, output_file="codebase.md"):
        """Save all content to markdown file"""
        print(f"\n💾 Saving to {output_file}...")

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("# Codebase Analysis\n\n")
            f.write(f"**Total Files:** {stats['total_files']}\n")
            f.write(f"**Total Words:** {stats['total_words']:,}\n")
            f.write(f"**Total Tokens:** {stats['total_tokens']:,}\n\n")

            f.write("## File Types\n\n")
            for file_type, count in stats['file_types'].items():
                f.write(f"- {file_type}: {count}\n")
            f.write("\n")

            f.write("## Source Code\n\n")
            f.write("".join(stats['content']))

        print(f"✅ Saved {len(stats['content'])} files to {output_file}")


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