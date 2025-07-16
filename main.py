#!/usr/bin/env python3
"""
Human Typer Mimicker - Main Entry Point

This is the main entry point for the Human Typer application.
It automatically detects the best interface to use (GUI or CLI).
"""

import sys

try:
    import tkinter
    GUI_AVAILABLE = True
except ImportError:
    GUI_AVAILABLE = False

from src.human_typer import PYNPUT_AVAILABLE


def main():
    """Main entry point - choose the best interface."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Human Typer Mimicker - Realistic typing simulation')
    parser.add_argument('--cli', action='store_true', help='Force CLI mode')
    parser.add_argument('--gui', action='store_true', help='Force GUI mode')
    parser.add_argument('--text', type=str, help='Text to type (CLI mode only)')
    parser.add_argument('--speed', type=int, default=200, help='Typing speed in CPM')
    parser.add_argument('--error-rate', type=float, default=0.08, help='Error rate (0.0-1.0)')
    parser.add_argument('--no-keyboard', action='store_true', help='Disable keyboard simulation')
    
    args = parser.parse_args()
    
    # Determine which interface to use
    use_gui = False
    use_cli = False
    
    if args.gui and not args.cli:
        use_gui = True
    elif args.cli and not args.gui:
        use_cli = True
    elif args.text:  # Text provided, use CLI
        use_cli = True
    elif GUI_AVAILABLE:  # Default to GUI if available
        use_gui = True
    else:  # Fallback to CLI
        use_cli = True
    
    # Launch appropriate interface
    if use_gui and GUI_AVAILABLE:
        print("Launching GUI interface...")
        from src.human_typer_gui import main as gui_main
        gui_main()
    else:
        if use_gui and not GUI_AVAILABLE:
            print("GUI not available (tkinter not found). Using CLI mode.")
        
        print("Launching CLI interface...")
        from src.human_typer import HumanTyper
        
        # Create typer
        use_keyboard = not args.no_keyboard
        typer = HumanTyper(use_keyboard=use_keyboard)
        
        # Configure settings
        typer.set_speed(args.speed)
        typer.set_error_rate(args.error_rate)
        
        if args.text:
            # Type provided text
            print(f"Typing: {args.text[:50]}{'...' if len(args.text) > 50 else ''}")
            typer.type_text(args.text, use_hotkey=use_keyboard, show_progress=True)
        else:
            # Run interactive demo
            from src.human_typer import main as cli_main
            cli_main()


if __name__ == '__main__':
    main()
