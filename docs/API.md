# API Documentation

## HumanTyper Class

The main class for simulating human typing behavior.

### Constructor

```python
HumanTyper(use_keyboard=True)
```

**Parameters:**
- `use_keyboard` (bool): Whether to use keyboard simulation. If False, text is printed to console.

**Example:**
```python
# With keyboard simulation
typer = HumanTyper()

# Console mode only
typer = HumanTyper(use_keyboard=False)
```

### Methods

#### `set_speed(characters_per_minute: int) -> None`

Set the base typing speed.

**Parameters:**
- `characters_per_minute` (int): Base typing speed (realistic range: 100-300)

**Example:**
```python
typer.set_speed(200)  # 200 characters per minute
```

#### `set_error_rate(rate: float) -> None`

Set the probability of making typing errors.

**Parameters:**
- `rate` (float): Error probability (0.0 to 1.0, where 0.1 = 10% error rate)

**Example:**
```python
typer.set_error_rate(0.08)  # 8% error rate
```

#### `set_correction_rate(rate: float) -> None`

Set the probability of correcting errors when they occur.

**Parameters:**
- `rate` (float): Correction probability (0.0 to 1.0, where 0.8 = 80% correction rate)

**Example:**
```python
typer.set_correction_rate(0.7)  # 70% of errors will be corrected
```

#### `type_text(text: str, delay_before_start: float = 0.0) -> None`

Type the given text with human-like behavior.

**Parameters:**
- `text` (str): The text to type
- `delay_before_start` (float): Seconds to wait before starting typing

**Example:**
```python
typer.type_text("Hello, world!", delay_before_start=3.0)
```

#### `get_current_settings() -> dict`

Get the current configuration settings.

**Returns:**
- `dict`: Current settings including speed, error rate, and correction rate

**Example:**
```python
settings = typer.get_current_settings()
print(f"Speed: {settings['speed']} CPM")
print(f"Error Rate: {settings['error_rate']*100}%")
```

## HumanTyperGUI Class

The graphical user interface for the Human Typer application.

### Constructor

```python
HumanTyperGUI()
```

Creates and initializes the GUI application.

**Example:**
```python
app = HumanTyperGUI()
app.run()
```

### Methods

#### `run() -> None`

Start the GUI application main loop.

**Example:**
```python
app = HumanTyperGUI()
app.run()
```

#### `load_sample_text(text_name: str) -> None`

Load a predefined sample text into the text area.

**Parameters:**
- `text_name` (str): Name of the sample text to load

**Available Sample Texts:**
- "Lorem Ipsum"
- "The Quick Brown Fox"
- "Programming Text"
- "Typing Test"

## Configuration Examples

### Basic Configuration
```python
from human_typer import HumanTyper

# Create typer with default settings
typer = HumanTyper()

# Type a simple message
typer.type_text("Hello, this is a test message.")
```

### Advanced Configuration
```python
from human_typer import HumanTyper

# Create typer with custom settings
typer = HumanTyper(use_keyboard=True)

# Configure behavior
typer.set_speed(150)           # Slower typing (150 CPM)
typer.set_error_rate(0.15)     # Higher error rate (15%)
typer.set_correction_rate(0.6) # Lower correction rate (60%)

# Type with delay
typer.type_text(
    "This text will be typed with custom settings and errors.",
    delay_before_start=5.0
)
```

### Console Mode (for Testing)
```python
from human_typer import HumanTyper

# Disable keyboard simulation for testing
typer = HumanTyper(use_keyboard=False)

# Set fast speed for quick testing
typer.set_speed(500)
typer.set_error_rate(0.2)

# Text will be printed to console with simulated timing
typer.type_text("This appears in the console with typing simulation.")
```

## Error Types

The Human Typer simulates several types of common typing errors:

### Adjacent Key Errors
Mistakes on keys that are physically close on the QWERTY keyboard.

**Example:**
- Typing 'r' instead of 't'
- Typing 'n' instead of 'm'

### Character Transposition
Swapping adjacent characters, a common human error.

**Example:**
- "the" becomes "teh"
- "form" becomes "from"

### Double Character Typing
Accidentally typing the same character twice.

**Example:**
- "hello" becomes "helllo"
- "test" becomes "tesst"

## Timing Behavior

### Speed Variation
The actual typing speed varies naturally around the base speed:
- Random variation factor: 0.5x to 1.5x base speed
- Natural fluctuations during typing
- Slower typing for complex characters

### Thinking Pauses
Natural pauses that occur during human typing:
- Random chance of occurrence
- Variable duration (0.5 to 2.0 seconds)
- More likely at punctuation and word boundaries

### Error Correction Timing
Realistic timing for error detection and correction:
- Delay before noticing error (0.2 to 0.8 seconds)
- Natural backspacing rhythm
- Slight pause before retyping corrected text

## Platform Considerations

### Windows
- No special permissions typically required
- Full keyboard simulation support
- Compatible with all applications

### macOS
- Requires accessibility permissions
- May need to add Python/Terminal to accessibility list
- Some applications may block simulated input

### Linux
- X11 or Wayland support required
- May need additional permissions
- Desktop environment compatibility varies

## Best Practices

### Performance Optimization
```python
# For long texts, consider breaking into chunks
long_text = "..." # Very long text
chunks = [long_text[i:i+100] for i in range(0, len(long_text), 100)]

for chunk in chunks:
    typer.type_text(chunk)
    time.sleep(1)  # Brief pause between chunks
```

### Error Handling
```python
try:
    typer = HumanTyper(use_keyboard=True)
    typer.type_text("Test message")
except Exception as e:
    print(f"Keyboard simulation failed: {e}")
    # Fallback to console mode
    typer = HumanTyper(use_keyboard=False)
    typer.type_text("Test message")
```

### Realistic Settings
```python
# Realistic human typing speeds and error rates
beginner_typer = HumanTyper()
beginner_typer.set_speed(120)      # 120 CPM
beginner_typer.set_error_rate(0.15) # 15% errors
beginner_typer.set_correction_rate(0.9) # 90% corrections

experienced_typer = HumanTyper()
experienced_typer.set_speed(250)    # 250 CPM
experienced_typer.set_error_rate(0.05) # 5% errors
experienced_typer.set_correction_rate(0.95) # 95% corrections
```

## Troubleshooting

### Common Issues and Solutions

#### "Module not found" errors
```python
# Ensure pynput is installed
import sys
import subprocess
subprocess.check_call([sys.executable, "-m", "pip", "install", "pynput"])
```

#### Keyboard simulation not working
```python
# Test if keyboard simulation is available
try:
    from pynput.keyboard import Key, Controller
    keyboard = Controller()
    print("Keyboard simulation available")
except Exception as e:
    print(f"Keyboard simulation unavailable: {e}")
    # Use console mode instead
    typer = HumanTyper(use_keyboard=False)
```

#### GUI not responding
```python
# Ensure typing runs in separate thread (automatically handled in GUI)
import threading

def type_in_background():
    typer.type_text("Background typing")

thread = threading.Thread(target=type_in_background)
thread.daemon = True
thread.start()
```
