import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime


class JarvisDashboard:
    """Professional desktop dashboard for JARVIS."""

    def __init__(self, root, command_callback):
        self.root = root
        self.command_callback = command_callback

        self.root.title("J.A.R.V.I.S. - Voice Intelligence System")
        self.root.geometry("850x600")
        self.root.configure(bg="#101820")
        self.root.minsize(700, 500)

        self.build_interface()

    def build_interface(self):
        # Header
        header = tk.Frame(
            self.root,
            bg="#162633",
            height=85
        )
        header.pack(fill="x")

        title = tk.Label(
            header,
            text="J.A.R.V.I.S.",
            font=("Segoe UI", 26, "bold"),
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
        status_frame.pack(fill="x", padx=20, pady=18)

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

        # Information cards
        cards_frame = tk.Frame(
            self.root,
            bg="#101820"
        )
        cards_frame.pack(fill="x", padx=20)

        self.create_card(
            cards_frame,
            "VOICE SYSTEM",
            "READY",
            0
        )

        self.create_card(
            cards_frame,
            "AI BRAIN",
            "ACTIVE",
            1
        )

        self.create_card(
            cards_frame,
            "SECURITY",
            "PROTECTED",
            2
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
            pady=(22, 8)
        )

        self.latest_response = tk.Label(
            self.root,
            text="JARVIS is waiting for your command...",
            font=("Segoe UI", 12),
            fg="#ffffff",
            bg="#1b2d3a",
            anchor="w",
            justify="left",
            wraplength=780,
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
        activity_title.pack(anchor="w", padx=20, pady=(25, 8))

        # Activity display
        self.activity_box = scrolledtext.ScrolledText(
            self.root,
            height=14,
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
        self.add_activity("Waiting for commands...")

        self.update_clock()

    def create_card(self, parent, title, value, column):
        card = tk.Frame(
            parent,
            bg="#1b2d3a",
            width=240,
            height=75
        )
        card.grid(
            row=0,
            column=column,
            padx=6,
            sticky="nsew"
        )
        card.grid_propagate(False)

        parent.grid_columnconfigure(column, weight=1)

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
            font=("Segoe UI", 13, "bold"),
            fg="#00ff9d",
            bg="#1b2d3a"
        )
        value_label.pack()

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

        self.time_label.config(text=current_time)
        self.root.after(1000, self.update_clock)

    def display_command(self, command, response):
        self.add_activity(f"USER: {command}")
        self.add_activity(f"JARVIS: {response}")
