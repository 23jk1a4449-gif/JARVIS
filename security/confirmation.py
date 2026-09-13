class ConfirmationManager:
    """Handles confirmation for sensitive JARVIS actions."""

    def ask_confirmation(self, action):
        print(f"\nCONFIRMATION REQUIRED: {action}")
        answer = input("Type YES to continue or NO to cancel: ")

        return answer.strip().lower() == "yes"