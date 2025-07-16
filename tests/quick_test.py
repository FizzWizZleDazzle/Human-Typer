#!/usr/bin/env python3
"""
Quick Test Script for Human Typer

Run this script to quickly test the human typer with a simple message.
"""

from human_typer import HumanTyper, PYNPUT_AVAILABLE

def main():
    print("Human Typer - Quick Test")
    print("=" * 30)
    
    if not PYNPUT_AVAILABLE:
        print("WARNING: pynput not installed!")
        print("Install with: pip install pynput")
        print("Running in console mode only.")
        print()
    
    # Get custom text or use default
    text = input("Enter text to type (or press Enter for default): ").strip()
    if not text:
        text = "This is a quick test of the Human Typer! It will simulate realistic human typing with occasional mistakes and corrections."
    
    # Get typing speed
    try:
        speed_input = input("Typing speed in CPM (default=200): ").strip()
        speed = int(speed_input) if speed_input else 200
    except ValueError:
        speed = 200
    
    # Get error rate
    try:
        error_input = input("Error rate 0-100% (default=8): ").strip()
        error_rate = float(error_input) / 100 if error_input else 0.08
    except ValueError:
        error_rate = 0.08
    
    # Create and configure typer
    typer = HumanTyper()
    typer.set_speed(speed)
    typer.set_error_rate(error_rate)
    
    print(f"\nConfiguration:")
    print(f"- Text: '{text[:50]}{'...' if len(text) > 50 else ''}'")
    print(f"- Speed: {speed} CPM")
    print(f"- Error rate: {error_rate*100:.1f}%")
    print(f"- Keyboard simulation: {PYNPUT_AVAILABLE}")
    
    if PYNPUT_AVAILABLE:
        print(f"\nYou have 5 seconds to switch to your target application...")
        input("Press Enter when ready...")
        typer.type_text(text, delay_before_start=5.0)
    else:
        input("\nPress Enter to simulate typing in console...")
        typer.type_text(text, delay_before_start=0.0)
    
    print("\nTest completed!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nTest cancelled by user.")
    except Exception as e:
        print(f"\nError: {e}")
