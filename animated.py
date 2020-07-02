import requests
from time import sleep


#CONFIG
token = "your-token" # Your Discord token (https://www.youtube.com/watch?v=co9TvsAtUmY)
status = "Look! Animated Status!" # Text you want to be animated
emoji = "😋" # Emoji like this: 😋 (Leave blank for none)
speed = 0.9 # Speed of animating, recommended 0.5 - 1.5 seconds (I tried it for like half hour for 0.5s and its not ratelimiting or something)



# Text
print("")
print("")
print("Animating..")




# The full code
while True:
    for _i in range(0, len(status)+1):
        if emoji != "":
            content = {
                "custom_status": {"text": status[:_i],"emoji_name": emoji}
            }
        else:
            content = {
                "custom_status": {"text": status[:_i]}
            }
        requests.patch("https://ptb.discordapp.com/api/v6/users/@me/settings", headers={"authorization": token}, json=content)
        sleep(speed)
