# Changelog

All notable changes to the Human Typer Mimicker project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2025-07-15

### Added
- **F6 Hotkey Support**: Press F6 to start/stop typing instead of delay-based timing
- **Cross-Platform Architecture**: Improved support for Windows, macOS, and Linux
- **Organized Project Structure**: 
  - `src/` directory for core source code
  - `scripts/` directory for build scripts and examples
  - `tests/` directory for testing utilities
  - `docs/` directory for comprehensive documentation
- **Smart Entry Point**: `main.py` automatically chooses GUI or CLI mode
- **Cross-Platform Build Scripts**: 
  - `scripts/build.py` - Universal Python build script
  - `scripts/build.bat` - Windows batch script
  - `scripts/build.sh` - macOS/Linux shell script
- **Enhanced GUI Interface**: 
  - Platform detection and display
  - F6 hotkey status indicator
  - Better progress tracking
  - Improved cross-platform theming
- **Comprehensive Documentation**:
  - User Guide with step-by-step tutorials
  - API Documentation with complete reference
  - Development Guide for contributors
  - Cross-platform installation instructions

### Changed
- **Replaced Start Delay with F6 Hotkey**: More intuitive and responsive control
- **Improved Project Organization**: Better separation of concerns and modularity
- **Enhanced Threading Model**: Better GUI responsiveness and hotkey handling
- **Updated Build Process**: Streamlined executable creation for all platforms
- **Modernized Documentation**: Professional formatting with comprehensive guides

### Improved
- **Cross-Platform Compatibility**: Better support for different operating systems
- **User Experience**: More intuitive interface and controls
- **Developer Experience**: Better project structure and build tools
- **Performance**: Optimized threading and resource management
- **Accessibility**: Clear instructions and better error handling

### Technical Enhancements
- Platform-specific GUI theming (Windows Vista, macOS Aqua, Linux Clam)
- Improved error handling and graceful fallbacks
- Better keyboard simulation detection and management
- Enhanced threading for non-blocking operations
- Comprehensive callback system for progress monitoring

## [1.0.0] - 2025-07-15

### Added
- Initial release of Human Typer Mimicker
- Core typing simulation with realistic human behavior
- Keyboard simulation using pynput library
- Adjacent key error simulation based on QWERTY layout
- Character transposition (letter swapping) simulation
- Double character typing errors
- Smart error correction with backspacing
- Variable typing speed with natural fluctuations
- Thinking pauses during typing
- Guaranteed text accuracy (final output always matches input)
- Command-line interface (`human_typer.py`)
- GUI interface using tkinter (`human_typer_gui.py`)
- Comprehensive usage examples (`examples.py`)
- Quick test script (`quick_test.py`)
- PyInstaller executable building support
- Configurable typing settings:
  - Typing speed (50-500 CPM)
  - Error rate (0-100%)
  - Correction rate (0-100%)
  - Start delay (0-10 seconds)
- Cross-platform support (Windows, macOS, Linux)
- Comprehensive documentation and README
- VS Code tasks for development
- GitHub workflows for CI/CD
- Automated executable building and releases

### Features
- **Realistic Human Behavior**: Simulates natural typing patterns with mistakes and corrections
- **Universal Compatibility**: Works with any application that accepts keyboard input
- **Highly Customizable**: Adjustable speed, error rates, and timing parameters
- **Dual Interface**: Both command-line and GUI versions available
- **Standalone Executable**: No installation required for end users
- **Developer Friendly**: Well-documented code with comprehensive examples

### Technical Details
- Python 3.6+ support
- Dependencies: pynput for keyboard simulation
- GUI framework: tkinter (included with Python)
- Build system: PyInstaller for executable creation
- Testing: Cross-platform CI with GitHub Actions
- Documentation: Comprehensive README and inline code documentation
