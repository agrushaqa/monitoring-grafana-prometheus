import psutil


def get_battery_percent():
    return psutil.sensors_battery().percent
