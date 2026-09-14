
import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime
import platform
import psutil


class JarvisDashboard:
    """Professional desktop dashboard for JARVIS."""

    def __init__(self, root, command_callback=None):
        self.root = root
        self.command_callback = command_callback

        self.root.title("J.A.R.V.I.S. - Voice Intelligence System")
        self.root.geometry("900x700")
        self.root.configure(bg="#101820")
        self.root.minsize(750, 600)

        self.build_interface()
        self.update_clock()
        self.update_system_information()

    def build_interface(self):
        # Header
        header = tk.Frame(
            self.root,
            bg="#162633",
            height=95
        )
        header.pack(fill="x")
        header.pack_propagate(False)

        title = tk.Label(
            header,
            text="J.A.R.V.I.S.",
            font=("Segoe UI", 28, "bold"),
            fg="#00e5ff",
            bg="#162633"
        )
        title.pack(pady=(12, 0))

        subtitle = tk.Label(
            header,
            text="Just-in-time Artificial Reasoning and Voice Intelligence System",
            font=("Segoe UI", 10),
            fg="#b8c7d1",
            bg="#162633"
        )
        subtitle.pack()

        # Status section
        status_frame = tk.Frame(
            self.root,
            bg="#101820"
        )
        status_frame.pack(
            fill="x",
            padx=20,
            pady=18
        )

        self.status_label = tk.Label(
            status_frame,
            text="● SYSTEM ONLINE",
            font=("Segoe UI", 12, "bold"),
            fg="#00ff9d",
            bg="#101820"
        )
        self.status_label.pack(side="left")

        self.time_label = tk.Label(
            status_frame,
            text="",
            font=("Segoe UI", 11),
            fg="#dce6ed",
            bg="#101820"
        )
        self.time_label.pack(side="right")

        # Live system information cards
        cards_frame = tk.Frame(
            self.root,
            bg="#101820"
        )
        cards_frame.pack(
            fill="x",
            padx=20
        )

        self.cpu_value = self.create_card(
            cards_frame,
            "CPU USAGE",
            "Loading...",
            0
        )

        self.memory_value = self.create_card(
            cards_frame,
            "RAM USAGE",
            "Loading...",
            1
        )

        self.battery_value = self.create_card(
            cards_frame,
            "BATTERY",
            "Loading...",
            2
        )

        self.computer_value = self.create_card(
            cards_frame,
            "COMPUTER",
            platform.node(),
            3
        )

        # Refresh button
        refresh_button = tk.Button(
            self.root,
            text="⟳ Refresh System Information",
            command=self.update_system_information,
            font=("Segoe UI", 10, "bold"),
            fg="#101820",
            bg="#00e5ff",
            activebackground="#00b8d4",
            relief="flat",
            padx=12,
            pady=8,
            cursor="hand2"
        )
        refresh_button.pack(
            anchor="e",
            padx=20,
            pady=(15, 0)
        )

        # Latest response panel
        latest_title = tk.Label(
            self.root,
            text="LATEST RESPONSE",
            font=("Segoe UI", 14, "bold"),
            fg="#00e5ff",
            bg="#101820"
        )
        latest_title.pack(
            anchor="w",
            padx=20,
            pady=(20, 8)
        )

        self.latest_response = tk.Label(
            self.root,
            text="JARVIS is waiting for your command...",
            font=("Segoe UI", 12),
            fg="#ffffff",
            bg="#1b2d3a",
            anchor="w",
            justify="left",
            wraplength=820,
            padx=15,
            pady=15
        )
        self.latest_response.pack(
            fill="x",
            padx=20
        )

        # Activity title
        activity_title = tk.Label(
            self.root,
            text="ACTIVITY MONITOR",
            font=("Segoe UI", 14, "bold"),
            fg="#00e5ff",
            bg="#101820"
        )
        activity_title.pack(
            anchor="w",
            padx=20,
            pady=(20, 8)
        )

        # Activity display
        self.activity_box = scrolledtext.ScrolledText(
            self.root,
            height=12,
            font=("Consolas", 10),
            bg="#0b1117",
            fg="#dce6ed",
            insertbackground="#ffffff",
            relief="flat",
            wrap=tk.WORD
        )
        self.activity_box.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(0, 15)
        )

        self.add_activity("JARVIS dashboard initialized.")
        self.add_activity("Voice system ready.")
        self.add_activity("Security layer protected.")
        self.add_activity("Live system monitoring enabled.")
        self.add_activity("Waiting for commands...")

    def create_card(self, parent, title, value, column):
        card = tk.Frame(
            parent,
            bg="#1b2d3a",
            height=85
        )
        card.grid(
            row=0,
            column=column,
            padx=5,
            sticky="nsew"
        )
        card.grid_propagate(False)

        parent.grid_columnconfigure(
            column,
            weight=1
        )

        title_label = tk.Label(
            card,
            text=title,
            font=("Segoe UI", 9, "bold"),
            fg="#91a7b5",
            bg="#1b2d3a"
        )
        title_label.pack(pady=(10, 0))

        value_label = tk.Label(
            card,
            text=value,
            font=("Segoe UI", 12, "bold"),
            fg="#00ff9d",
            bg="#1b2d3a"
        )
        value_label.pack()

        return value_label

    def update_system_information(self):
        cpu_usage = psutil.cpu_percent(interval=0.2)
        memory_usage = psutil.virtual_memory().percent
        battery = psutil.sensors_battery()

        self.cpu_value.config(
            text=f"{cpu_usage:.1f}%"
        )

        self.memory_value.config(
            text=f"{memory_usage:.1f}%"
        )

        if battery is None:
            self.battery_value.config(
                text="Not available"
            )
        else:
            charging_status = "Charging" if battery.power_plugged else "Not charging"
            self.battery_value.config(
                text=f"{battery.percent:.0f}%"
            )

        self.computer_value.config(
            text=platform.node()
        )

        self.add_activity("System information refreshed.")

    def add_activity(self, message):
        timestamp = datetime.now().strftime("%H:%M:%S")

        self.activity_box.insert(
            tk.END,
            f"[{timestamp}] {message}\n"
        )

        self.activity_box.see(tk.END)

    def update_clock(self):
        current_time = datetime.now().strftime(
            "%A, %d %B %Y | %I:%M:%S %p"
        )

        self.time_label.config(
            text=current_time
        )

        self.root.after(
            1000,
            self.update_clock
        )

    def display_command(self, command, response):
        self.latest_response.config(
            text=response
        )

        self.add_activity(
            f"USER: {command}"
        )

        self.add_activity(
            f"JARVIS: {response}"
        )