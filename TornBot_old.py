from math import e
import subprocess
import time
import pyppeteer
import requests
import json
from BotModes import BotMode #BotModes.py
from Gym import Gym #Gym.py
from pyppeteer import executablePath, launch
import re
import inspect

class TornBot:
    
    def __init__(self):
        self.status = BotMode.STARTING
        self.pages = []
        self.GymInstance = self.GymClass(self)
        self.status = BotMode.IDLE
    
    class GymClass(Gym):
        def __init__(self, tornBotInstance):
            super().__init__(tornBotInstance)
    
    def _LogError(self, error):
        try:
            frame = inspect.currentframe().f_back
            methodName = frame.f_code.co_name
            args, _, _, values = inspect.getargvalues(frame)
            message = "Failed to " + re.sub(r'([a-z])([A-Z])', r'\1 \2', methodName).replace("_","")
        
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
            subprocess.Popen(['C:\\Program Files\\Mozilla Firefox\\firefox.exe', '--remote-debugging-port=6969'])
            time.sleep(2)
            data = requests.get("http://127.0.0.1:6969/json/version").json()["webSocketDebuggerUrl"]
            self.browser = await pyppeteer.connect(browserWSEndpoint=data)
            
            self.pages = await self.browser.pages()
            self.activePage = self.pages[0]
            #self.browser = await launch(headless=False, executablePath= "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe")
            #self.pages = []
            #self.activePage = None
            self.status = BotMode.RUNNING
        except Exception as e:
            self._LogError(e)
            raise
    
    async def Attach(self):
        try:
            data = requests.get("http://127.0.0.1:6969/json/version").json()["webSocketDebuggerUrl"]
            self.browser = await pyppeteer.connect(browserWSEndpoint=data)
            #self.pages = await self.browser.pages()
            #self.activePage = self.pages[0]
        except Exception as e:
            self._LogError(e)
            raise
        
    async def CloseBrowser(self):
        try:
            await self.browser.close()
        except Exception as e:
            self._LogError(e)
            raise
        
    async def NavigateToSite(self, url, newPage = False):
        try:
            if (self.activePage is None) or newPage:
                page = await self.browser.newPage()
                self.pages.append(page)
                self.activePage = page;
            time.sleep(2)
            options = {"waitUntil": 'load', "timeout": 1}
            try:
                await self.activePage.goto(url, options=options);
            except TimeoutError as e:
                    pass  
        except Exception as e:
            self._LogError(e)
            raise
            
    async def SwitchPage(self, page):
        try:
            if page not in self.pages:
                raise Exception("Page does not exist in this browser instance")
            
            self.activePage = page;
            
        except Exception as e:
            self._LogError(e)
            raise
        
    async def RefeshPage(self):
        try:
            self.activePage.reload()
        except Exception as e:
            self._LogError(e)
            raise
    #endregion    
    
    #region Browser Automation Actions
    
    async def _FindElement(self, elementSelector):
        try:
            await self.activePage.waitForSelector("xpath/" + elementSelector, timeout=10000)
            return await self.activePage.xpath(elementSelector)[0]
            
        except Exception as e:
            self._LogError(e)
            raise
    
    async def _CheckElement(self, elementSelector):
        try:
            await self.activePage.waitForXPath(elementSelector, timeout=1000)
            return True
        #TODO: findout exceptiontype of not found elements
        except:
            return False
        
    async def ClickElement(self, elementSelector):
        element = await self._FindElement(elementSelector)
        
        try:
            element.click()
        except Exception as e:
            self._LogError(e)
            raise
        
    async def InputElement(self, elementSelector, value):
        element = await self._FindElement(elementSelector)
        try:
            await element.type(value)
        except Exception as e:
            self._LogError(e)
            raise
        
    async def SendKeyToElement(self, elementSelector, key):
        element = await self._FindElement(elementSelector)
        try:
            element.press(key)
        except Exception as e:
            self._LogError(e)
            raise
    
    #endregion        
    #region TornBot Basic Actions
    async def IsLoggedIn(self):
        profileButton = "//div[@class='profile-image-wrapper']"
        loggedIn = await self._CheckElement(profileButton)
        return loggedIn
    
    async def Login(self,username, password):
        loginButton = "//button[contains(@class,'loginBtn') and span[text() = 'Login']]"
        usernameInput = "//div[contains(@class,'popup')]/form[@name='login']//input[@id = 'player']"
        passwordInput ="//div[contains(@class,'popup')]/form[@name='login']//input[@id = 'password']"
        loginSubmitButton ="//div[contains(@class,'popup')]/form[@name='login']//input[@type = 'submit' and @value = 'Login']"
        profileButton = "//div[@class='profile-image-wrapper']"
        
        await self.ClickElement(loginButton)
        await self.InputElement(usernameInput,username)
        await self.InputElement(passwordInput,password)
        await self.ClickElement(loginSubmitButton)
        await self._FindElement(profileButton)
        
    async def NavigateToHome(self):
        homeButton = "//a[@aria-label='Index page' and @class='logo-link']"
        generalInformationLabel = "//h5[@class='box-title' and text()='General Information']"
        
        await self.ClickElement(homeButton)
        await self._FindElement(generalInformationLabel)     
    #endregion