import requests
from time import sleep
from colorama import Fore
import json
import os
import emoji

with open('config.json') as f:
    config = json.load(f)

token = config.get("token")

os.system("cls")

status = input(f"{Fore.WHITE}[ {Fore.YELLOW}> {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Text you want to display: ")
print(f"\n{Fore.WHITE}[ {Fore.YELLOW}? {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Search here: {Fore.WHITE}www.webfx.com/tools/emoji-cheat-sheet {Fore.LIGHTBLACK_EX}(Leave empty if you dont want emoji)")
emoji = emoji.emojize(input(f"{Fore.WHITE}[ {Fore.YELLOW}> {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Insert emoji name: "), use_aliases=True)
print(f"\n{Fore.WHITE}[ {Fore.YELLOW}? {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Reccomended time is 0.5-1.5s")
speed = float(input(f"{Fore.WHITE}[ {Fore.YELLOW}> {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Text speed: "))

print(f"\n\n{Fore.WHITE}[ {Fore.GREEN}+ {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Animating..")



# The full code
while True:
    for text in range(0, len(status)+1):
        if emoji != "":
            content = {
                "custom_status": {"text": status[:text], "emoji_name": emoji}
            }
        else:
            content = {
                "custom_status": {"text": status[:text]}
            }
        requests.patch("https://ptb.discordapp.com/api/v6/users/@me/settings", headers={"authorization": token}, json=content)
        sleep(speed)
