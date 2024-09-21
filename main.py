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
    time.sleep(10)
    Automation.TornBotMode = AutomationMode.BROWSING
    print("Browsing mode activated")
    while True:
        time.sleep(0.5)
    Automation.TornBotMode = AutomationMode.TRAINSTR
    print("Training Strength mode activated")
    print("done")

if __name__ == "__main__":
    main()

