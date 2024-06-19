

class Crime:

    def __init__(self, tornBotInstance: "TornBot"):
        self.tornBot = tornBotInstance 
    
    async def NavigateMain(self):
        crimesButton = "//span[contains(@class,'linkName') and text() = 'Crimes']/ancestor::a[@href]"
        crimesTitle = "//div[contains(@class,'crimes-app')]//h4[contains(text(),'Crimes')]"
        
        await self.tornBot._ClickElement(crimesButton)
        time.sleep(random.uniform(0.1,0.3))
        await self.tornBot._FindElement(crimesTitle)
        

    async def SelectCrimeCategory(self,crimeCategory : str):
        category = f"//span[contains(@class,'crimeTitle') and contains(text(),'{crimeCategory}')]"
        categoryHeader = f"//div[contains(@class,'appHeader')]//h4[contains(text(),'{crimeCategory}')]"
        
        await self.tornBot._ClickElement(category)
        time.sleep(random.uniform(0.1,0.3))
        await self.tornBot._FindElement(categoryHeader)
        
    async def FindLastCategory(self):
        category = "//a[contains(@class,'crimeType') and last()]//span[contains(@class,'crimeTitle')"
        return self.tornBot._ReadElement(category)
    
    #region Search for Cash
    
    async def SFC_SearchSubcategory(self, subcategory : str):
        subcategoryButton = f"//div[contains(@class,'crime-option-sections') and div[contains(@class,'crimeOptionSection') and contains(text(),'{subcategory}')]]//button[contains(@aria-label,'Search')]"
        await self.tornBot._ClickElement(subcategoryButton)

    async def SFC_SearchRandom(self):
        searchButton = "//button[contains(@aria-label,'Search')]"
        await self.tornBot._ClickRandomElement(searchButton)
        
    #endregion
    
    #region BootLegging
    async def BL_SelectDVDType(self, type : str):
        return
    
    async def BL_GetSelectedDVDType(self):
        return
    
    async def BL_CopyDVD(self):
        return
    
    async def BL_SellDVD(self):
        return
    
    #endregion
    
    #region Graffiti
    async def G_RefillNeeded(self):
        return
    
    async def G_Spray(self, district : str):
        return
    
    async def G_Refill(self):
        return
    #endregion
    
    #region Shoplifting
    async def SL_Shoplift(self, store : str):
        return
    
    async def SL_CheckSecurityLevel(self, store : str):
        return
    #endregion
    
    #region Pickpocketing
    async def PP_PickpocketAny(self):
        return
    
    async def PP_Pickpocket(self, person : str):
        return

    async def PP_GetAllPeople(self):
        return
    
    #endregion
       
    #region Card Skimming
    
    #endregion
    
    #region Burglary
    
    #endregion
    
    #region Hustling
    
    #endregion
    
    #region Disposal
    
    #endregion
    
    #region Cracking
    async def C_CrackAny(self):
        return
    
    async def C_Crack(self, target : str):
        return
    
    async def C_Hack(self, target : str):
        return
    
    async def C_GetAllTargets(self):
        return
    

    #endregion
    
    #region Forgery
    
    #endregion