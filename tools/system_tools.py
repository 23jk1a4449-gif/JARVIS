import platform
import psutil


class SystemTools:
    def request_shutdown(self):
        return "Shutdown request received. Confirmation is required."
    """Provides safe computer system information."""

    def get_cpu_usage(self):
        usage = psutil.cpu_percent(interval=1)
        return f"CPU usage is {usage} percent."

    def get_memory_usage(self):
        memory = psutil.virtual_memory()
        return f"Memory usage is {memory.percent} percent."

    def get_battery_status(self):
        battery = psutil.sensors_battery()

        if battery is None:
            return "Battery information is not available."

        status = "charging" if battery.power_plugged else "not charging"

        return (
            f"Battery level is {battery.percent} percent "
            f"and it is {status}."
        )

    def get_computer_name(self):
        computer_name = platform.node()
        return f"Your computer name is {computer_name}."