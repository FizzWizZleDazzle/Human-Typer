"""
Human Typer Mimicker - Usage Examples

This file demonstrates various ways to use the HumanTyper class
for realistic keyboard simulation.
"""

from human_typer import HumanTyper
import time


def basic_example():
    """Basic usage example."""
    print("=== Basic Example ===")
    print("This will type a simple message with default settings.")
    
    typer = HumanTyper()
    text = "Hello! This is a basic typing example with realistic human behavior."
    
    input("Press Enter when ready (switch to target app after pressing Enter)...")
    typer.type_text(text, delay_before_start=3.0)


def custom_settings_example():
    """Example with customized typing behavior."""
    print("\n=== Custom Settings Example ===")
    print("This example uses faster typing with more errors.")
    
    typer = HumanTyper()
    
    # Customize the typing behavior
    typer.set_speed(300)  # Fast typing - 300 CPM
    typer.set_error_rate(0.12)  # Higher error rate (12%)
    typer.set_correction_rate(0.90)  # High correction rate (90%)
    
    text = "This text will be typed faster with more mistakes and corrections to demonstrate realistic human typing patterns."
    
    input("Press Enter when ready for fast typing with errors...")
    typer.type_text(text, delay_before_start=3.0)


def slow_careful_typing_example():
    """Example of slow, careful typing with fewer errors."""
    print("\n=== Slow & Careful Typing Example ===")
    print("This example simulates careful, deliberate typing.")
    
    typer = HumanTyper()
    
    # Configure for slow, careful typing
    typer.set_speed(120)  # Slow typing - 120 CPM
    typer.set_error_rate(0.03)  # Low error rate (3%)
    typer.set_correction_rate(0.95)  # Very high correction rate
    
    text = "This message will be typed slowly and carefully, with minimal errors, like someone being very deliberate."
    
    input("Press Enter when ready for slow, careful typing...")
    typer.type_text(text, delay_before_start=3.0)


def programming_code_example():
    """Example of typing programming code."""
    print("\n=== Programming Code Example ===")
    print("This example types Python code with appropriate care.")
    
    typer = HumanTyper()
    
    # Configure for code typing (slower, more careful)
    typer.set_speed(150)  # Moderate speed for code
    typer.set_error_rate(0.05)  # Lower error rate for code
    typer.set_correction_rate(0.98)  # Very high correction rate for code
    
    code = '''def calculate_fibonacci(n):
    """Calculate the nth Fibonacci number."""
    if n <= 1:
        return n
    return calculate_fibonacci(n-1) + calculate_fibonacci(n-2)'''
    
    input("Press Enter when ready to type Python code...")
    typer.type_text(code, delay_before_start=3.0)


def long_text_example():
    """Example with longer text to show sustained typing patterns."""
    print("\n=== Long Text Example ===")
    print("This example types a longer paragraph to demonstrate sustained patterns.")
    
    typer = HumanTyper()
    typer.set_speed(200)  # Normal speed
    typer.set_error_rate(0.08)  # Normal error rate
    
    text = """Human typing simulation is a fascinating area that combines psychology, 
motor skills research, and computer science. When we type, we don't just press keys 
in perfect sequence - we make mistakes, correct them, have slight variations in 
timing, and occasionally pause to think. This human typer mimicker captures these 
natural patterns to create realistic typing behavior that can be used for testing, 
automation, or demonstration purposes. The key is balancing realism with accuracy."""
    
    input("Press Enter when ready for long text typing...")
    typer.type_text(text, delay_before_start=3.0)


def interactive_custom_text():
    """Let the user input custom text to type."""
    print("\n=== Custom Text Example ===")
    print("Enter your own text to be typed with human-like behavior.")
    
    custom_text = input("Enter the text you want to type: ").strip()
    
    if not custom_text:
        print("No text entered. Skipping this example.")
        return
    
    typer = HumanTyper()
    
    # Let user customize settings
    try:
        speed = int(input(f"Typing speed in CPM (50-500, default=200): ") or "200")
        error_rate = float(input("Error rate (0.0-1.0, default=0.08): ") or "0.08")
        typer.set_speed(speed)
        typer.set_error_rate(error_rate)
    except ValueError:
        print("Using default settings...")
    
    print(f"\nWill type: '{custom_text[:50]}{'...' if len(custom_text) > 50 else ''}'")
    input("Press Enter when ready (switch to target app after pressing Enter)...")
    typer.type_text(custom_text, delay_before_start=3.0)


def main():
    """Run all examples."""
    print("Human Typer Mimicker - Examples")
    print("=" * 40)
    print()
    print("This script demonstrates various uses of the HumanTyper class.")
    print("Each example will give you time to switch to your target application.")
    print()
    print("Examples available:")
    print("1. Basic Example")
    print("2. Custom Settings (Fast + More Errors)")
    print("3. Slow & Careful Typing")
    print("4. Programming Code")
    print("5. Long Text")
    print("6. Custom Text (Interactive)")
    print()
    
    # Check if keyboard simulation is available
    from human_typer import PYNPUT_AVAILABLE
    if not PYNPUT_AVAILABLE:
        print("WARNING: pynput not installed!")
        print("Install with: pip install pynput")
        print("Examples will run in console simulation mode.")
        print()
    
    try:
        # Run examples
        basic_example()
        custom_settings_example()
        slow_careful_typing_example()
        programming_code_example()
        long_text_example()
        interactive_custom_text()
        
        print("\n" + "=" * 40)
        print("All examples completed!")
        print("\nTips for using HumanTyper:")
        print("- Use delay_before_start to give yourself time to switch apps")
        print("- Adjust speed and error rates for different scenarios")
        print("- The final text will always match your input exactly")
        print("- Works in any application that accepts keyboard input")
        
    except KeyboardInterrupt:
        print("\n\nExamples interrupted by user.")
    except Exception as e:
        print(f"\nError occurred: {e}")


if __name__ == "__main__":
    main()
