# Development Guide

## Project Overview

Human Typer is a Python application that simulates realistic human typing behavior, including:
- Variable typing speeds with natural fluctuations
- Adjacent key errors based on QWERTY keyboard layout
- Character transposition and double-typing errors
- Realistic error correction patterns
- Natural thinking pauses

## Architecture

### Core Components

#### `human_typer.py` - Core Engine
The main typing simulation engine with these key classes:

- **HumanTyper**: Main class that orchestrates typing behavior
- **KeyboardLayout**: QWERTY layout mapping for adjacent key errors
- **Error Generation**: Probabilistic error injection system
- **Speed Control**: Variable typing speed with realistic fluctuations

#### `human_typer_gui.py` - GUI Interface
Tkinter-based graphical user interface featuring:

- **Settings Panel**: Speed, error rate, and correction rate controls
- **Text Input**: Multi-line text editor with sample texts
- **File Operations**: Load text files for typing
- **Progress Monitoring**: Real-time typing progress display
- **Threading**: Non-blocking UI during typing operations

#### `examples.py` - Usage Demonstrations
Various usage patterns and configuration examples for developers.

## Development Setup

### Prerequisites
- Python 3.6+ (tested with 3.12.4)
- Virtual environment (recommended)
- Git for version control

### Installation
```bash
# Clone repository
git clone https://github.com/yourusername/human-typer.git
cd human-typer

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Running Tests
```bash
# Quick functionality test
python quick_test.py

# GUI test
python human_typer_gui.py

# Example demonstrations
python examples.py
```

## Code Structure

### Key Algorithms

#### Typing Speed Calculation
```python
# Base speed with natural variation
base_interval = 60.0 / self.characters_per_minute
variation = random.uniform(0.5, 1.5)
actual_interval = base_interval * variation
```

#### Error Generation
Errors are generated using probability-based systems:
1. **Adjacent Key Errors**: Based on physical keyboard proximity
2. **Transposition**: Swapping adjacent characters
3. **Double Characters**: Repeating the same character

#### Error Correction
Smart correction system that:
- Detects when to correct errors
- Uses realistic backspacing behavior
- Maintains text accuracy while simulating human patterns

### Threading Model
The GUI uses Python's `threading` module to prevent UI blocking:
```python
typing_thread = threading.Thread(target=self.typing_worker, args=(text,))
typing_thread.daemon = True
typing_thread.start()
```

## Building and Distribution

### Executable Creation
Uses PyInstaller for creating standalone executables:

```bash
# Automated build
python build_exe.py

# Manual build
pyinstaller --onefile --windowed --name "HumanTyperGUI" --add-data "human_typer.py;." human_typer_gui.py
```

### GitHub Actions
Two workflows are configured:

1. **CI Pipeline** (`ci.yml`): Tests across Python 3.9-3.12 on Windows, macOS, Linux
2. **Release Pipeline** (`build-release.yml`): Automatic executable builds and GitHub releases

## Debugging Tips

### Common Development Issues

1. **Keyboard Simulation Not Working**
   - Check pynput installation
   - Verify system permissions
   - Test with `use_keyboard=False` for console mode

2. **GUI Freezing**
   - Ensure typing operations are in separate threads
   - Check for infinite loops in error correction
   - Monitor memory usage with long texts

3. **Import Errors**
   - Verify virtual environment activation
   - Check Python path configuration
   - Reinstall dependencies if needed

### Testing Strategies

1. **Unit Testing**: Test individual components (error generation, speed calculation)
2. **Integration Testing**: Test GUI and core engine interaction
3. **User Testing**: Test with various text types and lengths
4. **Performance Testing**: Monitor memory and CPU usage

## Contributing Guidelines

### Code Style
- Follow PEP 8 guidelines
- Use type hints for better code clarity
- Include docstrings for all classes and methods
- Meaningful variable names that describe behavior

### Testing Requirements
- Test with various text lengths and complexity
- Verify error rates are realistic
- Ensure corrections don't create infinite loops
- Test edge cases (empty strings, special characters)

### Performance Considerations
- Use `time.sleep()` for realistic timing delays
- Flush output immediately for real-time effect
- Consider memory usage with very long texts
- Optimize for smooth GUI responsiveness

## Future Development Areas

### Immediate Improvements
- Better error pattern algorithms
- Configurable keyboard layouts
- Enhanced GUI features
- Performance optimizations

### Long-term Goals
- Typing analytics and statistics
- Multi-language support
- Mobile keyboard simulation
- Machine learning-based typing patterns

## Troubleshooting Development Issues

### Environment Setup
If you encounter issues setting up the development environment:

1. **Python Version**: Ensure you're using Python 3.6+
2. **Virtual Environment**: Always use a virtual environment
3. **Dependencies**: Install exact versions from requirements.txt
4. **Permissions**: Some systems require elevated permissions

### Debugging Tools
- Use VS Code's integrated debugger
- Enable Python logging for detailed output
- Use `print()` statements for quick debugging
- Monitor system resources during testing

### Platform-Specific Considerations
- **Windows**: Generally works without special setup
- **macOS**: May require accessibility permissions
- **Linux**: May need additional X11 dependencies
