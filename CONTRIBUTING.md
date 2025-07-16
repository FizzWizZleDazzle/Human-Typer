# Contributing to Human Typer Mimicker

Thank you for your interest in contributing to the Human Typer Mimicker project! This document provides guidelines and information for contributors.

## 🚀 Quick Start

1. Fork the repository
2. Clone your fork: `git clone https://github.com/yourusername/human-typer-mimicker.git`
3. Create a virtual environment: `python -m venv .venv`
4. Activate it: `.venv\Scripts\activate` (Windows) or `source .venv/bin/activate` (Unix)
5. Install dependencies: `pip install -r requirements.txt`
6. Make your changes
7. Test your changes
8. Submit a pull request

## 📋 Development Setup

### Prerequisites
- Python 3.9 or higher
- Git
- Virtual environment tool

### Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/human-typer-mimicker.git
cd human-typer-mimicker

# Create and activate virtual environment
python -m venv .venv
# Windows
.venv\Scripts\activate
# Unix/macOS
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Install development dependencies
pip install flake8 black pytest mypy
```

### Running Tests
```bash
# Basic functionality tests
python -c "from human_typer import HumanTyper; print('✓ Import successful')"

# GUI test (if supported)
python human_typer_gui.py

# Build test
python build_exe.py
```

## 🎯 Types of Contributions

### 🐛 Bug Reports
- Use the GitHub issue tracker
- Include Python version, OS, and error messages
- Provide steps to reproduce
- Include expected vs actual behavior

### ✨ Feature Requests
- Check existing issues first
- Describe the use case
- Explain why it would be beneficial
- Consider backward compatibility

### 🔧 Code Contributions
- Bug fixes
- New features
- Performance improvements
- Documentation improvements
- Test coverage improvements

## 📝 Coding Standards

### Python Style
- Follow PEP 8 style guidelines
- Use type hints where appropriate
- Maximum line length: 88 characters
- Use descriptive variable names
- Include docstrings for classes and methods

### Code Quality
```bash
# Format code
black .

# Lint code
flake8 .

# Type checking
mypy human_typer.py human_typer_gui.py
```

### Example Code Style
```python
def calculate_typing_delay(self, base_speed: int, variance: int) -> float:
    """
    Calculate realistic typing delay between characters.
    
    Args:
        base_speed: Base typing speed in characters per minute
        variance: Speed variance range
        
    Returns:
        float: Delay in seconds
    """
    base_delay = 60.0 / base_speed
    variation = random.uniform(-variance/base_speed, variance/base_speed)
    return max(0.05, base_delay + variation)
```

## 🏗️ Architecture Guidelines

### Core Components
- `human_typer.py`: Core typing logic and keyboard simulation
- `human_typer_gui.py`: GUI interface using tkinter
- `examples.py`: Usage examples and demonstrations
- `quick_test.py`: Simple testing script

### Design Principles
1. **Modularity**: Keep functionality separated and reusable
2. **Configurability**: Make behavior customizable through parameters
3. **Compatibility**: Ensure cross-platform functionality
4. **User Experience**: Prioritize ease of use and clear interfaces
5. **Documentation**: Code should be self-documenting with good naming

### Adding New Features

#### Typing Behaviors
- Add to the `HumanTyper` class
- Ensure configurability through parameters
- Maintain accuracy guarantee (final text matches input)
- Test across different scenarios

#### GUI Features
- Follow tkinter best practices
- Ensure responsive design
- Add appropriate validation
- Update help text and tooltips

#### Error Types
- Base on real human typing research
- Make probability-based and configurable
- Ensure errors are correctable
- Test with various keyboard layouts

## 🧪 Testing Guidelines

### Manual Testing
1. Test basic functionality with console output
2. Test keyboard simulation in various applications
3. Test GUI interface with different settings
4. Test executable building process
5. Test on different operating systems

### Automated Testing
- CI runs on multiple Python versions (3.9-3.12)
- Cross-platform testing (Windows, Ubuntu, macOS)
- Import and basic functionality tests
- Build verification tests

### Test Cases to Cover
- Different typing speeds (slow, normal, fast)
- Various error rates (low, medium, high)
- Different text types (short, long, code, punctuation)
- Edge cases (empty text, single characters, special characters)
- GUI functionality (all controls, file loading, etc.)

## 📚 Documentation

### Code Documentation
- Use clear, descriptive docstrings
- Include type hints
- Document complex algorithms
- Provide usage examples

### User Documentation
- Update README.md for new features
- Add examples to examples.py
- Update help text in GUI
- Consider creating tutorials for complex features

## 🔄 Pull Request Process

### Before Submitting
1. Ensure your code follows the style guidelines
2. Test your changes thoroughly
3. Update documentation if needed
4. Check that CI tests pass
5. Rebase on the latest main branch

### Pull Request Description
- Clear title describing the change
- Detailed description of what was changed and why
- Reference any related issues
- Include screenshots for GUI changes
- List any breaking changes

### Review Process
1. Automated CI checks must pass
2. Code review by maintainers
3. Testing of new functionality
4. Documentation review
5. Merge approval

## 🚀 Release Process

### Version Numbering
- Follow Semantic Versioning (MAJOR.MINOR.PATCH)
- MAJOR: Breaking changes
- MINOR: New features (backward compatible)
- PATCH: Bug fixes

### Release Steps
1. Update CHANGELOG.md
2. Update version in relevant files
3. Create git tag: `git tag v1.x.x`
4. Push tag: `git push origin v1.x.x`
5. GitHub Actions will automatically build and create release

## 💬 Communication

### Getting Help
- GitHub Discussions for questions
- GitHub Issues for bugs and feature requests
- Check existing issues before creating new ones

### Community Guidelines
- Be respectful and constructive
- Help others learn and contribute
- Follow the project's code of conduct
- Credit contributors appropriately

## 🎖️ Recognition

Contributors will be recognized in:
- README.md contributors section
- Release notes
- CHANGELOG.md for significant contributions

## 📄 Legal

By contributing, you agree that your contributions will be licensed under the same MIT License that covers the project.

---

Thank you for contributing to the Human Typer Mimicker project! 🎉
