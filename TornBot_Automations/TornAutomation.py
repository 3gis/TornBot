from msilib.schema import Upgrade
import random
import time
from BotModes import AutomationMode, BotMode
from TornBot_Library.TornBot import TornBot

class TornAutomation:
    def __init__(self):
        self.TornBot = TornBot()
        self.TornBotMode = AutomationMode.IDLE
        self.LoggedIn = False
        self.TornBot.LaunchBrowser()

    async def Start(self):
        while True:
            match self.TornBotMode:
                case AutomationMode.IDLE:
                    self.TornBot.status = BotMode.IDLE
                    if self.TornBot._IsLoggedIn:
                        self.TornBot.NavigateToHome()
                    while self.TornBotMode == AutomationMode.IDLE:
                        time.sleep(10)
                case AutomationMode.PAUSED:
                    self.TornBot.status = BotMode.PAUSED
                    while self.TornBotMode == AutomationMode.PAUSED:
                        time.sleep(10)
                case AutomationMode.BROWSING:
                    self.TornBot.status = BotMode.BROWSING
                    websites = ["www.google.com","www.youtube.com","www.w3schools.com", "www.stackoverflow.com"]
                    while self.TornBotMode == AutomationMode.BROWSING:
                        self.TornBot._NavigateToSite(random.choice(websites))
                        for i in range(0,20):
                            time.sleep(60)
                        
                case AutomationMode.TRAINSTR:
                    await self.InitializeRobot()
                    await self.TornBot.GymInstance.NavigateMain()
                    upgradeable = await self.TornBot.GymInstance.IsUpgradeable()
                    if upgradeable:
                        await self.TornBot.GymInstance.UpgradeGym()
                    await self.TornBot.GymInstance.TrainStrength(69)
                    self.TornBotMode = AutomationMode.BROWSING
                case AutomationMode.TRAINDEF:
                    await self.InitializeRobot()
                    await self.TornBot.GymInstance.NavigateMain()
                    upgradeable = await self.TornBot.GymInstance.IsUpgradeable()
                    if upgradeable:
                        await self.TornBot.GymInstance.UpgradeGym()
                    await self.TornBot.GymInstance.TrainDefense(69)
                    self.TornBotMode = AutomationMode.BROWSING
                case AutomationMode.TRAINDEX:
                    await self.InitializeRobot()
                    await self.TornBot.GymInstance.NavigateMain()
                    upgradeable = await self.TornBot.GymInstance.IsUpgradeable()
                    if upgradeable:
                        await self.TornBot.GymInstance.UpgradeGym()
                    await self.TornBot.GymInstance.TrainDexterity(69)
                    self.TornBotMode = AutomationMode.BROWSING
                case AutomationMode.TRAINSPD:
                    await self.InitializeRobot()
                    await self.TornBot.GymInstance.NavigateMain()
                    upgradeable = await self.TornBot.GymInstance.IsUpgradeable()
                    if upgradeable:
                        await self.TornBot.GymInstance.UpgradeGym()
                    await self.TornBot.GymInstance.TrainSpeed(69)
                    self.TornBotMode = AutomationMode.BROWSING
                case AutomationMode.SEARCHCASH:
                    return
                    await self.InitializeRobot()
                    await self.TornBot.CrimeInstance.NavigateMain()
                    await self.TornBot.CrimeInstance.SelectCrimeCategory("Search For Cash")
                    while False: #TODO: status till no more nerve or jailed
                        await self.TornBot.CrimeInstance.SFC_SearchRandom()
                    self.TornBotMode = AutomationMode.BROWSING
                case AutomationMode.BOOTLEGGING:
                    return
                    await self.InitializeRobot()
                    await self.TornBot.CrimeInstance.NavigateMain()
                    await self.TornBot.CrimeInstance.SelectCrimeCategory("Bootlegging")
                    await self.TornBot.CrimeInstance.BL_SelectRandomDVDType() #TODO: SelectRandomDBDType method
                    while False: #TODO: status till no more nerve or jailed
                        await self.TornBot.CrimeInstance.BL_CopyDVD()
                    self.TornBotMode = AutomationMode.BROWSING
                
    async def InitializeRobot(self, newTab = False):
        await TornBot._NavigateToSite("www.Torn.com", newTab)
        self.LoggedIn = await TornBot._IsLoggedIn()
        if self.LoggedIn:
            await TornBot.NavigateToHome()
        else:
            await TornBot._NavigateToSite("www.Torn.com", newTab)
            await TornBot.Login(self.Username, self.Password)
            self.LoggedIn = True
            await TornBot.NavigateToHome()
            