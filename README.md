# 🖱️ Mouse Clicker Bot

A simple, periodic mouse clicker for Windows with a global emergency stop.

## 🚀 Quick Start

1.  **Install Dependencies**:
    Open a terminal in this folder and run:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Start Clicking**:
    Double-click **`start_clicker.bat`**.
    *By default, it clicks every 1 second.*

3.  **Stop Clicking**:
    *   Press the **`Esc`** key at any time (even if you are in another window).
    *   **OR** Close the terminal window.
    *   **OR** Double-click **`stop_clicker.bat`** for a forced emergency stop.

## 🛠️ Advanced Usage

If you want to change the click interval, you can run the script manually from the terminal:

```bash
# Click every 5 seconds
python mouse_clicker.py --interval 5.0

# Click very fast (every 0.1 seconds)
python mouse_clicker.py --interval 0.1
```

## 📂 File Structure

*   `mouse_clicker.py`: The main Python script.
*   `start_clicker.bat`: Quick-start shortcut (1s interval).
*   `stop_clicker.bat`: Emergency "Kill Switch" to stop all clicker processes.
*   `requirements.txt`: Required Python libraries (`pynput`).

## ⚠️ Safety Notes
- Be careful where you leave your mouse cursor! The bot will click wherever the mouse is positioned.
- The `stop_clicker.bat` is your best friend if the computer becomes hard to control due to fast clicking.
