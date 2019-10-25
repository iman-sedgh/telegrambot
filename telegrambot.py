import requests
class tbot:
    def __init__(self,token, teleurl ="http://api.telegram.org/bot{}/" ):
        self.teleurl = teleurl.format(token)  

    def getupdate(self):
        method = "getUpdates"
        params = {}
        Res = requests.get(self.teleurl + method ,params )
        return Res.json()

    def sendmessage(self,chat_id,text):
        method = "sendMessage?"
        params = {}
        Res = requests.get(self.teleurl + method +'chat_id='+chat_id+'&text='+text ,params)
        return Res.json()

