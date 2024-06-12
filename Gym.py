
class Gym:

    def __init__(self, tornBotInstance: "TornBot"):
        self.tornBot = tornBotInstance
        
    async def NavigateMain(self):
        gymButton = "//span[contains(@class,'linkName') and text() = 'Gym']/ancestor::a[@href]"
        gymTitle = "//div[contains(@class,'content-title')]//h4[contains(text(),'Gym')]"
        
        await self.tornBot.ClickElement(gymButton)
        time.sleep(random.uniform(0.1,0.3))
        await self.tornBot._FindElement(gymTitle)
    
    async def TrainStrength(self,amount = "200"):
        strengthInput = "//input[@aria-label='Enter the number of strength training']"
        trainButton = "//button[@aria-label='Train strength' and text() = 'TRAIN']"
        successfulTrainLabel = "//div[contains(@class,'messageWrapper')]//p[contains(text(),'You successfully completed')]"
        
        await self.tornBot.InputElement(strengthInput, str(amount))
        time.sleep(random.uniform(0.1,0.3))
        await self.tornBot.ClickElement(trainButton)
        time.sleep(random.uniform(0.1,0.3))
        await self.tornBot._FindElement(successfulTrainLabel)
        
    async def TrainDefense(self,amount = "200"):
        defenseInput = "//input[@aria-label='Enter the number of defense training']"
        trainButton = "//button[@aria-label='Train defense' and text() = 'TRAIN']"
        successfulTrainLabel = "//div[contains(@class,'messageWrapper')]//p[contains(text(),'You successfully completed')]"
        
        await self.tornBot.InputElement(defenseInput, str(amount))
        time.sleep(random.uniform(0.1,0.3))
        await self.tornBot.ClickElement(trainButton)
        time.sleep(random.uniform(0.1,0.3))
        await self.tornBot._FindElement(successfulTrainLabel)
        
    async def TrainSpeed(self,amount = "200"):
        speedInput = "//input[@aria-label='Enter the number of speed training']"
        trainButton = "//button[@aria-label='Train speed' and text() = 'TRAIN']"
        successfulTrainLabel = "//div[contains(@class,'messageWrapper')]//p[contains(text(),'You successfully completed')]"
        
        await self.tornBot.InputElement(speedInput, str(amount))
        time.sleep(random.uniform(0.1,0.3))
        await self.tornBot.ClickElement(trainButton)
        time.sleep(random.uniform(0.1,0.3))
        await self.tornBot._FindElement(successfulTrainLabel)
        
    async def TrainDexterity(self,amount = "200"):
        dexterityInput = "//input[@aria-label='Enter the number of dexterity training']"
        trainButton = "//button[@aria-label='Train dexterity' and text() = 'TRAIN']"
        successfulTrainLabel = "//div[contains(@class,'messageWrapper')]//p[contains(text(),'You successfully completed')]"
        
        await self.tornBot.InputElement(dexterityInput, str(amount))
        time.sleep(random.uniform(0.1,0.3))
        await self.tornBot.ClickElement(trainButton)
        time.sleep(random.uniform(0.1,0.3))
        await self.tornBot._FindElement(successfulTrainLabel)

    async def IsUpgradeable(self):
        activeGym = "//button[contains(@id,'gym') and div//div[contains(@class,'percentage')]/following-sibling::div[contains(@class,'progressBar')]]/preceding-sibling::button[1][contains(@class,'active')]"
        return not await self.tornBot._CheckElement(activeGym)
    
    async def UpgradeGym(self):
        newGymButton = "//button[contains(@id,'gym') and div//div[contains(@class,'percentage')]/following-sibling::div[contains(@class,'progressBar')]]/preceding-sibling::button[1][contains(@class,'newSeen')]"
        buyMembershipButton = "//button[text() = 'BUY MEMBERSHIP']"
        
        await self.tornBot.ClickElement(newGymButton)
        time.sleep(random.uniform(0.1,0.3))
        await self.tornBot.ClickElement(buyMembershipButton)
        time.sleep(random.uniform(0.1,0.3))
        upgradeable = await self.IsUpgradeable()
        
        if upgradeable == True:
            raise Exception("Failed to Upgrade Gym")
        
        await self.NavigateMain()
        
        