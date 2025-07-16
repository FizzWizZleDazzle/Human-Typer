#!/bin/bash
# Cross-Platform Build Script for Human Typer Mimicker
# Works on macOS and Linux

set -e

echo "======================================"
echo "Human Typer - Cross-Platform Builder"
echo "======================================"

# Detect platform
if [[ "$OSTYPE" == "darwin"* ]]; then
    PLATFORM="macOS"
    ARCH=$(uname -m)
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    PLATFORM="Linux"
    ARCH=$(uname -m)
else
    echo "Unsupported platform: $OSTYPE"
    exit 1
fi

echo "Platform: $PLATFORM $ARCH"
echo "Python: $(python3 --version)"
echo ""

# Install dependencies
echo "Installing dependencies..."
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

# Clean build directories
echo "Cleaning build directories..."
rm -rf build dist __pycache__ src/__pycache__

# Build GUI application
echo "Building GUI application..."
python3 -m PyInstaller \
    --onefile \
    --windowed \
    --name "HumanTyperGUI-$PLATFORM" \
    --add-data "src:src" \
    --distpath dist \
    --workpath build \
    src/human_typer_gui.py

# Build CLI application
echo "Building CLI application..."
python3 -m PyInstaller \
    --onefile \
    --console \
    --name "HumanTyper-$PLATFORM" \
    --distpath dist \
    --workpath build \
    src/human_typer.py

# Create distribution package
DIST_NAME="HumanTyper-$PLATFORM-$ARCH"
DIST_DIR="dist/$DIST_NAME"

echo "Creating distribution package..."
mkdir -p "$DIST_DIR"

# Copy executables
cp dist/HumanTyperGUI-$PLATFORM "$DIST_DIR/"
cp dist/HumanTyper-$PLATFORM "$DIST_DIR/"

# Copy documentation
cp README.md LICENSE CHANGELOG.md "$DIST_DIR/" 2>/dev/null || true
cp scripts/examples.py "$DIST_DIR/examples.py" 2>/dev/null || true

# Make executables... executable
chmod +x "$DIST_DIR"/*

echo ""
echo "======================================"
echo "Build completed successfully!"
echo "======================================"
echo "Distribution: $DIST_DIR"
echo "Executables:"
ls -la "$DIST_DIR"
echo ""
echo "To run:"
echo "  GUI: ./$DIST_DIR/HumanTyperGUI-$PLATFORM"
echo "  CLI: ./$DIST_DIR/HumanTyper-$PLATFORM"
