import time
from BotModes import AutomationMode
from TornBot_Automations.TornAutomation import TornAutomation
from TornBot_Library.TornBot import TornBot
import asyncio


async def main():
    Automation = TornAutomation()
    await asyncio.create_task(Automation.Start())
    time.sleep(60)
    Automation.TornBotMode = AutomationMode.BROWSING
    time.sleep(60)
    Automation.TornBotMode = AutomationMode.TRAINSTR
    print("done")

asyncio.get_event_loop().run_until_complete(main())

