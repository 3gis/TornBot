from TornBot import TornBot
import asyncio


async def main():
    tornBot = TornBot()
    await tornBot.LaunchBrowser()
    await tornBot._NavigateToSite("https://www.torn.com")
    await tornBot.Login("hello","bon")
    print("done")

asyncio.get_event_loop().run_until_complete(main())

