import subprocess
import time
import requests
import json
import random
from BotModes import BotMode  # BotModes.py
from TornBot_Library.Gym import Gym  # Gym.py
from TornBot_Library.Crime import Crime # Crime.py
import re
import inspect
import nodriver as uc



class TornBot:
    def __init__(self):
        self.status = BotMode.STARTING
        self.browser = None
        self.activePage = None
        self.pages = []
        self.GymInstance = self.GymClass(self)
        self.CrimeInstance = self.CrimeClass(self)
        self.status = BotMode.IDLE

    class GymClass(Gym):
        def __init__(self, tornBotInstance):
            super().__init__(tornBotInstance)


    class CrimeClass(Crime):
        def __init__(self, tornBotInstance):
            super().__init__(tornBotInstance)

    def _LogError(self, error):
        try:
            frame = inspect.currentframe().f_back
            methodName = frame.f_code.co_name
            args, _, _, values = inspect.getargvalues(frame)
            message = "Failed to " + re.sub(r'([a-z])([A-Z])', r'\1 \2', methodName).replace("_", "")

            for arg in args:
                if arg == 'self':
                    message += " "
                    continue
                message += f" {arg} {values[arg]}"
            message += f", error: {error}"

            print(message)
        except Exception as e:
            print(f"Failed to Log error {e}")
            pass

    # region Browser General Utility Actions


    async def LaunchBrowser(self):
        try:
            self.browser = await uc.start(browser_executable_path='C:\\Users\\Egidijus\\AppData\\Local\\ms-playwright\\chromium-1117\\chrome-win\\chrome.exe')
            self.status = BotMode.RUNNING
        except Exception as e:
            self._LogError(e)
            raise

    async def CloseBrowser(self):
        try:
            await self.browser.close()
        except Exception as e:
            self._LogError(e)
            raise

    async def _NavigateToSite(self, url, newTab=False):
        try:
            page = await self.browser.get(url = url, new_tab=newTab)
            self.activePage = page
            self.pages = self.browser.tabs
        except Exception as e:
            self._LogError(e)
            raise

    async def _SwitchPage(self, page):
        try:
            if page not in self.pages:
                raise Exception("Page does not exist in this browser instance")

            self.activePage = page
            self.activePage.activate()
        except Exception as e:
            self._LogError(e)
            raise

    async def _RefreshPage(self):
        try:
            await self.page.reload()
        except Exception as e:
            self._LogError(e)
            raise
    #endregion
    #region Browser Automation Actions
        
    async def _ReadElement(self, elementSelector):
        try:
            element = await self._FindElement(elementSelector)
            return element.text
        except Exception as e:
            self._LogError(e)
            raise
        
    async def _FindElement(self, elementSelector):
        try:
            element = await self.activePage.find(elementSelector, timeout=10)
            return element
        except Exception as e:
            self._LogError(e)
            raise
    async def _FindElements(self, elementSelector):
        try:
            elements = await self.activePage.find_all(elementSelector, timeout=10)
            return elements
        except Exception as e:
            self._LogError(e)
            raise

    async def _CheckElement(self, elementSelector):
        try:
            await self.page.find(elementSelector, timeout=0.5)
            return True
        except:
            return False

    async def _ClickElement(self, elementSelector):
        element = await self._FindElement(elementSelector)
        try:
            await element.click()
        except Exception as e:
            self._LogError(e)
            raise
        
    async def _ClickRandomElement(self, elementSelector):
        elements = await self._FindElements(elementSelector)
        try:
            randomElementIndex = int(random.uniform(0,elements.count()))
            await elements[randomElementIndex].click()
        except Exception as e:
            self._LogError(e)
            raise
        
    async def _InputElement(self, elementSelector, value):
        element = await self._FindElement(elementSelector)
        try:
            await element.clear_input()
            await element.send_keys(value)
        except Exception as e:
            self._LogError(e)
            raise

    async def _IsLoggedIn(self):
        profileButton = "//div[@class='profile-image-wrapper']"
        loggedIn = await self._CheckElement(profileButton)
        return loggedIn

    #endregion
    
    async def Login(self, username, password):
        loginButton = "//button[contains(@class,'loginBtn') and span[text() = 'Login']]"
        usernameInput = "//div[contains(@class,'popup')]/form[@name='login']//input[@id = 'player']"
        passwordInput = "//div[contains(@class,'popup')]/form[@name='login']//input[@id = 'password']"
        loginSubmitButton = "//div[contains(@class,'popup')]/form[@name='login']//input[@type = 'submit' and @value = 'Login']"
        profileButton = "//div[@class='profile-image-wrapper']"

        await self._ClickElement(loginButton)
        time.sleep(random.uniform(0.1,0.3))
        await self._InputElement(usernameInput, username)
        time.sleep(random.uniform(0.1,0.3))
        await self._InputElement(passwordInput, password)
        time.sleep(random.uniform(0.1,0.3))
        await self._ClickElement(loginSubmitButton)
        time.sleep(random.uniform(0.1,0.3))
        await self._FindElement(profileButton)

    async def NavigateToHome(self):
        homeButton = "//a[@aria-label='Index page' and @class='logo-link']"
        generalInformationLabel = "//h5[@class='box-title' and text()='General Information']"

        await self._ClickElement(homeButton)
        time.sleep(random.uniform(0.1,0.3))
        await self._FindElement(generalInformationLabel)


    async def GetStatus(self):
        #Get Energy
        #Get Nerve
        #Get Happy
        #Get Life
        #Get Money
        #Get Level - check upgradable
        #Get Points
        #Get Merits*
        return
