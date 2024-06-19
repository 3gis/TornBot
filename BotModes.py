from enum import Enum

class BotMode(Enum):
    RUNNING = "Running"
    IDLE = "Idle"
    BROWSING = "Browsing"
    PAUSED = "Paused"
    STARTING = "Starting"
    
   

class AutomationMode(Enum):
    IDLE = "Idle"
    PAUSED = "Paused"
    BROWSING = "Browsing"
    
    TRAINSTR = "Training Strength at Gym"
    TRAINDEF = "Training Defense at Gym"
    TRAINDEX = "Training Dexterity at Gym"
    TRAINSPD = "Training Speed at Gym"
    
    SEARCHCASH = "Searching for Cash"
    BOOTLEGGING = "Bootlegging"
    