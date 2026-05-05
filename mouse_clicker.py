import time
import threading
import argparse
from datetime import datetime
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, Key

class MouseClicker(threading.Thread):
    def __init__(self, interval):
        super(MouseClicker, self).__init__()
        self.interval = interval
        self.mouse = Controller()
        self.running = False
        self.daemon = True  # Ensures thread dies when main process exits

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def run(self):
        while True:
            if self.running:
                self.mouse.click(Button.left, 1)
                timestamp = datetime.now().strftime("%H:%M:%S")
                print(f"[{timestamp}] Click performed!")
                time.sleep(self.interval)
            else:
                time.sleep(0.1)

def on_press(key, clicker):
    if key == Key.esc:
        print("\n[Esc] pressed. Stopping clicker...")
        clicker.stop_clicking()
        return False  # Stops the listener

def main():
    parser = argparse.ArgumentParser(description="Periodic Mouse Clicker")
    parser.add_argument(
        "--interval", 
        type=float, 
        default=1.0, 
        help="Interval between clicks in seconds (default: 1.0)"
    )
    args = parser.parse_args()

    print("--- Mouse Clicker Started ---")
    print(f"Interval: {args.interval} seconds")
    print("Press [Esc] to stop.")
    print("Closing this terminal will also stop the clicker.")
    print("-----------------------------")

    clicker = MouseClicker(args.interval)
    clicker.start_clicking()
    clicker.start()

    # Collect events until released
    with Listener(on_press=lambda k: on_press(k, clicker)) as listener:
        listener.join()

if __name__ == "__main__":
    main()
