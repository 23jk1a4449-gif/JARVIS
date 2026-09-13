from datetime import datetime


class TimeTools:
    """Provides date and time information."""

    def get_current_time(self):
        current_time = datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time}, sir."

    def get_current_date(self):
        current_date = datetime.now().strftime("%A, %d %B %Y")
        return f"Today is {current_date}, sir."