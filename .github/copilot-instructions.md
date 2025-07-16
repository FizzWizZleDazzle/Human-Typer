<!-- Use this file to provide workspace-specific custom instructions to Copilot. For more details, visit https://code.visualstudio.com/docs/copilot/copilot-customization#_use-a-githubcopilotinstructionsmd-file -->

# Human Typer Mimicker Project Instructions

This is a Python project that simulates realistic human typing behavior with the following features:

## Key Features
- **Realistic Typing Speed**: Variable typing speed with natural fluctuations
- **Adjacent Key Errors**: Mistakes on keys that are physically close on the keyboard
- **Character Transposition**: Swapping adjacent characters (common human error)
- **Double Character Typing**: Accidentally typing the same character twice
- **Error Correction**: Realistic backspacing and correction behavior
- **Thinking Pauses**: Natural pauses that occur during human typing

## Code Guidelines
- Use type hints for better code clarity
- Follow PEP 8 style guidelines
- Include docstrings for all classes and methods
- Use meaningful variable names that describe the typing behavior
- Keep the keyboard layout mapping accurate to QWERTY layout
- Ensure timing calculations are realistic (based on actual human typing speeds)

## Testing Considerations
- Test with various text lengths and complexity
- Verify that error rates are realistic (not too high or too low)
- Ensure corrections don't create infinite loops
- Test edge cases like single characters, empty strings, and special characters

## Performance Notes
- Use `time.sleep()` for realistic timing delays
- Flush output immediately for real-time typing effect
- Consider memory usage when processing very long texts
