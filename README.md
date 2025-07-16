# Human Typer Mimicker

![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-windows%20%7C%20macos%20%7C%20linux-lightgrey.svg)
![Build](https://img.shields.io/github/actions/workflow/status/FizzWizzleDazzle/Human-Typer/ci.yml?branch=main)
![Release](https://img.shields.io/github/v/release/FizzWizzleDazzle/Human-Typer)

A sophisticated Python application that simulates realistic human typing behavior with natural mistakes, speed fluctuations, and corrections. Features **F6 hotkey control** for instant start/stop functionality. Perfect for testing applications, creating demonstrations, and automating workflows that require human-like text input.

## 🌟 Key Features

### 🎮 **F6 Hotkey Control** ⭐ NEW!
- **Press F6 to Start**: No more countdown delays - instant control when you're ready
- **Press F6 to Stop**: Cancel typing anytime with a single keypress
- **Intuitive Workflow**: Switch to your target app, then press F6 to begin typing

### 🎯 **Realistic Human Behavior**
- **Adjacent Key Errors**: Mistakes based on physical keyboard layout
- **Character Transposition**: Natural letter swapping patterns
- **Speed Fluctuations**: Variable typing rhythm with natural variations
- **Thinking Pauses**: Realistic breaks during typing
- **Smart Corrections**: Human-like error detection and backspacing

### ✅ **Guaranteed Accuracy**
- **Perfect Output**: Final text always matches your input exactly
- **Error Recovery**: All mistakes are automatically corrected
- **No Data Loss**: Never leaves incomplete or incorrect text

### 🔧 **Highly Configurable**
- **Typing Speed**: 50-500 characters per minute
- **Error Rates**: 0-100% mistake probability
- **Correction Behavior**: Customizable error correction patterns
- **Timing Control**: Adjustable delays and pause frequencies

### 🖥️ **Multiple Interfaces**
- **GUI Application**: User-friendly graphical interface
- **Command Line**: Scriptable and automation-friendly
- **Standalone Executable**: No installation required
- **Python Library**: Integrate into your own projects

## 📸 Screenshots

### GUI Interface
![GUI Screenshot](docs/images/gui-screenshot.png)
*User-friendly interface with configurable settings and real-time progress*

### Typing Demonstration
![Typing Demo](docs/images/typing-demo.gif)
*Realistic human typing with natural errors and corrections*

## 🎯 Use Cases

### 🧪 **Software Testing**
- Test web forms and input fields
- Validate text processing applications
- Simulate user input for automated testing
- Test typing-related features and performance

### 🎬 **Content Creation**
- Create realistic typing demonstrations for tutorials
- Generate typing videos for educational content
- Simulate user interaction in software demos
- Create engaging presentations with live typing effects

### 🔧 **Automation & Development**
- Add human-like delays to automation scripts
- Test applications with realistic user input patterns
- Simulate typing for quality assurance testing
- Create more believable automated workflows

### 🎓 **Education & Research**
- Demonstrate human-computer interaction concepts
- Study typing patterns and behaviors
- Create accessibility testing scenarios
- Research input method effectiveness

### 🌐 **Cross-Platform Compatibility**
Test applications across different platforms:
- **Windows**: Native keyboard simulation support
- **macOS**: Full compatibility with accessibility permissions
- **Linux**: Works with X11 and Wayland display servers

## 📥 Installation

### Option 1: Download Executable (Recommended)
1. Go to [Releases](https://github.com/yourusername/human-typer-mimicker/releases)
2. Download `HumanTyperGUI.exe`
3. Run directly - no installation required!

### Option 2: Install from Source
```bash
# Clone the repository
git clone https://github.com/yourusername/human-typer-mimicker.git
cd human-typer-mimicker

# Install dependencies
pip install -r requirements.txt

# Run the application
python human_typer_gui.py
```

### Option 3: Install via pip (Coming Soon)
```bash
pip install human-typer-mimicker
```

### System Requirements
- Python 3.6 or higher
- Windows, macOS, or Linux
- For keyboard simulation: `pynput` library

### Permissions
On some systems, you may need to grant accessibility permissions:
- **macOS**: Go to System Preferences → Security & Privacy → Privacy → Accessibility and add your terminal/Python
- **Linux**: May require running with appropriate permissions depending on your window manager

## 🚀 Quick Start

### Option 1: Download Executable (Easiest)
1. Go to [Releases](https://github.com/yourusername/human-typer/releases)
2. Download the executable for your platform
3. Run it directly - no installation needed!

### Option 2: Run from Source
```bash
# Clone the repository
git clone https://github.com/yourusername/human-typer.git
cd human-typer

# Install dependencies
pip install -r requirements.txt

# Run with automatic interface detection
python main.py

# Or force GUI mode
python main.py --gui

# Or force CLI mode
python main.py --cli
```

### F6 Hotkey Usage (Recommended)
1. **Start the application** (GUI or CLI)
2. **Enter your text** in the interface
3. **Click "Start Typing"** or run the command
4. **Switch to your target application** (text editor, browser, etc.)
5. **Press F6** when you're ready to start typing
6. **Press F6 again** to stop anytime

### GUI Application
```bash
# Run the cross-platform GUI
python main.py --gui
```

### Command Line Usage
```python
from src.human_typer import HumanTyper

# Create typer with F6 hotkey support
typer = HumanTyper()

# Configure settings
typer.set_speed(200)  # 200 characters per minute
typer.set_error_rate(0.08)  # 8% error rate

# Type text with F6 hotkey control (recommended)
typer.type_text("Hello, world! Press F6 to start typing.", use_hotkey=True)
```

### Console Mode (No Keyboard Simulation)
```python
# For testing without keyboard simulation
typer = HumanTyper(use_keyboard=False)
typer.type_text("This will be printed to console")
```

## 🎯 Usage Examples

### Basic Usage
```python
from human_typer import HumanTyper

typer = HumanTyper()
typer.type_text("Your text here")
```

### Advanced Configuration
```python
from human_typer import HumanTyper

# Create typer with custom settings
typer = HumanTyper(use_keyboard=True)

# Configure typing behavior
typer.set_speed(150)           # 150 characters per minute
typer.set_error_rate(0.12)     # 12% error rate
typer.set_correction_rate(0.7) # 70% of errors will be corrected

# Type with delay
typer.type_text("This text will be typed with human-like behavior", 
                delay_before_start=3.0)
```

### Console Mode (Testing)
```python
# For testing without keyboard simulation
typer = HumanTyper(use_keyboard=False)
typer.type_text("This will be printed to console for testing")
```

## ⚙️ Configuration Options

### Speed Settings
- `set_speed(cpm)`: Characters per minute (default: 180)
- Realistic range: 100-300 CPM
- Speed naturally fluctuates during typing

### Error Settings
- `set_error_rate(rate)`: Probability of making errors (0.0-1.0)
- `set_correction_rate(rate)`: Probability of correcting errors (0.0-1.0)
- Default error rate: 10%
- Default correction rate: 80%

### Timing Settings
- `delay_before_start`: Seconds to wait before starting
- `thinking_pause_chance`: Probability of natural pauses
- `thinking_pause_duration`: Duration of thinking pauses

## 🔧 Troubleshooting

### Common Issues

#### Permission Denied Errors
```
PermissionError: [Errno 13] Permission denied
```
**Solution**: Grant accessibility permissions to your terminal/Python application:
- **macOS**: System Preferences → Security & Privacy → Privacy → Accessibility
- **Linux**: Run with appropriate permissions or check your window manager settings
- **Windows**: Run as administrator if needed

#### Import Error: pynput
```
ModuleNotFoundError: No module named 'pynput'
```
**Solution**: Install pynput:
```bash
pip install pynput
```

#### GUI Not Responding
If the GUI becomes unresponsive during typing:
- The typing process is running in a separate thread
- Use the "Stop" button to cancel typing
- Close other applications that might interfere with keyboard simulation

#### Keyboard Simulation Not Working
If text appears in console instead of being typed:
- Check if `use_keyboard=True` is set
- Verify pynput installation
- Check system permissions
- Try running the application with elevated privileges

### Platform-Specific Notes

#### Windows
- No special permissions typically required
- Windows Defender might flag the executable (false positive)
- Use Windows Terminal or PowerShell for best experience

#### macOS
- Accessibility permissions required for keyboard simulation
- May need to add Python/Terminal to accessibility list
- Some applications may block simulated input

#### Linux
- X11 or Wayland support required
- May need to install additional dependencies: `sudo apt install python3-tk`
- Some desktop environments may require additional permissions

### Performance Tips
- Close unnecessary applications during typing simulation
- Use console mode for testing (`use_keyboard=False`)
- Adjust speed and error rates for better performance on slower systems
- For very long texts, consider breaking them into smaller chunks

### Customize Typing Speed
```python
typer = HumanTyper()
typer.set_speed(250)  # 250 characters per minute
typer.type_text("Faster typing example")
```

### Adjust Error Rates
```python
typer = HumanTyper()
typer.set_error_rate(0.15)      # 15% chance of errors
typer.set_correction_rate(0.80)  # 80% chance of correcting errors
typer.type_text("Text with more mistakes")
```

### Create Different Typing Personalities
```python
# Sloppy, fast typer
sloppy_typer = HumanTyper()
sloppy_typer.set_speed(350)
sloppy_typer.set_error_rate(0.20)
sloppy_typer.set_correction_rate(0.60)

# Careful, slow typer
careful_typer = HumanTyper()
careful_typer.set_speed(120)
careful_typer.set_error_rate(0.03)
careful_typer.set_correction_rate(0.95)
```

## Configuration Options

### Speed Settings
- **Base Speed**: 50-500 characters per minute (default: 200)
- **Speed Variance**: Natural fluctuation around base speed (default: 50)

### Error Settings
- **Typo Probability**: 0.0-1.0 (default: 0.08 = 8%)
- **Correction Probability**: 0.0-1.0 (default: 0.85 = 85%)
- **Double Character Probability**: 0.0-1.0 (default: 0.03 = 3%)
- **Character Swap Probability**: 0.0-1.0 (default: 0.02 = 2%)

### Behavior Settings
- **Pause Probability**: Chance of thinking pauses (default: 0.05 = 5%)
- **Keyboard Layout**: QWERTY layout for adjacent key errors

## Running the Demo

```bash
# Run the main demo
python human_typer.py

# Run usage examples
python examples.py
```

## How It Works

The Human Typer Mimicker uses several techniques to simulate realistic human typing:

1. **Keyboard Layout Mapping**: Uses a QWERTY keyboard layout map to determine which keys are adjacent for realistic typos
2. **Timing Variations**: Calculates realistic delays between keystrokes with natural variation
3. **Error Injection**: Randomly introduces different types of errors based on probability settings
4. **Correction Simulation**: Implements backspacing and retyping when errors are "noticed"
5. **Behavioral Patterns**: Adds thinking pauses and other natural human behaviors

## Error Types

### Adjacent Key Errors
Based on physical keyboard layout:
- 'q' might become 'w', 'a', or 's'
- 'hello' might become 'hwllo' (h is adjacent to g on keyboard)

### Character Transposition
Common human error of swapping adjacent characters:
- 'the' might become 'teh'
- 'typing' might become 'typnig'

### Double Characters
Accidentally pressing a key twice:
- 'hello' might become 'heello'
- 'world' might become 'worrld'

## Use Cases

- **Testing**: Test typing-related applications with realistic input patterns
- **Demonstrations**: Create engaging typing demonstrations for presentations
- **Automation**: Add human-like delays and errors to automation scripts
- **Education**: Teach about human-computer interaction patterns
- **Accessibility**: Simulate different typing abilities and speeds
- **Content Creation**: Generate realistic typing videos or GIFs
- **Quality Assurance**: Test how applications handle real-world typing patterns

## Practical Usage Tips

### For Any Application
1. Run your Python script with the human typer
2. When prompted, switch to your target application (text editor, web form, etc.)
3. The script will wait a few seconds, then start typing
4. The final text will exactly match what you specified

### Best Practices
- **Use adequate delays**: Give yourself 3-5 seconds to switch applications
- **Test settings first**: Start with default settings, then adjust as needed
- **Consider context**: Use slower, more careful settings for important text
- **Monitor corrections**: Watch how realistic the error correction patterns look
- **Application compatibility**: Works with any app that accepts keyboard input

### Example Applications
- **Word processors**: Microsoft Word, Google Docs, Notepad
- **Code editors**: VS Code, Sublime Text, Vim
- **Web forms**: Contact forms, comments, social media posts
- **Chat applications**: Discord, Slack, Teams
- **Terminals**: Command line interfaces, SSH sessions

## Contributing

Feel free to contribute improvements, bug fixes, or new features:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📚 Documentation

### For Users
- **[User Guide](docs/USER_GUIDE.md)**: Complete manual with step-by-step tutorials
- **[Troubleshooting](#-troubleshooting)**: Common issues and solutions (above)

### For Developers
- **[API Documentation](docs/API.md)**: Complete API reference and examples
- **[Development Guide](docs/DEVELOPMENT.md)**: Setup, architecture, and contribution info
- **[Project Structure](docs/PROJECT_STRUCTURE.md)**: Detailed project organization

### Project Info
- **[Contributing Guidelines](CONTRIBUTING.md)**: How to contribute to the project
- **[Changelog](CHANGELOG.md)**: Version history and release notes
- **[License](LICENSE)**: MIT License details

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details on how to:
- Report bugs
- Suggest features
- Submit pull requests
- Set up the development environment

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🗺️ Roadmap

### Planned Features
- [ ] Support for different keyboard layouts (Dvorak, Colemak, etc.)
- [ ] Fatigue simulation (slower typing over time)
- [ ] Punctuation-specific behaviors
- [ ] Word-level error patterns
- [ ] Typing rhythm analysis
- [ ] Mobile keyboard simulation
- [ ] Multi-language support
- [ ] Custom error pattern configuration
- [ ] Typing statistics and analytics

### Version History
See [CHANGELOG.md](CHANGELOG.md) for detailed version history.

## 🙏 Acknowledgments

- Built with Python and the powerful [pynput](https://github.com/moses-palmer/pynput) library
- Inspired by real human typing behavior research
- Special thanks to the Python community for excellent tools and documentation

## 📊 Project Stats

![Lines of Code](https://img.shields.io/tokei/lines/github/yourusername/human-typer)
![Code Size](https://img.shields.io/github/languages/code-size/yourusername/human-typer)
![Repository Size](https://img.shields.io/github/repo-size/yourusername/human-typer)

---

## Building Executable

To build your own executable:

### Windows
```bash
# Install PyInstaller
pip install pyinstaller

# Build executable
pyinstaller --onefile --windowed --name "HumanTyperGUI" --add-data "human_typer.py;." human_typer_gui.py
```

Or simply run the provided batch file:
```bash
build_gui.bat
```

### Alternative Build Methods
```bash
# Using the Python build script
python build_exe.py

# Manual PyInstaller command
python -m PyInstaller --onefile --windowed --name "HumanTyperGUI" --add-data "human_typer.py;." human_typer_gui.py
```

The executable will be created in the `dist` folder as `HumanTyperGUI.exe`.

---

**Note**: This tool is designed for educational and testing purposes. Please use responsibly and in accordance with any applicable terms of service when using with other applications.
