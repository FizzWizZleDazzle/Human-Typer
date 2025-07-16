#!/usr/bin/env python3
"""
Cross-Platform Build Script for Human Typer Mimicker

This script builds the Human Typer application for multiple platforms.
Supports Windows, macOS, and Linux.
"""

import os
import sys
import platform
import subprocess
import shutil
from pathlib import Path


def get_platform_info():
    """Get platform-specific information."""
    system = platform.system()
    return {
        'system': system,
        'architecture': platform.machine(),
        'python_version': platform.python_version(),
        'is_windows': system == 'Windows',
        'is_macos': system == 'Darwin',
        'is_linux': system == 'Linux'
    }


def install_dependencies():
    """Install required dependencies."""
    print("Installing dependencies...")
    
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
        print("OK Installed dependencies from requirements.txt")
        return True
    except subprocess.CalledProcessError as e:
        print(f"ERROR Failed to install dependencies: {e}")
        return False


def clean_build_dirs():
    """Clean previous build directories."""
    print("Cleaning build directories...")
    
    dirs_to_clean = ['build', 'dist', '__pycache__']
    for dir_name in dirs_to_clean:
        if os.path.exists(dir_name):
            shutil.rmtree(dir_name)
            print(f"OK Removed {dir_name}")


def build_gui_executable(platform_info):
    """Build the GUI executable."""
    print("Building GUI executable...")
    
    # Platform-specific executable name
    if platform_info['is_windows']:
        exe_name = "HumanTyperGUI.exe"
        icon_option = []  # Add icon later if available
    elif platform_info['is_macos']:
        exe_name = "HumanTyperGUI.app"
        icon_option = []  # Add icon later if available
    else:  # Linux
        exe_name = "HumanTyperGUI"
        icon_option = []
    
    # Build command
    build_cmd = [
        sys.executable, '-m', 'PyInstaller',
        '--onefile',
        '--windowed',
        '--name', f'HumanTyperGUI-{platform_info["system"]}',
        '--add-data', f'src{os.pathsep}src',
        '--distpath', 'dist',
        '--workpath', 'build',
        'src/human_typer_gui.py'
    ]
    
    # Add platform-specific options
    if platform_info['is_macos']:
        build_cmd.extend(['--osx-bundle-identifier', 'com.humantyper.app'])
    
    try:
        subprocess.check_call(build_cmd)
        print(f"OK Built GUI executable: {exe_name}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"ERROR Failed to build GUI executable: {e}")
        return False


def build_cli_executable(platform_info):
    """Build the CLI executable."""
    print("Building CLI executable...")
    
    # Platform-specific executable name
    if platform_info['is_windows']:
        exe_name = "HumanTyper.exe"
    else:
        exe_name = "HumanTyper"
    
    # Build command
    build_cmd = [
        sys.executable, '-m', 'PyInstaller',
        '--onefile',
        '--console',
        '--name', f'HumanTyper-{platform_info["system"]}',
        '--distpath', 'dist',
        '--workpath', 'build',
        'src/human_typer.py'
    ]
    
    try:
        subprocess.check_call(build_cmd)
        print(f"OK Built CLI executable: {exe_name}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"ERROR Failed to build CLI executable: {e}")
        return False


def create_distribution_package(platform_info):
    """Create a distribution package."""
    print("Creating distribution package...")
    
    dist_name = f"HumanTyper-{platform_info['system']}-{platform_info['architecture']}"
    dist_dir = f"dist/{dist_name}"
    
    # Create distribution directory
    os.makedirs(dist_dir, exist_ok=True)
    
    # Copy executables
    for file in os.listdir('dist'):
        if file.startswith('HumanTyper') and not os.path.isdir(f'dist/{file}'):
            shutil.copy(f'dist/{file}', f'{dist_dir}/{file}')
    
    # Copy documentation
    docs_to_copy = ['README.md', 'LICENSE', 'CHANGELOG.md']
    for doc in docs_to_copy:
        if os.path.exists(doc):
            shutil.copy(doc, f'{dist_dir}/{doc}')
    
    # Copy examples
    if os.path.exists('scripts/examples.py'):
        shutil.copy('scripts/examples.py', f'{dist_dir}/examples.py')
    
    print(f"OK Created distribution package: {dist_dir}")
    return dist_dir


def main():
    """Main build process."""
    print("=" * 60)
    print("Human Typer Mimicker - Cross-Platform Build Script")
    print("=" * 60)
    
    # Get platform information
    platform_info = get_platform_info()
    print(f"Platform: {platform_info['system']} {platform_info['architecture']}")
    print(f"Python: {platform_info['python_version']}")
    print()
    
    # Install dependencies
    if not install_dependencies():
        print("Failed to install dependencies. Exiting.")
        sys.exit(1)
    
    print()
    
    # Clean build directories
    clean_build_dirs()
    print()
    
    # Build executables
    gui_success = build_gui_executable(platform_info)
    cli_success = build_cli_executable(platform_info)
    
    if not gui_success and not cli_success:
        print("All builds failed. Exiting.")
        sys.exit(1)
    
    print()
    
    # Create distribution package
    dist_dir = create_distribution_package(platform_info)
    
    print()
    print("=" * 60)
    print("Build Summary")
    print("=" * 60)
    print(f"Platform: {platform_info['system']} {platform_info['architecture']}")
    print(f"GUI Build: {'SUCCESS' if gui_success else 'FAILED'}")
    print(f"CLI Build: {'SUCCESS' if cli_success else 'FAILED'}")
    print(f"Distribution: {dist_dir}")
    print()
    
    if gui_success or cli_success:
        print("Build completed successfully!")
        print(f"Check the '{dist_dir}' directory for your executables.")
    else:
        print("Build failed. Check the error messages above.")
        sys.exit(1)


if __name__ == "__main__":
    main()
