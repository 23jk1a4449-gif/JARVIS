import tkinter as tk
from tkinter import ttk


class JarvisDashboard:
    def __init__(self, root, manual_command_callback=None):
        self.root = root
        self.manual_command_callback = manual_command_callback

        self.root.title("J.A.R.V.I.S. - Desktop AI Assistant")
        self.root.geometry("850x600")
        self.root.minsize(700, 450)
        self.root.configure(bg="#101820")

        self.create_header()
        self.create_status_section()
        self.create_activity_section()
        self.create_manual_command_section()

    def create_header(self):
        header = tk.Frame(
            self.root,
            bg="#16232e",
            height=80
        )
        header.pack(fill="x")
        header.pack_propagate(False)

        title = tk.Label(
            header,
            text="J.A.R.V.I.S.",
            font=("Segoe UI", 25, "bold"),
            fg="#00e5ff",
            bg="#16232e"
        )
        title.pack(pady=(12, 0))

        subtitle = tk.Label(
            header,
            text="Just A Rather Very Intelligent System",
            font=("Segoe UI", 10),
            fg="#b8c7d1",
            bg="#16232e"
        )
        subtitle.pack()

    def create_status_section(self):
        status_frame = tk.Frame(
            self.root,
            bg="#101820"
        )
        status_frame.pack(fill="x", padx=20, pady=15)

        self.status_label = tk.Label(
            status_frame,
            text="● JARVIS ONLINE",
            font=("Segoe UI", 14, "bold"),
            fg="#00ff88",
            bg="#101820"
        )
        self.status_label.pack(anchor="w")

        self.info_label = tk.Label(
            status_frame,
            text="Voice assistant is ready.",
            font=("Segoe UI", 10),
            fg="#c7d5df",
            bg="#101820"
        )
        self.info_label.pack(anchor="w", pady=(5, 0))

    def create_activity_section(self):
        activity_title = tk.Label(
            self.root,
            text="Activity History",
            font=("Segoe UI", 14, "bold"),
            fg="#00e5ff",
            bg="#101820"
        )
        activity_title.pack(anchor="w", padx=20)

        activity_frame = tk.Frame(
            self.root,
            bg="#101820"
        )
        activity_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(8, 15)
        )

        self.activity_text = tk.Text(
            activity_frame,
            height=15,
            bg="#0b1117",
            fg="#d9f7ff",
            insertbackground="white",
            font=("Consolas", 10),
            relief="flat",
            wrap="word"
        )
        self.activity_text.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar = ttk.Scrollbar(
            activity_frame,
            orient="vertical",
            command=self.activity_text.yview
        )
        scrollbar.pack(side="right", fill="y")

        self.activity_text.configure(
            yscrollcommand=scrollbar.set
        )

        self.activity_text.insert(
            "end",
            "JARVIS dashboard started...\n"
        )
        self.activity_text.configure(state="disabled")

    def create_manual_command_section(self):
        command_frame = tk.Frame(
            self.root,
            bg="#16232e"
        )
        command_frame.pack(fill="x", padx=20, pady=(0, 20))

        self.command_entry = tk.Entry(
            command_frame,
            font=("Segoe UI", 11),
            bg="#ffffff",
            fg="#000000"
        )
        self.command_entry.pack(
            side="left",
            fill="x",
            expand=True,
            padx=(10, 5),
            pady=10
        )

        self.command_entry.bind(
            "<Return>",
            self.send_manual_command
        )

        send_button = tk.Button(
            command_frame,
            text="Send",
            font=("Segoe UI", 10, "bold"),
            bg="#00bcd4",
            fg="#000000",
            relief="flat",
            padx=20,
            command=self.send_manual_command
        )
        send_button.pack(
            side="right",
            padx=(5, 10),
            pady=10
        )

    def send_manual_command(self, event=None):
        command = self.command_entry.get().strip()

        if not command:
            return

        self.command_entry.delete(0, "end")

        if self.manual_command_callback:
            self.manual_command_callback(command)

    def add_activity(self, command, response=None):
        self.activity_text.configure(state="normal")

        self.activity_text.insert(
            "end",
            f"\nYou: {command}\n"
        )

        if response:
            self.activity_text.insert(
                "end",
                f"JARVIS: {response}\n"
            )

        self.activity_text.see("end")
        self.activity_text.configure(state="disabled")

    def update_status(self, message):
        self.info_label.config(text=message)

    def update_activity(self, command, response):
        self.add_activity(command, response)

    def log_activity(self, command, response):
        self.add_activity(command, response)