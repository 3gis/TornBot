import time
from BotModes import AutomationMode
from TornBot_Automations.TornAutomation import TornAutomation
from TornBot_Library.TornBot import TornBot
import asyncio
import threading

def main():
    Automation = TornAutomation()
    thread = threading.Thread(target=asyncio.run, args=(Automation.Start(),))
    thread.start()
    print("Browser Started")
    time.sleep(2)
    while True:
        Automation.TornBotMode = AutomationMode.TRAINSTR
        print("Training Strength mode activated")
        time.sleep(1800)

if __name__ == "__main__":
    main()

