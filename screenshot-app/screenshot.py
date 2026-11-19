from datetime import datetime
import os
from pathlib import Path
import platform
import subprocess
import time
import tkinter as tk
from tkinter import ttk
import darkdetect
import pyautogui
import sv_ttk

SAVE_DIR = Path.home() / "Pictures" / "Screenshots_Data"
SAVE_DIR.mkdir(parents=True, exist_ok=True)


def open_path(target_path: Path):
    """Opens a file or folder in the OS default application."""
    system = platform.system()
    if system == "Windows":
        os.startfile(target_path)
    elif system == "Darwin":  # macOS
        subprocess.Popen(["open", str(target_path)])
    else:  # Linux
        subprocess.Popen(["xdg-open", str(target_path)])


def take_screenshot():
    root.withdraw()
    root.update()
    time.sleep(0.2)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S_%f")[:-3]
    filepath = SAVE_DIR / f"screenshot_{timestamp}.png"

    pyautogui.screenshot(str(filepath))

    root.deiconify()
    open_path(SAVE_DIR)
    open_path(filepath)


# GUI Setup
root = tk.Tk()
root.title("Screenshot Tool")
root.attributes("-topmost", True)
root.resizable(False, False)  # Keeps the floating toolbar compact and neat

# Use ttk.Frame and ttk.Button instead of tk.* so the theme applies
frame = ttk.Frame(root, padding=12)
frame.pack()

# "Accent.TButton" highlights the primary action button in your theme's accent color
capture_btn = ttk.Button(
    frame,
    text="Take Screenshot",
    style="Accent.TButton",
    command=take_screenshot,
)
capture_btn.pack(side=tk.LEFT, padx=(0, 6))

folder_btn = ttk.Button(frame, text="Open Folder", command=lambda: open_path(SAVE_DIR))
folder_btn.pack(side=tk.LEFT, padx=6)

close_btn = ttk.Button(frame, text="Quit", command=root.destroy)
close_btn.pack(side=tk.LEFT, padx=(6, 0))

# Automatically match your system's current Light or Dark theme
current_theme = darkdetect.theme() or "dark"
sv_ttk.set_theme(current_theme.lower())

root.mainloop()
