# Yet-Another-Kicad-Library-Merger

the following tutorial was made by ChatGPT (will rewrite later)

# KiCad Library Merger – Linux AppImage Build Guide

This project is a Python Tkinter script that merges KiCad symbol libraries. This guide explains how to turn the script into a standalone `.AppImage` for Linux.

---

## Requirements

- Python 3
- `pip`
- `wget` (for downloading AppImage creation tool)
- Linux environment

---

## Steps to Build

### 1. Install Required Tools

Install PyInstaller:

```bash
pip install pyinstaller
```

Download the AppImage creation tool:

```bash
wget "https://github.com/AppImage/AppImageKit/releases/download/continuous/appimagetool-x86_64.AppImage"
chmod +x appimagetool-x86_64.AppImage
```

---

### 2. Use PyInstaller to Create a Linux Executable

From your script’s directory, run:

```bash
pyinstaller --onefile --windowed your_script.py
```

- `--onefile` → bundles everything into a single executable  
- `--windowed` → hides the terminal for GUI apps  

After building, the executable will be located in:

```
dist/your_script
```

Test it:

```bash
./dist/your_script
```

If the GUI works, continue to creating the AppImage.

---

### 3. Create the AppDir Structure

AppImage requires a specific directory structure:

```
AppDir/
├── AppRun
├── your_script         # PyInstaller executable
├── icon.png
└── your_script.desktop
```

Create `AppRun` as a shell script:

```bash
#!/bin/bash
HERE="$(dirname "$(readlink -f "${0}")")"
"$HERE/your_script"
```

Make it executable:

```bash
chmod +x AppDir/AppRun
```

---

### 4. Create a `.desktop` File

Example: `AppDir/your_script.desktop`

```ini
[Desktop Entry]
Name=KiCad Library Merger
Comment=Merge KiCad libraries easily
Exec=your_script
Icon=icon
Type=Application
Categories=Utility;
```

- Place your icon (PNG or SVG) in `AppDir/icon.png`.

---

### 5. Build the AppImage

Run:

```bash
./appimagetool-x86_64.AppImage AppDir
```

It will produce an AppImage file like:

```
KiCad_Library_Merger-x86_64.AppImage
```

Double-click it to run your app.

---

## Optional Tips

- Test on a clean Linux VM to ensure all dependencies are included.
- PyInstaller bundles Python, so users do not need Python installed.
- Customize the icon and desktop entry as needed.
