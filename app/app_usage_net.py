from dataclasses import dataclass


@dataclass
class AppUsageNet:
    ip: str
    port: int
    app_name: str
