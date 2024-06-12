from enum import Enum

class BotMode(Enum):
    RUNNING = "Running"
    IDLE = "Idle"
    BROWSING = "Browsing"
    PAUSED = "Paused"
    STARTING = "Starting"