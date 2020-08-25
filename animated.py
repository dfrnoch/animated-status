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

print(f"{Fore.WHITE}[ {Fore.CYAN}§ {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Discord Status Animator made by {Fore.WHITE}LnX{Fore.LIGHTBLACK_EX} | Licensed under {Fore.WHITE}MIT {Fore.LIGHTBLACK_EX}License")
print(f"{Fore.WHITE}[ {Fore.CYAN}§ {Fore.WHITE}] {Fore.LIGHTBLACK_EX}You can follow me on Github: {Fore.WHITE}https://github.com/lnxcz\n")

status = input(f"{Fore.WHITE}[ {Fore.YELLOW}> {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Text you want to display: {Fore.WHITE}")
print(f"\n{Fore.WHITE}[ {Fore.YELLOW}? {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Search here: {Fore.WHITE}www.webfx.com/tools/emoji-cheat-sheet {Fore.LIGHTBLACK_EX}(Leave empty if you dont want emoji)")
emoji = emoji.emojize(input(f"{Fore.WHITE}[ {Fore.YELLOW}> {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Insert emoji name: {Fore.WHITE}"), use_aliases=True)
print(f"\n{Fore.WHITE}[ {Fore.YELLOW}? {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Reccomended time is 0.5-1.5s")
speed = float(input(f"{Fore.WHITE}[ {Fore.YELLOW}> {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Text speed: {Fore.WHITE}"))

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
