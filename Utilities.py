import json


class Utilities:
    
    async def LoadAppSettings(filePath :str):
        with open(filePath, 'r') as file:
            data = json.load(file)
            return data