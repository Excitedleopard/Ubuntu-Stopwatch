import tkinter as tk
from tkinter import ttk
from datetime import datetime

class StopwatchApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Stopwatch")
        self.start_time = None
        self.running = False

        # Set the background color of the master window
        self.master.configure(bg="black")

        # Check if borderradius option is available (Python 3.11 and later)
        ttk.Style().configure("Rounded.TButton", padding=5, borderwidth=1, relief="flat", background="black", foreground="white", bordercolor="white", borderradius=10)
        ttk.Style().map("Rounded.TButton", background=[("active", "black"), ("pressed", "black")])

        # Use the custom style for buttons
        self.start_button = ttk.Button(self.master, text="Start", command=self.start_stopwatch, style="Rounded.TButton")
        self.start_button.pack(side=tk.LEFT, anchor="sw")

        self.reset_button = ttk.Button(self.master, text="Reset", command=self.reset_stopwatch, style="Rounded.TButton")
        self.reset_button.pack(side=tk.RIGHT, anchor="se")

        self.label = tk.Label(self.master, text="00:00:00", font=("Helvetica", 48), fg="white", bg="black")
        self.label.pack(pady=20)

        # Make the window stay on top
        self.master.wm_attributes("-topmost", True)

        # Make the window non-resizable
        self.master.resizable(False, False)

    def start_stopwatch(self):
        if not self.running:
            self.start_time = datetime.now()
            self.update_time()
            self.start_button.configure(text="Stop")
        else:
            self.start_button.configure(text="Start")
        self.running = not self.running
        self.master.after(1000, self.update_time)

    def update_time(self):
        if self.running:
            elapsed_time = datetime.now() - self.start_time
            elapsed_str = str(elapsed_time).split(".")[0]
            elapsed_str_padded = elapsed_str.zfill(8)  # Pad with zeros to ensure a width of 8 characters (HH:MM:SS)
            self.label.configure(text=elapsed_str_padded)
            self.master.after(1000, self.update_time)

    def reset_stopwatch(self):
        self.start_button.configure(text="Start")
        self.label.configure(text="00:00:00")
        self.running = False

if __name__ == "__main__":
    root = tk.Tk()
    app = StopwatchApp(root)
    root.mainloop()
