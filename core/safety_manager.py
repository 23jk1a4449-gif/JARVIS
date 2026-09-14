
class SafetyManager:
    """Controls confirmation for risky desktop actions."""

    RISKY_ACTIONS = {
        "shutdown",
        "restart",
        "delete_file",
        "delete_folder",
        "install_software",
        "send_message",
        "admin_command",
        "change_system_setting",
    }

    def __init__(self):
        self.pending_action = None

    def requires_confirmation(self, action_name):
        return action_name in self.RISKY_ACTIONS

    def request_confirmation(self, action_description):
        self.pending_action = action_description

        return (
            f"Sir, you asked me to {action_description}. "
            "Please say yes to confirm or no to cancel."
        )

    def confirm(self):
        if self.pending_action is None:
            return "There is no pending action to confirm."

        action = self.pending_action
        self.pending_action = None

        return f"Confirmed: {action}"

    def cancel(self):
        self.pending_action = None
        return "Cancelled, sir."

    def has_pending_action(self):
        return self.pending_action is not None